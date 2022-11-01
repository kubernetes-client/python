from kubernetes.client.paths.apis_rbac_authorization_k8s_io_v1_clusterroles.get import ApiForget
from kubernetes.client.paths.apis_rbac_authorization_k8s_io_v1_clusterroles.post import ApiForpost
from kubernetes.client.paths.apis_rbac_authorization_k8s_io_v1_clusterroles.delete import ApiFordelete


class ApisRbacAuthorizationK8sIoV1Clusterroles(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
