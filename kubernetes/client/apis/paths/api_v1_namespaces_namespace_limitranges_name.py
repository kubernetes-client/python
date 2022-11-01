from kubernetes.client.paths.api_v1_namespaces_namespace_limitranges_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_limitranges_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_limitranges_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_limitranges_name.patch import ApiForpatch


class ApiV1NamespacesNamespaceLimitrangesName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
