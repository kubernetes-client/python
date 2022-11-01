from kubernetes.client.paths.apis_storage_k8s_io_v1_csinodes_name.get import ApiForget
from kubernetes.client.paths.apis_storage_k8s_io_v1_csinodes_name.put import ApiForput
from kubernetes.client.paths.apis_storage_k8s_io_v1_csinodes_name.delete import ApiFordelete
from kubernetes.client.paths.apis_storage_k8s_io_v1_csinodes_name.patch import ApiForpatch


class ApisStorageK8sIoV1CsinodesName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
