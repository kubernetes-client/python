from kubernetes.client.paths.api_v1_namespaces_namespace_limitranges.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_limitranges.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_limitranges.delete import ApiFordelete


class ApiV1NamespacesNamespaceLimitranges(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
