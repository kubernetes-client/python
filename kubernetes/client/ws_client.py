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

from .rest import ApiException

import certifi
import collections
import websocket
import six
import ssl
from six.moves.urllib.parse import urlencode
from six.moves.urllib.parse import quote_plus


class WSClient:
    def __init__(self, configuration, url, headers):
        self.messages = []
        self.errors = []
        websocket.enableTrace(False)
        header = None

        # We just need to pass the Authorization, ignore all the other
        # http headers we get from the generated code
        if 'Authorization' in headers:
            header = "Authorization: %s" % headers['Authorization']

        self.ws = websocket.WebSocketApp(url,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close,
                                         header=[header] if header else None)
        self.ws.on_open = self.on_open

        if url.startswith('wss://') and configuration.verify_ssl:
            ssl_opts = {
                'cert_reqs': ssl.CERT_REQUIRED,
                'keyfile': configuration.key_file,
                'certfile': configuration.cert_file,
                'ca_certs': configuration.ssl_ca_cert or certifi.where(),
            }
            if configuration.assert_hostname is not None:
                ssl_opts['check_hostname'] = configuration.assert_hostname
        else:
            ssl_opts = {'cert_reqs': ssl.CERT_NONE}

        self.ws.run_forever(sslopt=ssl_opts)

    def on_message(self, ws, message):
        if message[0] == '\x01':
            message = message[1:]
        if message:
            if six.PY3 and isinstance(message, six.binary_type):
                message = message.decode('utf-8')
            self.messages.append(message)

    def on_error(self, ws, error):
        self.errors.append(error)

    def on_close(self, ws):
        pass

    def on_open(self, ws):
        pass


WSResponse = collections.namedtuple('WSResponse', ['data'])


def GET(configuration, url, query_params, _request_timeout, headers):
    # switch protocols from http to websocket
    url = url.replace('http://', 'ws://')
    url = url.replace('https://', 'wss://')

    # patch extra /
    url = url.replace('//api', '/api')

    # Extract the command from the list of tuples
    commands = None
    for key, value in query_params:
        if key == 'command':
            commands = value
            break

    # drop command from query_params as we will be processing it separately
    query_params = [(key, value) for key, value in query_params if
                    key != 'command']

    # if we still have query params then encode them
    if query_params:
        url += '?' + urlencode(query_params)

    # tack on the actual command to execute at the end
    if isinstance(commands, list):
        for command in commands:
            url += "&command=%s&" % quote_plus(command)
    else:
        url += '&command=' + quote_plus(commands)

    client = WSClient(configuration, url, headers)
    if client.errors:
        raise ApiException(
            status=0,
            reason='\n'.join([str(error) for error in client.errors])
        )
    return WSResponse('%s' % ''.join(client.messages))
