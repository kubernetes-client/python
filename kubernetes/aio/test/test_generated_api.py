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

import inspect
import json
import ssl
from unittest import IsolatedAsyncioTestCase

from aiohttp import web

from kubernetes.aio.client import (
    ApiClient,
    BatchV1Api,
    Configuration,
    CoreV1Api,
    V1ConfigMap,
    V1ObjectMeta,
    V1Pod,
    V1ServicePort,
)
from kubernetes.aio.client.rest import RESTClientObject
from kubernetes.aio.dynamic import DynamicClient
from kubernetes.aio.stream import WsApiClient
from kubernetes.aio.watch import Watch


class GeneratedAsyncApiTest(IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.requests = []
        self.response = {
            'apiVersion': 'v1',
            'kind': 'NamespaceList',
            'metadata': {'resourceVersion': '1'},
            'items': [],
        }
        self.response_status = 200
        self.response_headers = {}
        self.responses = None
        app = web.Application()
        app.router.add_route('*', '/{path:.*}', self._handle_request)
        self.runner = web.AppRunner(app)
        await self.runner.setup()
        site = web.TCPSite(self.runner, '127.0.0.1', 0)
        await site.start()
        port = site._server.sockets[0].getsockname()[1]
        self.configuration = Configuration(
            host='http://127.0.0.1:{}'.format(port),
        )
        self.api_client = ApiClient(self.configuration)

    async def asyncTearDown(self):
        await self.api_client.close()
        await self.runner.cleanup()

    async def _handle_request(self, request):
        body = await request.read()
        self.requests.append((request, body))
        if request.path.endswith('/exec'):
            response = web.WebSocketResponse(
                protocols=('v4.channel.k8s.io',),
            )
            await response.prepare(request)
            await response.send_bytes(b'\x01remote output')
            await response.close()
            return response
        if request.query.get('watch') == 'true':
            response = web.StreamResponse(
                headers={'Content-Type': 'application/json'},
            )
            await response.prepare(request)
            await response.write(json.dumps({
                'type': 'ADDED',
                'object': {
                    'apiVersion': 'v1',
                    'kind': 'Pod',
                    'metadata': {
                        'name': 'observed-pod',
                        'resourceVersion': '7',
                    },
                },
            }).encode() + b'\n')
            await response.write_eof()
            return response
        if self.responses is not None:
            index = len(self.requests) - 1
            response, status, headers = self.responses[
                min(index, len(self.responses) - 1)
            ]
            return web.json_response(response, status=status, headers=headers)
        return web.json_response(
            self.response,
            status=self.response_status,
            headers=self.response_headers,
        )

    async def test_bearer_alias_supports_synchronous_token_refresh(self):
        self.configuration.api_key['authorization'] = 'expired-token'
        self.configuration.api_key_prefix['authorization'] = 'Bearer'

        def refresh(configuration):
            configuration.api_key['authorization'] = 'refreshed-token'

        self.configuration.refresh_api_key_hook = refresh
        await CoreV1Api(self.api_client).list_namespace()

        self.assertEqual(
            'Bearer refreshed-token',
            self.requests[-1][0].headers['Authorization'],
        )

    async def test_bearer_alias_supports_asynchronous_token_refresh(self):
        self.configuration.api_key['authorization'] = 'expired-token'
        self.configuration.api_key_prefix['authorization'] = 'Bearer'

        async def refresh(configuration):
            configuration.api_key['authorization'] = 'refreshed-token'

        self.configuration.refresh_api_key_hook = refresh
        await CoreV1Api(self.api_client).list_namespace()

        self.assertEqual(
            'Bearer refreshed-token',
            self.requests[-1][0].headers['Authorization'],
        )

    async def test_client_go_retry_retries_get_retry_after_response(self):
        self.configuration.client_go_retries = True
        self.configuration.retries = 1
        self.responses = [
            ({'message': 'retry later'}, 429, {'Retry-After': '0'}),
            (self.response, 200, {}),
        ]

        namespaces = await CoreV1Api(self.api_client).list_namespace()

        self.assertEqual([], namespaces.items)
        self.assertEqual(2, len(self.requests))
        self.assertIsNone(self.api_client.rest_client.retry_client)

    async def test_delete_job_accepts_job_and_status_responses(self):
        responses = (
            (
                {
                    'apiVersion': 'batch/v1',
                    'kind': 'Job',
                    'metadata': {'name': 'sample'},
                    'status': {'ready': 0},
                },
                'Job',
                {'ready': 0},
            ),
            (
                {
                    'apiVersion': 'v1',
                    'kind': 'Status',
                    'status': 'Success',
                    'details': {'name': 'sample', 'kind': 'jobs'},
                },
                'Status',
                'Success',
            ),
        )

        for response_status in (200, 202):
            for response, expected_kind, expected_status in responses:
                with self.subTest(
                    status=response_status, kind=expected_kind
                ):
                    self.response_status = response_status
                    self.response = response
                    deleted = await BatchV1Api(
                        self.api_client,
                    ).delete_namespaced_job(
                        name='sample', namespace='default', body={},
                    )

                    self.assertIsInstance(deleted, dict)
                    self.assertIsNot(response, deleted)
                    self.assertEqual(response, deleted)
                    self.assertEqual(expected_kind, deleted['kind'])
                    self.assertEqual(expected_status, deleted['status'])
                    if expected_kind == 'Job':
                        self.assertIsInstance(deleted['status'], dict)
                        self.assertIsNot(response['status'], deleted['status'])
                    else:
                        self.assertIsInstance(deleted['status'], str)
                    request, body = self.requests[-1]
                    self.assertEqual({}, json.loads(body))
                    self.assertEqual(
                        '/apis/batch/v1/namespaces/default/jobs/sample',
                        request.path,
                    )

    async def test_object_patches_use_strategic_merge(self):
        self.response = {
            'apiVersion': 'v1',
            'kind': 'ConfigMap',
            'metadata': {'name': 'settings'},
            'data': {'key': 'value'},
        }
        for body in (
            {'data': {'key': 'value'}},
            V1ConfigMap(
                metadata=V1ObjectMeta(name='settings'),
                data={'key': 'value'},
            ),
        ):
            with self.subTest(body=type(body).__name__):
                result = await CoreV1Api(
                    self.api_client,
                ).patch_namespaced_config_map(
                    'settings', 'default', body,
                )
                request, encoded_body = self.requests[-1]
                self.assertEqual(
                    'application/strategic-merge-patch+json',
                    request.headers['Content-Type'],
                )
                self.assertEqual(
                    {'key': 'value'},
                    json.loads(encoded_body)['data'],
                )
                self.assertEqual('value', result.data['key'])

    async def test_operation_patches_use_json_patch(self):
        self.response = {
            'apiVersion': 'v1',
            'kind': 'ConfigMap',
            'metadata': {'name': 'settings'},
        }
        operations = [{'op': 'remove', 'path': '/data/key'}]

        await CoreV1Api(self.api_client).patch_namespaced_config_map(
            'settings', 'default', operations,
        )

        request, encoded_body = self.requests[-1]
        self.assertEqual(
            'application/json-patch+json',
            request.headers['Content-Type'],
        )
        self.assertEqual(operations, json.loads(encoded_body))

    async def test_server_side_apply_serializes_object_body(self):
        self.response = {
            'apiVersion': 'v1',
            'kind': 'ConfigMap',
            'metadata': {'name': 'settings'},
        }
        body = {'data': {'key': 'value'}}

        await CoreV1Api(self.api_client).patch_namespaced_config_map(
            'settings',
            'default',
            body,
            _content_type='application/apply-patch+yaml',
        )

        request, encoded_body = self.requests[-1]
        self.assertEqual(
            'application/apply-patch+yaml',
            request.headers['Content-Type'],
        )
        self.assertEqual(body, json.loads(encoded_body))

    async def test_watch_deserializes_real_streamed_pod(self):
        watcher = Watch()
        async with watcher:
            stream = watcher.stream(
                CoreV1Api(self.api_client).list_namespaced_pod,
                'default',
                timeout_seconds=1,
            )
            event = await anext(stream)

        self.assertEqual('ADDED', event['type'])
        self.assertIsInstance(event['object'], V1Pod)
        self.assertEqual('observed-pod', event['object'].metadata.name)
        self.assertEqual('7', watcher.resource_version)

    async def test_websocket_exec_returns_buffered_output(self):
        websocket_client = WsApiClient(self.configuration)
        self.addAsyncCleanup(websocket_client.close)

        output = await CoreV1Api(
            websocket_client,
        ).connect_get_namespaced_pod_exec(
            'pod', 'default', command=['echo', 'hello'], stdout=True,
        )

        self.assertEqual('remote output', output)
        self.assertEqual(
            'v4.channel.k8s.io',
            self.requests[-1][0].headers['Sec-WebSocket-Protocol'],
        )

    async def test_websocket_exec_preserves_interactive_raw_stream(self):
        websocket_client = WsApiClient(self.configuration)
        self.addAsyncCleanup(websocket_client.close)

        stream = await CoreV1Api(
            websocket_client,
        ).connect_get_namespaced_pod_exec_without_preload_content(
            'pod', 'default', command=['echo', 'hello'], stdout=True,
        )

        async with stream as websocket:
            message = await websocket.receive()

        self.assertEqual(b'\x01remote output', message.data)

    async def test_dynamic_discovery_uses_real_async_transport(self):
        self.response = {'major': '1', 'minor': '36'}
        dynamic = DynamicClient(self.api_client)

        response = await dynamic.request('get', '/version', serialize=False)

        self.assertEqual(self.response, await response.json())
        self.assertEqual('/version', self.requests[-1][0].path)
        self.assertEqual(
            'application/json',
            self.requests[-1][0].headers['Content-Type'],
        )

    async def test_closing_api_does_not_close_borrowed_client(self):
        api = CoreV1Api(self.api_client)
        await api.list_namespace()
        session = self.api_client.rest_client.pool_manager

        await api.close()

        self.assertFalse(session.closed)
        await self.api_client.close()
        self.assertTrue(session.closed)

    async def test_watch_buffer_preserves_kubernetes_resource_limit(self):
        await CoreV1Api(self.api_client).list_namespace()

        self.assertEqual(
            2**21,
            self.api_client.rest_client.pool_manager._read_bufsize,
        )

    async def test_strict_tls_verification_can_be_disabled(self):
        self.configuration.disable_strict_ssl_verification = True

        rest_client = RESTClientObject(self.configuration)

        self.assertFalse(
            rest_client.ssl_context.verify_flags & ssl.VERIFY_X509_STRICT,
        )

    async def test_models_preserve_int_or_string_and_python_field_names(self):
        port = V1ServicePort(port=80, target_port='https')

        self.assertEqual('https', port.target_port)
        self.assertEqual('https', port.to_dict()['target_port'])
        self.assertIn(
            'resource_version',
            inspect.signature(V1ObjectMeta).parameters,
        )
