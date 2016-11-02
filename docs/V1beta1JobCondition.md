# V1beta1JobCondition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | [**UnversionedTime**](UnversionedTime.md) | Last time the condition was checked. | [optional] 
**last_transition_time** | [**UnversionedTime**](UnversionedTime.md) | Last time the condition transit from one status to another. | [optional] 
**message** | **str** | Human readable message indicating details about last transition. | [optional] 
**reason** | **str** | (brief) reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of job condition, Complete or Failed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


