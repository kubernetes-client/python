# Copyright 2025 The Kubernetes Authors.

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
List all pod with logs.

"""

from kubernetes import client, config

def list_pods_with_logs():
    try:
        #Load Minikube configuration
        config.load_kube_config()

        #Create Kubernetes API client
        v1 = client.CoreV1Api()

        # List pods in all namespaces
        pods = v1.list_pod_for_all_namespaces(watch=False)

        # Print details of each pod and retrieve logs
        for pod in pods.items:
            pod_name = pod.metadata.name
            namespace = pod.metadata.namespace
            pod_ip = pod.status.pod_ip
            node_name = pod.spec.node_name

            print(f"Name: {pod_name}, Namespace: {namespace}, IP: {pod_ip}, Node: {node_name}")

            #Retrieve and print logs for each container in the pod
            for container in pod.spec.containers:
                container_name = container.name
                print(f"Logs for container {container_name}:")
                try:
                    logs = v1.read_namespaced_pod_log(name=pod_name, namespace=namespace, container=container_name, tail_lines=5)
                    print(logs)
                except Exception as e:
                    print(f"Error getting logs for pod {pod_name}, container {container_name}: {e}")

    except Exception as e:
        print(f"Error: {e}")


def main():
	list_pods_with_logs()


if __name__ == "__main__":
	main()





