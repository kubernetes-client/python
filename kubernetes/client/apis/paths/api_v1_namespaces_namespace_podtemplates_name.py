from kubernetes.client.paths.api_v1_namespaces_namespace_podtemplates_name.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_podtemplates_name.put import ApiForput
from kubernetes.client.paths.api_v1_namespaces_namespace_podtemplates_name.delete import ApiFordelete
from kubernetes.client.paths.api_v1_namespaces_namespace_podtemplates_name.patch import ApiForpatch


class ApiV1NamespacesNamespacePodtemplatesName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
