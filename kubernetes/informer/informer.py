# Copyright 2024 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Informer implementation for the Kubernetes Python client.

Provides SharedInformer: a background watcher that keeps a local
ObjectCache in sync with the Kubernetes API server and notifies
registered event-handler callbacks.
"""

import logging
import threading
import time

from kubernetes.client.exceptions import ApiException
from kubernetes.watch import Watch

from .cache import ObjectCache, _meta_namespace_key

logger = logging.getLogger(__name__)


# Event types emitted to registered handlers
ADDED = "ADDED"
MODIFIED = "MODIFIED"
DELETED = "DELETED"
ERROR = "ERROR"


class SharedInformer:
    """Watch a Kubernetes resource and maintain a local cache.

    The informer starts a daemon thread that continuously watches the
    given resource via ``list_func``.  On each event the local
    :class:`ObjectCache` is updated and registered
    event-handler callbacks are invoked.

    Parameters
    ----------
    list_func:
        Bound API method used for the initial list **and** as the watch
        source.  It must accept a watch keyword argument (e.g.
        CoreV1Api().list_namespaced_pod).
    namespace:
        Kubernetes namespace to watch.  Pass None for cluster-scoped
        or all-namespace list functions.
    resync_period:
        How often (seconds) to perform a full re-list from the API server.
        Defaults to 0 which disables periodic resyncs.
    label_selector:
        Optional label selector string forwarded to the API server.
    field_selector:
        Optional field selector string forwarded to the API server.
    key_func:
        Optional callable (obj) -> str used to key objects in the
        cache.  Defaults to namespace/name.
    """

    def __init__(
        self,
        list_func,
        namespace=None,
        resync_period=0,
        label_selector=None,
        field_selector=None,
        key_func=None,
    ):
        self._list_func = list_func
        self._namespace = namespace
        self._resync_period = resync_period
        self._label_selector = label_selector
        self._field_selector = field_selector

        self._cache = ObjectCache(key_func=key_func)
        self._handlers = {ADDED: [], MODIFIED: [], DELETED: [], ERROR: []}
        self._handler_lock = threading.Lock()

        self._watch = None
        self._thread = None
        self._stop_event = threading.Event()

    # ---------------------------------------------------------------- #
    # Public API                                                        #
    # ---------------------------------------------------------------- #

    @property
    def cache(self):
        """The :class:`ObjectCache` maintained by this informer."""
        return self._cache

    def add_event_handler(self, event_type, handler):
        """Register a callback for a specific event type.

        Parameters
        ----------
        event_type:
            One of :data:`ADDED`, :data:`MODIFIED`, :data:`DELETED` or
            :data:`ERROR`.
        handler:
            Callable invoked with the event object (or the raw exception for
            ERROR events).
        """
        if event_type not in self._handlers:
            raise ValueError(
                "Unknown event_type {!r}. Use one of: {}".format(
                    event_type, ", ".join(sorted(self._handlers)),
                )
            )
        with self._handler_lock:
            self._handlers[event_type].append(handler)

    def remove_event_handler(self, event_type, handler):
        """Deregister a previously registered *handler*.

        No-op if *handler* is not registered.
        """
        with self._handler_lock:
            try:
                self._handlers[event_type].remove(handler)
            except (KeyError, ValueError):
                pass

    def start(self):
        """Start the background watch loop in a daemon thread.

        Calling :meth:`start` more than once without an intervening
        :meth:`stop` is a no-op.
        """
        if self._thread is not None and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._run_loop,
            name="SharedInformer",
            daemon=True,
        )
        self._thread.start()

    def stop(self):
        """Ask the background watch loop to stop and join the thread."""
        self._stop_event.set()
        if self._watch is not None:
            self._watch.stop()
        if self._thread is not None:
            self._thread.join()
        self._thread = None

    # ---------------------------------------------------------------- #
    # Internal helpers                                                  #
    # ---------------------------------------------------------------- #

    def _build_kwargs(self):
        kw = {}
        if self._namespace is not None:
            kw["namespace"] = self._namespace
        if self._label_selector is not None:
            kw["label_selector"] = self._label_selector
        if self._field_selector is not None:
            kw["field_selector"] = self._field_selector
        return kw

    def _fire(self, event_type, obj):
        with self._handler_lock:
            handlers = list(self._handlers.get(event_type, []))
        for fn in handlers:
            try:
                fn(obj)
            except Exception:
                logger.exception(
                    "Exception in informer handler for %s", event_type
                )

    def _initial_list(self):
        """Do the initial list and populate the cache."""
        kw = self._build_kwargs()
        resource_version = "0"
        resp = self._list_func(**kw)
        items = getattr(resp, "items", []) or []
        self._cache._replace_all(items)
        rv = None
        meta = getattr(resp, "metadata", None)
        if meta is not None:
            rv = getattr(meta, "resource_version", None)
        if rv:
            resource_version = rv
        return resource_version

    def _run_loop(self):
        """Background loop: list then watch, reconnect on errors."""
        while not self._stop_event.is_set():
            try:
                resource_version = self._initial_list()
            except Exception as exc:
                logger.exception("Error during initial list; retrying")
                self._fire(ERROR, exc)
                self._stop_event.wait(timeout=5)
                continue

            # Watch loop
            last_resync = time.monotonic()
            self._watch = Watch()
            kw = self._build_kwargs()
            kw["resource_version"] = resource_version
            try:
                for event in self._watch.stream(self._list_func, **kw):
                    if self._stop_event.is_set():
                        break
                    evt_type = event.get("type")
                    obj = event.get("object")
                    if evt_type == ADDED:
                        self._cache._put(obj)
                        self._fire(ADDED, obj)
                    elif evt_type == MODIFIED:
                        self._cache._put(obj)
                        self._fire(MODIFIED, obj)
                    elif evt_type == DELETED:
                        self._cache._remove(obj)
                        self._fire(DELETED, obj)
                    elif evt_type == ERROR:
                        self._fire(ERROR, obj)
                    # Periodic resync: re-list and fire MODIFIED for all cached objects
                    if (
                        self._resync_period > 0
                        and (time.monotonic() - last_resync) >= self._resync_period
                    ):
                        logger.debug("Informer resync triggered")
                        for cached_obj in self._cache.list():
                            self._fire(MODIFIED, cached_obj)
                        last_resync = time.monotonic()
            except ApiException as exc:
                logger.warning(
                    "Watch stream ended with ApiException (status=%s); reconnecting",
                    exc.status,
                )
                self._fire(ERROR, exc)
            except Exception as exc:
                logger.exception("Unexpected error in watch loop; reconnecting")
                self._fire(ERROR, exc)
            finally:
                self._watch = None
