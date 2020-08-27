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

import types

from . import ws_client


def stream(func, *args, **kwargs):
    """Stream given API call using websocket.
    Extra kwarg: capture-all=True - captures all stdout+stderr for use with WSClient.read_all()"""

    api_client = func.__self__.api_client
    prev_request = api_client.request
    try:
        api_client.request = types.MethodType(ws_client.websocket_call, api_client)
        return func(*args, **kwargs)
    finally:
        api_client.request = prev_request
