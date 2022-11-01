from kubernetes.client.paths.api_v1_namespaces_namespace_secrets.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_secrets.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_secrets.delete import ApiFordelete


class ApiV1NamespacesNamespaceSecrets(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
