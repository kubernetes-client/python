# V1TopologySelectorLabelRequirement

A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The label key that the selector applies to. | 
**values** | **List[str]** | An array of string values. One value must match the label to be selected. Each entry in Values is ORed. | 

## Example

```python
from kubernetes.client.models.v1_topology_selector_label_requirement import V1TopologySelectorLabelRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of V1TopologySelectorLabelRequirement from a JSON string
v1_topology_selector_label_requirement_instance = V1TopologySelectorLabelRequirement.from_json(json)
# print the JSON string representation of the object
print V1TopologySelectorLabelRequirement.to_json()

# convert the object into a dict
v1_topology_selector_label_requirement_dict = v1_topology_selector_label_requirement_instance.to_dict()
# create an instance of V1TopologySelectorLabelRequirement from a dict
v1_topology_selector_label_requirement_form_dict = v1_topology_selector_label_requirement.from_dict(v1_topology_selector_label_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


