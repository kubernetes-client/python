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

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading
import unittest

from kubernetes.client import ApiClient, Configuration

from .client import DynamicClient
from .exceptions import NotFoundError


class DynamicClientTest(unittest.TestCase):
    def test_request_translates_http_errors(self):
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                body = json.dumps({'message': 'missing'}).encode()
                self.send_response(404)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format, *args):
                pass

        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever)
        thread.start()
        try:
            dynamic = DynamicClient.__new__(DynamicClient)
            dynamic.client = ApiClient(Configuration(
                host=f'http://127.0.0.1:{server.server_port}',
                proxy='',
                no_proxy='',
            ))

            with self.assertRaises(NotFoundError) as raised:
                dynamic.request(
                    'get',
                    '/missing',
                    serializer=lambda _, data: data,
                )

            self.assertEqual('missing', raised.exception.summary())
        finally:
            server.shutdown()
            thread.join()
            server.server_close()

    def test_request_preserves_resolved_async_req_response(self):
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.server.request_path = self.path
                self.server.content_type = self.headers['Content-Type']
                body = json.dumps({'kind': 'APIResourceList'}).encode()
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format, *args):
                pass

        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever)
        thread.start()
        try:
            dynamic = DynamicClient.__new__(DynamicClient)
            dynamic.client = ApiClient(Configuration(
                host=f'http://127.0.0.1:{server.server_port}',
                proxy='',
                no_proxy='',
            ))

            response = dynamic.request(
                'get',
                '/apis',
                async_req=True,
                pretty='true',
                serializer=lambda _, data: data,
            )

            self.assertEqual({'kind': 'APIResourceList'}, response)
            self.assertEqual('/apis?pretty=true', server.request_path)
            self.assertEqual('application/json', server.content_type)
        finally:
            server.shutdown()
            thread.join()
            server.server_close()

    def test_apply_patch_serializes_object_body(self):
        class Handler(BaseHTTPRequestHandler):
            def do_PATCH(self):
                length = int(self.headers['Content-Length'])
                self.server.request_body = self.rfile.read(length)
                self.server.content_type = self.headers['Content-Type']
                body = b'{}'
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format, *args):
                pass

        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever)
        thread.start()
        try:
            dynamic = DynamicClient.__new__(DynamicClient)
            dynamic.client = ApiClient(Configuration(
                host=f'http://127.0.0.1:{server.server_port}',
                proxy='',
                no_proxy='',
            ))

            dynamic.request(
                'patch',
                '/apis/example',
                body={'apiVersion': 'example/v1'},
                content_type='application/apply-patch+yaml',
                serializer=lambda _, data: data,
            )

            self.assertEqual(
                'application/apply-patch+yaml', server.content_type)
            self.assertEqual(
                {'apiVersion': 'example/v1'},
                json.loads(server.request_body),
            )
        finally:
            server.shutdown()
            thread.join()
            server.server_close()

    def test_no_proxy_bypasses_configured_proxy(self):
        class TargetHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.server.received_request = True
                body = b'{}'
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format, *args):
                pass

        class ProxyHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.server.received_request = True
                body = b'{}'
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format, *args):
                pass

        target = ThreadingHTTPServer(('127.0.0.1', 0), TargetHandler)
        target.received_request = False
        proxy = ThreadingHTTPServer(('127.0.0.1', 0), ProxyHandler)
        proxy.received_request = False
        target_thread = threading.Thread(target=target.serve_forever)
        proxy_thread = threading.Thread(target=proxy.serve_forever)
        target_thread.start()
        proxy_thread.start()
        try:
            dynamic = DynamicClient.__new__(DynamicClient)
            dynamic.client = ApiClient(Configuration(
                host=f'http://127.0.0.1:{target.server_port}',
                proxy=f'http://127.0.0.1:{proxy.server_port}',
                no_proxy='127.0.0.1',
            ))

            dynamic.request(
                'get',
                '/apis',
                serializer=lambda _, data: data,
            )

            self.assertTrue(target.received_request)
            self.assertFalse(proxy.received_request)
        finally:
            target.shutdown()
            proxy.shutdown()
            target_thread.join()
            proxy_thread.join()
            target.server_close()
            proxy.server_close()


if __name__ == '__main__':
    unittest.main()
