from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_cronjobs.get import ApiForget
from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_cronjobs.post import ApiForpost
from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_cronjobs.delete import ApiFordelete


class ApisBatchV1NamespacesNamespaceCronjobs(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
