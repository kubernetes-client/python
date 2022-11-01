from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_daemonsets_name.get import ApiForget
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_daemonsets_name.put import ApiForput
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_daemonsets_name.delete import ApiFordelete
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_daemonsets_name.patch import ApiForpatch


class ApisAppsV1NamespacesNamespaceDaemonsetsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
