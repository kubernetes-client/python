# kubernetes.client.model.v1_certificate_signing_request.V1CertificateSigningRequest

CertificateSigningRequest objects provide a mechanism to obtain x509 certificates by submitting a certificate signing request, and having it asynchronously approved and issued.  Kubelets use this API to obtain:  1. kubernetes.client certificates to authenticate to kube-apiserver (with the \"kubernetes.io/kube-apiserver-kubernetes.client-kubelet\" signerName).  2. serving certificates for TLS endpoints kube-apiserver can connect to securely (with the \"kubernetes.io/kubelet-serving\" signerName).  This API can be used to request kubernetes.client certificates to authenticate to kube-apiserver (with the \"kubernetes.io/kube-apiserver-kubernetes.client\" signerName), or to obtain certificates from custom non-Kubernetes signers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CertificateSigningRequest objects provide a mechanism to obtain x509 certificates by submitting a certificate signing request, and having it asynchronously approved and issued.  Kubelets use this API to obtain:  1. kubernetes.client certificates to authenticate to kube-apiserver (with the \&quot;kubernetes.io/kube-apiserver-kubernetes.client-kubelet\&quot; signerName).  2. serving certificates for TLS endpoints kube-apiserver can connect to securely (with the \&quot;kubernetes.io/kubelet-serving\&quot; signerName).  This API can be used to request kubernetes.client certificates to authenticate to kube-apiserver (with the \&quot;kubernetes.io/kube-apiserver-kubernetes.client\&quot; signerName), or to obtain certificates from custom non-Kubernetes signers. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**spec** | [**V1CertificateSigningRequestSpec**](V1CertificateSigningRequestSpec.md) | [**V1CertificateSigningRequestSpec**](V1CertificateSigningRequestSpec.md) |  | 
**apiVersion** | str,  | str,  | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | str,  | str,  | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**status** | [**V1CertificateSigningRequestStatus**](V1CertificateSigningRequestStatus.md) | [**V1CertificateSigningRequestStatus**](V1CertificateSigningRequestStatus.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

