# V1beta1PodCertificateRequest

PodCertificateRequest encodes a pod requesting a certificate from a given signer.  Kubelets use this API to implement podCertificate projected volumes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1beta1PodCertificateRequestSpec**](V1beta1PodCertificateRequestSpec.md) |  |
**status** | [**V1beta1PodCertificateRequestStatus**](V1beta1PodCertificateRequestStatus.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1beta1_pod_certificate_request import V1beta1PodCertificateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1PodCertificateRequest from a JSON string
v1beta1_pod_certificate_request_instance = V1beta1PodCertificateRequest.from_json(json)
# print the JSON string representation of the object
print(V1beta1PodCertificateRequest.to_json())

# convert the object into a dict
v1beta1_pod_certificate_request_dict = v1beta1_pod_certificate_request_instance.to_dict()
# create an instance of V1beta1PodCertificateRequest from a dict
v1beta1_pod_certificate_request_from_dict = V1beta1PodCertificateRequest.from_dict(v1beta1_pod_certificate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
