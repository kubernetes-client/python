# -*- coding: utf-8 -*-

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
import select
import socket
import time
import unittest
import urllib.request
import uuid

from kubernetes.client import api_client
from kubernetes.client.api import core_v1_api
from kubernetes.e2e_test import base
from kubernetes.stream import stream, portforward
from kubernetes.stream.ws_client import ERROR_CHANNEL


def short_uuid():
    id = str(uuid.uuid4())
    return id[-12:]


def manifest_with_command(name, command):
    return {
        'apiVersion': 'v1',
        'kind': 'Pod',
        'metadata': {
            'name': name
        },
        'spec': {
            'containers': [{
                'image': 'busybox',
                'name': 'sleep',
                "args": [
                    "/bin/sh",
                    "-c",
                    command
                ]
            }]
        }
    }

class TestClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = base.get_e2e_configuration()

    def test_pod_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'busybox-test-' + short_uuid()
        pod_manifest = manifest_with_command(name, "while true;do date;sleep 5; done")
        resp = api.create_namespaced_pod(body=pod_manifest,
                                         namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status.phase)

        while True:
            resp = api.read_namespaced_pod(name=name,
                                           namespace='default')
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status.phase)
            if resp.status.phase != 'Pending':
                break
            time.sleep(1)

        exec_command = ['/bin/sh',
                        '-c',
                        'for i in $(seq 1 3); do date; done']
        resp = stream(api.connect_get_namespaced_pod_exec, name, 'default',
                                                   command=exec_command,
                                                   stderr=False, stdin=False,
                                                   stdout=True, tty=False)
        print('EXEC response : %s' % resp)
        self.assertEqual(3, len(resp.splitlines()))

        exec_command = 'uptime'
        resp = stream(api.connect_post_namespaced_pod_exec, name, 'default',
                                                    command=exec_command,
                                                    stderr=False, stdin=False,
                                                    stdout=True, tty=False)
        print('EXEC response : %s' % resp)
        self.assertEqual(1, len(resp.splitlines()))

        resp = stream(api.connect_post_namespaced_pod_exec, name, 'default',
                                                    command='/bin/sh',
                                                    stderr=True, stdin=True,
                                                    stdout=True, tty=False,
                                                    _preload_content=False)
        resp.write_stdin("echo test string 1\n")
        line = resp.readline_stdout(timeout=5)
        self.assertFalse(resp.peek_stderr())
        self.assertEqual("test string 1", line)
        resp.write_stdin("echo test string 2 >&2\n")
        line = resp.readline_stderr(timeout=5)
        self.assertFalse(resp.peek_stdout())
        self.assertEqual("test string 2", line)
        resp.write_stdin("exit\n")
        resp.update(timeout=5)
        line = resp.read_channel(ERROR_CHANNEL)
        status = json.loads(line)
        self.assertEqual(status['status'], 'Success')
        resp.update(timeout=5)
        self.assertFalse(resp.is_open())

        number_of_pods = len(api.list_pod_for_all_namespaces().items)
        self.assertTrue(number_of_pods > 0)

        resp = api.delete_namespaced_pod(name=name, body={},
                                         namespace='default')

    def test_exit_code(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'busybox-test-' + short_uuid()
        pod_manifest = manifest_with_command(name, "while true;do date;sleep 5; done")
        resp = api.create_namespaced_pod(body=pod_manifest,
                                         namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status.phase)

        while True:
            resp = api.read_namespaced_pod(name=name,
                                           namespace='default')
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status.phase)
            if resp.status.phase == 'Running':
                break
            time.sleep(1)

        commands_expected_values = (
            (["false", 1]),
            (["/bin/sh", "-c", "sleep 1; exit 3"], 3),
            (["true", 0]),
            (["/bin/sh", "-c", "ls /"], 0)
        )
        for command, value in commands_expected_values:
            client = stream(api.connect_get_namespaced_pod_exec, name, 'default',
                                                       command=command,
                                                       stderr=True, stdin=False,
                                                       stdout=True, tty=False,
                                                       _preload_content=False)

            self.assertIsNone(client.returncode)
            client.run_forever(timeout=10)
            self.assertEqual(client.returncode, value)

        resp = api.delete_namespaced_pod(name=name, body={},
                                         namespace='default')

    def test_portforward_raw(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'portforward-raw-' + short_uuid()
        pod_manifest = manifest_with_command(
            name,
            'for port in 1234 1235;do ((while true;do nc -l -p $port -e /bin/cat; done)&);done;sleep 60',
        )
        resp = api.create_namespaced_pod(body=pod_manifest,
                                         namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status.phase)

        while True:
            resp = api.read_namespaced_pod(name=name,
                                           namespace='default')
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status.phase)
            if resp.status.phase != 'Pending':
                break
            time.sleep(1)

        pf = portforward(api.connect_get_namespaced_pod_portforward,
                         name, 'default',
                         ports='1234,1235')
        sock1234 = pf.socket(1234)
        sock1235 = pf.socket(1235)
        sock1234.setblocking(True)
        sock1235.setblocking(True)
        sent1234 = b'Test port 1234 forwarding...'
        sent1235 = b'Test port 1235 forwarding...'
        sock1234.sendall(sent1234)
        sock1235.sendall(sent1235)
        reply1234 = b''
        reply1235 = b''
        while True:
            rlist = []
            if sock1234.fileno() != -1:
                rlist.append(sock1234)
            if sock1235.fileno() != -1:
                rlist.append(sock1235)
            if not rlist:
                break
            r, _w, _x = select.select(rlist, [], [], 1)
            if not r:
                break
            if sock1234 in r:
                data = sock1234.recv(1024)
                if data:
                    reply1234 += data
                else:
                    assert False, 'Unexpected sock1234 close'
            if sock1235 in r:
                data = sock1235.recv(1024)
                if data:
                    reply1235 += data
                else:
                    assert False, 'Unexpected sock1235 close'
        self.assertEqual(reply1234, sent1234)
        self.assertEqual(reply1235, sent1235)
        for sock in (sock1234, sock1235):
            sent = b'Another test using fileno %s' % str(sock.fileno()).encode()
            sock.sendall(sent)
            reply = b''
            while True:
                r, _w, _x = select.select([sock], [], [], 1)
                if not r:
                    break
                data = sock.recv(1024)
                if data:
                    reply += data
                else:
                    assert False, 'Unexpected sock close'
            self.assertEqual(reply, sent)
            sock.close()
        self.assertIsNone(pf.error(1234))
        self.assertIsNone(pf.error(1235))

        resp = api.delete_namespaced_pod(name=name, body={},
                                         namespace='default')

    def test_portforward_http(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'portforward-http-' +  short_uuid()
        pod_manifest = {
            'apiVersion': 'v1',
            'kind': 'Pod',
            'metadata': {
                'name': name
            },
            'spec': {
                'containers': [{
                    'name': 'nginx',
                    'image': 'nginx',
                }]
            }
        }

        resp = api.create_namespaced_pod(body=pod_manifest,
                                         namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status.phase)

        while True:
            resp = api.read_namespaced_pod(name=name,
                                           namespace='default')
            self.assertEqual(name, resp.metadata.name)
            self.assertTrue(resp.status.phase)
            if resp.status.phase != 'Pending':
                break
            time.sleep(1)

        def kubernetes_create_connection(address, *args, **kwargs):
            dns_name = address[0]
            if isinstance(dns_name, bytes):
                dns_name = dns_name.decode()
            dns_name = dns_name.split(".")
            if len(dns_name) != 3 or dns_name[2] != "kubernetes":
                return socket_create_connection(address, *args, **kwargs)
            pf = portforward(api.connect_get_namespaced_pod_portforward,
                             dns_name[0], dns_name[1], ports=str(address[1]))
            return pf.socket(address[1])

        socket_create_connection = socket.create_connection
        try:
            socket.create_connection = kubernetes_create_connection
            response = urllib.request.urlopen('http://%s.default.kubernetes/' % name)
            html = response.read().decode('utf-8')
        finally:
            socket.create_connection = socket_create_connection

        self.assertEqual(response.status, 200)
        self.assertTrue('<h1>Welcome to nginx!</h1>' in html)

        resp = api.delete_namespaced_pod(name=name, body={},
                                         namespace='default')

    def test_service_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'frontend-' + short_uuid()
        service_manifest = {'apiVersion': 'v1',
                            'kind': 'Service',
                            'metadata': {'labels': {'name': name},
                                         'name': name,
                                         'resourceversion': 'v1'},
                            'spec': {'ports': [{'name': 'port',
                                                'port': 80,
                                                'protocol': 'TCP',
                                                'targetPort': 80}],
                                     'selector': {'name': name}}}

        resp = api.create_namespaced_service(body=service_manifest,
                                             namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        resp = api.read_namespaced_service(name=name,
                                           namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        service_manifest['spec']['ports'] = [{'name': 'new',
                                              'port': 8080,
                                              'protocol': 'TCP',
                                              'targetPort': 8080}]
        resp = api.patch_namespaced_service(body=service_manifest,
                                            name=name,
                                            namespace='default')
        self.assertEqual(2, len(resp.spec.ports))
        self.assertTrue(resp.status)

        resp = api.delete_namespaced_service(name=name, body={},
                                             namespace='default')

    def test_replication_controller_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'frontend-' + short_uuid()
        rc_manifest = {
            'apiVersion': 'v1',
            'kind': 'ReplicationController',
            'metadata': {'labels': {'name': name},
                         'name': name},
            'spec': {'replicas': 2,
                     'selector': {'name': name},
                     'template': {'metadata': {
                         'labels': {'name': name}},
                         'spec': {'containers': [{
                             'image': 'nginx',
                             'name': 'nginx',
                             'ports': [{'containerPort': 80,
                                        'protocol': 'TCP'}]}]}}}}

        resp = api.create_namespaced_replication_controller(
            body=rc_manifest, namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertEqual(2, resp.spec.replicas)

        resp = api.read_namespaced_replication_controller(
            name=name, namespace='default')
        self.assertEqual(name, resp.metadata.name)
        self.assertEqual(2, resp.spec.replicas)

        resp = api.delete_namespaced_replication_controller(
            name=name, body={}, namespace='default')

    def test_configmap_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'test-configmap-' + short_uuid()
        test_configmap = {
            "kind": "ConfigMap",
            "apiVersion": "v1",
            "metadata": {
                "name": name,
            },
            "data": {
                "config.json": "{\"command\":\"/usr/bin/mysqld_safe\"}",
                "frontend.cnf": "[mysqld]\nbind-address = 10.0.0.3\nport = 3306\n"
            }
        }

        resp = api.create_namespaced_config_map(
            body=test_configmap, namespace='default'
        )
        self.assertEqual(name, resp.metadata.name)

        resp = api.read_namespaced_config_map(
            name=name, namespace='default')
        self.assertEqual(name, resp.metadata.name)

        test_configmap['data']['config.json'] = "{}"
        resp = api.patch_namespaced_config_map(
            name=name, namespace='default', body=test_configmap)

        resp = api.delete_namespaced_config_map(
            name=name, body={}, namespace='default')

        resp = api.list_namespaced_config_map('default', pretty=True)
        self.assertEqual([], resp.items)

    def test_node_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        for item in api.list_node().items:
            node = api.read_node(name=item.metadata.name)
            self.assertTrue(len(node.metadata.labels) > 0)
            self.assertTrue(isinstance(node.metadata.labels, dict))
