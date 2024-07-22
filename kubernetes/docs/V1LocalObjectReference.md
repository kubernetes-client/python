# V1LocalObjectReference

LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | [optional] 

## Example

```python
from kubernetes.client.models.v1_local_object_reference import V1LocalObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1LocalObjectReference from a JSON string
v1_local_object_reference_instance = V1LocalObjectReference.from_json(json)
# print the JSON string representation of the object
print V1LocalObjectReference.to_json()

# convert the object into a dict
v1_local_object_reference_dict = v1_local_object_reference_instance.to_dict()
# create an instance of V1LocalObjectReference from a dict
v1_local_object_reference_form_dict = v1_local_object_reference.from_dict(v1_local_object_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


