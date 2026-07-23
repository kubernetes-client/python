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

import json
from urllib.parse import urlencode, urlparse, urlunparse

from kubernetes.aio.client import ApiClient
from kubernetes.aio.client.rest import RESTResponse

STDIN_CHANNEL = 0
STDOUT_CHANNEL = 1
STDERR_CHANNEL = 2
ERROR_CHANNEL = 3
RESIZE_CHANNEL = 4


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

        if headers is None:
            headers = {}
        if 'sec-websocket-protocol' not in headers:
            headers['sec-websocket-protocol'] = 'v4.channel.k8s.io'

        if query_params:
            url += '?' + urlencode(query_params)

        url = get_websocket_url(url)
        pool_manager = self.rest_client.pool_manager
        if pool_manager is None:
            pool_manager = self.rest_client._create_pool_manager()
            self.rest_client.pool_manager = pool_manager

        if _preload_content:

            resp_all = ''
            async with pool_manager.ws_connect(
                url, headers=headers, heartbeat=self.heartbeat
            ) as ws:
                async for msg in ws:
                    msg = msg.data.decode('utf-8')
                    if len(msg) > 1:
                        channel = ord(msg[0])
                        data = msg[1:]
                        if data:
                            if channel in [STDOUT_CHANNEL, STDERR_CHANNEL]:
                                resp_all += data

            return WsResponse(200, resp_all.encode('utf-8'))

        else:

            return pool_manager.ws_connect(
                url, headers=headers, heartbeat=self.heartbeat
            )
