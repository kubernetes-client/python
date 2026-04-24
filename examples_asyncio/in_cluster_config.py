# Copyright 2017 The Kubernetes Authors.
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

# Simple example to show loading config from the cluster

#
# If you get 403 errors from API server you will have to configure
# RBAC to add necessay permissions.
#
# ---
# kind: ClusterRole
# apiVersion: rbac.authorization.k8s.io/v1
# metadata:
#   name: pods-list
# rules:
# - apiGroups: [""]
#   resources: ["pods"]
#   verbs: ["list"]
# ---
# kind: ClusterRoleBinding
# apiVersion: rbac.authorization.k8s.io/v1
# metadata:
#   name: pods-list
# subjects:
# - kind: ServiceAccount
#   name: default
#   namespace: default
# roleRef:
#   kind: ClusterRole
#   name: pods-list
#   apiGroup: rbac.authorization.k8s.io
# ---
#
# Doc: https://kubernetes.io/docs/reference/access-authn-authz/rbac/
#
# This example can be run from the image: https://hub.docker.com/r/tpimages/kubernetes_asyncio_examples/
#
# $ kubectl run kubernetes-asyncio-examples --image tpimages/kubernetes_asyncio_examples
#

import asyncio
import sys
import traceback

from kubernetes_asyncio import client, config


async def main():

    while True:

        try:

            # it works only if this script is run by K8s as a POD
            config.load_incluster_config()

            v1 = client.CoreV1Api()
            print("Listing pods with their IPs:")
            ret = await v1.list_pod_for_all_namespaces()

            for i in ret.items:
                print(i.status.pod_ip, i.metadata.namespace, i.metadata.name)

        except Exception:
            traceback.print_exc(file=sys.stdout)

        finally:
            print("sleep 10s")
            await asyncio.sleep(10)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
