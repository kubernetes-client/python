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

    extension = client.ExtensionsV1beta1Api()

    # Container
    container = client.V1Container(
      name="nginx",
      image="nginx:1.7.9",
      image_pull_policy="IfNotPresent",
      ports=[client.V1ContainerPort(container_port=80)]
    )

    # Template
    template = client.V1PodTemplateSpec(
      metadata=client.V1ObjectMeta(labels={"app": "nginx", "version": "v2.0"}),
      spec=client.V1PodSpec(containers=[container]))

    # Spec
    spec = client.ExtensionsV1beta1DeploymentSpec(
      replicas=3,
      selector=client.V1LabelSelector(match_labels={"app": "nginx"}),
      strategy=client.ExtensionsV1beta1DeploymentStrategy(
          rolling_update=client.ExtensionsV1beta1RollingUpdateDeployment(
              max_surge=1,
              max_unavailable=0)),
      template=template)

    # Deployment
    deployment = client.ExtensionsV1beta1Deployment(
      api_version="extensions/v1beta1",
      kind="Deployment",
      metadata=client.V1ObjectMeta(name="nginx-deployment"),
      spec=spec)

    # Creation of the Deployment in specified namespace
    extension.patch_namespaced_deployment(
        name="nginx-deployment",
        namespace="kube-client",
        body=deployment)


if __name__ == "__main__":
    main()
