# V1LabelSelector

A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expressions** | [**List[V1LabelSelectorRequirement]**](V1LabelSelectorRequirement.md) | matchExpressions is a list of label selector requirements. The requirements are ANDed. | [optional] 
**match_labels** | **Dict[str, str]** | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \&quot;key\&quot;, the operator is \&quot;In\&quot;, and the values array contains only \&quot;value\&quot;. The requirements are ANDed. | [optional] 

## Example

```python
from kubernetes.client.models.v1_label_selector import V1LabelSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1LabelSelector from a JSON string
v1_label_selector_instance = V1LabelSelector.from_json(json)
# print the JSON string representation of the object
print V1LabelSelector.to_json()

# convert the object into a dict
v1_label_selector_dict = v1_label_selector_instance.to_dict()
# create an instance of V1LabelSelector from a dict
v1_label_selector_form_dict = v1_label_selector.from_dict(v1_label_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


