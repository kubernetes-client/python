from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_deployments_name_status.get import ApiForget
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_deployments_name_status.put import ApiForput
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_deployments_name_status.patch import ApiForpatch


class ApisAppsV1NamespacesNamespaceDeploymentsNameStatus(
    ApiForget,
    ApiForput,
    ApiForpatch,
):
    pass
