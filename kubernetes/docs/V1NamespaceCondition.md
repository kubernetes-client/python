# V1NamespaceCondition

NamespaceCondition contains details about state of namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | Last time the condition transitioned from one status to another. | [optional]
**message** | **str** | Human-readable message indicating details about last transition. | [optional]
**reason** | **str** | Unique, one-word, CamelCase reason for the condition&#39;s last transition. | [optional]
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
print(V1NamespaceCondition.to_json())

# convert the object into a dict
v1_namespace_condition_dict = v1_namespace_condition_instance.to_dict()
# create an instance of V1NamespaceCondition from a dict
v1_namespace_condition_from_dict = V1NamespaceCondition.from_dict(v1_namespace_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
