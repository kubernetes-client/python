from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_replicasets_name.get import ApiForget
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_replicasets_name.put import ApiForput
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_replicasets_name.delete import ApiFordelete
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_replicasets_name.patch import ApiForpatch


class ApisAppsV1NamespacesNamespaceReplicasetsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
