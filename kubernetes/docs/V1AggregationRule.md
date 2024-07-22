# V1AggregationRule

AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_role_selectors** | [**List[V1LabelSelector]**](V1LabelSelector.md) | ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole&#39;s permissions will be added | [optional] 

## Example

```python
from kubernetes.client.models.v1_aggregation_rule import V1AggregationRule

# TODO update the JSON string below
json = "{}"
# create an instance of V1AggregationRule from a JSON string
v1_aggregation_rule_instance = V1AggregationRule.from_json(json)
# print the JSON string representation of the object
print V1AggregationRule.to_json()

# convert the object into a dict
v1_aggregation_rule_dict = v1_aggregation_rule_instance.to_dict()
# create an instance of V1AggregationRule from a dict
v1_aggregation_rule_form_dict = v1_aggregation_rule.from_dict(v1_aggregation_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


