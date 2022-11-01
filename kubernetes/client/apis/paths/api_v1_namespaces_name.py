from kubernetes.client.paths.api_v1_namespaces_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_name.patch import ApiForpatch


class ApiV1NamespacesName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
