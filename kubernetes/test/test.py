from kubernetes import client, config

# Load kubeconfig (Ensure you have access to a cluster)
config.load_kube_config()

# Create API client
v1 = client.CoreV1Api()

# Fetch pods
pods = v1.list_pod_for_all_namespaces()

# Debugging: Print the total number of pods
print(f"Total pods found: {len(pods.items)}")

# Iterate only if there are pods
if pods.items:
    for pod in pods.items:
        print(f"Pod: {pod.metadata.name}, Namespace: {pod.metadata.namespace}")
else:
    print("No pods found.")
