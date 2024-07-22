# V1Eviction

Eviction evicts a pod from its node subject to certain policies and safety constraints. This is a subresource of Pod.  A request to cause such an eviction is created by POSTing to .../pods/<pod name>/evictions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**delete_options** | [**V1DeleteOptions**](V1DeleteOptions.md) |  | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_eviction import V1Eviction

# TODO update the JSON string below
json = "{}"
# create an instance of V1Eviction from a JSON string
v1_eviction_instance = V1Eviction.from_json(json)
# print the JSON string representation of the object
print V1Eviction.to_json()

# convert the object into a dict
v1_eviction_dict = v1_eviction_instance.to_dict()
# create an instance of V1Eviction from a dict
v1_eviction_form_dict = v1_eviction.from_dict(v1_eviction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


