from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name_proxy_path.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name_proxy_path.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name_proxy_path.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name_proxy_path.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name_proxy_path.options import ApiForoptions
from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name_proxy_path.head import ApiForhead
from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name_proxy_path.patch import ApiForpatch


class ApiV1NamespacesNamespacePodsNameProxyPath(
    ApiForget,
    ApiForput,
    ApiForpost,
    ApiFordelete,
    ApiForoptions,
    ApiForhead,
    ApiForpatch,
):
    pass
