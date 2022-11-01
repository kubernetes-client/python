from kubernetes.client.paths.apis_coordination_k8s_io_v1_namespaces_namespace_leases.get import ApiForget
from kubernetes.client.paths.apis_coordination_k8s_io_v1_namespaces_namespace_leases.post import ApiForpost
from kubernetes.client.paths.apis_coordination_k8s_io_v1_namespaces_namespace_leases.delete import ApiFordelete


class ApisCoordinationK8sIoV1NamespacesNamespaceLeases(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
