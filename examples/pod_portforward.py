# Copyright 2020 The Kubernetes Authors.
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

"""
Shows the functionality of portforward streaming using an nginx container.
"""

import socket
import time
import urllib.request

from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import portforward


def portforward_commands(api_instance):
    name = 'portforward-example'
    resp = None
    try:
        resp = api_instance.read_namespaced_pod(name=name,
                                                namespace='default')
    except ApiException as e:
        if e.status != 404:
            print("Unknown error: %s" % e)
            exit(1)

    if not resp:
        print("Pod %s does not exist. Creating it..." % name)
        pod_manifest = {
            'apiVersion': 'v1',
            'kind': 'Pod',
            'metadata': {
                'name': name
            },
            'spec': {
                'containers': [{
                    'image': 'nginx',
                    'name': 'nginx',
                }]
            }
        }
        resp = api_instance.create_namespaced_pod(body=pod_manifest,
                                                  namespace='default')
        while True:
            resp = api_instance.read_namespaced_pod(name=name,
                                                    namespace='default')
            if resp.status.phase != 'Pending':
                break
            time.sleep(1)
        print("Done.")

    pf = portforward(api_instance.connect_get_namespaced_pod_portforward,
                     name, 'default',
                     ports='80,8080:80')
    for port in (80, 8080):
        http = pf.socket(port)
        http.settimeout(1)
        http.sendall(b'GET / HTTP/1.1\r\n')
        http.sendall(b'Host: 127.0.0.1\r\n')
        http.sendall(b'Accept: */*\r\n')
        http.sendall(b'\r\n')
        response = b''
        while True:
            try:
                response += http.recv(1024)
            except socket.timeout:
                break
        print(response.decode('utf-8'))
        http.close()

    # Monkey patch socket.create_connection which is used by http.client and
    # urllib.request. The same can be done with urllib3.util.connection.create_connection
    # if the "requests" package is used.
    def kubernetes_create_connection(address, *args, **kwargs):
        dns_name = address[0]
        if isinstance(dns_name, bytes):
            dns_name = dns_name.decode()
        # Look for "<pod-name>.<namspace>.kubernetes" dns names and if found
        # provide a socket that is port forwarded to the kuberntest pod.
        dns_name = dns_name.split(".")
        if len(dns_name) != 3 or dns_name[2] != "kubernetes":
            return socket_create_connection(address, *args, **kwargs)
        pf = portforward(api_instance.connect_get_namespaced_pod_portforward,
                         dns_name[0], dns_name[1], ports=str(address[1]))
        return pf.socket(address[1])

    socket_create_connection = socket.create_connection
    socket.create_connection = kubernetes_create_connection

    # Access the nginx http server using the "<pod-name>.<namespace>.kubernetes" dns name.
    response = urllib.request.urlopen('http://%s.default.kubernetes' % name)
    html = response.read().decode('utf-8')
    response.close()
    print('Status:', response.status)
    print(html)


def main():
    config.load_kube_config()
    c = Configuration()
    c.assert_hostname = False
    #Configuration.set_default(c)
    core_v1 = core_v1_api.CoreV1Api()

    portforward_commands(core_v1)


if __name__ == '__main__':
    main()
