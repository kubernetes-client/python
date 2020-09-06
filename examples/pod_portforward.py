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

import select
import socket
import time
import urllib.request

from kubernetes import config
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import portforward

##############################################################################
# Kubernetes pod port forwarding works by directly providing a socket which
# the python application uses to send and receive data on. This is in contrast
# to the go client, which opens a local port that the go application then has
# to open to get a socket to transmit data.
#
# This simplifies the python application, there is not local port to worry
# about if that port number is available. Nor does the python application have
# to then deal with opening this local port. The socket used to transmit data
# is immediately provided to the python application.
#
# Below also is an example of monkey patching the socket.create_connection
# function so that DNS names of the following formats will access kubernetes
# ports:
#
#    <pod-name>.<namespace>.kubernetes
#    <pod-name>.pod.<namespace>.kubernetes
#    <service-name>.svc.<namespace>.kubernetes
#    <service-name>.service.<namespace>.kubernetes
#
# These DNS name can be used to interact with pod ports using python libraries,
# such as urllib.request and http.client. For example:
#
# response = urllib.request.urlopen(
#     'https://metrics-server.service.kube-system.kubernetes/'
# )
#
##############################################################################


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
        api_instance.create_namespaced_pod(body=pod_manifest,
                                           namespace='default')
        while True:
            resp = api_instance.read_namespaced_pod(name=name,
                                                    namespace='default')
            if resp.status.phase != 'Pending':
                break
            time.sleep(1)
        print("Done.")

    pf = portforward(
        api_instance.connect_get_namespaced_pod_portforward,
        name, 'default',
        ports='80',
    )
    http = pf.socket(80)
    http.setblocking(True)
    http.sendall(b'GET / HTTP/1.1\r\n')
    http.sendall(b'Host: 127.0.0.1\r\n')
    http.sendall(b'Connection: close\r\n')
    http.sendall(b'Accept: */*\r\n')
    http.sendall(b'\r\n')
    response = b''
    while True:
        select.select([http], [], [])
        data = http.recv(1024)
        if not data:
            break
        response += data
    http.close()
    print(response.decode('utf-8'))
    error = pf.error(80)
    if error is None:
        print("No port forward errors on port 80.")
    else:
        print("Port 80 has the following error: %s" % error)

    # Monkey patch socket.create_connection which is used by http.client and
    # urllib.request. The same can be done with urllib3.util.connection.create_connection
    # if the "requests" package is used.
    socket_create_connection = socket.create_connection
    def kubernetes_create_connection(address, *args, **kwargs):
        dns_name = address[0]
        if isinstance(dns_name, bytes):
            dns_name = dns_name.decode()
        dns_name = dns_name.split(".")
        if dns_name[-1] != 'kubernetes':
            return socket_create_connection(address, *args, **kwargs)
        if len(dns_name) not in (3, 4):
            raise RuntimeError("Unexpected kubernetes DNS name.")
        namespace = dns_name[-2]
        name = dns_name[0]
        port = address[1]
        if len(dns_name) == 4:
            if dns_name[1] in ('svc', 'service'):
                service = api_instance.read_namespaced_service(name, namespace)
                for service_port in service.spec.ports:
                    if service_port.port == port:
                        port = service_port.target_port
                        break
                else:
                    raise RuntimeError("Unable to find service port: %s" % port)
                label_selector = []
                for key, value in service.spec.selector.items():
                    label_selector.append("%s=%s" % (key, value))
                pods = api_instance.list_namespaced_pod(
                    namespace, label_selector=",".join(label_selector)
                )
                if not pods.items:
                    raise RuntimeError("Unable to find service pods.")
                name = pods.items[0].metadata.name
                if isinstance(port, str):
                    for container in pods.items[0].spec.containers:
                        for container_port in container.ports:
                            if container_port.name == port:
                                port = container_port.container_port
                                break
                        else:
                            continue
                        break
                    else:
                        raise RuntimeError("Unable to find service port name: %s" % port)
            elif dns_name[1] != 'pod':
                raise RuntimeError("Unsupported resource type: %s" % dns_name[1])
        pf = portforward(api_instance.connect_get_namespaced_pod_portforward,
                         name, namespace, ports=str(port))
        return pf.socket(port)
    socket.create_connection = kubernetes_create_connection

    # Access the nginx http server using the "<pod-name>.pod.<namespace>.kubernetes" dns name.
    response = urllib.request.urlopen('http://%s.pod.default.kubernetes' % name)
    html = response.read().decode('utf-8')
    response.close()
    print('Status:', response.status)
    print(html)


def main():
    config.load_kube_config()
    c = Configuration.get_default_copy()
    c.assert_hostname = False
    Configuration.set_default(c)
    core_v1 = core_v1_api.CoreV1Api()

    portforward_commands(core_v1)


if __name__ == '__main__':
    main()
