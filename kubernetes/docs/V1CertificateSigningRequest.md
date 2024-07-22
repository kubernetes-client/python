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

## Example

```python
from kubernetes.client.models.v1_certificate_signing_request import V1CertificateSigningRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1CertificateSigningRequest from a JSON string
v1_certificate_signing_request_instance = V1CertificateSigningRequest.from_json(json)
# print the JSON string representation of the object
print V1CertificateSigningRequest.to_json()

# convert the object into a dict
v1_certificate_signing_request_dict = v1_certificate_signing_request_instance.to_dict()
# create an instance of V1CertificateSigningRequest from a dict
v1_certificate_signing_request_form_dict = v1_certificate_signing_request.from_dict(v1_certificate_signing_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


