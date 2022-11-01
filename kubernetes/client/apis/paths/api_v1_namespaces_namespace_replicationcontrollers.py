from kubernetes.client.paths.api_v1_namespaces_namespace_replicationcontrollers.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_replicationcontrollers.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_replicationcontrollers.delete import ApiFordelete


class ApiV1NamespacesNamespaceReplicationcontrollers(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
