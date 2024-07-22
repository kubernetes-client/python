# V1Binding

Binding ties one object to another; for example, a pod is bound to a node by a scheduler. Deprecated in 1.7, please use the bindings subresource of pods instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**target** | [**V1ObjectReference**](V1ObjectReference.md) |  | 

## Example

```python
from kubernetes.client.models.v1_binding import V1Binding

# TODO update the JSON string below
json = "{}"
# create an instance of V1Binding from a JSON string
v1_binding_instance = V1Binding.from_json(json)
# print the JSON string representation of the object
print V1Binding.to_json()

# convert the object into a dict
v1_binding_dict = v1_binding_instance.to_dict()
# create an instance of V1Binding from a dict
v1_binding_form_dict = v1_binding.from_dict(v1_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


