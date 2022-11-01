# kubernetes.client.model.v1_job_condition.V1JobCondition

JobCondition describes current state of a job.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JobCondition describes current state of a job. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Type of job condition, Complete or Failed. | 
**status** | str,  | str,  | Status of the condition, one of True, False, Unknown. | 
**lastProbeTime** | str, datetime,  | str,  | Last time the condition was checked. | [optional] value must conform to RFC-3339 date-time
**lastTransitionTime** | str, datetime,  | str,  | Last time the condition transit from one status to another. | [optional] value must conform to RFC-3339 date-time
**message** | str,  | str,  | Human readable message indicating details about last transition. | [optional] 
**reason** | str,  | str,  | (brief) reason for the condition&#x27;s last transition. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

