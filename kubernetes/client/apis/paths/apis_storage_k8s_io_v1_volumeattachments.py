from kubernetes.client.paths.apis_storage_k8s_io_v1_volumeattachments.get import ApiForget
from kubernetes.client.paths.apis_storage_k8s_io_v1_volumeattachments.post import ApiForpost
from kubernetes.client.paths.apis_storage_k8s_io_v1_volumeattachments.delete import ApiFordelete


class ApisStorageK8sIoV1Volumeattachments(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
