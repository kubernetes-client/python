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

from kubernetes import client, config


def main():
    # Fetching and loading Kubernetes Information
    config.load_kube_config()

    v1 = client.CoreV1Api()

    # Creating namespace
    create_namespace = v1.create_namespace(client.V1Namespace(
        metadata=client.V1ObjectMeta(
            name="kube-client-test"
        )
        )
    )

    # Listing pods in the namespace that we created
    list_namespaces = v1.list_namespaced_pod("kube-client")

    # Displaying Pod Information
    for i in list_namespaces.items:
        print("%s\t%s\t%s" % (
            i.status.pod_ip,
            i.metadata.namespace,
            i.metadata.name)
              )


if __name__ == "__main__":
    main()
