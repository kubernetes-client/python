from kubernetes.client.paths.api_v1_namespaces_namespace_resourcequotas_name_status.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_resourcequotas_name_status.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_resourcequotas_name_status.patch import ApiForpatch


class ApiV1NamespacesNamespaceResourcequotasNameStatus(
    ApiForget,
    ApiForput,
    ApiForpatch,
):
    pass
