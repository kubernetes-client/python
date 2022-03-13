# V1CustomResourceDefinitionCondition

CustomResourceDefinitionCondition contains details for the current condition of this pod.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | status is the status of the condition. Can be True, False, Unknown. | 
**type** | **str** | type is the type of the condition. Types include Established, NamesAccepted and Terminating. | 
**last_transition_time** | **datetime** | lastTransitionTime last time the condition transitioned from one status to another. | [optional] 
**message** | **str** | message is a human-readable message indicating details about last transition. | [optional] 
**reason** | **str** | reason is a unique, one-word, CamelCase reason for the condition&#39;s last transition. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


