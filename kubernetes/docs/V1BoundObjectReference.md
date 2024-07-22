# V1BoundObjectReference

BoundObjectReference is a reference to an object that a token is bound to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | API version of the referent. | [optional] 
**kind** | **str** | Kind of the referent. Valid kinds are &#39;Pod&#39; and &#39;Secret&#39;. | [optional] 
**name** | **str** | Name of the referent. | [optional] 
**uid** | **str** | UID of the referent. | [optional] 

## Example

```python
from kubernetes.client.models.v1_bound_object_reference import V1BoundObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1BoundObjectReference from a JSON string
v1_bound_object_reference_instance = V1BoundObjectReference.from_json(json)
# print the JSON string representation of the object
print V1BoundObjectReference.to_json()

# convert the object into a dict
v1_bound_object_reference_dict = v1_bound_object_reference_instance.to_dict()
# create an instance of V1BoundObjectReference from a dict
v1_bound_object_reference_form_dict = v1_bound_object_reference.from_dict(v1_bound_object_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


