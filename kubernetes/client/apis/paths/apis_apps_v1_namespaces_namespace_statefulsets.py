from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_statefulsets.get import ApiForget
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_statefulsets.post import ApiForpost
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_statefulsets.delete import ApiFordelete


class ApisAppsV1NamespacesNamespaceStatefulsets(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
