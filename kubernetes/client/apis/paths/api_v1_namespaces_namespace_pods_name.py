from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name.patch import ApiForpatch


class ApiV1NamespacesNamespacePodsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
