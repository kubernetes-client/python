# Copyright 2016 The Kubernetes Authors.
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

import asyncio
import json
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock, Mock, call, create_autospec

import kubernetes.aio
from kubernetes.aio.watch import Watch


async def _watch_operation(*args, **kwargs):
    pass


class WatchTest(IsolatedAsyncioTestCase):

    async def test_watch_with_decode(self):
        fake_resp = Mock()
        fake_resp.content.readline = AsyncMock()
        fake_resp.release = Mock()
        side_effects = [
            {
                "type": "ADDED",
                "object": {
                    "metadata": {"name": "test{}".format(uid),
                                 "resourceVersion": str(uid)},
                    "spec": {}, "status": {}
                }
            }
            for uid in range(3)
        ]
        side_effects = [json.dumps(_).encode('utf8') for _ in side_effects]
        side_effects.extend([AssertionError('Should not have been called')])
        fake_resp.content.readline.side_effect = side_effects

        fake_api = Mock()
        fake_api.get_namespaces = create_autospec(
            _watch_operation, return_value=fake_resp)
        fake_api.get_namespaces.__doc__ = ':rtype: V1NamespaceList'

        watch = kubernetes.aio.watch.Watch()
        count = 0
        async with watch:
            async for e in watch.stream(fake_api.get_namespaces, resource_version='123'):
                self.assertEqual("ADDED", e['type'])
                # make sure decoder worked and we got a model with the right name
                self.assertEqual("test%d" % count, e['object'].metadata.name)
                # make sure decoder worked and updated Watch.resource_version
                self.assertEqual(e['object'].metadata.resource_version, str(count))
                self.assertEqual(watch.resource_version, str(count))

                # Stop the watch. This must not return the next event which would
                # be an AssertionError exception.
                count += 1
                if count == len(side_effects) - 1:
                    watch.stop()

        fake_api.get_namespaces.assert_called_once_with(
            _preload_content=False, watch=True, resource_version='123')
        fake_resp.release.assert_called_once_with()

        # last resource_version has to be stored in the object
        self.assertEqual(watch.resource_version, '2')

    async def test_watch_for_follow(self):
        fake_resp = Mock()
        fake_resp.content.readline = AsyncMock()
        fake_resp.release = Mock()
        side_effects = ['log_line_1', 'log_line_2', '']
        side_effects = [_.encode('utf8') for _ in side_effects]
        side_effects.extend([AssertionError('Should not have been called')])
        fake_resp.content.readline.side_effect = side_effects

        fake_api = Mock()
        fake_api.read_namespaced_pod_log = create_autospec(
            _watch_operation, return_value=fake_resp)
        fake_api.read_namespaced_pod_log.__doc__ = ':param follow:\n:type follow: bool\n:rtype: str'

        watch = kubernetes.aio.watch.Watch()
        logs = []
        async with watch:
            async for e in watch.stream(fake_api.read_namespaced_pod_log):
                logs.append(e)

        self.assertListEqual(logs, ['log_line_1', 'log_line_2'])
        fake_api.read_namespaced_pod_log.assert_called_once_with(
            _preload_content=False, follow=True)
        fake_resp.release.assert_called_once_with()

    async def test_watch_k8s_empty_response(self):
        """Stop the iterator when the response is empty.

        This typically happens when the user supplied timeout expires.

        """
        # Mock the readline return value to first return a valid response
        # followed by an empty response.
        fake_resp = Mock()
        fake_resp.content.readline = AsyncMock()
        side_effects = [
            {"type": "ADDED", "object": {"metadata": {"name": "test0"}, "spec": {}, "status": {}}},
            {"type": "ADDED", "object": {"metadata": {"name": "test1"}, "spec": {}, "status": {}}},
        ]
        side_effects = [json.dumps(_).encode('utf8') for _ in side_effects]
        fake_resp.content.readline.side_effect = side_effects + [b'']

        # Fake the K8s resource object to watch.
        fake_api = Mock()
        fake_api.get_namespaces = create_autospec(
            _watch_operation, return_value=fake_resp)
        fake_api.get_namespaces.__doc__ = ':rtype: V1NamespaceList'

        # Iteration must cease after all valid responses were received.
        watch = kubernetes.aio.watch.Watch()
        cnt = 0
        async for _ in watch.stream(fake_api.get_namespaces): # noqa
            cnt += 1
        self.assertEqual(cnt, len(side_effects))

    async def test_unmarshal_with_float_object(self):
        w = Watch()
        event = w.unmarshal_event('{"type": "ADDED", "object": 1}', 'float')
        self.assertEqual("ADDED", event['type'])
        self.assertEqual(1.0, event['object'])
        self.assertTrue(isinstance(event['object'], float))
        self.assertEqual(1, event['raw_object'])

    async def test_unmarshal_without_return_type(self):
        w = Watch()
        event = w.unmarshal_event(
            '{"type": "ADDED", "object": ["test1"]}', None)
        self.assertEqual("ADDED", event['type'])
        self.assertEqual(["test1"], event['object'])
        self.assertEqual(["test1"], event['raw_object'])

    async def test_unmarshal_with_empty_return_type(self):
        # empty string as a return_type is a default value
        # if watch can't detect object by function's name
        w = Watch()
        event = w.unmarshal_event(
            '{"type": "ADDED", "object": ["test1"]}', '')
        self.assertEqual("ADDED", event['type'])
        self.assertEqual(["test1"], event['object'])
        self.assertEqual(["test1"], event['raw_object'])

    async def test_unmarshall_k8s_error_response(self):
        """Never parse messages of type ERROR.

        This test uses an actually recorded error, in this case for an outdated
        resource version.

        """
        # An actual error response sent by K8s during testing.
        k8s_err = {
            'type': 'ERROR',
            'object': {
                'kind': 'Status',
                'apiVersion': 'v1',
                'metadata': {},
                'status': 'Failure',
                'message': 'too old resource version: 1 (8146471)',
                'reason': 'Gone',
                'code': 410
            }
        }

        with self.assertRaisesRegex(
                kubernetes.aio.client.exceptions.ApiException,
                r'\(410\)\nReason: Gone: too old resource version: 1 \(8146471\)'):
            Watch().unmarshal_event(json.dumps(k8s_err), None)

    async def test_unmarshall_k8s_error_response_401_gke(self):
        """Never parse messages of type ERROR.

        This test uses an actually recorded error returned by GKE.

        """
        # An actual error response sent by K8s during testing.
        k8s_err = {
            'kind': 'Status',
            'apiVersion': 'v1',
            'metadata': {},
            'status': 'Failure',
            'message': 'Unauthorized',
            'reason': 'Unauthorized',
            'code': 401
        }

        with self.assertRaisesRegex(
                kubernetes.aio.client.exceptions.ApiException,
                r'\(401\)\nReason: Unauthorized: Unauthorized'):
            Watch().unmarshal_event(json.dumps(k8s_err), None)

    async def test_unmarshal_with_custom_object(self):
        w = Watch()
        event = w.unmarshal_event('{"type": "ADDED", "object": {"apiVersion":'
                                  '"test.com/v1beta1","kind":"foo","metadata":'
                                  '{"name": "bar", "resourceVersion": "1"}}}',
                                  'object')
        self.assertEqual("ADDED", event['type'])
        # make sure decoder deserialized json into dictionary and updated
        # Watch.resource_version
        self.assertTrue(isinstance(event['object'], dict))
        self.assertEqual("1", event['object']['metadata']['resourceVersion'])
        self.assertEqual("1", w.resource_version)

    async def test_watch_with_exception(self):
        fake_resp = Mock()
        fake_resp.content.readline = AsyncMock()
        fake_resp.content.readline.side_effect = KeyError("expected")
        fake_api = Mock()
        fake_api.get_namespaces = create_autospec(
            _watch_operation, return_value=fake_resp)
        fake_api.get_namespaces.__doc__ = ':rtype: V1NamespaceList'

        with self.assertRaises(KeyError):
            watch = kubernetes.aio.watch.Watch()
            async for e in watch.stream(fake_api.get_namespaces, timeout_seconds=10): # noqa
                pass

    async def test_watch_retry_timeout(self):
        fake_resp = Mock()
        fake_resp.content.readline = AsyncMock()
        fake_resp.release = Mock()

        mock_event = {"type": "ADDED",
                      "object": {"metadata": {"name": "test1555",
                                              "resourceVersion": "1555"},
                                 "spec": {},
                                 "status": {}}}

        fake_resp.content.readline.side_effect = [json.dumps(mock_event).encode('utf8'),
                                                  asyncio.TimeoutError(),
                                                  b""]

        fake_api = Mock()
        fake_api.get_namespaces = create_autospec(
            _watch_operation, return_value=fake_resp)
        fake_api.get_namespaces.__doc__ = ':rtype: V1NamespaceList'

        watch = kubernetes.aio.watch.Watch()
        async with watch.stream(fake_api.get_namespaces) as stream:
            async for e in stream: # noqa
                pass

        fake_api.get_namespaces.assert_has_calls(
            [call(_preload_content=False, watch=True),
             call(_preload_content=False, watch=True, resource_version='1555')])
        fake_resp.release.assert_called_once_with()

    async def test_watch_retry_410(self):
        fake_resp = Mock()
        fake_resp.content.readline = AsyncMock()
        fake_resp.release = Mock()

        mock_event1 = {
            "type": "ADDED",
            "object": {
                "metadata":
                    {
                        "name": "test1555",
                        "resourceVersion": "1555"
                    },
                "spec": {},
                "status": {}
            }
        }

        mock_event2 = {
            "type": "ADDED",
            "object": {
                "metadata":
                    {
                        "name": "test1555",
                        "resourceVersion": "1555"
                    },
                "spec": {},
                "status": {}
            }
        }

        mock_410 = {
            'type': 'ERROR',
            'object': {
                'kind': 'Status',
                'apiVersion': 'v1',
                'metadata': {},
                'status': 'Failure',
                'message': 'too old resource version: 1 (8146471)',
                'reason': 'Gone',
                'code': 410
            }
        }

        # retry 410
        fake_resp.content.readline.side_effect = [json.dumps(mock_event1).encode('utf8'),
                                                  json.dumps(mock_410).encode('utf8'),
                                                  json.dumps(mock_event2).encode('utf8'),
                                                  json.dumps(mock_410).encode('utf8'),
                                                  b""]

        fake_api = Mock()
        fake_api.get_namespaces = create_autospec(
            _watch_operation, return_value=fake_resp)
        fake_api.get_namespaces.__doc__ = ':rtype: V1NamespaceList'

        watch = kubernetes.aio.watch.Watch()
        async with watch.stream(fake_api.get_namespaces) as stream:
            async for e in stream: # noqa
                pass

        fake_api.get_namespaces.assert_has_calls(
            [call(_preload_content=False, watch=True),
             call(_preload_content=False, watch=True, resource_version='1555')])
        fake_resp.release.assert_called_once_with()

        # retry 410 only once
        fake_resp.content.readline.side_effect = [json.dumps(mock_event1).encode('utf8'),
                                                  json.dumps(mock_410).encode('utf8'),
                                                  json.dumps(mock_event2).encode('utf8'),
                                                  json.dumps(mock_410).encode('utf8'),
                                                  json.dumps(mock_410).encode('utf8'),
                                                  b""]

        fake_api = Mock()
        fake_api.get_namespaces = create_autospec(
            _watch_operation, return_value=fake_resp)
        fake_api.get_namespaces.__doc__ = ':rtype: V1NamespaceList'

        with self.assertRaisesRegex(
                kubernetes.aio.client.exceptions.ApiException,
                r'\(410\)\nReason: Gone: too old resource version: 1 \(8146471\)'):
            watch = kubernetes.aio.watch.Watch()
            async with watch.stream(fake_api.get_namespaces) as stream:
                async for e in stream: # noqa
                    pass

        # no retry 410 if timeout is passed
        fake_resp.content.readline.side_effect = [json.dumps(mock_event1).encode('utf8'),
                                                  json.dumps(mock_410).encode('utf8'),
                                                  b""]

        fake_api = Mock()
        fake_api.get_namespaces = create_autospec(
            _watch_operation, return_value=fake_resp)
        fake_api.get_namespaces.__doc__ = ':rtype: V1NamespaceList'

        with self.assertRaisesRegex(
                kubernetes.aio.client.exceptions.ApiException,
                r'\(410\)\nReason: Gone: too old resource version: 1 \(8146471\)'):
            watch = kubernetes.aio.watch.Watch()
            async with watch.stream(fake_api.get_namespaces, timeout_seconds=10) as stream:
                async for e in stream: # noqa
                    pass

    async def test_watch_timeout_with_resource_version(self):
        fake_resp = Mock()
        fake_resp.content.readline = AsyncMock()
        fake_resp.release = Mock()

        fake_resp.content.readline.side_effect = [asyncio.TimeoutError(),
                                                  b""]

        fake_api = Mock()
        fake_api.get_namespaces = create_autospec(
            _watch_operation, return_value=fake_resp)
        fake_api.get_namespaces.__doc__ = ':rtype: V1NamespaceList'

        watch = kubernetes.aio.watch.Watch()
        async with watch.stream(fake_api.get_namespaces, resource_version='10') as stream:
            async for e in stream: # noqa
                pass

        # all calls use the passed resource version
        fake_api.get_namespaces.assert_has_calls(
            [call(_preload_content=False, watch=True, resource_version='10'),
             call(_preload_content=False, watch=True, resource_version='10')])

        fake_resp.release.assert_called_once_with()
        self.assertEqual(watch.resource_version, '10')

    async def test_unmarshal_bookmark_succeeds_and_preserves_resource_version(self):
        w = Watch()
        event = w.unmarshal_event('{"type": "BOOKMARK", "object": {"apiVersion":'
                                  '"test.com/v1beta1","kind":"foo","metadata":'
                                  '{"name": "bar", "resourceVersion": "1"}}}',
                                  'object')
        self.assertEqual("BOOKMARK", event['type'])

        # make sure the resource version is preserved,
        # and the watcher's resource_version is updated
        self.assertTrue(isinstance(event['raw_object'], dict))
        self.assertEqual("1", event['raw_object']['metadata']['resourceVersion'])
        self.assertEqual("1", w.resource_version)

    async def test_unmarshal_job_bookmark_succeeds_and_preserves_resource_version(self):
        w = Watch()
        event = w.unmarshal_event('{"type": "BOOKMARK", "object": {"apiVersion":'
                                  '"batch/v1","kind":"Job","metadata":'
                                  '{"name": "bar", "resourceVersion": "1"},'
                                  '"spec": {"template": {"metadata": '
                                  '{"creationTimestamp":null}, "spec": '
                                  '{"containers":null}}}}}',
                                  'object')
        self.assertEqual("BOOKMARK", event['type'])

        # make sure the resource version is preserved,
        # and the watcher's resource_version is updated
        self.assertTrue(isinstance(event['raw_object'], dict))
        self.assertEqual("1", event['raw_object']['metadata']['resourceVersion'])
        self.assertEqual("1", w.resource_version)

    async def test_unmarshall_job_bookmark_malformed_object_fails(self):
        # An actual error response sent by K8s during testing.
        k8s_err = {
            'type': 'BOOKMARK',
            'object': {
                'kind': 'Job',
                'apiVersion': 'batch/v1',
                'metadata': {},
            }
        }

        with self.assertRaises(Exception):
            Watch().unmarshal_event(json.dumps(k8s_err), None)
