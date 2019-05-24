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

from pprint import pprint

from kubernetes import client, config


def main():
    """
    Change labels of the "minikube" node:
     - Add label "foo" with value "bar". This will overwrite the "foo" label
       if it already exists.
     - Remove the label "baz" from the node.
    """

    config.load_kube_config()

    api_instance = client.CoreV1Api()

    body = {
        "metadata": {
            "labels": {
                "foo": "bar",
                "baz": None}
        }
    }

    api_response = api_instance.patch_node("minikube", body)

    pprint(api_response)


if __name__ == '__main__':
    main()
