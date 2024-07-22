# V1NodeSelector

A node selector represents the union of the results of one or more label queries over a set of nodes; that is, it represents the OR of the selectors represented by the node selector terms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_selector_terms** | [**List[V1NodeSelectorTerm]**](V1NodeSelectorTerm.md) | Required. A list of node selector terms. The terms are ORed. | 

## Example

```python
from kubernetes.client.models.v1_node_selector import V1NodeSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeSelector from a JSON string
v1_node_selector_instance = V1NodeSelector.from_json(json)
# print the JSON string representation of the object
print V1NodeSelector.to_json()

# convert the object into a dict
v1_node_selector_dict = v1_node_selector_instance.to_dict()
# create an instance of V1NodeSelector from a dict
v1_node_selector_form_dict = v1_node_selector.from_dict(v1_node_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


