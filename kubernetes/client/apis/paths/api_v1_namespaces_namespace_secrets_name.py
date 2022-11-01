from kubernetes.client.paths.api_v1_namespaces_namespace_secrets_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_secrets_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_secrets_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_secrets_name.patch import ApiForpatch


class ApiV1NamespacesNamespaceSecretsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
