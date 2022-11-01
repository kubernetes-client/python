from kubernetes.client.paths.apis_storage_k8s_io_v1_storageclasses_name.get import ApiForget
from kubernetes.client.paths.apis_storage_k8s_io_v1_storageclasses_name.put import ApiForput
from kubernetes.client.paths.apis_storage_k8s_io_v1_storageclasses_name.delete import ApiFordelete
from kubernetes.client.paths.apis_storage_k8s_io_v1_storageclasses_name.patch import ApiForpatch


class ApisStorageK8sIoV1StorageclassesName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
