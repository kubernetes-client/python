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
    - Creation of a k8s configmap using dynamic-client
    - List, patch(update), delete the configmap
"""

from kubernetes import config, dynamic
from kubernetes.client import api_client


def main():
    # Creating a dynamic client
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )

    # fetching the configmap api
    api = client.resources.get(api_version="v1", kind="ConfigMap")

    configmap_name = "test-configmap"

    configmap_manifest = {
        "kind": "ConfigMap",
        "apiVersion": "v1",
        "metadata": {
            "name": configmap_name,
            "labels": {
                "foo": "bar",
            },
        },
        "data": {
            "config.json": '{"command":"/usr/bin/mysqld_safe"}',
            "frontend.cnf": "[mysqld]\nbind-address = 10.0.0.3\n",
        },
    }

    # Creating configmap `test-configmap` in the `default` namespace

    configmap = api.create(body=configmap_manifest, namespace="default")

    print("\n[INFO] configmap `test-configmap` created\n")

    # Listing the configmaps in the `default` namespace

    configmap_list = api.get(
        name=configmap_name, namespace="default", label_selector="foo=bar"
    )

    print("NAME:\n%s\n" % (configmap_list.metadata.name))
    print("DATA:\n%s\n" % (configmap_list.data))

    # Updating the configmap's data, `config.json`

    configmap_manifest["data"]["config.json"] = "{}"

    configmap_patched = api.patch(
        name=configmap_name, namespace="default", body=configmap_manifest
    )

    print("\n[INFO] configmap `test-configmap` patched\n")
    print("NAME:\n%s\n" % (configmap_patched.metadata.name))
    print("DATA:\n%s\n" % (configmap_patched.data))

    # Deleting configmap `test-configmap` from the `default` namespace

    configmap_deleted = api.delete(name=configmap_name, body={}, namespace="default")
    print("\n[INFO] configmap `test-configmap` deleted\n")


if __name__ == "__main__":
    main()
