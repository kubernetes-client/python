# V1TypedLocalObjectReference

TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. | [optional] 
**kind** | **str** | Kind is the type of resource being referenced | 
**name** | **str** | Name is the name of resource being referenced | 

## Example

```python
from kubernetes.client.models.v1_typed_local_object_reference import V1TypedLocalObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1TypedLocalObjectReference from a JSON string
v1_typed_local_object_reference_instance = V1TypedLocalObjectReference.from_json(json)
# print the JSON string representation of the object
print V1TypedLocalObjectReference.to_json()

# convert the object into a dict
v1_typed_local_object_reference_dict = v1_typed_local_object_reference_instance.to_dict()
# create an instance of V1TypedLocalObjectReference from a dict
v1_typed_local_object_reference_form_dict = v1_typed_local_object_reference.from_dict(v1_typed_local_object_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


