from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_daemonsets_name_status.get import ApiForget
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_daemonsets_name_status.put import ApiForput
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_daemonsets_name_status.patch import ApiForpatch


class ApisAppsV1NamespacesNamespaceDaemonsetsNameStatus(
    ApiForget,
    ApiForput,
    ApiForpatch,
):
    pass
