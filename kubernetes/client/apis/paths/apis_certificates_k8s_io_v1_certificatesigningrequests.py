from kubernetes.client.paths.apis_certificates_k8s_io_v1_certificatesigningrequests.get import ApiForget
from kubernetes.client.paths.apis_certificates_k8s_io_v1_certificatesigningrequests.post import ApiForpost
from kubernetes.client.paths.apis_certificates_k8s_io_v1_certificatesigningrequests.delete import ApiFordelete


class ApisCertificatesK8sIoV1Certificatesigningrequests(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
