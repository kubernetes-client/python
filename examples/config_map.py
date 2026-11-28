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
Demonstrates how to create a V1ConfigMap and consume it in a V1Pod using
typed CoreV1Api models.

This example illustrates:
1. Creating a V1ConfigMap with scalar values and multi-line file data.
2. Injecting ConfigMap data as environment variables via `env_from`
   and `V1ConfigMapEnvSource`.
3. Mounting the ConfigMap as a volume into the container via
   `V1ConfigMapVolumeSource` and `V1VolumeMount`.

For more information, see:
https://kubernetes.io/docs/concepts/configuration/configmap/
"""

import time
from kubernetes import client, config
from kubernetes.client.rest import ApiException

CONFIGMAP_NAME = "demo-configmap"
POD_NAME = "demo-configmap-pod"
NAMESPACE = "default"


def main():
    # Load kubeconfig from default location (~/.kube/config)
    config.load_kube_config()
    v1 = client.CoreV1Api()

    # 1. Define the ConfigMap
    cm_metadata = client.V1ObjectMeta(
        name=CONFIGMAP_NAME,
        labels={"app": "demo-configmap"},
    )
    cm_data = {
        "player_initial_lives": "3",
        "ui_properties_file_name": "user-interface.properties",
        "game.properties": (
            "enemy.types=aliens,monsters\n"
            "player.maximum-lives=5\n"
        ),
    }
    config_map = client.V1ConfigMap(
        api_version="v1",
        kind="ConfigMap",
        metadata=cm_metadata,
        data=cm_data,
    )

    # 2. Define the Volume and VolumeMount for the Pod
    volume_name = "config-volume"
    volume = client.V1Volume(
        name=volume_name,
        config_map=client.V1ConfigMapVolumeSource(
            name=CONFIGMAP_NAME,
        ),
    )
    volume_mount = client.V1VolumeMount(
        name=volume_name,
        mount_path="/etc/config",
        read_only=True,
    )

    # 3. Define environment variable source from ConfigMap
    env_from = client.V1EnvFromSource(
        config_map_ref=client.V1ConfigMapEnvSource(
            name=CONFIGMAP_NAME,
        ),
    )

    # 4. Define the container using the volume mount and env_from
    container = client.V1Container(
        name="demo-app",
        image="busybox:latest",
        command=["sh", "-c", "echo ConfigMap mounted; sleep 3600"],
        volume_mounts=[volume_mount],
        env_from=[env_from],
    )

    # 5. Define the PodSpec and V1Pod
    pod_spec = client.V1PodSpec(
        containers=[container],
        volumes=[volume],
        restart_policy="Never",
    )
    pod = client.V1Pod(
        api_version="v1",
        kind="Pod",
        metadata=client.V1ObjectMeta(
            name=POD_NAME,
            labels={"app": "demo-configmap"},
        ),
        spec=pod_spec,
    )

    try:
        # Create the ConfigMap
        print(f"Creating ConfigMap '{CONFIGMAP_NAME}'...")
        v1.create_namespaced_config_map(namespace=NAMESPACE, body=config_map)
        print("ConfigMap created successfully.")

        # Create the Pod consuming the ConfigMap
        print(f"Creating Pod '{POD_NAME}' consuming ConfigMap...")
        v1.create_namespaced_pod(namespace=NAMESPACE, body=pod)
        print("Pod created successfully.")

        # Wait for the pod to be scheduled / running
        for _ in range(10):
            p = v1.read_namespaced_pod(name=POD_NAME, namespace=NAMESPACE)
            if p.status.phase in ("Running", "Succeeded"):
                print(f"Pod is currently in phase: {p.status.phase}")
                break
            time.sleep(1)

    except ApiException as e:
        if e.status == 409:
            print(f"Resource already exists: {e.reason}")
        else:
            print(f"API exception occurred: {e}")
    finally:
        # Clean up resources
        print("\nCleaning up resources...")
        try:
            v1.delete_namespaced_pod(name=POD_NAME, namespace=NAMESPACE)
            print(f"Pod '{POD_NAME}' deleted.")
        except ApiException:
            pass

        try:
            v1.delete_namespaced_config_map(
                name=CONFIGMAP_NAME, namespace=NAMESPACE
            )
            print(f"ConfigMap '{CONFIGMAP_NAME}' deleted.")
        except ApiException:
            pass


if __name__ == "__main__":
    main()
