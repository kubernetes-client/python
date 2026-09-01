# Copyright 2018 The Kubernetes Authors.
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

import functools
from types import SimpleNamespace

from . import ws_client


def _websocket_request(websocket_request, force_kwargs, api_method, *args, **kwargs):
    """Call a generated API method using the WebSocket transport."""
    if force_kwargs:
        for kwarg, value in force_kwargs.items():
            kwargs[kwarg] = value
    api_client = api_method.__self__.api_client
    configuration = api_client.configuration
    preload_content = kwargs.pop('_preload_content', True)
    kwargs['_preload_content'] = False
    binary = kwargs.pop('binary', False)
    previous_call_api = api_client.call_api

    # Legacy-compatible generated methods preserve _preload_content=False
    # instead of emitting *_without_preload_content siblings. Keep generated
    # request serialization, then satisfy the raw-response shape it expects.
    def call_api(
        method,
        url,
        header_params=None,
        body=None,
        post_params=None,
        _request_timeout=None,
    ):
        response = websocket_request(
            configuration,
            method,
            url,
            headers=header_params,
            body=body,
            post_params=post_params,
            _request_timeout=_request_timeout,
            _preload_content=preload_content,
            binary=binary,
        )
        return SimpleNamespace(
            response=response,
            status=response.status
            if isinstance(response, ws_client.WSResponse)
            else 200,
        )

    try:
        api_client.call_api = call_api
        response = api_method(*args, **kwargs)
    finally:
        api_client.call_api = previous_call_api

    if isinstance(response, ws_client.WSResponse):
        return response.data
    return response


stream = functools.partial(_websocket_request, ws_client.websocket_call, None)
portforward = functools.partial(_websocket_request, ws_client.portforward_call, {'_preload_content':False})
