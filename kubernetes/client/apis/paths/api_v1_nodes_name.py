from kubernetes.client.paths.api_v1_nodes_name.get import ApiForget
from kubernetes.client.paths.api_v1_nodes_name.put import ApiForput
from kubernetes.client.paths.api_v1_nodes_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_nodes_name.patch import ApiForpatch


class ApiV1NodesName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
