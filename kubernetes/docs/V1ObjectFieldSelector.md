# V1ObjectFieldSelector

ObjectFieldSelector selects an APIVersioned field of an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | Version of the schema the FieldPath is written in terms of, defaults to \&quot;v1\&quot;. | [optional] 
**field_path** | **str** | Path of the field to select in the specified API version. | 

## Example

```python
from kubernetes.client.models.v1_object_field_selector import V1ObjectFieldSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1ObjectFieldSelector from a JSON string
v1_object_field_selector_instance = V1ObjectFieldSelector.from_json(json)
# print the JSON string representation of the object
print V1ObjectFieldSelector.to_json()

# convert the object into a dict
v1_object_field_selector_dict = v1_object_field_selector_instance.to_dict()
# create an instance of V1ObjectFieldSelector from a dict
v1_object_field_selector_form_dict = v1_object_field_selector.from_dict(v1_object_field_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


