# V1NodeSelectorTerm

A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expressions** | [**List[V1NodeSelectorRequirement]**](V1NodeSelectorRequirement.md) | A list of node selector requirements by node&#39;s labels. | [optional] 
**match_fields** | [**List[V1NodeSelectorRequirement]**](V1NodeSelectorRequirement.md) | A list of node selector requirements by node&#39;s fields. | [optional] 

## Example

```python
from kubernetes.client.models.v1_node_selector_term import V1NodeSelectorTerm

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeSelectorTerm from a JSON string
v1_node_selector_term_instance = V1NodeSelectorTerm.from_json(json)
# print the JSON string representation of the object
print V1NodeSelectorTerm.to_json()

# convert the object into a dict
v1_node_selector_term_dict = v1_node_selector_term_instance.to_dict()
# create an instance of V1NodeSelectorTerm from a dict
v1_node_selector_term_form_dict = v1_node_selector_term.from_dict(v1_node_selector_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


