# Copyright 2017 The Kubernetes Authors.
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

from unittest import IsolatedAsyncioTestCase
from unittest.mock import Mock, patch

from kubernetes.aio import client
from kubernetes.aio.stream import WsApiClient
from kubernetes.aio.stream.ws_client import WsResponse, get_websocket_url


class WsMock:
    def __init__(self):
        self.iter = 0

    def __aiter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return self

    async def __aenter__(self):
        return self

    async def __anext__(self):
        self.iter += 1
        if self.iter > 5:
            raise StopAsyncIteration
        return WsResponse(200, (chr(1) + 'mock').encode('utf-8'))


class WSClientTest(IsolatedAsyncioTestCase):

    def test_websocket_client(self):
        for url, ws_url in [
                ('http://localhost/api', 'ws://localhost/api'),
                ('https://localhost/api', 'wss://localhost/api'),
                ('https://domain.com/api', 'wss://domain.com/api'),
                ('https://api.domain.com/api', 'wss://api.domain.com/api'),
                ('http://api.domain.com', 'ws://api.domain.com'),
                ('https://api.domain.com', 'wss://api.domain.com'),
                ('http://api.domain.com/', 'ws://api.domain.com/'),
                ('https://api.domain.com/', 'wss://api.domain.com/'),
        ]:
            self.assertEqual(get_websocket_url(url), ws_url)

    async def test_exec_ws(self):
        mock = Mock()
        mock.RESTClientObject.return_value.pool_manager = mock
        mock.ws_connect.return_value = WsMock()
        with patch('kubernetes.aio.client.api_client.rest', mock):

            api_client = WsApiClient()
            api_client.configuration.host = 'https://localhost'
            ws = client.CoreV1Api(api_client=api_client)
            resp = ws.connect_get_namespaced_pod_exec('pod', 'namespace',
                                                      command=["mock-command"],
                                                      stderr=True, stdin=False,
                                                      stdout=True, tty=False)

            ret = await resp
            self.assertEqual(ret, 'mock' * 5)
            mock.ws_connect.assert_called_once_with(
                'wss://localhost/api/v1/namespaces/namespace/pods/pod/exec?'
                'command=mock-command&stderr=true&stdin=false&stdout=true&tty=false',
                headers={
                    'sec-websocket-protocol': 'v4.channel.k8s.io',
                    'Accept': '*/*',
                    'User-Agent': api_client.user_agent
                },
                heartbeat=None
            )

    async def test_exec_ws_with_heartbeat(self):
        mock = Mock()
        mock.RESTClientObject.return_value.pool_manager = mock
        mock.ws_connect.return_value = WsMock()
        with patch('kubernetes.aio.client.api_client.rest', mock):

            api_client = WsApiClient(heartbeat=30)
            api_client.configuration.host = 'https://localhost'
            ws = client.CoreV1Api(api_client=api_client)
            resp = ws.connect_get_namespaced_pod_exec('pod', 'namespace',
                                                      command=['mock-command'],
                                                      stderr=True, stdin=False,
                                                      stdout=True, tty=False)

            ret = await resp
            self.assertEqual(ret, 'mock' * 5)
            mock.ws_connect.assert_called_once_with(
                'wss://localhost/api/v1/namespaces/namespace/pods/pod/exec?'
                'command=mock-command&stderr=true&stdin=false&stdout=true&tty=false',
                headers={
                    'sec-websocket-protocol': 'v4.channel.k8s.io',
                    'Accept': '*/*',
                    'User-Agent': api_client.user_agent
                },
                heartbeat=30
            )

    def test_parse_error_data_success(self):
        error_data = '{"metadata":{},"status":"Success"}'
        return_code = WsApiClient.parse_error_data(error_data)
        self.assertEqual(return_code, 0)

    def test_parse_error_data_failure(self):
        error_data = (
            '{"metadata":{},"status":"Failure",'
            '"message":"command terminated with non-zero exit code",'
            '"reason":"NonZeroExitCode",'
            '"details":{"causes":[{"reason":"ExitCode","message":"1"}]}}')
        return_code = WsApiClient.parse_error_data(error_data)
        self.assertEqual(return_code, 1)
