from kubernetes.client.paths.api_v1_namespaces_namespace_resourcequotas.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_resourcequotas.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_resourcequotas.delete import ApiFordelete


class ApiV1NamespacesNamespaceResourcequotas(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
