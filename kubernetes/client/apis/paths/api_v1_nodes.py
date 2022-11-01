from kubernetes.client.paths.api_v1_nodes.get import ApiForget
from kubernetes.client.paths.api_v1_nodes.post import ApiForpost
from kubernetes.client.paths.api_v1_nodes.delete import ApiFordelete


class ApiV1Nodes(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
