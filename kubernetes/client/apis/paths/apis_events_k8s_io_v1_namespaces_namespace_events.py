from kubernetes.client.paths.apis_events_k8s_io_v1_namespaces_namespace_events.get import ApiForget
from kubernetes.client.paths.apis_events_k8s_io_v1_namespaces_namespace_events.post import ApiForpost
from kubernetes.client.paths.apis_events_k8s_io_v1_namespaces_namespace_events.delete import ApiFordelete


class ApisEventsK8sIoV1NamespacesNamespaceEvents(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
