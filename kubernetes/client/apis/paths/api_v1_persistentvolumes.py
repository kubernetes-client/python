from kubernetes.client.paths.api_v1_persistentvolumes.get import ApiForget
from kubernetes.client.paths.api_v1_persistentvolumes.post import ApiForpost
from kubernetes.client.paths.api_v1_persistentvolumes.delete import ApiFordelete


class ApiV1Persistentvolumes(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
