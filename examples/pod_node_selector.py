# Copyright 2026 The Kubernetes Authors.
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
Demonstrates how to assign a Pod to specific nodes using `node_selector`
in `V1PodSpec`.

`node_selector` in `client.V1PodSpec` corresponds to the `spec.nodeSelector`
field in Kubernetes manifests. It accepts a dictionary of key-value string
pairs that must match labels on a node for the pod to be eligible for
scheduling onto that node.

For more information, see:
https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector
"""

import time
from kubernetes import client, config
from kubernetes.client.rest import ApiException

POD_NAME = "demo-node-selector-pod"
NAMESPACE = "default"


def main():
    # Load kubeconfig from default location (~/.kube/config)
    config.load_kube_config()
    v1 = client.CoreV1Api()

    # 1. Discover existing nodes to demonstrate matching labels
    print("Listing cluster nodes and their operating system labels...")
    nodes = v1.list_node()
    for node in nodes.items:
        os_label = node.metadata.labels.get("kubernetes.io/os", "unknown")
        arch_label = node.metadata.labels.get("kubernetes.io/arch", "unknown")
        print(
            f"Node: {node.metadata.name} (OS: {os_label}, Arch: {arch_label})"
        )

    # 2. Define the container
    container = client.V1Container(
        name="nginx",
        image="nginx:alpine",
        resources=client.V1ResourceRequirements(
            requests={"cpu": "100m", "memory": "128Mi"},
            limits={"cpu": "200m", "memory": "256Mi"},
        ),
    )

    # 3. Define the PodSpec with node_selector
    # You can specify any key-value pairs matching node labels
    # e.g., standard labels like 'kubernetes.io/os': 'linux'
    # or custom labels like 'disktype': 'ssd' set on nodes.
    pod_spec = client.V1PodSpec(
        containers=[container],
        node_selector={"kubernetes.io/os": "linux"},
        restart_policy="Never",
    )

    # 4. Construct the V1Pod object
    pod_metadata = client.V1ObjectMeta(
        name=POD_NAME,
        labels={"app": "demo-node-selector"},
    )
    pod_body = client.V1Pod(
        api_version="v1",
        kind="Pod",
        metadata=pod_metadata,
        spec=pod_spec,
    )

    try:
        # 5. Create the Pod in the specified namespace
        print(
            f"\nCreating pod '{POD_NAME}' with "
            f"nodeSelector: {pod_spec.node_selector}..."
        )
        created_pod = v1.create_namespaced_pod(
            namespace=NAMESPACE, body=pod_body
        )
        print(f"Pod created successfully in phase: {created_pod.status.phase}")

        # 6. Wait for the scheduler to bind the pod to a matching node
        print("Waiting for pod scheduling...")
        for _ in range(10):
            pod = v1.read_namespaced_pod(name=POD_NAME, namespace=NAMESPACE)
            if pod.spec.node_name:
                print(
                    f"Pod successfully scheduled to node: {pod.spec.node_name}"
                )
                break
            time.sleep(1)
        else:
            print("Pod is still pending scheduling.")

    except ApiException as e:
        if e.status == 409:
            print(f"Pod '{POD_NAME}' already exists. Please remove it first.")
        else:
            print(f"Exception when creating pod: {e}")
    finally:
        # 7. Clean up the created pod (optional)
        print(f"\nCleaning up pod '{POD_NAME}'...")
        try:
            v1.delete_namespaced_pod(name=POD_NAME, namespace=NAMESPACE)
            print("Pod deleted.")
        except ApiException as e:
            if e.status != 404:
                print(f"Error cleaning up pod: {e}")


if __name__ == "__main__":
    main()
