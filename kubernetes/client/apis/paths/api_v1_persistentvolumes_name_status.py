from kubernetes.client.paths.api_v1_persistentvolumes_name_status.get import ApiForget
from kubernetes.client.paths.api_v1_persistentvolumes_name_status.put import ApiForput
from kubernetes.client.paths.api_v1_persistentvolumes_name_status.patch import ApiForpatch


class ApiV1PersistentvolumesNameStatus(
    ApiForget,
    ApiForput,
    ApiForpatch,
):
    pass
