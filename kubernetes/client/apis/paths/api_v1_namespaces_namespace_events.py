from kubernetes.client.paths.api_v1_namespaces_namespace_events.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_events.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_events.delete import ApiFordelete


class ApiV1NamespacesNamespaceEvents(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
