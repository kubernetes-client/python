from kubernetes.client.paths.apis_scheduling_k8s_io_v1_priorityclasses.get import ApiForget
from kubernetes.client.paths.apis_scheduling_k8s_io_v1_priorityclasses.post import ApiForpost
from kubernetes.client.paths.apis_scheduling_k8s_io_v1_priorityclasses.delete import ApiFordelete


class ApisSchedulingK8sIoV1Priorityclasses(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
