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
from unittest.mock import AsyncMock, Mock, patch

from aiohttp import WSMessage, WSMsgType

from kubernetes.aio import client
from kubernetes.aio.stream import WsApiClient
from kubernetes.aio.stream.ws_client import get_websocket_url


class WsMock:
    def __init__(self, messages=None, protocol=None, exception=None):
        self.iter = 0
        self.messages = messages
        self.protocol = protocol
        self._exception = exception

    def exception(self):
        return self._exception

    def __aiter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return False

    async def __aenter__(self):
        return self

    async def __anext__(self):
        self.iter += 1
        if self.messages is not None:
            if self.iter > len(self.messages):
                raise StopAsyncIteration
            return self.messages[self.iter - 1]
        if self.iter > 5:
            raise StopAsyncIteration
        return WSMessage(WSMsgType.BINARY, b'\x01mock', '')


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
                    'sec-websocket-protocol': (
                        'v5.channel.k8s.io,v4.channel.k8s.io'
                    ),
                    'Accept': '*/*',
                    'User-Agent': api_client.user_agent
                },
                protocols=['v5.channel.k8s.io', 'v4.channel.k8s.io'],
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
                    'sec-websocket-protocol': (
                        'v5.channel.k8s.io,v4.channel.k8s.io'
                    ),
                    'Accept': '*/*',
                    'User-Agent': api_client.user_agent
                },
                protocols=['v5.channel.k8s.io', 'v4.channel.k8s.io'],
                heartbeat=30
            )

    async def test_exec_ws_preserves_explicit_subprotocol(self):
        mock = Mock()
        mock.RESTClientObject.return_value.pool_manager = mock
        with patch('kubernetes.aio.client.api_client.rest', mock):
            api_client = WsApiClient()
            await api_client.request(
                'GET',
                'https://localhost/api',
                headers={'Sec-WebSocket-Protocol': 'v4.channel.k8s.io'},
                _preload_content=False,
            )

        mock.ws_connect.assert_called_once_with(
            'wss://localhost/api',
            headers={'Sec-WebSocket-Protocol': 'v4.channel.k8s.io'},
            protocols=['v4.channel.k8s.io'],
            heartbeat=None,
        )

    async def test_exec_ws_v5_channel_close_stops_channel_data(self):
        mock = Mock()
        mock.RESTClientObject.return_value.pool_manager = mock
        mock.ws_connect.return_value = WsMock(
            messages=[
                WSMessage(WSMsgType.BINARY, b'\x01before', ''),
                WSMessage(WSMsgType.BINARY, b'\xff\x01', ''),
                WSMessage(WSMsgType.BINARY, b'\x01after', ''),
                WSMessage(WSMsgType.BINARY, b'\x02stderr', ''),
            ],
            protocol='v5.channel.k8s.io',
        )
        with patch('kubernetes.aio.client.api_client.rest', mock):
            api_client = WsApiClient()
            response = await api_client.request(
                'GET',
                'https://localhost/api',
            )

        self.assertEqual(await response.read(), b'beforestderr')
        self.assertEqual(
            ['v5.channel.k8s.io', 'v4.channel.k8s.io'],
            mock.ws_connect.call_args.kwargs['protocols'],
        )

    async def test_exec_ws_does_not_mutate_headers(self):
        for headers in ({}, {'Accept': '*/*'}):
            with self.subTest(headers=headers):
                original = headers.copy()
                mock = Mock()
                mock.RESTClientObject.return_value.close = AsyncMock()
                mock.RESTClientObject.return_value.pool_manager = mock
                with patch('kubernetes.aio.client.api_client.rest', mock):
                    async with WsApiClient() as api_client:
                        await api_client.request(
                            'GET', 'https://localhost/api', headers=headers,
                            _preload_content=False,
                        )
                self.assertEqual(original, headers)
                self.assertEqual(
                    'v5.channel.k8s.io,v4.channel.k8s.io',
                    mock.ws_connect.call_args.kwargs['headers'][
                        'sec-websocket-protocol'
                    ],
                )

    async def test_exec_ws_rejects_empty_subprotocol(self):
        for value in ('', ' \t ', ' , , '):
            with self.subTest(value=value):
                mock = Mock()
                mock.RESTClientObject.return_value.close = AsyncMock()
                mock.RESTClientObject.return_value.pool_manager = mock
                with patch('kubernetes.aio.client.api_client.rest', mock):
                    async with WsApiClient() as api_client:
                        with self.assertRaisesRegex(
                            ValueError, 'Sec-WebSocket-Protocol'
                        ):
                            await api_client.request(
                                'GET', 'https://localhost/api',
                                headers={'Sec-WebSocket-Protocol': value},
                                _preload_content=False,
                            )
                mock.ws_connect.assert_not_called()

    async def test_exec_ws_buffered_frames(self):
        cases = [
            ('v4 ignores close channel', 'v4.channel.k8s.io', [
                b'\x01before', b'\xff\x01', b'\xff\x80', b'\x01after',
            ], 'beforeafter'),
            ('v5 ignores malformed closes', 'v5.channel.k8s.io', [
                b'\xff', b'\xff\x01\x02', b'\xff\x01extra', b'\x01after',
            ], 'after'),
            ('empty frames', 'v5.channel.k8s.io', [
                b'', b'\x01', b'\x02', b'\x01after',
            ], 'after'),
            ('ignored non-UTF-8 channel', 'v5.channel.k8s.io', [
                b'\x03\x80', b'\x01stdout',
            ], 'stdout'),
            ('interleaved split UTF-8', 'v5.channel.k8s.io', [
                b'\x01\xe2', b'\x02\xc3', b'\x01\x82\xac', b'\x02\xa9',
            ], '€é'),
            ('replace invalid UTF-8', 'v5.channel.k8s.io', [
                b'\x01\x80', b'\x02\xff',
            ], '\ufffd\ufffd'),
            ('flush on websocket close', 'v4.channel.k8s.io', [
                b'\x01\xe2', b'\x02\xc3',
            ], '\ufffd\ufffd'),
            ('flush on v5 channel close', 'v5.channel.k8s.io', [
                b'\x01\xe2', b'\xff\x01', b'\xff\x01',
                b'\x01\x82\xac', b'\x02stderr',
            ], '\ufffdstderr'),
            ('flush stderr on v5 close', 'v5.channel.k8s.io', [
                b'\x02\xc3', b'\xff\x02', b'\x02\xa9', b'\x01stdout',
            ], '\ufffdstdout'),
        ]
        for name, protocol, frames, expected in cases:
            with self.subTest(name=name):
                mock = Mock()
                mock.RESTClientObject.return_value.close = AsyncMock()
                mock.RESTClientObject.return_value.pool_manager = mock
                mock.ws_connect.return_value = WsMock(
                    [WSMessage(WSMsgType.BINARY, frame, '') for frame in frames],
                    protocol=protocol,
                )
                with patch('kubernetes.aio.client.api_client.rest', mock):
                    async with WsApiClient() as api_client:
                        response = await api_client.request(
                            'GET', 'https://localhost/api',
                        )
                self.assertEqual(expected.encode('utf-8'), await response.read())

    async def test_exec_ws_text_and_control_frames(self):
        mock = Mock()
        mock.RESTClientObject.return_value.close = AsyncMock()
        mock.RESTClientObject.return_value.pool_manager = mock
        mock.ws_connect.return_value = WsMock(
            messages=[
                WSMessage(WSMsgType.TEXT, '\xff\x01', ''),
                WSMessage(WSMsgType.PING, b'ping', ''),
                WSMessage(WSMsgType.PONG, b'pong', ''),
                WSMessage(WSMsgType.TEXT, '\x01stdout', ''),
                WSMessage(WSMsgType.BINARY, b'\x02stderr', ''),
            ],
            protocol='v5.channel.k8s.io',
        )
        with patch('kubernetes.aio.client.api_client.rest', mock):
            async with WsApiClient() as api_client:
                response = await api_client.request(
                    'GET', 'https://localhost/api',
                )
        self.assertEqual(b'stdoutstderr', await response.read())

    async def test_exec_ws_raises_websocket_error(self):
        message_error = RuntimeError('message error')
        websocket_error = RuntimeError('websocket error')
        for error in (None, websocket_error):
            with self.subTest(error=error):
                mock = Mock()
                mock.RESTClientObject.return_value.close = AsyncMock()
                mock.RESTClientObject.return_value.pool_manager = mock
                mock.ws_connect.return_value = WsMock(
                    messages=[WSMessage(WSMsgType.ERROR, message_error, '')],
                    exception=error,
                )
                with patch('kubernetes.aio.client.api_client.rest', mock):
                    async with WsApiClient() as api_client:
                        with self.assertRaises(RuntimeError) as raised:
                            await api_client.request(
                                'GET', 'https://localhost/api',
                            )
                self.assertIs(error or message_error, raised.exception)

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
