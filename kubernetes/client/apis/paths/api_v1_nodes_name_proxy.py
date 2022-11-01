from kubernetes.client.paths.api_v1_nodes_name_proxy.get import ApiForget
from kubernetes.client.paths.api_v1_nodes_name_proxy.put import ApiForput
from kubernetes.client.paths.api_v1_nodes_name_proxy.post import ApiForpost
from kubernetes.client.paths.api_v1_nodes_name_proxy.delete import ApiFordelete
from kubernetes.client.paths.api_v1_nodes_name_proxy.options import ApiForoptions
from kubernetes.client.paths.api_v1_nodes_name_proxy.head import ApiForhead
from kubernetes.client.paths.api_v1_nodes_name_proxy.patch import ApiForpatch


class ApiV1NodesNameProxy(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForoptions,
    ApiForhead,
    ApiForpatch,
):
    pass
