from kubernetes.client.paths.api_v1_namespaces_namespace_persistentvolumeclaims_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_persistentvolumeclaims_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_persistentvolumeclaims_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_persistentvolumeclaims_name.patch import ApiForpatch


class ApiV1NamespacesNamespacePersistentvolumeclaimsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
