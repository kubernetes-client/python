# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import codecs
import json
from urllib.parse import urlencode, urlparse, urlunparse

from aiohttp import WSMsgType

from kubernetes.aio.client import ApiClient
from kubernetes.aio.client.rest import RESTResponse

STDIN_CHANNEL = 0
STDOUT_CHANNEL = 1
STDERR_CHANNEL = 2
ERROR_CHANNEL = 3
RESIZE_CHANNEL = 4
CLOSE_CHANNEL = 255

V4_CHANNEL_PROTOCOL = 'v4.channel.k8s.io'
V5_CHANNEL_PROTOCOL = 'v5.channel.k8s.io'


def get_websocket_url(url):
    parsed_url = urlparse(url)
    parts = list(parsed_url)
    if parsed_url.scheme == 'http':
        parts[0] = 'ws'
    elif parsed_url.scheme == 'https':
        parts[0] = 'wss'
    return urlunparse(parts)


class WsResponse(RESTResponse):

    def __init__(self, status, data, response=None):
        self.status = status
        self.data = data
        self.response = response
        self._headers = {}
        self.reason = None

    @property
    def headers(self):
        return self._headers

    async def read(self):
        return self.data

    def getheaders(self):
        return self.headers

    def getheader(self, name, default=None):
        return self.headers.get(name, default)


class WsApiClient(ApiClient):
    """Async exec transport.

    Preloaded responses incrementally decode UTF-8 stdout and stderr with
    replacement for invalid bytes and honor v5 binary channel close frames.
    Without preloading, the raw aiohttp WebSocket is returned; callers are
    responsible for channel framing and close messages. Explicitly empty
    Sec-WebSocket-Protocol headers are rejected.
    """

    def __init__(self, configuration=None, header_name=None, header_value=None,
                 cookie=None, pool_threads=1, heartbeat=None):
        super().__init__(configuration, header_name, header_value, cookie)
        self.heartbeat = heartbeat

    @classmethod
    def parse_error_data(cls, error_data):
        """
        Parse data received on ERROR_CHANNEL and return the command exit code.
        """
        error_data_json = json.loads(error_data)
        if error_data_json.get("status") == "Success":
            return 0
        return int(error_data_json["details"]["causes"][0]['message'])

    async def call_api(
        self,
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None,
        _preload_content=True,
    ):
        response = await self.request(
            method,
            url,
            headers=header_params,
            body=body,
            post_params=post_params,
            _request_timeout=_request_timeout,
            _preload_content=_preload_content,
        )
        if _preload_content:
            return response
        return WsResponse(200, b'', response=response)

    async def request(self, method, url, query_params=None, headers=None,
                      post_params=None, body=None, _preload_content=True,
                      _request_timeout=None):

        # Expand command parameter list to indivitual command params
        if query_params:
            new_query_params = []
            for key, value in query_params:
                if key == 'command' and isinstance(value, list):
                    for command in value:
                        new_query_params.append((key, command))
                else:
                    new_query_params.append((key, value))
            query_params = new_query_params

        headers = headers.copy() if headers is not None else {}
        protocol_header = next(
            (key for key in headers if key.lower() == 'sec-websocket-protocol'),
            None,
        )
        if protocol_header is None:
            protocols = [V5_CHANNEL_PROTOCOL, V4_CHANNEL_PROTOCOL]
            headers['sec-websocket-protocol'] = ','.join(protocols)
        else:
            protocols = [
                protocol.strip()
                for protocol in headers[protocol_header].split(',')
                if protocol.strip()
            ]
            if not protocols:
                raise ValueError('Sec-WebSocket-Protocol must not be empty')

        if query_params:
            url += '?' + urlencode(query_params)

        url = get_websocket_url(url)
        pool_manager = self.rest_client.pool_manager
        if pool_manager is None:
            pool_manager = self.rest_client._create_pool_manager()
            self.rest_client.pool_manager = pool_manager

        if _preload_content:

            resp_all = ''
            decoders = {
                channel: codecs.getincrementaldecoder('utf-8')('replace')
                for channel in (STDOUT_CHANNEL, STDERR_CHANNEL)
            }
            async with pool_manager.ws_connect(
                url, headers=headers, protocols=protocols,
                heartbeat=self.heartbeat,
            ) as ws:
                async for msg in ws:
                    if msg.type == WSMsgType.ERROR:
                        raise ws.exception() or msg.data
                    if msg.type not in (WSMsgType.BINARY, WSMsgType.TEXT):
                        continue
                    data = msg.data
                    if not data:
                        continue
                    channel = data[0] if isinstance(data, bytes) else ord(data[0])
                    if channel == CLOSE_CHANNEL:
                        if (
                            msg.type == WSMsgType.BINARY
                            and len(data) == 2
                            and ws.protocol == V5_CHANNEL_PROTOCOL
                        ):
                            decoder = decoders.pop(data[1], None)
                            if decoder is not None:
                                resp_all += decoder.decode(b'', final=True)
                        continue
                    if channel not in decoders:
                        continue
                    data = data[1:]
                    if isinstance(data, str):
                        data = data.encode('utf-8')
                    resp_all += decoders[channel].decode(data)

            for decoder in decoders.values():
                resp_all += decoder.decode(b'', final=True)

            return WsResponse(200, resp_all.encode('utf-8'))

        else:

            return pool_manager.ws_connect(
                url, headers=headers, protocols=protocols,
                heartbeat=self.heartbeat,
            )
