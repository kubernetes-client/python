from kubernetes.client.paths.apis_group_version_plural_name_status.get import ApiForget
from kubernetes.client.paths.apis_group_version_plural_name_status.put import ApiForput
from kubernetes.client.paths.apis_group_version_plural_name_status.patch import ApiForpatch


class ApisGroupVersionPluralNameStatus(
    ApiForget,
    ApiForput,
    ApiForpatch,
):
    pass
