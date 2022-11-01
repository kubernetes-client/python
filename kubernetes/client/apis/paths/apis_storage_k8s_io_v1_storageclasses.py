from kubernetes.client.paths.apis_storage_k8s_io_v1_storageclasses.get import ApiForget
from kubernetes.client.paths.apis_storage_k8s_io_v1_storageclasses.post import ApiForpost
from kubernetes.client.paths.apis_storage_k8s_io_v1_storageclasses.delete import ApiFordelete


class ApisStorageK8sIoV1Storageclasses(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
