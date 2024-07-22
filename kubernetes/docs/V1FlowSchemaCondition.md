# V1FlowSchemaCondition

FlowSchemaCondition describes conditions for a FlowSchema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | &#x60;lastTransitionTime&#x60; is the last time the condition transitioned from one status to another. | [optional] 
**message** | **str** | &#x60;message&#x60; is a human-readable message indicating details about last transition. | [optional] 
**reason** | **str** | &#x60;reason&#x60; is a unique, one-word, CamelCase reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | &#x60;status&#x60; is the status of the condition. Can be True, False, Unknown. Required. | [optional] 
**type** | **str** | &#x60;type&#x60; is the type of the condition. Required. | [optional] 

## Example

```python
from kubernetes.client.models.v1_flow_schema_condition import V1FlowSchemaCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowSchemaCondition from a JSON string
v1_flow_schema_condition_instance = V1FlowSchemaCondition.from_json(json)
# print the JSON string representation of the object
print V1FlowSchemaCondition.to_json()

# convert the object into a dict
v1_flow_schema_condition_dict = v1_flow_schema_condition_instance.to_dict()
# create an instance of V1FlowSchemaCondition from a dict
v1_flow_schema_condition_form_dict = v1_flow_schema_condition.from_dict(v1_flow_schema_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


