from kubernetes.client.paths.apis_storage_k8s_io_v1_csidrivers.get import ApiForget
from kubernetes.client.paths.apis_storage_k8s_io_v1_csidrivers.post import ApiForpost
from kubernetes.client.paths.apis_storage_k8s_io_v1_csidrivers.delete import ApiFordelete


class ApisStorageK8sIoV1Csidrivers(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
