# V1CertificateSigningRequest

CertificateSigningRequest objects provide a mechanism to obtain x509 certificates by submitting a certificate signing request, and having it asynchronously approved and issued.  Kubelets use this API to obtain:  1. kubernetes.client certificates to authenticate to kube-apiserver (with the \"kubernetes.io/kube-apiserver-kubernetes.client-kubelet\" signerName).  2. serving certificates for TLS endpoints kube-apiserver can connect to securely (with the \"kubernetes.io/kubelet-serving\" signerName).  This API can be used to request kubernetes.client certificates to authenticate to kube-apiserver (with the \"kubernetes.io/kube-apiserver-kubernetes.client\" signerName), or to obtain certificates from custom non-Kubernetes signers.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1CertificateSigningRequestSpec**](V1CertificateSigningRequestSpec.md) |  | 
**status** | [**V1CertificateSigningRequestStatus**](V1CertificateSigningRequestStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


