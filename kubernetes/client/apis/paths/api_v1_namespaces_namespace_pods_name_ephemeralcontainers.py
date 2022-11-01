from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name_ephemeralcontainers.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name_ephemeralcontainers.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_pods_name_ephemeralcontainers.patch import ApiForpatch


class ApiV1NamespacesNamespacePodsNameEphemeralcontainers(
    ApiForget,
    ApiForput,
    ApiForpatch,
):
    pass
