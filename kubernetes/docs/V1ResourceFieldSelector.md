# V1ResourceFieldSelector

ResourceFieldSelector represents container resources (cpu, memory) and their output format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_name** | **str** | Container name: required for volumes, optional for env vars | [optional] 
**divisor** | **str** | Specifies the output format of the exposed resources, defaults to \&quot;1\&quot; | [optional] 
**resource** | **str** | Required: resource to select | 

## Example

```python
from kubernetes.client.models.v1_resource_field_selector import V1ResourceFieldSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceFieldSelector from a JSON string
v1_resource_field_selector_instance = V1ResourceFieldSelector.from_json(json)
# print the JSON string representation of the object
print V1ResourceFieldSelector.to_json()

# convert the object into a dict
v1_resource_field_selector_dict = v1_resource_field_selector_instance.to_dict()
# create an instance of V1ResourceFieldSelector from a dict
v1_resource_field_selector_form_dict = v1_resource_field_selector.from_dict(v1_resource_field_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


