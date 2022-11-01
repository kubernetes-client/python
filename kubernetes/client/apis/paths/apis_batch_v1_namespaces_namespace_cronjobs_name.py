from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_cronjobs_name.get import ApiForget
from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_cronjobs_name.put import ApiForput
from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_cronjobs_name.delete import ApiFordelete
from kubernetes.client.paths.apis_batch_v1_namespaces_namespace_cronjobs_name.patch import ApiForpatch


class ApisBatchV1NamespacesNamespaceCronjobsName(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
