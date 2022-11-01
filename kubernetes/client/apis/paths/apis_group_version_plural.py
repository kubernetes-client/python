from kubernetes.client.paths.apis_group_version_plural.get import ApiForget
from kubernetes.client.paths.apis_group_version_plural.post import ApiForpost
from kubernetes.client.paths.apis_group_version_plural.delete import ApiFordelete


class ApisGroupVersionPlural(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
