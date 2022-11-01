from kubernetes.client.paths.api_v1_namespaces_namespace_replicationcontrollers_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_replicationcontrollers_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_replicationcontrollers_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_replicationcontrollers_name.patch import ApiForpatch


class ApiV1NamespacesNamespaceReplicationcontrollersName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
