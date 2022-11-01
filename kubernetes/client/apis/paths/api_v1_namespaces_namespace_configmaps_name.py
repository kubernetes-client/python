from kubernetes.client.paths.api_v1_namespaces_namespace_configmaps_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_configmaps_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_configmaps_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_configmaps_name.patch import ApiForpatch


class ApiV1NamespacesNamespaceConfigmapsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
