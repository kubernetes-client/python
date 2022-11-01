from kubernetes.client.paths.api_v1_namespaces_namespace_events_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_events_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_events_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_events_name.patch import ApiForpatch


class ApiV1NamespacesNamespaceEventsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
