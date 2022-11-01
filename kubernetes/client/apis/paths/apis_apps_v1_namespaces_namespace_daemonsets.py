from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_daemonsets.get import ApiForget
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_daemonsets.post import ApiForpost
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_daemonsets.delete import ApiFordelete


class ApisAppsV1NamespacesNamespaceDaemonsets(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
