from kubernetes.client.paths.apis_storage_k8s_io_v1_csinodes.get import ApiForget
from kubernetes.client.paths.apis_storage_k8s_io_v1_csinodes.post import ApiForpost
from kubernetes.client.paths.apis_storage_k8s_io_v1_csinodes.delete import ApiFordelete


class ApisStorageK8sIoV1Csinodes(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
