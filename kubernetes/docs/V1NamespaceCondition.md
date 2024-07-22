# V1NamespaceCondition

NamespaceCondition contains details about state of namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON.  Wrappers are provided for many of the factory methods that the time package offers. | [optional] 
**message** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of namespace controller condition. | 

## Example

```python
from kubernetes.client.models.v1_namespace_condition import V1NamespaceCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1NamespaceCondition from a JSON string
v1_namespace_condition_instance = V1NamespaceCondition.from_json(json)
# print the JSON string representation of the object
print V1NamespaceCondition.to_json()

# convert the object into a dict
v1_namespace_condition_dict = v1_namespace_condition_instance.to_dict()
# create an instance of V1NamespaceCondition from a dict
v1_namespace_condition_form_dict = v1_namespace_condition.from_dict(v1_namespace_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


