# V1APIServiceCondition

APIServiceCondition describes the state of an APIService at a particular point

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status is the status of the condition. Can be True, False, Unknown. | 
**type** | **str** | Type is the type of the condition. | 
**last_transition_time** | **datetime** | Last time the condition transitioned from one status to another. | [optional] 
**message** | **str** | Human-readable message indicating details about last transition. | [optional] 
**reason** | **str** | Unique, one-word, CamelCase reason for the condition&#39;s last transition. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


