# Copyright 2019 The Kubernetes Authors.
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

# This example use an example CRD from this tutorial:
# https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/
#
# The following yaml manifest has to be applied first:
#
# apiVersion: apiextensions.k8s.io/v1beta1
# kind: CustomResourceDefinition
# metadata:
#   name: crontabs.stable.example.com
# spec:
#   group: stable.example.com
#   versions:
#     - name: v1
#       served: true
#       storage: true
#   scope: Namespaced
#   names:
#     plural: crontabs
#     singular: crontab
#     kind: CronTab
#     shortNames:
#     - ct


from pprint import pprint

from kubernetes import client, config


def main():

    config.load_kube_config()

    api = client.CustomObjectsApi()

    # it's my custom resource defined as Dict
    my_resource = {
        "apiVersion": "stable.example.com/v1",
        "kind": "CronTab",
        "metadata": {"name": "my-new-cron-object"},
        "cronSpec": "* * * * */5",
        "image": "my-awesome-cron-image",
    }

    # create the resource
    api.create_namespaced_custom_object(
        group="stable.example.com",
        version="v1",
        namespace="default",
        plural="crontabs",
        body=my_resource,
    )
    print("Resource created")

    # get the resource and print out data
    resource = api.get_namespaced_custom_object(
        group="stable.example.com",
        version="v1",
        name="my-new-cron-object",
        namespace="default",
        plural="crontabs",
    )
    print("Resource details:")
    pprint(resource)

    # delete it
    api.delete_namespaced_custom_object(
        group="stable.example.com",
        version="v1",
        name="my-new-cron-object",
        namespace="default",
        plural="crontabs",
        body=client.V1DeleteOptions(),
    )
    print("Resource deleted")


if __name__ == "__main__":
    main()
