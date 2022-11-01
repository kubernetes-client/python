from kubernetes.client.paths.api_v1_namespaces_namespace_serviceaccounts.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_serviceaccounts.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_serviceaccounts.delete import ApiFordelete


class ApiV1NamespacesNamespaceServiceaccounts(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
