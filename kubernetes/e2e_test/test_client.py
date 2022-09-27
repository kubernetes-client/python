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
import os
import select
import socket
import time
import unittest
import uuid
import six

from kubernetes.client import api_client
from kubernetes.client.api import core_v1_api
from kubernetes.e2e_test import base
from kubernetes.stream import stream, portforward
from kubernetes.stream.ws_client import ERROR_CHANNEL
from kubernetes.client.rest import ApiException

import six.moves.urllib.request as urllib_request

if six.PY3:
    from http import HTTPStatus
else:
    import httplib


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
        pod_manifest = manifest_with_command(
            name, "while true;do date;sleep 5; done")

        # wait for the default service account to be created
        timeout = time.time() + 30
        while True:
            if time.time() > timeout:
                print('timeout waiting for default service account creation')
                break
            try:
                resp = api.read_namespaced_service_account(name='default',
                                                           namespace='default')
            except ApiException as e:
                if (six.PY3 and e.status != HTTPStatus.NOT_FOUND) or (
                        six.PY3 is False and e.status != httplib.NOT_FOUND):
                    print('error: %s' % e)
                    self.fail(
                        msg="unexpected error getting default service account")
                print('default service not found yet: %s' % e)
                time.sleep(1)
                continue
            self.assertEqual('default', resp.metadata.name)
            break

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
        while True:
            line = resp.read_channel(ERROR_CHANNEL)
            if line != '':
                break
            time.sleep(1)
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
        pod_manifest = manifest_with_command(
            name, "while true;do date;sleep 5; done")

        # wait for the default service account to be created
        timeout = time.time() + 30
        while True:
            if time.time() > timeout:
                print('timeout waiting for default service account creation')
                break

            try:
                resp = api.read_namespaced_service_account(name='default',
                                                           namespace='default')
            except ApiException as e:
                if (six.PY3 and e.status != HTTPStatus.NOT_FOUND) or (
                        six.PY3 is False and e.status != httplib.NOT_FOUND):
                    print('error: %s' % e)
                    self.fail(
                        msg="unexpected error getting default service account")
                print('default service not found yet: %s' % e)
                time.sleep(1)
                continue
            self.assertEqual('default', resp.metadata.name)
            break

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
            client = stream(
                api.connect_get_namespaced_pod_exec,
                name,
                'default',
                command=command,
                stderr=True,
                stdin=False,
                stdout=True,
                tty=False,
                _preload_content=False)

            self.assertIsNone(client.returncode)
            client.run_forever(timeout=10)
            self.assertEqual(client.returncode, value)
            self.assertEqual(client.returncode, value)  # check idempotence

        resp = api.delete_namespaced_pod(name=name, body={},
                                         namespace='default')

    def test_portforward_raw(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        with open(os.path.join(os.path.dirname(__file__), 'port_server.py')) as fh:
            port_server_py = fh.read()
        name = 'portforward-raw-' + short_uuid()
        resp = api.create_namespaced_config_map(
            body={
                'apiVersion': 'v1',
                'kind': 'ConfigMap',
                'metadata': {
                    'name': name,
                },
                'data': {
                    'port-server.py': port_server_py,
                }
            },
            namespace='default',
        )
        resp = api.create_namespaced_pod(
            body={
                'apiVersion': 'v1',
                'kind': 'Pod',
                'metadata': {
                    'name': name
                },
                'spec': {
                    'containers': [
                        {
                            'name': 'port-server',
                            'image': 'python',
                            'command': [
                                'python', '-u', '/opt/port-server.py', '1234', '1235',
                            ],
                            'volumeMounts': [
                                {
                                    'name': 'port-server',
                                    'mountPath': '/opt',
                                    'readOnly': True,
                                },
                            ],
                            'startupProbe': {
                                'tcpSocket': {
                                    'port': 1235,
                                },
                                'periodSeconds': 1,
                                'failureThreshold': 30,
                            },
                        },
                    ],
                    'restartPolicy': 'Never',
                    'volumes': [
                        {
                            'name': 'port-server',
                            'configMap': {
                                'name': name,
                            },
                        },
                    ],
                },
            },
            namespace='default',
        )
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status.phase)

        timeout = time.time() + 60
        while True:
            resp = api.read_namespaced_pod(name=name,
                                           namespace='default')
            self.assertEqual(name, resp.metadata.name)
            if resp.status.phase == 'Running':
                if resp.status.container_statuses[0].ready:
                    break
            else:
                self.assertEqual(resp.status.phase, 'Pending')
            self.assertTrue(time.time() < timeout)
            time.sleep(1)

        for ix in range(10):
            ix = str(ix + 1).encode()
            pf = portforward(api.connect_get_namespaced_pod_portforward,
                             name, 'default',
                             ports='1234,1235,1236')
            self.assertTrue(pf.connected)
            sock1234 = pf.socket(1234)
            sock1235 = pf.socket(1235)
            sock1234.setblocking(True)
            sock1235.setblocking(True)
            sent1234 = b'Test ' + ix + b' port 1234 forwarding'
            sent1235 = b'Test ' + ix + b' port 1235 forwarding'
            sock1234.sendall(sent1234)
            sock1235.sendall(sent1235)
            reply1234 = b''
            reply1235 = b''
            timeout = time.time() + 60
            while reply1234 != sent1234 or reply1235 != sent1235:
                self.assertNotEqual(sock1234.fileno(), -1)
                self.assertNotEqual(sock1235.fileno(), -1)
                self.assertTrue(time.time() < timeout)
                r, _w, _x = select.select([sock1234, sock1235], [], [], 1)
                if sock1234 in r:
                    data = sock1234.recv(1024)
                    self.assertNotEqual(data, b'', 'Unexpected socket close')
                    reply1234 += data
                    self.assertTrue(sent1234.startswith(reply1234))
                if sock1235 in r:
                    data = sock1235.recv(1024)
                    self.assertNotEqual(data, b'', 'Unexpected socket close')
                    reply1235 += data
                    self.assertTrue(sent1235.startswith(reply1235))
            self.assertTrue(pf.connected)

            sock = pf.socket(1236)
            sock.setblocking(True)
            self.assertEqual(sock.recv(1024), b'')
            self.assertIsNotNone(pf.error(1236))
            sock.close()

            for sock in (sock1234, sock1235):
                self.assertTrue(pf.connected)
                sent = b'Another test ' + ix + b' using fileno ' + str(sock.fileno()).encode()
                sock.sendall(sent)
                reply = b''
                timeout = time.time() + 60
                while reply != sent:
                    self.assertNotEqual(sock.fileno(), -1)
                    self.assertTrue(time.time() < timeout)
                    r, _w, _x = select.select([sock], [], [], 1)
                    if r:
                        data = sock.recv(1024)
                        self.assertNotEqual(data, b'', 'Unexpected socket close')
                        reply += data
                        self.assertTrue(sent.startswith(reply))
                sock.close()
            time.sleep(1)
            self.assertFalse(pf.connected)
            self.assertIsNone(pf.error(1234))
            self.assertIsNone(pf.error(1235))

        resp = api.delete_namespaced_pod(name=name, namespace='default')
        resp = api.delete_namespaced_config_map(name=name, namespace='default')

    def test_portforward_http(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'portforward-http-' + short_uuid()
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
            response = urllib_request.urlopen(
                'http://%s.default.kubernetes/' % name)
            html = response.read().decode('utf-8')
        finally:
            socket.create_connection = socket_create_connection

        self.assertEqual(response.code, 200)
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
            name=name, namespace='default', propagation_policy='Background')

    def test_configmap_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        name = 'test-configmap-' + short_uuid()
        test_configmap = {
            "kind": "ConfigMap",
            "apiVersion": "v1",
            "metadata": {
                "name": name,
                "labels": {"e2e-tests": "true"},
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

        json_patch_name = "json_patch_name"
        json_patch_body = [
            {
                "op": "replace",
                "path": "/data",
                "value": {
                    "new_value": json_patch_name,
                    "config.json": "{\"command\":\"/usr/bin/mysqld_safe\"}",
                    "frontend.cnf": "[mysqld]\nbind-address = 10.0.0.3\nport = 3306\n"
                }
            }
        ]
        resp = api.patch_namespaced_config_map(
            name=name, namespace='default', body=json_patch_body)
        self.assertEqual(json_patch_name, resp.data["new_value"])

        merge_patch_name = "merge_patch_name"
        merge_patch_body = {"data": {
            "new_value": merge_patch_name,
            "config.json": "{\"command\":\"/usr/bin/mysqld_safe\"}",
            "frontend.cnf": "[mysqld]\nbind-address = 10.0.0.3\nport = 3306\n"
        }}
        resp = api.patch_namespaced_config_map(
            name=name, namespace='default', body=merge_patch_body)
        self.assertEqual(merge_patch_name, resp.data["new_value"])

        resp = api.delete_namespaced_config_map(
            name=name, body={}, namespace='default')

        resp = api.list_namespaced_config_map(
            'default', pretty=True, label_selector="e2e-tests=true")
        self.assertEqual([], resp.items)

    def test_node_apis(self):
        client = api_client.ApiClient(configuration=self.config)
        api = core_v1_api.CoreV1Api(client)

        for item in api.list_node().items:
            node = api.read_node(name=item.metadata.name)
            self.assertTrue(len(node.metadata.labels) > 0)
            self.assertTrue(isinstance(node.metadata.labels, dict))
