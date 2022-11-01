from kubernetes.client.paths.apis_apiregistration_k8s_io_v1_apiservices_name.get import ApiForget
from kubernetes.client.paths.apis_apiregistration_k8s_io_v1_apiservices_name.put import ApiForput
from kubernetes.client.paths.apis_apiregistration_k8s_io_v1_apiservices_name.delete import ApiFordelete
from kubernetes.client.paths.apis_apiregistration_k8s_io_v1_apiservices_name.patch import ApiForpatch


class ApisApiregistrationK8sIoV1ApiservicesName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
