from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_controllerrevisions.get import ApiForget
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_controllerrevisions.post import ApiForpost
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_controllerrevisions.delete import ApiFordelete


class ApisAppsV1NamespacesNamespaceControllerrevisions(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
