# V1SelectableField

SelectableField specifies the JSON path of a field that may be used with field selectors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_path** | **str** | jsonPath is a simple JSON path which is evaluated against each custom resource to produce a field selector value. Only JSON paths without the array notation are allowed. Must point to a field of type string, boolean or integer. Types with enum values and strings with formats are allowed. If jsonPath refers to absent field in a resource, the jsonPath evaluates to an empty string. Must not point to metdata fields. Required. | 

## Example

```python
from kubernetes.client.models.v1_selectable_field import V1SelectableField

# TODO update the JSON string below
json = "{}"
# create an instance of V1SelectableField from a JSON string
v1_selectable_field_instance = V1SelectableField.from_json(json)
# print the JSON string representation of the object
print V1SelectableField.to_json()

# convert the object into a dict
v1_selectable_field_dict = v1_selectable_field_instance.to_dict()
# create an instance of V1SelectableField from a dict
v1_selectable_field_form_dict = v1_selectable_field.from_dict(v1_selectable_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


