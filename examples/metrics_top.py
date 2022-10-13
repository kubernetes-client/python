from kubernetes.utils import top
from kubernetes import config,client

config.load_kube_config()
api_client = client.ApiClient()

# Get metrics of all nodes
data = top.nodes(api_client=api_client)
print(data)

# Get metrics of a particular node
data = top.nodes(api_client=api_client,node_name="ip-20-0-47-152.ec2.internal")
print(data)


# Get metrics of pods in default namespace
data = top.pods(api_client=api_client)
print(data)


# Get metrics of pods in a particular namespace
data = top.pods(api_client=api_client,namespace="apiserver")
print(data)

# Get metrics of pods in all namespaces
data = top.pods(api_client=api_client,all_namespaces=True)
print(data)

# Get metrics of a particular pod running in a particular namespace
data = top.pods(api_client=api_client,namespace="apiserver",pod_name="robin-7476956966-nq7xr")
print(data)