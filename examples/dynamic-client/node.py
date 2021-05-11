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
This example demonstrates how to list cluster nodes using dynamic client.

"""

from kubernetes import config, dynamic
from kubernetes.client import api_client


def main():
    # Creating a dynamic client
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )

    # fetching the node api
    api = client.resources.get(api_version="v1", kind="Node")

    # Listing cluster nodes

    print("%s\t\t%s\t\t%s" % ("NAME", "STATUS", "VERSION"))
    for item in api.get().items:
        node = api.get(name=item.metadata.name)
        print(
            "%s\t%s\t\t%s\n"
            % (
                node.metadata.name,
                node.status.conditions[3]["type"],
                node.status.nodeInfo.kubeProxyVersion,
            )
        )


if __name__ == "__main__":
    main()
