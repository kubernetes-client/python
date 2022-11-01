from kubernetes.client.paths.apis_group_version_plural_name_scale.get import ApiForget
from kubernetes.client.paths.apis_group_version_plural_name_scale.put import ApiForput
from kubernetes.client.paths.apis_group_version_plural_name_scale.patch import ApiForpatch


class ApisGroupVersionPluralNameScale(
    ApiForget,
    ApiForput,
    ApiForpatch,
):
    pass
