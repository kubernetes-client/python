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

"""
Shows how to enable TCP keepalive on the client connections.

Long-lived requests such as watches or `follow=True` log streams can hang
silently when the connection is dropped by a load balancer or a firewall
without a FIN/RST reaching the client. Enabling TCP keepalive lets the
kernel detect a dead peer and close the socket, so the client raises an
error instead of blocking forever.

The `socket_options` on `Configuration` are passed straight to the
underlying urllib3 connection pool, on top of urllib3's own defaults.
"""

import socket

from kubernetes import client, config


def keepalive_socket_options():
    """Return socket options that enable TCP keepalive.

    TCP_KEEPIDLE / TCP_KEEPINTVL / TCP_KEEPCNT are not available on every
    platform, so they are added only when the running platform exposes them.
    """
    options = [(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)]

    # Start probing after 30s idle, probe every 10s, drop after 6 failures.
    if hasattr(socket, "TCP_KEEPIDLE"):
        options.append((socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 30))
    if hasattr(socket, "TCP_KEEPINTVL"):
        options.append((socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 10))
    if hasattr(socket, "TCP_KEEPCNT"):
        options.append((socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 6))

    return options


def main():
    config.load_kube_config()

    configuration = client.Configuration.get_default_copy()
    configuration.socket_options = keepalive_socket_options()

    api_client = client.ApiClient(configuration=configuration)
    v1 = client.CoreV1Api(api_client=api_client)

    print("Listing pods with TCP keepalive enabled:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print(f"{i.status.pod_ip}\t{i.metadata.namespace}\t{i.metadata.name}")


if __name__ == '__main__':
    main()
