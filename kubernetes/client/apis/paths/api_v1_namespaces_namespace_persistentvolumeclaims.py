from kubernetes.client.paths.api_v1_namespaces_namespace_persistentvolumeclaims.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_persistentvolumeclaims.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_persistentvolumeclaims.delete import ApiFordelete


class ApiV1NamespacesNamespacePersistentvolumeclaims(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
