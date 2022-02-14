# V1JobCondition

JobCondition describes current state of a job.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | **datetime** | Last time the condition was checked. | [optional] 
**last_transition_time** | **datetime** | Last time the condition transit from one status to another. | [optional] 
**message** | **str** | Human readable message indicating details about last transition. | [optional] 
**reason** | **str** | (brief) reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of job condition, Complete or Failed.  Possible enum values:  - &#x60;\&quot;Complete\&quot;&#x60; means the job has completed its execution.  - &#x60;\&quot;Failed\&quot;&#x60; means the job has failed its execution.  - &#x60;\&quot;Suspended\&quot;&#x60; means the job has been suspended. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


