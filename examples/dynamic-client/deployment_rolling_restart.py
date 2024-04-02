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
    - Creation of a k8s deployment using dynamic-client
    - Rolling restart of the deployment (demonstrate patch/update action)
    - Listing & deletion of the deployment
"""


from kubernetes import config, dynamic
from kubernetes.client import api_client
import datetime
import pytz

def main():
    # Creating a dynamic client
    client = dynamic.DynamicClient(
        api_client.ApiClient(configuration=config.load_kube_config())
    )

    # fetching the deployment api
    api = client.resources.get(api_version="apps/v1", kind="Deployment")

    name = "nginx-deployment"

    deployment_manifest = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {"labels": {"app": "nginx"}, "name": name},
        "spec": {
            "replicas": 3,
            "selector": {"matchLabels": {"app": "nginx"}},
            "template": {
                "metadata": {"labels": {"app": "nginx"}},
                "spec": {
                    "containers": [
                        {
                            "name": "nginx",
                            "image": "nginx:1.14.2",
                            "ports": [{"containerPort": 80}],
                        }
                    ]
                },
            },
        },
    }

    # Creating deployment `nginx-deployment` in the `default` namespace

    deployment = api.create(body=deployment_manifest, namespace="default")

    print("\n[INFO] deployment `nginx-deployment` created\n")

    # Listing deployment `nginx-deployment` in the `default` namespace

    deployment_created = api.get(name=name, namespace="default")

    print("%s\t%s\t\t\t%s\t%s" % ("NAMESPACE", "NAME", "REVISION", "RESTARTED-AT"))
    print(
        "%s\t\t%s\t%s\t\t%s\n"
        % (
            deployment_created.metadata.namespace,
            deployment_created.metadata.name,
            deployment_created.metadata.annotations,
            deployment_created.spec.template.metadata.annotations,
        )
    )

    # Patching the `spec.template.metadata` section to add `kubectl.kubernetes.io/restartedAt` annotation
    # In order to perform a rolling restart on the deployment `nginx-deployment`

    deployment_manifest["spec"]["template"]["metadata"] = {
        "annotations": {
            "kubectl.kubernetes.io/restartedAt": datetime.datetime.now(tz=pytz.UTC)
            .isoformat()
        }
    }

    deployment_patched = api.patch(
        body=deployment_manifest, name=name, namespace="default"
    )

    print("\n[INFO] deployment `nginx-deployment` restarted\n")
    print(
        "%s\t%s\t\t\t%s\t\t\t\t\t\t%s"
        % ("NAMESPACE", "NAME", "REVISION", "RESTARTED-AT")
    )
    print(
        "%s\t\t%s\t%s\t\t%s\n"
        % (
            deployment_patched.metadata.namespace,
            deployment_patched.metadata.name,
            deployment_patched.metadata.annotations,
            deployment_patched.spec.template.metadata.annotations,
        )
    )

    # Deleting deployment `nginx-deployment` from the `default` namespace

    deployment_deleted = api.delete(name=name, body={}, namespace="default")

    print("\n[INFO] deployment `nginx-deployment` deleted\n")


if __name__ == "__main__":
    main()
