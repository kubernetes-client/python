# V1FieldSelectorRequirement

FieldSelectorRequirement is a selector that contains values, a key, and an operator that relates the key and values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | key is the field selector key that the requirement applies to. |
**operator** | **str** | operator represents a key&#39;s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. The list of operators may grow in the future. |
**values** | **List[str]** | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. | [optional]

## Example

```python
from kubernetes.client.models.v1_field_selector_requirement import V1FieldSelectorRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of V1FieldSelectorRequirement from a JSON string
v1_field_selector_requirement_instance = V1FieldSelectorRequirement.from_json(json)
# print the JSON string representation of the object
print(V1FieldSelectorRequirement.to_json())

# convert the object into a dict
v1_field_selector_requirement_dict = v1_field_selector_requirement_instance.to_dict()
# create an instance of V1FieldSelectorRequirement from a dict
v1_field_selector_requirement_from_dict = V1FieldSelectorRequirement.from_dict(v1_field_selector_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
