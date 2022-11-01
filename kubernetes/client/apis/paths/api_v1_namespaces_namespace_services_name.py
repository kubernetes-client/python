from kubernetes.client.paths.api_v1_namespaces_namespace_services_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_services_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_services_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_services_name.patch import ApiForpatch


class ApiV1NamespacesNamespaceServicesName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
