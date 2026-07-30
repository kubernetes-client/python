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

"""End-to-end reproduction for kubernetes-client/python#2387.

Spins up a mock HTTPS forward proxy and a mock HTTPS Kubernetes API server,
each with their own independent self-signed certificate, matching the
"HTTPS Proxy + HTTPS Destination" scenario from urllib3's advanced usage
docs that the issue links to:
https://urllib3.readthedocs.io/en/stable/advanced-usage.html#https-proxy-https-destination

Unlike the rest of this package, this test does not require a live
Kubernetes cluster - it only requires openssl on PATH to generate throwaway
certificates.
"""

import shutil
import socket
import ssl
import subprocess
import tempfile
import threading
import unittest
from pathlib import Path

import urllib3

from kubernetes import client


def _generate_cert(cert_dir, name):
    subprocess.run(
        [
            "openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes",
            "-keyout", str(cert_dir / f"{name}.key"),
            "-out", str(cert_dir / f"{name}.crt"),
            "-days", "1", "-subj", f"/CN={name}.test",
            "-addext", f"subjectAltName=DNS:localhost,DNS:{name}.test,IP:127.0.0.1",
        ],
        check=True, capture_output=True,
    )


def _free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _relay(a, b):
    try:
        while True:
            data = a.recv(4096)
            if not data:
                break
            b.sendall(data)
    except OSError:
        pass
    finally:
        for s in (a, b):
            try:
                s.shutdown(socket.SHUT_RDWR)
            except OSError:
                pass


def _run_destination_server(cert_dir, port, ready):
    import http.server

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                b'{"major": "1", "minor": "31", "gitVersion": "v1.31.0-mock",'
                b'"gitCommit": "mock", "gitTreeState": "clean",'
                b'"buildDate": "2026-01-01T00:00:00Z", "goVersion": "go1.23",'
                b'"compiler": "gc", "platform": "linux/amd64"}'
            )

        def log_message(self, *args):
            pass

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(f"{cert_dir}/destination.crt", f"{cert_dir}/destination.key")
    server = http.server.HTTPServer(("127.0.0.1", port), Handler)
    server.socket = ctx.wrap_socket(server.socket, server_side=True)
    ready.set()
    server.serve_forever()


def _run_proxy_server(cert_dir, port, ready):
    def handle(conn):
        request_line = b""
        while not request_line.endswith(b"\r\n\r\n"):
            chunk = conn.recv(1)
            if not chunk:
                return
            request_line += chunk
        method, target, _ = request_line.split(b"\r\n", 1)[0].decode().split(" ")
        if method != "CONNECT":
            conn.sendall(b"HTTP/1.1 405 Method Not Allowed\r\n\r\n")
            conn.close()
            return
        host, port_str = target.split(":")
        upstream = socket.create_connection((host, int(port_str)), timeout=5)
        conn.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")
        threading.Thread(target=_relay, args=(conn, upstream), daemon=True).start()
        threading.Thread(target=_relay, args=(upstream, conn), daemon=True).start()

    def accept_and_handshake(raw_conn, ctx):
        try:
            tls_conn = ctx.wrap_socket(raw_conn, server_side=True)
        except ssl.SSLError:
            return  # client rejected our cert - expected without proxy_ssl_context
        handle(tls_conn)

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(f"{cert_dir}/proxy.crt", f"{cert_dir}/proxy.key")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", port))
    sock.listen(5)
    ready.set()
    while True:
        raw_conn, _ = sock.accept()
        threading.Thread(
            target=accept_and_handshake, args=(raw_conn, ctx), daemon=True
        ).start()


@unittest.skipUnless(shutil.which("openssl"), "requires openssl on PATH")
class TestProxySslContext(unittest.TestCase):
    """Regression coverage for #2387: proxy_ssl_context lets the client
    trust an HTTPS proxy independently of the destination TLS settings."""

    @classmethod
    def setUpClass(cls):
        cls.cert_dir = Path(tempfile.mkdtemp())
        for name in ("proxy", "destination"):
            _generate_cert(cls.cert_dir, name)

        cls.dest_port = _free_port()
        cls.proxy_port = _free_port()

        dest_ready = threading.Event()
        proxy_ready = threading.Event()
        threading.Thread(
            target=_run_destination_server,
            args=(cls.cert_dir, cls.dest_port, dest_ready), daemon=True,
        ).start()
        threading.Thread(
            target=_run_proxy_server,
            args=(cls.cert_dir, cls.proxy_port, proxy_ready), daemon=True,
        ).start()
        dest_ready.wait(timeout=5)
        proxy_ready.wait(timeout=5)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.cert_dir, ignore_errors=True)

    def _make_config(self):
        config = client.Configuration()
        config.host = f"https://127.0.0.1:{self.dest_port}"
        config.verify_ssl = True
        config.ssl_ca_cert = f"{self.cert_dir}/destination.crt"
        config.proxy = f"https://127.0.0.1:{self.proxy_port}"
        return config

    def test_without_proxy_ssl_context_fails_when_proxy_ca_differs(self):
        config = self._make_config()
        api_client = client.ApiClient(config)
        version_api = client.VersionApi(api_client)

        with self.assertRaises(urllib3.exceptions.MaxRetryError) as ctx:
            version_api.get_code()
        self.assertIn("CERTIFICATE_VERIFY_FAILED", str(ctx.exception))

    def test_with_proxy_ssl_context_succeeds_when_proxy_ca_differs(self):
        config = self._make_config()
        config.proxy_ssl_context = ssl.create_default_context(
            cafile=f"{self.cert_dir}/proxy.crt"
        )
        api_client = client.ApiClient(config)
        version_api = client.VersionApi(api_client)

        version = version_api.get_code()
        self.assertEqual(version.git_version, "v1.31.0-mock")


if __name__ == "__main__":
    unittest.main()
