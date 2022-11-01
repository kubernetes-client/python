from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_statefulsets_name.get import ApiForget
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_statefulsets_name.put import ApiForput
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_statefulsets_name.delete import ApiFordelete
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_statefulsets_name.patch import ApiForpatch


class ApisAppsV1NamespacesNamespaceStatefulsetsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
