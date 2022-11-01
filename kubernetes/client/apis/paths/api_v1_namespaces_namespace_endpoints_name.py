from kubernetes.client.paths.api_v1_namespaces_namespace_endpoints_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_endpoints_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_endpoints_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_endpoints_name.patch import ApiForpatch


class ApiV1NamespacesNamespaceEndpointsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
