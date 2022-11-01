from kubernetes.client.paths.apis_group_version_namespaces_namespace_plural.get import ApiForget
from kubernetes.client.paths.apis_group_version_namespaces_namespace_plural.post import ApiForpost
from kubernetes.client.paths.apis_group_version_namespaces_namespace_plural.delete import ApiFordelete


class ApisGroupVersionNamespacesNamespacePlural(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
