from kubernetes.client.paths.api_v1_namespaces_namespace_services.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_services.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_services.delete import ApiFordelete


class ApiV1NamespacesNamespaceServices(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
