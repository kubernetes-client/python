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
# It works only from a pod. You can start an image with Python
# (for example python:latest), exec into the pod, install the library,
# then try out this example.
#
# If you get 403 errors from API server you will have to configure
# RBAC to add the permission to list pods.
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

from kubernetes import client, config


def main():

    # it works only if this script is run by K8s as a POD
    config.load_incluster_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" %
              (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


if __name__ == '__main__':
    main()
