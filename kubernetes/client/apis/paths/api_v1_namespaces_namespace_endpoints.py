from kubernetes.client.paths.api_v1_namespaces_namespace_endpoints.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_endpoints.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_endpoints.delete import ApiFordelete


class ApiV1NamespacesNamespaceEndpoints(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
