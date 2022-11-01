from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_deployments.get import ApiForget
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_deployments.post import ApiForpost
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_deployments.delete import ApiFordelete


class ApisAppsV1NamespacesNamespaceDeployments(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
