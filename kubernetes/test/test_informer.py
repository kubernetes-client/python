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

import threading
import time
import unittest
from unittest.mock import MagicMock, patch

from kubernetes.informer.cache import ObjectCache, _meta_namespace_key
from kubernetes.informer.informer import (
    ADDED,
    BOOKMARK,
    DELETED,
    ERROR,
    MODIFIED,
    SharedInformer,
)


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

    def test_bookmark_advances_resource_version(self):
        """A BOOKMARK event causes the informer's _resource_version to advance.

        PR #2505 added BOOKMARK-aware handling to Watch.unmarshal_event: it
        extracts resourceVersion from the raw BOOKMARK dict and stores it on
        self.resource_version *without* deserialising the object (because
        BOOKMARK events may be incomplete).  The informer must read that value
        back so that the next watch reconnect starts from the BOOKMARK's RV
        rather than the initial-list RV.
        """
        bookmark_obj = {"metadata": {"resourceVersion": "100"}}

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="5")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            # Simulate Watch.unmarshal_event updating resource_version on BOOKMARK.
            mock_w.resource_version = "100"

            def fake_stream(func, **kw):
                yield {"type": "BOOKMARK", "object": bookmark_obj, "raw_object": bookmark_obj}
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        # The informer must have synced the RV from the BOOKMARK.
        self.assertEqual(informer._resource_version, "100")

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

        rv_sequence = iter(["10", "20", "30"])

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
            # Sequence of time.monotonic() calls inside _run_loop:
            #   1. last_resync = time.monotonic()            → 0.0  (watch-loop start)
            #   2. post-stream: time.monotonic()             → 61.0 (≥60 → resync fires)
            #   3. last_resync = time.monotonic()            → 61.0 (second watch-loop start)
            # The stop_event is set during the second stream, so the
            # post-stream check is short-circuited and no further calls occur.
            mock_time.monotonic.side_effect = [0.0, 61.0, 61.0]
            mock_time.sleep = time.sleep  # keep real sleep/wait working

            mock_w = MagicMock()
            mock_w.resource_version = "5"

            def fake_stream(func, **kw):
                stream_calls["n"] += 1
                if stream_calls["n"] == 1:
                    # Simulate the stream timing out (timeout_seconds expired)
                    # with no events – the resync should fire after this returns.
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

    def test_resource_version_stored_from_watch(self):
        """After the watch stream ends the latest RV is preserved for reconnect."""
        pod = _make_pod("default", "rv-pod")
        events = [{"type": "ADDED", "object": pod}]

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="10")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)

        call_count = {"n": 0}

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            mock_w.resource_version = "99"

            def fake_stream(func, **kw):
                call_count["n"] += 1
                yield from events
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        # The Watch reported RV "99"; the informer should have stored it.
        self.assertEqual(informer._resource_version, "99")
        # list_func should have been called once for the initial list only.
        self.assertEqual(list_func.call_count, 1)

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

    def test_410_gone_triggers_relist(self):
        """A 410 Gone ApiException must reset resource_version and trigger re-list."""
        from kubernetes.client.exceptions import ApiException

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = []
        list_resp.metadata = MagicMock(resource_version="3")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func)

        stream_calls = {"n": 0}

        with patch("kubernetes.informer.informer.Watch") as MockWatch:
            mock_w = MagicMock()
            mock_w.resource_version = "3"

            def fake_stream(func, **kw):
                stream_calls["n"] += 1
                if stream_calls["n"] == 1:
                    raise ApiException(status=410, reason="Gone")
                # Second stream (after re-list): stop cleanly
                informer._stop_event.set()
                return iter([])

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        # list_func called twice: initial list + re-list after 410.
        self.assertEqual(list_func.call_count, 2)

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


if __name__ == "__main__":
    unittest.main()

