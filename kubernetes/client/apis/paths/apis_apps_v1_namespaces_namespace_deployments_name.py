from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_deployments_name.get import ApiForget
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_deployments_name.put import ApiForput
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_deployments_name.delete import ApiFordelete
from kubernetes.client.paths.apis_apps_v1_namespaces_namespace_deployments_name.patch import ApiForpatch


class ApisAppsV1NamespacesNamespaceDeploymentsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
