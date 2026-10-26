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

"""Unit tests for kubernetes.informer."""

import json
import threading
import time
import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from kubernetes.client.exceptions import ApiException
from kubernetes.informer.cache import ObjectCache, _meta_namespace_key
from kubernetes.informer.informer import (ADDED, BOOKMARK, DELETED, ERROR,
                                          MODIFIED, SharedInformer)
from kubernetes.watch import Watch


def _make_pod(namespace, name):
    """Return a simple dict-based pod object."""
    return {"metadata": {"namespace": namespace, "name": name}}


class TestMetaNamespaceKey(unittest.TestCase):
    def test_namespaced_dict(self):
        obj = {"metadata": {"namespace": "ns", "name": "pod"}}
        self.assertEqual(_meta_namespace_key(obj), "ns/pod")

    def test_cluster_scoped_dict(self):
        obj = {"metadata": {"name": "node1"}}
        self.assertEqual(_meta_namespace_key(obj), "node1")

    def test_no_metadata(self):
        obj = MagicMock()
        obj.metadata = None
        self.assertEqual(_meta_namespace_key(obj), "")

    def test_model_object(self):
        meta = MagicMock()
        meta.namespace = "default"
        meta.name = "mypod"
        obj = MagicMock()
        obj.metadata = meta
        self.assertEqual(_meta_namespace_key(obj), "default/mypod")


class TestObjectCache(unittest.TestCase):
    def setUp(self):
        self.cache = ObjectCache()

    def test_put_and_list(self):
        pod = _make_pod("default", "p1")
        self.cache._put(pod)
        self.assertIn(pod, self.cache.list())

    def test_remove(self):
        pod = _make_pod("default", "p1")
        self.cache._put(pod)
        self.cache._remove(pod)
        self.assertEqual(self.cache.list(), [])

    def test_remove_nonexistent_is_noop(self):
        pod = _make_pod("default", "missing")
        self.cache._remove(pod)  # should not raise

    def test_replace_all(self):
        pod1 = _make_pod("default", "p1")
        pod2 = _make_pod("default", "p2")
        self.cache._put(pod1)
        self.cache._replace_all([pod2])
        keys = self.cache.list_keys()
        self.assertNotIn("default/p1", keys)
        self.assertIn("default/p2", keys)

    def test_get_by_key(self):
        pod = _make_pod("default", "p1")
        self.cache._put(pod)
        self.assertIs(self.cache.get_by_key("default/p1"), pod)
        self.assertIsNone(self.cache.get_by_key("default/ghost"))

    def test_get(self):
        pod = _make_pod("kube-system", "coredns")
        self.cache._put(pod)
        self.assertIs(self.cache.get(pod), pod)

    def test_thread_safety(self):
        """Concurrent puts should not raise exceptions."""
        errors = []

        def worker(n):
            try:
                for i in range(50):
                    self.cache._put(_make_pod("default", "pod-{}-{}".format(n, i)))
            except Exception as exc:
                errors.append(exc)

        threads = [threading.Thread(target=worker, args=(t,)) for t in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(errors, [])
        # Verify that the cache actually holds the objects that were put into it.
        for n in range(5):
            for i in range(50):
                key = "default/pod-{}-{}".format(n, i)
                self.assertIsNotNone(
                    self.cache.get_by_key(key),
                    "expected key {} in cache".format(key),
                )


class TestSharedInformerHandlers(unittest.TestCase):
    def setUp(self):
        self.list_func = MagicMock()
        # Minimal list response
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        self.list_func.return_value = list_resp

        self.informer = SharedInformer(list_func=self.list_func)

    def test_add_handler_and_fire(self):
        received = []
        self.informer.add_event_handler(ADDED, received.append)
        pod = _make_pod("default", "p1")
        self.informer._fire(ADDED, pod)
        self.assertEqual(received, [pod])

    def test_remove_handler(self):
        received = []
        self.informer.add_event_handler(ADDED, received.append)
        self.informer.remove_event_handler(ADDED, received.append)
        self.informer._fire(ADDED, _make_pod("default", "p1"))
        self.assertEqual(received, [])

    def test_remove_unknown_handler_noop(self):
        self.informer.remove_event_handler(MODIFIED, lambda x: x)  # should not raise

    def test_invalid_event_type_raises(self):
        with self.assertRaises(ValueError):
            self.informer.add_event_handler("UNKNOWN", lambda x: x)

    def test_handler_exception_is_swallowed(self):
        """A crashing handler must not stop the informer loop."""
        def bad_handler(obj):
            raise RuntimeError("boom")

        self.informer.add_event_handler(ADDED, bad_handler)
        # Should not raise
        self.informer._fire(ADDED, _make_pod("default", "p1"))


class TestSharedInformerWatchLoop(unittest.TestCase):
    """Test the watch loop by mocking Watch.stream."""

    def _make_informer_with_events(self, events):
        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)

        def fake_stream(func, **kw):
            yield from events
            informer.stop()

        mock_watch = MagicMock()
        mock_watch.stream.side_effect = fake_stream
        informer._watch_factory = lambda: mock_watch
        return informer, mock_watch

    def test_added_event_updates_cache(self):
        pod = _make_pod("default", "new-pod")
        events = [{"type": "ADDED", "object": pod}]
        informer, _ = self._make_informer_with_events(events)

        received = []
        informer.add_event_handler(ADDED, received.append)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()

            def fake_stream(func, **kw):
                yield from events
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        self.assertIn(pod, informer.cache.list())
        self.assertIn(pod, received)

    def test_deleted_event_removes_from_cache(self):
        pod = _make_pod("default", "gone-pod")
        events = [
            {"type": "ADDED", "object": pod},
            {"type": "DELETED", "object": pod},
        ]

        deleted = []
        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)
        informer.add_event_handler(DELETED, deleted.append)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()

            def fake_stream(func, **kw):
                yield from events
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        self.assertEqual(informer.cache.list(), [])
        self.assertIn(pod, deleted)

    def test_modified_event_updates_cache(self):
        pod_v1 = _make_pod("default", "mod-pod")
        pod_v2 = dict(pod_v1)
        pod_v2["status"] = "Running"

        events = [
            {"type": "ADDED", "object": pod_v1},
            {"type": "MODIFIED", "object": pod_v2},
        ]

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()

            def fake_stream(func, **kw):
                yield from events
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        cached = informer.cache.get_by_key("default/mod-pod")
        self.assertIs(cached, pod_v2)


    def test_start_is_idempotent(self):
        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            mock_w.stream.return_value = iter([])
            MockWatch.return_value = mock_w

            informer.start()
            first_thread = informer._thread
            informer.start()  # should be a no-op
            self.assertIs(informer._thread, first_thread)
            informer.stop()

    def test_bookmark_event_fires_handler(self):
        bookmark_obj = {"metadata": {"resourceVersion": "42"}}
        events = [
            {"type": "BOOKMARK", "object": bookmark_obj, "raw_object": bookmark_obj},
        ]

        received = []
        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)
        informer.add_event_handler(BOOKMARK, received.append)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()

            def fake_stream(func, **kw):
                yield from events
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        self.assertEqual(len(received), 1)
        self.assertEqual(received[0], bookmark_obj)
        # Cache should be unchanged (BOOKMARK does not add/modify/delete objects)
        self.assertEqual(informer.cache.list(), [])

    def test_bookmark_event_does_not_modify_cache(self):
        pod = _make_pod("default", "stable-pod")
        bookmark_obj = {"metadata": {"resourceVersion": "99"}}
        events = [
            {"type": "ADDED", "object": pod},
            {"type": "BOOKMARK", "object": bookmark_obj, "raw_object": bookmark_obj},
        ]

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()

            def fake_stream(func, **kw):
                yield from events
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        # BOOKMARK must not have altered the cache content
        cached = informer.cache.list()
        self.assertEqual(len(cached), 1)
        self.assertIs(cached[0], pod)

    def test_bookmark_handler_receives_raw_dict(self):
        """BOOKMARK handlers receive the raw dict, not a deserialized model.

        Watch intentionally skips deserialization for BOOKMARK events (PR #2505)
        because BOOKMARK objects may be incomplete. The informer passes
        ``event.get('raw_object', obj)`` to the BOOKMARK handler, so it must
        always be a dict rather than a typed Kubernetes model object.
        """
        bookmark_obj = {"metadata": {"resourceVersion": "77"}}
        received = []

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)
        informer.add_event_handler(BOOKMARK, received.append)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            mock_w.resource_version = "77"

            def fake_stream(func, **kw):
                yield {"type": "BOOKMARK", "object": bookmark_obj, "raw_object": bookmark_obj}
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        self.assertEqual(len(received), 1)
        # Must be the raw dict, not a deserialized model.
        self.assertIsInstance(received[0], dict)
        self.assertEqual(received[0]["metadata"]["resourceVersion"], "77")

    def test_multiple_bookmarks_advance_resource_version_to_latest(self):
        """Multiple BOOKMARK events each update _resource_version to the latest value."""
        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()

            def fake_stream(func, **kw):
                for rv in ["10", "20", "30"]:
                    bk = {"metadata": {"resourceVersion": rv}}
                    mock_w.resource_version = rv
                    yield {"type": "BOOKMARK", "object": bk, "raw_object": bk}
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        self.assertEqual(informer._resource_version, "30")

    def test_resync_period_triggers_full_list(self):
        """A full List call must be made to the API server on every resync_period.

        With the new implementation the watch stream is given a server-side
        timeout equal to resync_period (via timeout_seconds).  When the stream
        exits, the elapsed-time check fires the resync even if no events
        arrived – this is exactly the scenario this test exercises.
        """
        pod = _make_pod("default", "resync-pod")

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = [pod]
        list_resp.metadata = MagicMock(resource_version="5")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func, resync_period=60)

        stream_calls = {"n": 0}

        with patch("kubernetes.informer.informer.Watch") as MockWatch, \
                patch("kubernetes.informer.informer.time") as mock_time:
            clock = [0.0]
            mock_time.monotonic.side_effect = lambda: clock[0]

            mock_w = MagicMock()
            mock_w.resource_version = "5"

            def fake_stream(func, **kw):
                stream_calls["n"] += 1
                if stream_calls["n"] == 1:
                    # Simulate the stream timing out (timeout_seconds expired)
                    # with no events – the resync should fire after this returns.
                    clock[0] = 61.0
                    return iter([])
                # Second iteration: stop the informer.
                informer._stop_event.set()
                return iter([])

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        # list_func called once for the initial list + once for the resync = 2
        self.assertEqual(list_func.call_count, 2)

    # ------------------------------------------------------------------
    # Tests analogous to the JavaScript cache_test.ts and Java
    # DefaultSharedIndexInformerWireMockTest scenarios.
    # ------------------------------------------------------------------

    def test_multiple_handlers_all_fire(self):
        """All handlers registered for the same event type must be invoked."""
        pod = _make_pod("default", "multi-pod")
        received1 = []
        received2 = []

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)
        informer.add_event_handler(ADDED, received1.append)
        informer.add_event_handler(ADDED, received2.append)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()

            def fake_stream(func, **kw):
                yield {"type": "ADDED", "object": pod}
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        self.assertEqual(received1, [pod])
        self.assertEqual(received2, [pod])

    def test_selectors_and_namespace_forwarded(self):
        """namespace, label_selector, and field_selector are forwarded to list_func
        and Watch.stream kwargs."""
        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(
            list_func=list_func,
            namespace="kube-system",
            label_selector="app=myapp",
            field_selector="status.phase=Running",
        )

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            mock_w.resource_version = "1"

            def fake_stream(func, **kw):
                informer._stop_event.set()
                return iter([])

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        # Initial list call must include all selectors.
        list_func.assert_called_once_with(
            namespace="kube-system",
            label_selector="app=myapp",
            field_selector="status.phase=Running",
        )
        # Watch.stream must also receive them.
        _, stream_kw = mock_w.stream.call_args
        self.assertEqual(stream_kw.get("namespace"), "kube-system")
        self.assertEqual(stream_kw.get("label_selector"), "app=myapp")
        self.assertEqual(stream_kw.get("field_selector"), "status.phase=Running")

    def test_watch_resource_version_passed_after_initial_list(self):
        """After the initial list, Watch.stream is called with that list's resourceVersion."""
        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="42")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            mock_w.resource_version = "42"

            def fake_stream(func, **kw):
                informer._stop_event.set()
                return iter([])

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        _, stream_kw = mock_w.stream.call_args
        self.assertEqual(stream_kw.get("resource_version"), "42")

    def test_non_410_api_exception_reconnects_without_relist(self):
        """A non-410 ApiException fires ERROR and reconnects without calling list_func again."""
        from kubernetes.client.exceptions import ApiException

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        error_received = []
        informer = SharedInformer(list_func=list_func)
        informer.add_event_handler(ERROR, error_received.append)

        stream_calls = {"n": 0}

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            mock_w.resource_version = "1"

            def fake_stream(func, **kw):
                stream_calls["n"] += 1
                if stream_calls["n"] == 1:
                    raise ApiException(status=409, reason="Conflict")
                informer._stop_event.set()
                return iter([])

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        # ERROR fires once for the 409; list_func not called a second time.
        self.assertEqual(len(error_received), 1)
        self.assertIsInstance(error_received[0], ApiException)
        self.assertEqual(error_received[0].status, 409)
        self.assertEqual(list_func.call_count, 1)
        self.assertEqual(stream_calls["n"], 2)

    def test_list_func_error_fires_error_handler(self):
        """If the list function raises an exception the ERROR handler is called."""
        from kubernetes.client.exceptions import ApiException

        def always_fails(**kw):
            raise ApiException(status=403, reason="Forbidden")

        error_received = []
        informer = SharedInformer(list_func=always_fails)

        def on_error(exc):
            error_received.append(exc)
            informer._stop_event.set()  # stop after first error so the test is fast

        informer.add_event_handler(ERROR, on_error)

        with patch("kubernetes.informer.informer.Watch"):
            informer.start()
            informer._thread.join(timeout=3)

        self.assertEqual(len(error_received), 1)
        self.assertIsInstance(error_received[0], ApiException)
        self.assertEqual(error_received[0].status, 403)

    def test_initial_list_fires_added_for_each_item(self):
        """Items returned by the initial list must each fire an ADDED event."""
        pod1 = _make_pod("default", "pod1")
        pod2 = _make_pod("default", "pod2")

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = [pod1, pod2]
        list_resp.metadata = MagicMock(resource_version="5")
        list_func.return_value = list_resp

        received = []
        informer = SharedInformer(list_func=list_func)
        informer.add_event_handler(ADDED, received.append)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            mock_w.resource_version = "5"

            def fake_stream(func, **kw):
                informer._stop_event.set()
                return iter([])

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        self.assertIn(pod1, received)
        self.assertIn(pod2, received)
        self.assertEqual(len(received), 2)

    def test_relist_after_410_fires_delete_for_removed_items(self):
        """After a 410-triggered re-list, items absent from the new list fire DELETED."""
        from kubernetes.client.exceptions import ApiException

        pod_keep = _make_pod("default", "pod-keep")
        pod_delete = _make_pod("default", "pod-delete")

        list_call = {"n": 0}

        def list_func(**kw):
            list_call["n"] += 1
            resp = MagicMock()
            if list_call["n"] == 1:
                resp.items = [pod_keep, pod_delete]
            else:
                resp.items = [pod_keep]   # pod_delete is gone after 410 re-list
            resp.metadata = MagicMock(resource_version=str(list_call["n"]))
            return resp

        deleted = []
        informer = SharedInformer(list_func=list_func)
        informer.add_event_handler(DELETED, deleted.append)

        stream_calls = {"n": 0}

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            mock_w.resource_version = "1"

            def fake_stream(func, **kw):
                stream_calls["n"] += 1
                if stream_calls["n"] == 1:
                    raise ApiException(status=410, reason="Gone")
                informer._stop_event.set()
                return iter([])

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        self.assertIn(pod_delete, deleted)
        self.assertNotIn(pod_keep, deleted)
        self.assertIsNone(informer.cache.get_by_key("default/pod-delete"))
        self.assertIsNotNone(informer.cache.get_by_key("default/pod-keep"))

    def test_reconnect_skips_relist_when_rv_known(self):
        """On reconnect without 410 the informer must NOT call the list function again."""
        pod = _make_pod("default", "reconnect-pod")

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = [pod]
        list_resp.metadata = MagicMock(resource_version="5")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)

        stream_calls = {"n": 0}

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            mock_w.resource_version = "7"

            def fake_stream(func, **kw):
                stream_calls["n"] += 1
                if stream_calls["n"] == 1:
                    # First stream: yield nothing then let it reconnect
                    return iter([])
                # Second stream: stop the informer
                informer._stop_event.set()
                return iter([])

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        # list_func is called only once (initial list); reconnect reuses the RV.
        self.assertEqual(list_func.call_count, 1)
        self.assertEqual(stream_calls["n"], 2)

    # ------------------------------------------------------------------
    # Tests analogous to client-go shared_informer_test.go scenarios.
    # ------------------------------------------------------------------

    def test_same_handler_registered_twice_fires_twice(self):
        """Registering the same callable twice is two independent registrations.

        Analogous to Go TestSharedInformerMultipleRegistration: the same
        handler callable can be added twice, fires twice per event, and
        removing one registration leaves the other active.
        """
        pod = _make_pod("default", "dup-pod")
        received = []

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)
        handler = received.append
        informer.add_event_handler(ADDED, handler)
        informer.add_event_handler(ADDED, handler)  # same callable, second registration

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()

            def fake_stream(func, **kw):
                yield {"type": "ADDED", "object": pod}
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        # Two registrations → two calls
        self.assertEqual(received.count(pod), 2)

        # After removing one registration the other still works.
        informer.remove_event_handler(ADDED, handler)
        received.clear()
        informer._fire(ADDED, pod)
        self.assertEqual(received.count(pod), 1)

    def test_remove_handler_while_running_stops_events(self):
        """Removing a handler mid-run stops it receiving subsequent events.

        Analogous to Go TestRemoveWhileActive.
        """
        pod1 = _make_pod("default", "pod1")
        pod2 = _make_pod("default", "pod2")
        received = []

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        # pod1_seen is set by the handler after pod1 is processed.
        pod1_seen = threading.Event()
        # can_send_pod2 is set by the test thread to allow pod2 to be yielded.
        can_send_pod2 = threading.Event()

        informer = SharedInformer(list_func=list_func)

        def handler(obj):
            received.append(obj)
            if obj is pod1:
                pod1_seen.set()

        informer.add_event_handler(ADDED, handler)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()

            def fake_stream(func, **kw):
                yield {"type": "ADDED", "object": pod1}
                # Block until the test thread has removed the handler.
                can_send_pod2.wait(timeout=5)
                yield {"type": "ADDED", "object": pod2}
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            # Wait until pod1 has been processed, then remove the handler.
            pod1_seen.wait(timeout=3)
            informer.remove_event_handler(ADDED, handler)
            can_send_pod2.set()
            informer._thread.join(timeout=3)

        self.assertIn(pod1, received)
        self.assertNotIn(pod2, received)

    def test_add_handler_while_running_receives_subsequent_events(self):
        """Adding a handler while the informer is running fires it for subsequent events.

        Analogous to Go TestAddWhileActive.
        """
        pod1 = _make_pod("default", "pod1-aw")
        pod2 = _make_pod("default", "pod2-aw")
        received1 = []
        received2 = []

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        pod1_processed = threading.Event()
        can_send_pod2 = threading.Event()

        informer = SharedInformer(list_func=list_func)
        informer.add_event_handler(ADDED, received1.append)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()

            def fake_stream(func, **kw):
                yield {"type": "ADDED", "object": pod1}
                # Signal that pod1 has been yielded and processed.
                pod1_processed.set()
                # Wait until the test thread registers handler2.
                can_send_pod2.wait(timeout=5)
                yield {"type": "ADDED", "object": pod2}
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            # After pod1 is processed, register the second handler.
            pod1_processed.wait(timeout=3)
            informer.add_event_handler(ADDED, received2.append)
            can_send_pod2.set()
            informer._thread.join(timeout=3)

        # handler1 sees both pods; handler2 (added late) only sees pod2.
        self.assertIn(pod1, received1)
        self.assertIn(pod2, received1)
        self.assertNotIn(pod1, received2)
        self.assertIn(pod2, received2)

    def test_concurrent_handler_registration_is_thread_safe(self):
        """Concurrent add/remove of handlers from many threads must not raise.

        Analogous to Go TestSharedInformerHandlerAbuse (thread safety portion).
        """
        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="1")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)
        errors = []

        def worker():
            try:
                for _ in range(30):
                    fn = lambda obj: None  # noqa: E731
                    informer.add_event_handler(ADDED, fn)
                    informer.add_event_handler(MODIFIED, fn)
                    informer.remove_event_handler(ADDED, fn)
                    informer.remove_event_handler(MODIFIED, fn)
            except Exception as exc:
                errors.append(exc)

        threads = [threading.Thread(target=worker) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        self.assertEqual(errors, [])

    def test_watch_disruption_existing_items_fire_modified_after_relist(self):
        """After a 410-triggered re-list, items in both old and new list fire MODIFIED.

        Analogous to Go TestSharedInformerWatchDisruption: when a watch is
        disrupted and the re-list returns the same objects (possibly with
        updates), listeners receive MODIFIED for them.
        """
        from kubernetes.client.exceptions import ApiException

        pod = _make_pod("default", "stable-pod")

        list_call = {"n": 0}

        def list_func(**kw):
            list_call["n"] += 1
            resp = MagicMock()
            resp.items = [pod]  # pod present in both lists
            resp.metadata = MagicMock(resource_version=str(list_call["n"]))
            return resp

        modified = []
        added = []
        deleted = []
        informer = SharedInformer(list_func=list_func)
        informer.add_event_handler(MODIFIED, modified.append)
        informer.add_event_handler(ADDED, added.append)
        informer.add_event_handler(DELETED, deleted.append)

        stream_calls = {"n": 0}

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            mock_w.resource_version = "1"

            def fake_stream(func, **kw):
                stream_calls["n"] += 1
                if stream_calls["n"] == 1:
                    raise ApiException(status=410, reason="Gone")
                informer._stop_event.set()
                return iter([])

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        # pod was in both the initial list (call 1) and the re-list (call 2).
        # On the re-list it should fire MODIFIED (not ADDED again).
        self.assertIn(pod, modified)
        # ADDED fires exactly once: for the initial list.  The re-list must
        # NOT fire a second ADDED for an already-cached item.
        self.assertEqual(len(added), 1, "ADDED should fire once (initial list) but not again on re-list")
        # DELETED must not fire for an item present in both lists.
        self.assertEqual(deleted, [], "DELETED should not fire for an item present in both lists")
        # Still in cache.
        self.assertIsNotNone(informer.cache.get_by_key("default/stable-pod"))


class TestSharedInformerWatchCheckpoint(unittest.TestCase):
    """Exercise checkpoints with the real Watch parser and retry scheduler."""

    def setUp(self):
        # Timing is verified separately with a fake clock below.
        jitter = patch(
            "kubernetes.informer.informer.random.uniform",
            return_value=0)
        jitter.start()
        self.addCleanup(jitter.stop)

    def _make_checkpoint_object(self, resource_version):
        return {
            "metadata": {
                "namespace": "default",
                "name": "pod",
                "resourceVersion": resource_version,
            }
        }

    def _make_event(self, event_type, resource_version):
        return {
            "type": event_type,
            "object": self._make_checkpoint_object(resource_version),
        }

    def _make_watch_response(self, *events):
        response = MagicMock()
        response.status = 200
        response.stream.return_value = iter(
            (
                (json.dumps(event) if isinstance(event, dict) else event)
                + "\n"
            ).encode()
            for event in events
        )
        return response

    def _make_list_source(self, responses, initial_items=()):
        responses = iter(responses)
        requests = []

        def list_func(**kwargs):
            requests.append(kwargs)
            if not kwargs.get("watch"):
                return SimpleNamespace(
                    items=list(initial_items),
                    metadata=SimpleNamespace(resource_version="10"),
                )
            return next(responses)

        return list_func, requests

    def _stop_on_error(self, informer):
        errors = []

        def on_error(error):
            errors.append(error)
            informer.stop()

        informer.add_event_handler(ERROR, on_error)
        return errors

    def test_watch_reconnect_uses_applied_event_and_bookmark(self):
        for return_type in [None, "V1Pod"]:
            with self.subTest(return_type=return_type):
                list_func, requests = self._make_list_source(
                    [
                        self._make_watch_response(
                            self._make_event(ADDED, "11")
                        ),
                        self._make_watch_response(
                            {
                                "type": BOOKMARK,
                                "object": {
                                    "metadata": {"resourceVersion": "12"}
                                },
                            }
                        ),
                        self._make_watch_response(
                            self._make_event(MODIFIED, "13")
                        ),
                    ]
                )
                informer = SharedInformer(list_func)
                errors = self._stop_on_error(informer)
                checkpoints = []
                bookmark_cache = []
                informer.add_event_handler(
                    ADDED,
                    lambda obj: checkpoints.append(informer._resource_version),
                )

                def on_bookmark(obj):
                    checkpoints.append(informer._resource_version)
                    bookmark_cache.extend(informer.cache.list_keys())

                informer.add_event_handler(BOOKMARK, on_bookmark)
                informer.add_event_handler(
                    MODIFIED, lambda obj: informer.stop()
                )
                with patch(
                    "kubernetes.informer.informer.Watch",
                    side_effect=lambda **kw: Watch(return_type, **kw),
                ) as factory:
                    informer._run_loop()

                self.assertFalse(errors)
                # Each reconnect passes through the informer scheduler.
                self.assertEqual(factory.call_count, 3)
                self.assertEqual(
                    [
                        request["resource_version"]
                        for request in requests
                        if request.get("watch")
                    ],
                    ["10", "11", "12"],
                )
                self.assertEqual(checkpoints, ["11", "12"])
                self.assertEqual(bookmark_cache, ["default/pod"])
                self.assertEqual(informer._resource_version, "13")

    def test_empty_and_invalid_lines_do_not_interrupt_watch(self):
        for return_type in [None, "V1Pod"]:
            with self.subTest(return_type=return_type):
                response = self._make_watch_response(
                    "", "not json", self._make_event(ADDED, "11")
                )
                list_func, requests = self._make_list_source([response])
                informer = SharedInformer(list_func)
                errors = self._stop_on_error(informer)
                informer.add_event_handler(ADDED, lambda obj: informer.stop())

                with patch(
                    "kubernetes.informer.informer.Watch",
                    lambda **kw: Watch(return_type, **kw),
                ):
                    informer._run_loop()

                self.assertFalse(errors)
                # One LIST and one WATCH, with no reconnect.
                self.assertEqual(len(requests), 2)
                self.assertIsNotNone(informer.cache.get_by_key("default/pod"))
                self.assertEqual(informer._resource_version, "11")
                response.close.assert_called_once()
                response.release_conn.assert_called_once()

    def test_unknown_event_does_not_advance_internal_watch_checkpoint(self):
        list_func, requests = self._make_list_source(
            [
                self._make_watch_response(self._make_event("UNKNOWN", "11")),
                self._make_watch_response(self._make_event(ADDED, "12")),
            ]
        )
        informer = SharedInformer(list_func)
        errors = self._stop_on_error(informer)
        informer.add_event_handler(ADDED, lambda obj: informer.stop())
        with patch(
            "kubernetes.informer.informer.Watch",
            lambda **kw: Watch("V1Pod", **kw)
        ):
            informer._run_loop()

        self.assertFalse(errors)
        self.assertEqual(
            [
                request["resource_version"]
                for request in requests
                if request.get("watch")
            ],
            ["10", "10"],
        )
        self.assertEqual(informer._resource_version, "12")

    def test_cache_failure_reconnects_from_last_applied_event(self):
        for return_type in [None, "V1Pod"]:
            for event_type in [ADDED, MODIFIED, DELETED]:
                with self.subTest(
                    return_type=return_type, event_type=event_type
                ):
                    list_func, requests = self._make_list_source(
                        [
                            self._make_watch_response(
                                self._make_event(event_type, "11")
                            ),
                            self._make_watch_response(
                                self._make_event(event_type, "11")
                            ),
                        ],
                        initial_items=(
                            [self._make_checkpoint_object("10")]
                            if event_type != ADDED
                            else []
                        ),
                    )
                    failed = False

                    def key_func(obj):
                        nonlocal failed
                        resource_version = (
                            obj["metadata"]["resourceVersion"]
                            if isinstance(obj, dict)
                            else obj.metadata.resource_version
                        )
                        if resource_version == "11" and not failed:
                            failed = True
                            raise ValueError("cache key failed")
                        return _meta_namespace_key(obj)

                    informer = SharedInformer(list_func, key_func=key_func)
                    errors = []
                    informer.add_event_handler(ERROR, errors.append)
                    checkpoints = []

                    def on_applied(obj):
                        resource_version = (
                            obj["metadata"]["resourceVersion"]
                            if isinstance(obj, dict)
                            else obj.metadata.resource_version
                        )
                        if resource_version == "11":
                            checkpoints.append(informer._resource_version)
                            informer.stop()

                    informer.add_event_handler(event_type, on_applied)
                    # Stop on unexpected exhaustion instead of retrying
                    # an invalid test fixture.
                    informer.add_event_handler(
                        ERROR,
                        lambda error: (
                            informer.stop()
                            if isinstance(error, StopIteration)
                            else None
                        ),
                    )
                    with patch(
                        "kubernetes.informer.informer.Watch",
                        lambda **kw: Watch(return_type, **kw),
                    ):
                        informer._run_loop()

                    self.assertEqual(len(errors), 1)
                    self.assertIsInstance(errors[0], ValueError)
                    self.assertEqual(
                        [
                            request["resource_version"]
                            for request in requests
                            if request.get("watch")
                        ],
                        ["10", "10"],
                    )
                    self.assertEqual(checkpoints, ["11"])
                    self.assertEqual(
                        informer.cache.get_by_key("default/pod") is None,
                        event_type == DELETED,
                    )

    def test_handler_failure_preserves_applied_checkpoint_and_other_handlers(
        self,
    ):
        list_func, requests = self._make_list_source(
            [
                self._make_watch_response(self._make_event(ADDED, "11")),
                self._make_watch_response(self._make_event(MODIFIED, "12")),
            ]
        )
        informer = SharedInformer(list_func)
        errors = self._stop_on_error(informer)
        checkpoints = []

        def failing_handler(obj):
            raise ValueError("handler failed after cache application")

        informer.add_event_handler(ADDED, failing_handler)
        informer.add_event_handler(
            ADDED, lambda obj: checkpoints.append(informer._resource_version)
        )
        informer.add_event_handler(MODIFIED, lambda obj: informer.stop())
        informer._run_loop()

        # Handler failures retain the existing log-and-continue policy.
        self.assertFalse(errors)
        self.assertEqual(checkpoints, ["11"])
        self.assertEqual(
            [
                request["resource_version"]
                for request in requests
                if request.get("watch")
            ],
            ["10", "11"],
        )
        self.assertEqual(informer._resource_version, "12")

    def test_stop_after_deserialization_replays_unapplied_event_on_restart(
        self,
    ):
        list_func, requests = self._make_list_source(
            [
                self._make_watch_response(self._make_event(ADDED, "11")),
                self._make_watch_response(self._make_event(ADDED, "11")),
            ]
        )
        informer = SharedInformer(list_func)
        errors = self._stop_on_error(informer)
        first_watch = Watch("V1Pod")
        unmarshal_event = first_watch.unmarshal_event

        def stop_after_unmarshal(data, return_type):
            event = unmarshal_event(data, return_type)
            # Simulate stop between parsing and cache application.
            informer.stop()
            return event

        first_watch.unmarshal_event = stop_after_unmarshal
        with patch(
            "kubernetes.informer.informer.Watch", return_value=first_watch
        ):
            informer._run_loop()

        # Received, but not applied.
        self.assertEqual(first_watch.resource_version, "11")
        self.assertEqual(informer.cache.list(), [])
        checkpoint_after_stop = informer._resource_version
        informer.add_event_handler(ADDED, lambda obj: informer.stop())
        informer._stop_event.clear()
        with patch(
            "kubernetes.informer.informer.Watch",
            lambda **kw: Watch("V1Pod", **kw)
        ):
            informer._run_loop()

        self.assertFalse(errors)
        self.assertEqual(checkpoint_after_stop, "10")
        self.assertEqual(
            [
                request["resource_version"]
                for request in requests
                if request.get("watch")
            ],
            ["10", "10"],
        )
        self.assertIsNotNone(informer.cache.get_by_key("default/pod"))
        self.assertEqual(informer._resource_version, "11")

    def test_repeated_410_relists_without_restoring_expired_checkpoint(self):
        expired = {
            "type": ERROR,
            "object": {
                "code": 410,
                "reason": "Gone",
                "message": "resource version expired",
            },
        }
        list_func, requests = self._make_list_source(
            [
                self._make_watch_response(
                    self._make_event(ADDED, "11"), expired
                ),
                self._make_watch_response(expired),
                self._make_watch_response(self._make_event(MODIFIED, "12")),
            ]
        )
        informer = SharedInformer(list_func)
        errors = []
        informer.add_event_handler(ERROR, errors.append)
        informer.add_event_handler(
            ERROR,
            lambda error: (
                informer.stop()
                if not isinstance(error, ApiException)
                else None
            ),
        )
        informer.add_event_handler(MODIFIED, lambda obj: informer.stop())
        with patch(
            "kubernetes.informer.informer.Watch",
            lambda **kw: Watch("V1Pod", **kw)
        ):
            informer._run_loop()

        self.assertEqual(len(errors), 2)
        self.assertTrue(all(isinstance(error, ApiException)
                        for error in errors))
        self.assertTrue(all(error.status == 410 for error in errors))
        self.assertEqual(
            [
                request["resource_version"]
                for request in requests
                if request.get("watch")
            ],
            ["10", "10", "10"],
        )
        self.assertEqual(
            len([request for request in requests if not request.get("watch")]),
            3,
        )
        self.assertEqual(informer._resource_version, "12")


class TestSharedInformerRetryScheduling(unittest.TestCase):
    """Exercise scheduler deadlines without sleeping or replacing Watch."""

    def setUp(self):
        self.now = 0.0
        self.requests = []
        self.waits = []
        self.list_action = None
        self.watch_action = None
        clock = patch("kubernetes.informer.informer.time.monotonic",
                      side_effect=lambda: self.now)
        jitter = patch("kubernetes.informer.informer.random.uniform",
                       side_effect=lambda lower, upper: upper)
        clock.start()
        self.jitter = jitter.start()
        self.addCleanup(clock.stop)
        self.addCleanup(jitter.stop)

    def _make_informer(self, resync_period=0):
        def source(**kwargs):
            watching = kwargs.get("watch", False)
            self.requests.append(("watch" if watching else "list",
                                  self.now, kwargs))
            if watching:
                return self.watch_action()
            if self.list_action:
                return self.list_action()
            return SimpleNamespace(
                items=[], metadata=SimpleNamespace(resource_version="10"))

        informer = SharedInformer(source, resync_period=resync_period)

        def wait(timeout):
            self.assertGreater(timeout, 0)
            self.waits.append(timeout)
            self.assertLess(len(self.waits), 30, "unexpected retry loop")
            self.now += timeout
            return False

        informer._stop_event.wait = MagicMock(side_effect=wait)
        return informer

    def _response(self, duration=0, events=(), error=None):
        def chunks():
            self.now += duration
            for event in events:
                line = json.dumps(event) if isinstance(event, dict) else event
                yield (line + "\n").encode()
            if error:
                raise error

        response = MagicMock()
        response.status = 200
        response.stream.side_effect = lambda **kwargs: chunks()
        return response

    def _event(self, event_type=BOOKMARK):
        return {"type": event_type,
                "object": {"metadata": {"name": "pod",
                                        "resourceVersion": "11"}}}

    def test_short_streams_back_off_even_after_events_or_bookmarks(self):
        for event_type in [None, ADDED, BOOKMARK]:
            with self.subTest(event_type=event_type):
                self.now = 0
                self.requests.clear()
                self.waits.clear()
                informer = self._make_informer()
                count = [0]

                def watch():
                    count[0] += 1
                    if count[0] == 4:
                        informer._stop_event.set()
                    events = [self._event(event_type)] if event_type else []
                    return self._response(events=events)

                self.watch_action = watch
                informer._run_loop()
                self.assertEqual(self.waits, [1, 2, 4])
                self.assertEqual(
                    [t for op, t, _ in self.requests if op == "watch"],
                    [0, 1, 3, 7])

    def test_slow_watch_errors_keep_failure_history_and_cap_jitter(self):
        informer = self._make_informer()
        count = [0]

        def watch():
            count[0] += 1
            if count[0] == 9:
                informer._stop_event.set()
                return self._response()
            return self._response(
                duration=70, error=RuntimeError("read failed"))

        self.watch_action = watch
        informer._run_loop()
        self.assertEqual(self.waits, [1, 2, 4, 8, 16, 32, 60, 60])
        self.assertEqual(
            [entry.args for entry in self.jitter.call_args_list[:8]],
            [(0.5, 1), (1, 2), (2, 4), (4, 8), (8, 16),
             (16, 32), (30, 60), (30, 60)])

    def test_long_clean_watch_resets_backoff(self):
        informer = self._make_informer()
        count = [0]

        def watch():
            count[0] += 1
            if count[0] == 5:
                informer._stop_event.set()
            return self._response(duration=60 if count[0] == 3 else 0)

        self.watch_action = watch
        informer._run_loop()
        self.assertEqual(self.waits, [1, 2, 1])
        self.assertEqual([t for op, t, _ in self.requests if op == "watch"],
                         [0, 1, 3, 63, 64])

    def test_backoff_wakes_for_periodic_list_before_next_watch(self):
        informer = self._make_informer(resync_period=5)
        count = [0]

        def watch():
            count[0] += 1
            if count[0] == 4:
                informer._stop_event.set()
            return self._response()

        self.watch_action = watch
        informer._run_loop()
        self.assertEqual([(op, t) for op, t, _ in self.requests],
                         [("list", 0), ("watch", 0), ("watch", 1),
                          ("watch", 3), ("list", 5), ("watch", 7)])
        self.assertEqual([kw["timeout_seconds"] for op, _, kw in self.requests
                          if op == "watch"], [5, 4, 2, 3])

    def test_periodic_list_failures_back_off_while_watch_keeps_delivering(
            self):
        informer = self._make_informer(resync_period=2)
        list_count = [0]

        def list_objects():
            list_count[0] += 1
            if list_count[0] == 1:
                return SimpleNamespace(
                    items=[], metadata=SimpleNamespace(resource_version="10"))
            if list_count[0] == 5:
                informer._stop_event.set()
            raise RuntimeError("list unavailable")

        self.list_action = list_objects
        self.watch_action = lambda: self._response(
            duration=1, events=[self._event()])
        informer._run_loop()
        self.assertEqual([t for op, t, _ in self.requests if op == "list"],
                         [0, 2, 3, 5, 9])
        self.assertEqual(informer._resource_version, "11")
        self.assertGreater(
            len([op for op, _, _ in self.requests if op == "watch"]), 3)

    def test_initial_and_expired_list_failures_prevent_watch(self):
        for expired in [False, True]:
            with self.subTest(expired=expired):
                self.now = 0
                self.requests.clear()
                self.waits.clear()
                informer = self._make_informer()
                count = [0]

                def list_objects():
                    count[0] += 1
                    if expired and count[0] == 1:
                        return SimpleNamespace(
                            items=[], metadata=SimpleNamespace(
                                resource_version="10"))
                    if count[0] == (4 if expired else 3):
                        informer._stop_event.set()
                    raise RuntimeError("list unavailable")

                self.list_action = list_objects
                self.watch_action = lambda: self._response(events=[{
                    "type": ERROR, "object": {"code": 410, "reason": "Gone",
                                              "message": "expired"}}])
                informer._run_loop()
                self.assertEqual(len([op for op, _, _ in self.requests
                                      if op == "watch"]), int(expired))
                self.assertEqual(self.waits, [1, 2])
                self.assertIsNone(informer._resource_version)

    def test_slow_relist_does_not_make_short_watch_healthy(self):
        informer = self._make_informer(resync_period=2)
        list_count = [0]
        watch_count = [0]

        def list_objects():
            list_count[0] += 1
            if list_count[0] > 1:
                self.now += 70
            return SimpleNamespace(items=[], metadata=SimpleNamespace(
                resource_version="10"))

        def watch():
            watch_count[0] += 1
            if watch_count[0] == 4:
                informer._stop_event.set()
            return self._response()

        self.list_action = list_objects
        self.watch_action = watch
        informer._run_loop()
        # Delays keep growing across the slow LIST, and resync starts anew
        # from each LIST completion, not its start time.
        self.assertEqual([t for op, t, _ in self.requests if op == "watch"],
                         [0, 1, 72, 144])
        self.assertEqual([t for op, t, _ in self.requests if op == "list"],
                         [0, 2, 74])
        self.assertEqual(
            [entry.args for entry in self.jitter.call_args_list[:3]],
            [(0.5, 1), (1, 2), (2, 4)])

    def test_fractional_period_busy_watch_does_not_accumulate_backoff(self):
        informer = self._make_informer(resync_period=0.5)
        count = [0]

        def watch():
            count[0] += 1
            if count[0] == 4:
                informer._stop_event.set()
            return self._response(duration=0.5, events=[self._event()])

        self.watch_action = watch
        informer._run_loop()
        self.assertEqual([t for op, t, _ in self.requests if op == "watch"],
                         [0, 0.5, 1, 1.5])
        self.assertEqual(self.waits, [])

    def test_planned_relist_preserves_previous_watch_failure_history(self):
        informer = self._make_informer(resync_period=0.5)
        count = [0]

        def watch():
            count[0] += 1
            if count[0] == 4:
                informer._stop_event.set()
            if count[0] == 2:
                return self._response(duration=0.5, events=[self._event()])
            return self._response()

        self.watch_action = watch
        informer._run_loop()
        self.assertEqual([t for op, t, _ in self.requests if op == "watch"],
                         [0, 1, 1.5, 3.5])
        self.assertEqual(
            [entry.args for entry in self.jitter.call_args_list[:2]],
            [(0.5, 1), (1, 2)])

    def test_normal_idle_timeout_relists_without_failure_delay(self):
        informer = self._make_informer(resync_period=2)
        count = [0]

        def watch():
            count[0] += 1
            if count[0] == 2:
                informer._stop_event.set()
            return self._response(duration=2)

        self.watch_action = watch
        informer._run_loop()
        self.assertEqual([(op, t) for op, t, _ in self.requests], [
                         ("list", 0), ("watch", 0), ("list", 2), ("watch", 2)])
        self.assertEqual(self.waits, [])

    def test_cancel_during_backoff_prevents_another_request(self):
        informer = self._make_informer()
        self.watch_action = lambda: self._response()
        informer._stop_event.wait.side_effect = (
            lambda timeout: informer._stop_event.set())
        informer._run_loop()
        self.assertEqual([op for op, _, _ in self.requests], ["list", "watch"])

    def test_invalid_lines_followed_by_410_relist_without_internal_retry(self):
        informer = self._make_informer()
        count = [0]

        def watch():
            count[0] += 1
            if count[0] == 3:
                informer._stop_event.set()
                return self._response()
            return self._response(events=["", "not json", {
                "type": ERROR, "object": {"code": 410, "reason": "Gone",
                                          "message": "expired"}}])

        self.watch_action = watch
        informer._run_loop()
        self.assertEqual([op for op, _, _ in self.requests],
                         ["list", "watch", "list", "watch", "list", "watch"])
        self.assertEqual(self.waits, [1, 2])

    def test_restart_preserves_periodic_list_deadline(self):
        informer = self._make_informer(resync_period=5)
        count = [0]

        def watch():
            count[0] += 1
            if count[0] in (1, 3):
                informer._stop_event.set()
                return self._response()
            return self._response(duration=4)

        self.watch_action = watch
        informer._run_loop()
        self.now = 1
        informer._stop_event.clear()
        informer._run_loop()
        self.assertEqual([(op, t) for op, t, _ in self.requests],
                         [("list", 0), ("watch", 0), ("watch", 1),
                          ("list", 5), ("watch", 5)])
        self.assertEqual([kw["timeout_seconds"] for op, _, kw in self.requests
                          if op == "watch"], [5, 4, 5])

    def test_response_close_failure_at_resync_is_retried(self):
        informer = self._make_informer(resync_period=1)
        errors = []
        informer.add_event_handler(ERROR, errors.append)
        response = self._response(duration=1, events=[self._event()])
        response.close.side_effect = RuntimeError("close failed")
        count = [0]

        def watch():
            count[0] += 1
            if count[0] == 1:
                return response
            informer._stop_event.set()
            return self._response()

        self.watch_action = watch
        informer._run_loop()
        self.assertEqual(len(errors), 1)
        self.assertEqual(str(errors[0]), "close failed")
        response.release_conn.assert_called_once()
        self.assertEqual(count[0], 2)
        self.assertIsNone(informer._watch)

    def test_default_resync_accepts_callable_without_timeout_parameter(self):
        informer = None
        requests = []

        def source(watch=False, resource_version=None, _preload_content=True):
            requests.append(watch)
            if watch:
                informer._stop_event.set()
                return self._response()
            return SimpleNamespace(items=[], metadata=SimpleNamespace(
                resource_version="10"))

        informer = SharedInformer(source)
        informer._run_loop()
        self.assertEqual(requests, [False, True])


if __name__ == "__main__":
    unittest.main()
