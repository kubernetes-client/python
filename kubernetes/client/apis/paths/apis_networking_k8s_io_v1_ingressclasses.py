from kubernetes.client.paths.apis_networking_k8s_io_v1_ingressclasses.get import ApiForget
from kubernetes.client.paths.apis_networking_k8s_io_v1_ingressclasses.post import ApiForpost
from kubernetes.client.paths.apis_networking_k8s_io_v1_ingressclasses.delete import ApiFordelete


class ApisNetworkingK8sIoV1Ingressclasses(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
