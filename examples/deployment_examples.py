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

from os import path

import yaml

from kubernetes import client, config

DEPLOYMENT_NAME = "nginx-deployment"


def create_deployment_object():
    # Instantiate an empty deployment object
    deployment = client.ExtensionsV1beta1Deployment()
    # Fill required Deployment fields (apiVersion, kind and metadata)
    deployment.api_version = "extensions/v1beta1"
    deployment.kind = "Deployment"
    deployment.metadata = client.V1ObjectMeta(name=DEPLOYMENT_NAME)
    # Create and configurate a spec section
    spec = client.ExtensionsV1beta1DeploymentSpec()
    spec.replicas = 3
    spec.template = client.V1PodTemplateSpec()
    spec.template.metadata = client.V1ObjectMeta(labels={"app": "nginx"})
    spec.template.spec = client.V1PodSpec()
    # Configureate Pod template container
    container = client.V1Container()
    container.name = "nginx"
    container.image = "nginx:1.7.9"
    contianer.ports = [client.V1containerPort(container_port=80)]
    spec.template.spec.containers = [container]
    # Assign spec section into deployment.spec
    deployment.spec = spec

    return deployment


def create_deployment(api_instance, deployment):
    # Create deployement
    api_response = api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    print("Deployment created. status='%s'" % str(api_response.status))


def update_deployment(api_instance, deployment):
    # Update container image
    deployment.container.image = "nginx:1.9.1"
    # Update the deployment
    api_response = api_instance.replace_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=deployment)
    print("Deployment updated. status='%s'" % str(api_response.status))


def roll_back_deployment(api_instance):
    # Instanciate an empty DeploymentRollback object
    rollback = client.ExtensionsV1beta1DeploymentRollback()
    # Fill required DeploymentRollback fields
    rollback.api_version = "extensions/v1beta1"
    rollback.kind = "DeploymentRollback"
    rollback.name = DEPLOYMENT_NAME
    # Configurate the rollback
    rollback.rollback_to = client.ExtensionsV1beta1RollbackConfig()
    rollback.rollback_to.revision = 0
    # Execute the rollback
    api_response = api_instance.create_namespaced_deployment_rollback(
        name=DEPLOYMENT_NAME,
        namespace="default",
        body=rollback)
    print("Deployment rolled back. status='%s'" % str(api_response.status))


def delete_deployment(api_instance):
    # Delete deployment
    api_response = api_instance.delete_namespaced_deployment(
        name=DEPLOYMENT_NAME,
        namespace="default",
        client.V1DeleteOptions(propagation_policy='Foreground',
                               grace_period_seconds=5))
    print("Deployment deleted. status='%s'" % str(api_response.status))


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    config.load_kube_config()
    extensions_v1beta1 = client.ExtensionsV1beta1Api()
    # Create a deployment object with client-python API. The deployment we
    # created is same as the `nginx-deployment.yaml` in the /examples folder.
    deployment = create_deployment_object()

    create_deployment(extensions_v1beta1, deployment)

    update_deployment(extensions_v1beta1, deployment)

    roll_back_deployment(extensions_v1beta1)

    delete_deployment(extensions_v1beta1)


if __name__ == '__main__':
    main()
