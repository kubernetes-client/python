# Copyright 2021 The Kubernetes Authors.
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
This example demonstrates the following:
    - Creation of a k8s service using dynamic-client
    - List, patch(update), delete the service
"""

from kubernetes import config, dynamic
from kubernetes.client import api_client


def main():
    # Creating a dynamic client
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )

    # fetching the service api
    api = client.resources.get(api_version="v1", kind="Service")

    name = "frontend-service"

    service_manifest = {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {"labels": {"name": name}, "name": name, "resourceversion": "v1"},
        "spec": {
            "ports": [
                {"name": "port", "port": 80, "protocol": "TCP", "targetPort": 80}
            ],
            "selector": {"name": name},
        },
    }

    # Creating service `frontend-service` in the `default` namespace

    service = api.create(body=service_manifest, namespace="default")

    print("\n[INFO] service `frontend-service` created\n")

    # Listing service `frontend-service` in the `default` namespace
    service_created = api.get(name=name, namespace="default")

    print("%s\t%s" % ("NAMESPACE", "NAME"))
    print(
        "%s\t\t%s\n"
        % (service_created.metadata.namespace, service_created.metadata.name)
    )

    # Patching the `spec` section of the `frontend-service`

    service_manifest["spec"]["ports"] = [
        {"name": "new", "port": 8080, "protocol": "TCP", "targetPort": 8080}
    ]

    service_patched = api.patch(body=service_manifest, name=name, namespace="default")

    print("\n[INFO] service `frontend-service` patched\n")
    print("%s\t%s\t\t\t%s" % ("NAMESPACE", "NAME", "PORTS"))
    print(
        "%s\t\t%s\t%s\n"
        % (
            service_patched.metadata.namespace,
            service_patched.metadata.name,
            service_patched.spec.ports,
        )
    )

    # Deleting service `frontend-service` from the `default` namespace
    service_deleted = api.delete(name=name, body={}, namespace="default")

    print("\n[INFO] service `frontend-service` deleted\n")


if __name__ == "__main__":
    main()
