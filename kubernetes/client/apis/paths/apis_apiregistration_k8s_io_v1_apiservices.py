from kubernetes.client.paths.apis_apiregistration_k8s_io_v1_apiservices.get import ApiForget
from kubernetes.client.paths.apis_apiregistration_k8s_io_v1_apiservices.post import ApiForpost
from kubernetes.client.paths.apis_apiregistration_k8s_io_v1_apiservices.delete import ApiFordelete


class ApisApiregistrationK8sIoV1Apiservices(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
