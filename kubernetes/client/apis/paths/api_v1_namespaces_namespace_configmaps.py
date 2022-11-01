from kubernetes.client.paths.api_v1_namespaces_namespace_configmaps.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_configmaps.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_configmaps.delete import ApiFordelete


class ApiV1NamespacesNamespaceConfigmaps(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
