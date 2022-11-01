from kubernetes.client.paths.api_v1_namespaces_namespace_resourcequotas_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_resourcequotas_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_resourcequotas_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_resourcequotas_name.patch import ApiForpatch


class ApiV1NamespacesNamespaceResourcequotasName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
