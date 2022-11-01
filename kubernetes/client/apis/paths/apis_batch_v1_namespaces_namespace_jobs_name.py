from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_jobs_name.get import ApiForget
from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_jobs_name.put import ApiForput
from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_jobs_name.delete import ApiFordelete
from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_jobs_name.patch import ApiForpatch


class ApisBatchV1NamespacesNamespaceJobsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
