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

"""
Uses a Custom Resource Definition (CRD) to create a custom object, in this case
a CronTab. This example use an example CRD from this tutorial:
https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/

Apply the following yaml manifest to create a cluster-scoped CustomResourceDefinition (CRD)

apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: crontabs.stable.example.com
spec:
  group: stable.example.com
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                cronSpec:
                  type: string
                image:
                  type: string
                replicas:
                  type: integer
  scope: Cluster
  names:
    plural: crontabs
    singular: crontab
    kind: CronTab
    shortNames:
    - ct
"""

from pprint import pprint

from kubernetes import client, config


def main():
    config.load_kube_config()

    api = client.CustomObjectsApi()

    # definition of custom resource
    test_resource = {
        "apiVersion": "stable.example.com/v1",
        "kind": "CronTab",
        "metadata": {"name": "test-crontab"},
        "spec": {"cronSpec": "* * * * */5", "image": "my-awesome-cron-image"},
    }

    # patch to update the `spec.cronSpec` field
    cronspec_patch = {
        "spec": {"cronSpec": "* * * * */15", "image": "my-awesome-cron-image"}
    }

    # patch to add the `metadata.labels` field
    metadata_label_patch = {
        "metadata": {
            "labels": {
                "foo": "bar",
            }
        }
    }

    # create a cluster scoped resource
    created_resource = api.create_cluster_custom_object(
        group="stable.example.com",
        version="v1",
        plural="crontabs",
        body=test_resource,
    )

    # get the cluster scoped resource
    resource = api.get_cluster_custom_object(
        group="stable.example.com",
        version="v1",
        name="test-crontab",
        plural="crontabs",
    )
    print("%s\t\t%s" % ("NAME", "SCHEDULE"))
    print(
        "%s\t%s\n" %
        (resource["metadata"]["name"],
         resource["spec"]["cronSpec"]))

    # patch the `spec.cronSpec` field of the custom resource
    patched_resource = api.patch_cluster_custom_object(
        group="stable.example.com",
        version="v1",
        plural="crontabs",
        name="test-crontab",
        body=cronspec_patch,
    )
    print("%s\t\t%s" % ("NAME", "PATCHED_SCHEDULE"))
    print(
        "%s\t%s\n" %
        (patched_resource["metadata"]["name"],
         patched_resource["spec"]["cronSpec"]))

    # patch the `metadata.labels` field of the custom resource
    patched_resource = api.patch_cluster_custom_object(
        group="stable.example.com",
        version="v1",
        plural="crontabs",
        name="test-crontab",
        body=metadata_label_patch,
    )
    print("%s\t\t%s" % ("NAME", "PATCHED_LABELS"))
    print(
        "%s\t%s\n" %
        (patched_resource["metadata"]["name"],
         patched_resource["metadata"]["labels"]))

    # delete the custom resource "test-crontab"
    api.delete_cluster_custom_object(
        group="stable.example.com",
        version="v1",
        name="test-crontab",
        plural="crontabs",
        body=client.V1DeleteOptions(),
    )
    print("Resource `test-crontab` deleted!")


if __name__ == "__main__":
    main()
