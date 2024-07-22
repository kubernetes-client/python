# V1Ingress

Ingress is a collection of rules that allow inbound connections to reach the endpoints defined by a backend. An Ingress can be configured to give services externally-reachable urls, load balance traffic, terminate SSL, offer name based virtual hosting etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1IngressSpec**](V1IngressSpec.md) |  | [optional] 
**status** | [**V1IngressStatus**](V1IngressStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_ingress import V1Ingress

# TODO update the JSON string below
json = "{}"
# create an instance of V1Ingress from a JSON string
v1_ingress_instance = V1Ingress.from_json(json)
# print the JSON string representation of the object
print V1Ingress.to_json()

# convert the object into a dict
v1_ingress_dict = v1_ingress_instance.to_dict()
# create an instance of V1Ingress from a dict
v1_ingress_form_dict = v1_ingress.from_dict(v1_ingress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


