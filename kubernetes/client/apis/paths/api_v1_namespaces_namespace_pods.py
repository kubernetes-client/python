from kubernetes.client.paths.api_v1_namespaces_namespace_pods.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_pods.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_pods.delete import ApiFordelete


class ApiV1NamespacesNamespacePods(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
