from kubernetes.client.paths.apis_node_k8s_io_v1_runtimeclasses.get import ApiForget
from kubernetes.client.paths.apis_node_k8s_io_v1_runtimeclasses.post import ApiForpost
from kubernetes.client.paths.apis_node_k8s_io_v1_runtimeclasses.delete import ApiFordelete


class ApisNodeK8sIoV1Runtimeclasses(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
