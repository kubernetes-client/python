# Copyright 2026 The Kubernetes Authors.
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
import math
import random
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
BOOKMARK = "BOOKMARK"
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
        Defaults to 0 which disables periodic resyncs. The interval starts
        after a successful list completes; reconnects do not reset it.
        Failed lists and watches use separate exponential retry delays
        (0.5 to 60 seconds, with jitter). Network calls can extend the
        interval beyond the configured period.
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
        self._handlers = {ADDED: [], MODIFIED: [], DELETED: [], BOOKMARK: [], ERROR: []}
        self._handler_lock = threading.Lock()

        self._watch = None
        self._thread = None
        self._stop_event = threading.Event()
        # Last applied RV; None forces a full re-list.
        self._resource_version = None
        self._last_list_time = None

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
            One of :data:`ADDED`, :data:`MODIFIED`, :data:`DELETED`,
            :data:`BOOKMARK` or :data:`ERROR`.
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
        """Execute all registered callbacks for *event_type*, passing *obj*.

        Callbacks are invoked sequentially on the informer's background thread.
        Any exception raised by an individual handler is logged and swallowed so
        that remaining handlers still run.
        """
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
        """List all objects and populate the cache, firing ADDED/MODIFIED/DELETED events.

        On the first call (empty cache) every returned item fires ADDED.
        On subsequent calls (resync or after a 410 Gone) the new list is
        diffed against the existing cache:
        * Items absent from the new list fire DELETED.
        * Items present in both fire MODIFIED.
        * Items only in the new list fire ADDED.
        """
        kw = self._build_kwargs()
        resp = self._list_func(**kw)
        items = getattr(resp, "items", []) or []

        # Build key → item map for incoming items.
        new_items_map = {}
        for item in items:
            key = self._cache._key_func(item)
            new_items_map[key] = item

        # Snapshot the old keys before replacing the cache.
        old_keys = set(self._cache.list_keys())

        # Fire DELETED for items no longer present in the new list.
        for key in old_keys:
            if key not in new_items_map:
                old_obj = self._cache.get_by_key(key)
                if old_obj is not None:
                    self._fire(DELETED, old_obj)

        # Atomically replace the cache.
        self._cache._replace_all(items)

        # Fire ADDED for genuinely new items, MODIFIED for existing ones.
        for key, item in new_items_map.items():
            if key in old_keys:
                self._fire(MODIFIED, item)
            else:
                self._fire(ADDED, item)

        rv = None
        meta = getattr(resp, "metadata", None)
        if meta is not None:
            rv = getattr(meta, "resource_version", None)
        self._resource_version = rv or "0"

    def _run_loop(self):
        """Own LIST/WATCH retries and resume only from applied events.

        LIST deadlines are measured from successful LIST completion. A failed
        periodic LIST leaves its previous RV usable while its retry backs off;
        initial and expired-RV LISTs must succeed before another WATCH starts.
        """
        next_resync = float("inf")
        if self._resync_period > 0:
            last_list = self._last_list_time
            if last_list is None:
                last_list = time.monotonic()
            next_resync = last_list + self._resync_period
        list_retry_at = watch_retry_at = 0.0
        list_backoff = watch_backoff = 1.0
        while not self._stop_event.is_set():
            now = time.monotonic()
            list_required = self._resource_version is None
            list_due = max(next_resync, list_retry_at)
            if list_required:
                list_due = list_retry_at
            if now >= list_due:
                try:
                    self._initial_list()
                except Exception as exc:
                    logger.exception("Error during list; retrying")
                    self._fire(ERROR, exc)
                    list_retry_at = time.monotonic() + random.uniform(
                        list_backoff / 2, list_backoff)
                    list_backoff = min(60.0, list_backoff * 2)
                else:
                    list_backoff = 1.0
                    list_retry_at = 0.0
                    self._last_list_time = time.monotonic()
                    next_resync = (
                        self._last_list_time + self._resync_period
                        if self._resync_period > 0 else float("inf")
                    )
                continue

            if list_required:
                self._stop_event.wait(timeout=max(0, list_due - now))
                continue
            if now < watch_retry_at:
                self._stop_event.wait(
                    timeout=max(0, min(watch_retry_at, list_due) - now))
                continue

            # One HTTP request per stream: retries and expired RV recovery
            # belong here, so Watch's internal EOF retries cannot bypass
            # delays.
            self._watch = Watch(retry=False)
            kw = self._build_kwargs()
            kw["resource_version"] = self._resource_version
            if self._resync_period > 0:
                kw["timeout_seconds"] = max(1, math.ceil(list_due - now))
            watch_started = time.monotonic()
            watch_failed = False
            resync_requested = False
            stream = None
            try:
                stream = self._watch.stream(self._list_func, **kw)
                for event in stream:
                    if self._stop_event.is_set():
                        break
                    # A busy stream must also yield to a due periodic LIST.
                    if time.monotonic() >= list_due:
                        resync_requested = True
                        break
                    if event is None:
                        continue
                    evt_type = event.get("type")
                    obj = event.get("object")
                    if evt_type in (ADDED, MODIFIED):
                        self._cache._put(obj)
                    elif evt_type == DELETED:
                        self._cache._remove(obj)
                    elif evt_type == BOOKMARK:
                        obj = event.get("raw_object", obj)

                    if evt_type in (ADDED, MODIFIED, DELETED, BOOKMARK):
                        # Acknowledge only events applied to the cache (or a
                        # BOOKMARK), before notifying handlers. Watch advances
                        # its own RV during parsing, before cache mutation can
                        # fail or a stop request can interrupt processing.
                        if isinstance(obj, dict):
                            metadata = obj.get("metadata") or {}
                            resource_version = metadata.get("resourceVersion")
                        else:
                            metadata = getattr(obj, "metadata", None)
                            resource_version = getattr(
                                metadata, "resource_version", None)
                        if resource_version:
                            self._resource_version = resource_version

                    self._fire(evt_type, obj)
            except ApiException as exc:
                watch_failed = True
                if exc.status == 410:
                    logger.warning(
                        "Watch expired (410 Gone); will re-list from scratch"
                    )
                    self._resource_version = None
                else:
                    logger.warning(
                        "Watch failed (status=%s); reconnecting", exc.status)
                self._fire(ERROR, exc)
            except Exception as exc:
                watch_failed = True
                logger.exception(
                    "Unexpected error in watch loop; reconnecting")
                self._fire(ERROR, exc)
            finally:
                watch_finished = time.monotonic()
                # Explicitly finalize generators when stop/resync breaks the
                # loop, so their HTTP response is released before the next
                # LIST.
                try:
                    if hasattr(stream, "close"):
                        stream.close()
                except Exception as exc:
                    watch_failed = True
                    logger.exception(
                        "Error closing watch stream; reconnecting")
                    self._fire(ERROR, exc)
                finally:
                    self._watch = None

            duration = watch_finished - watch_started
            # An event or BOOKMARK alone does not prove a healthy connection.
            # Only a clean server timeout or long-lived EOF resets history;
            # a slow failure is still a failure.
            healthy = not watch_failed and (
                duration >= min(60, kw.get("timeout_seconds", 60))
            )
            # A planned relist is neither a failed connection nor evidence
            # of recovery. Preserve prior failures without adding a delay.
            if resync_requested and not watch_failed:
                watch_retry_at = watch_finished
                continue
            if healthy:
                watch_backoff = 1.0
                watch_retry_at = watch_finished
            else:
                watch_retry_at = watch_finished + random.uniform(
                    watch_backoff / 2, watch_backoff)
                watch_backoff = min(60.0, watch_backoff * 2)
