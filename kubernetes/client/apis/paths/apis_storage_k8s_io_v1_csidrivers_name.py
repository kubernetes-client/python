from kubernetes.client.paths.apis_storage_k8s_io_v1_csidrivers_name.get import ApiForget
from kubernetes.client.paths.apis_storage_k8s_io_v1_csidrivers_name.put import ApiForput
from kubernetes.client.paths.apis_storage_k8s_io_v1_csidrivers_name.delete import ApiFordelete
from kubernetes.client.paths.apis_storage_k8s_io_v1_csidrivers_name.patch import ApiForpatch


class ApisStorageK8sIoV1CsidriversName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
