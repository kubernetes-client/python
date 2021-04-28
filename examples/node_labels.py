# Copyright 2016 The Kubernetes Authors.
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
    - Get a list of all the cluster nodes
    - Iterate through each node list item
        - Add or overwirite label "foo" with the value "bar"
        - Remove the label "baz"
    - Return the list of node with updated labels
"""

from kubernetes import client, config


def main():
    config.load_kube_config()

    api_instance = client.CoreV1Api()

    body = {
        "metadata": {
            "labels": {
                "foo": "bar",
                "baz": None}
        }
    }
   
    # Listing the cluster nodes
    node_list = api_instance.list_node()   
    print("%s\t\t%s" % ("NAME", "LABELS"))

    # Patching the node labels
    for node in node_list.items:
        api_response = api_instance.patch_node(node.metadata.name, body)
        print("%s\t%s" % (node.metadata.name, node.metadata.labels))


if __name__ == '__main__':
    main()
