# V1CustomResourceDefinitionCondition

CustomResourceDefinitionCondition contains details for the current condition of this pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | lastTransitionTime last time the condition transitioned from one status to another. | [optional] 
**message** | **str** | message is a human-readable message indicating details about last transition. | [optional] 
**reason** | **str** | reason is a unique, one-word, CamelCase reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | status is the status of the condition. Can be True, False, Unknown. | 
**type** | **str** | type is the type of the condition. Types include Established, NamesAccepted and Terminating. | 

## Example

```python
from kubernetes.client.models.v1_custom_resource_definition_condition import V1CustomResourceDefinitionCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1CustomResourceDefinitionCondition from a JSON string
v1_custom_resource_definition_condition_instance = V1CustomResourceDefinitionCondition.from_json(json)
# print the JSON string representation of the object
print V1CustomResourceDefinitionCondition.to_json()

# convert the object into a dict
v1_custom_resource_definition_condition_dict = v1_custom_resource_definition_condition_instance.to_dict()
# create an instance of V1CustomResourceDefinitionCondition from a dict
v1_custom_resource_definition_condition_form_dict = v1_custom_resource_definition_condition.from_dict(v1_custom_resource_definition_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


