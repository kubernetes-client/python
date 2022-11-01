from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_replicasets.get import ApiForget
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_replicasets.post import ApiForpost
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_replicasets.delete import ApiFordelete


class ApisAppsV1NamespacesNamespaceReplicasets(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
