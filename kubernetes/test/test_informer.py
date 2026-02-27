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

    def test_resync_period_triggers_full_list(self):
        """A full List call must be made to the API server on every resync_period."""
        pod = _make_pod("default", "resync-pod")

        list_func = MagicMock()
        list_resp = MagicMock()
        list_resp.items = [pod]
        list_resp.metadata = MagicMock(resource_version="5")
        list_func.return_value = list_resp

        informer = SharedInformer(list_func=list_func, resync_period=60)

        with patch("kubernetes.informer.informer.Watch") as MockWatch, \
                patch("kubernetes.informer.informer.time") as mock_time:
            # Sequence of time.monotonic() calls:
            #   1. last_resync = time.monotonic()          → 0.0
            #   2. (time.monotonic() - last_resync) check  → 61.0  (triggers resync)
            #   3. last_resync = time.monotonic()          → 61.0  (reset after resync)
            mock_time.monotonic.side_effect = [0.0, 61.0, 61.0]

            mock_w = MagicMock()
            mock_w.resource_version = "5"

            def fake_stream(func, **kw):
                yield {"type": "ADDED", "object": pod}
                informer._stop_event.set()

            mock_w.stream.side_effect = fake_stream
            MockWatch.return_value = mock_w

            informer.start()
            informer._thread.join(timeout=3)

        # list_func called once for the initial list + once for the resync = 2
        self.assertEqual(list_func.call_count, 2)

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


if __name__ == "__main__":
    unittest.main()

