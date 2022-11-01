from kubernetes.client.paths.api_v1_persistentvolumes_name.get import ApiForget
from kubernetes.client.paths.api_v1_persistentvolumes_name.put import ApiForput
from kubernetes.client.paths.api_v1_persistentvolumes_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_persistentvolumes_name.patch import ApiForpatch


class ApiV1PersistentvolumesName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
