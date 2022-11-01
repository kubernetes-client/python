from kubernetes.client.paths.api_v1_namespaces.get import ApiForget
from kubernetes.client.paths.api_v1_namespaces.post import ApiForpost


class ApiV1Namespaces(
    ApiForget,
    ApiForpost,
):
    pass
