# V1JobCondition

JobCondition describes current state of a job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of job condition, Complete or Failed. | 
**last_probe_time** | **datetime** | Last time the condition was checked. | [optional] 
**last_transition_time** | **datetime** | Last time the condition transit from one status to another. | [optional] 
**message** | **str** | Human readable message indicating details about last transition. | [optional] 
**reason** | **str** | (brief) reason for the condition&#39;s last transition. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


