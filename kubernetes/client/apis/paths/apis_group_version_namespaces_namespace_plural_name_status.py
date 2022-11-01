from kubernetes.client.paths.apis_group_version_namespaces_namespace_plural_name_status.get import ApiForget
from kubernetes.client.paths.apis_group_version_namespaces_namespace_plural_name_status.put import ApiForput
from kubernetes.client.paths.apis_group_version_namespaces_namespace_plural_name_status.patch import ApiForpatch


class ApisGroupVersionNamespacesNamespacePluralNameStatus(
    ApiForget,
    ApiForput,
    ApiForpatch,
):
    pass
