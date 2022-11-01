from kubernetes.client.paths.api_v1_namespaces_namespace_podtemplates.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces_namespace_podtemplates.post import ApiForpost
from kubernetes.client.paths.api_v1_namespaces_namespace_podtemplates.delete import ApiFordelete


class ApiV1NamespacesNamespacePodtemplates(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
