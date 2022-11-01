from kubernetes.client.paths.api_v1_namespaces_namespace_serviceaccounts_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_serviceaccounts_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_serviceaccounts_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_serviceaccounts_name.patch import ApiForpatch


class ApiV1NamespacesNamespaceServiceaccountsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
