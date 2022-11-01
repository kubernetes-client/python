from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_jobs.get import ApiForget
from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_jobs.post import ApiForpost
from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_jobs.delete import ApiFordelete


class ApisBatchV1NamespacesNamespaceJobs(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
