from kubernetes.client.paths.apis_group_version_plural_name.get import ApiForget
from kubernetes.client.paths.apis_group_version_plural_name.put import ApiForput
from kubernetes.client.paths.apis_group_version_plural_name.delete import ApiFordelete
from kubernetes.client.paths.apis_group_version_plural_name.patch import ApiForpatch


class ApisGroupVersionPluralName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
