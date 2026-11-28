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
import random
import threading
import time

from urllib3.exceptions import ProtocolError, ReadTimeoutError

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

# Delay before reconnecting a failed watch: 0.8s doubling up to 30s, plus up
# to 100% jitter, so a persistent failure costs at most one request every
# 30-60s.
_WATCH_BACKOFF_INITIAL = 0.8
_WATCH_BACKOFF_MAX = 30.0
# The backoff starts over when it has not backed off for more than this many
# seconds, so a failure after a long healthy period starts again from 0.8s.
_WATCH_BACKOFF_RESET = 120.0
# Errors raised while reading a watch stream (connection reset or closed,
# incomplete read, read timeout) that mean the stream closed rather than
# failed, so the watch is resumed without waiting.
_WATCH_CLOSED_ERRORS = (ProtocolError, ReadTimeoutError)
# A stream that closes within this many seconds of the watch request without
# delivering an event is a failure ("very short watch"), so a server that
# ends every stream at once does not cause a reconnect loop.
_VERY_SHORT_WATCH = 1.0


def _list_items_and_resource_version(resp):
    """Return the items and resourceVersion of a list response.

    Supports both generated model objects and the plain dicts returned by
    CustomObjectsApi list functions.
    """
    if isinstance(resp, dict):
        meta = resp.get("metadata") or {}
        return resp.get("items") or [], meta.get("resourceVersion")
    items = getattr(resp, "items", []) or []
    meta = getattr(resp, "metadata", None)
    return items, getattr(meta, "resource_version", None)


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
        self._handlers = {ADDED: [], MODIFIED: [], DELETED: [], BOOKMARK: [], ERROR: []}
        self._handler_lock = threading.Lock()

        self._watch = None
        self._thread = None
        self._stop_event = threading.Event()
        self._resource_version = None  # most recent RV seen; None forces a full re-list
        # Guards _synced; notified after each list and by stop() after it
        # sets _stop_event.
        self._sync_cond = threading.Condition()
        self._synced = False

    # ---------------------------------------------------------------- #
    # Public API                                                        #
    # ---------------------------------------------------------------- #

    @property
    def cache(self):
        """The :class:`ObjectCache` maintained by this informer."""
        return self._cache

    def has_synced(self):
        """Return True once the initial list has been applied.

        The informer is synced when the objects of a full list are in
        :attr:`cache` and the ADDED, MODIFIED and DELETED handlers for that
        list have returned.  It stays synced afterwards, including during
        re-lists, watch failures and after :meth:`stop` and :meth:`start`,
        since the cache is kept across a restart.
        """
        return self._synced

    def wait_for_sync(self, timeout=None):
        """Block until the informer has synced (see :meth:`has_synced`).

        Returns True once synced.  Returns False when *timeout* seconds pass
        first, or when the informer is stopped (and not restarted) while
        waiting.  On a stopped informer it returns the current
        :meth:`has_synced` without waiting.  When called before
        :meth:`start`, it waits for the informer to be started and synced.

        Do not call it from an event handler: handlers run on the informer
        thread, which cannot finish the list while it waits.

        Parameters
        ----------
        timeout:
            Maximum number of seconds to wait.  None (the default) waits until
            the informer syncs or is stopped.
        """
        with self._sync_cond:
            self._sync_cond.wait_for(
                lambda: self._synced or self._stop_event.is_set(), timeout)
            return self._synced

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
        with self._sync_cond:
            self._sync_cond.notify_all()
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
        items, rv = _list_items_and_resource_version(resp)

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

        self._resource_version = rv or "0"
        with self._sync_cond:
            self._synced = True
            self._sync_cond.notify_all()

    def _run_loop(self):
        """Background loop: list then watch, reconnect on errors.

        After a watch error, including 410 Gone, the loop waits with an
        exponential backoff before it watches or lists again: the delay
        starts at 0.8s and doubles up to 30s, each wait adds up to 100%
        jitter (so at most 60s), and the delay starts over after 2 minutes
        without a backoff.  A stream that ends or drops (for example a
        connection reset) is watched again right away unless it closed
        within a second of the request without an event.
        Without ``resync_period``, ``Watch.stream`` reconnects a stream that
        ended normally by itself, so the loop only sees streams that drop.

        A full re-list is only performed when ``self._resource_version`` is
        ``None`` (first start or after a 410 Gone response).  On all other
        reconnects the most recent ``resourceVersion`` is reused so that no
        events are missed and the API server does not need to send a full
        object snapshot.
        """
        backoff_duration = _WATCH_BACKOFF_INITIAL
        last_backoff_at = time.monotonic()
        while not self._stop_event.is_set():
            # Full re-list only when we have no resource version to resume from.
            if self._resource_version is None:
                try:
                    self._initial_list()
                except Exception as exc:
                    logger.exception("Error during initial list; retrying")
                    self._fire(ERROR, exc)
                    self._stop_event.wait(timeout=5)
                    continue

            # Watch loop
            last_resync = time.monotonic()
            self._watch = Watch()
            kw = self._build_kwargs()
            kw["resource_version"] = self._resource_version
            # When a resync period is configured, set a matching server-side
            # watch timeout so that the stream exits after resync_period seconds
            # even if no events arrive.  Without this, a quiet period longer
            # than resync_period would never trigger a resync because the check
            # below only runs when the generator yields an event.
            if self._resync_period > 0:
                kw["timeout_seconds"] = max(1, int(self._resync_period))
            stream_closed = False
            got_event = False
            watch_start = time.monotonic()
            try:
                for event in self._watch.stream(self._list_func, **kw):
                    if self._stop_event.is_set():
                        break
                    got_event = True
                    evt_type = event.get("type")
                    obj = event.get("object")
                    # Sync the most recent resource version from the Watch
                    # instance (updated by unmarshal_event before yielding).
                    # Do this before firing handlers so consumers that wake on
                    # an event immediately see the advanced resource version.
                    if self._watch is not None and self._watch.resource_version:
                        self._resource_version = self._watch.resource_version
                    if evt_type == ADDED:
                        self._cache._put(obj)
                        self._fire(ADDED, obj)
                    elif evt_type == MODIFIED:
                        self._cache._put(obj)
                        self._fire(MODIFIED, obj)
                    elif evt_type == DELETED:
                        self._cache._remove(obj)
                        self._fire(DELETED, obj)
                    elif evt_type == BOOKMARK:
                        # BOOKMARK events carry an updated resource version but
                        # no object state change; the Watch instance already
                        # records the new resource_version internally.
                        self._fire(BOOKMARK, event.get("raw_object", obj))
                    elif evt_type == ERROR:
                        self._fire(ERROR, obj)
                stream_closed, watch_end = True, time.monotonic()
            except ApiException as exc:
                if exc.status == 410:
                    # The stored resource version is too old; force a full re-list.
                    logger.warning(
                        "Watch expired (410 Gone); will re-list from scratch"
                    )
                    self._resource_version = None
                else:
                    logger.warning(
                        "Watch stream ended with ApiException (status=%s); reconnecting",
                        exc.status,
                    )
                self._fire(ERROR, exc)
            except Exception as exc:
                stream_closed = isinstance(exc, _WATCH_CLOSED_ERRORS)
                watch_end = time.monotonic()
                logger.exception("Unexpected error in watch loop; reconnecting")
                self._fire(ERROR, exc)
            finally:
                # Capture the most recent resource version seen by the Watch
                # (updated on every ADDED/MODIFIED/DELETED/BOOKMARK event) so
                # that the next watch connection can resume without re-listing.
                # Do not overwrite a None that was set by a 410 handler above.
                if (
                    self._resource_version is not None
                    and self._watch is not None
                    and self._watch.resource_version
                ):
                    self._resource_version = self._watch.resource_version
                self._watch = None

            # Back off after any failure (410 included) and after a very short
            # watch, but not after a stream that closed.
            if not self._stop_event.is_set() and (not stream_closed or (
                    not got_event
                    and watch_end - watch_start < _VERY_SHORT_WATCH)):
                now = time.monotonic()
                if now - last_backoff_at > _WATCH_BACKOFF_RESET:
                    backoff_duration = _WATCH_BACKOFF_INITIAL
                last_backoff_at = now
                delay = backoff_duration + random.random() * backoff_duration
                backoff_duration = min(
                    backoff_duration * 2, _WATCH_BACKOFF_MAX)
                self._stop_event.wait(delay)

            # Periodic resync: after the watch stream exits (whether due to the
            # server-side timeout_seconds, a stop request, or an error) check if
            # a resync is due.  This path is what actually fires the resync when
            # the cluster is quiet and no events arrive for resync_period seconds.
            if (
                not self._stop_event.is_set()
                and self._resource_version is not None  # 410 already schedules a re-list
                and self._resync_period > 0
                and (time.monotonic() - last_resync) >= self._resync_period
            ):
                logger.debug("Informer resync triggered")
                try:
                    self._initial_list()
                except Exception as exc:
                    logger.exception("Error during resync list; continuing")
                    self._fire(ERROR, exc)
