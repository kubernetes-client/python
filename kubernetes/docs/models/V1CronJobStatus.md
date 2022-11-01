# kubernetes.client.model.v1_cron_job_status.V1CronJobStatus

CronJobStatus represents the current state of a cron job.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CronJobStatus represents the current state of a cron job. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[active](#active)** | list, tuple,  | tuple,  | A list of pointers to currently running jobs. | [optional] 
**lastScheduleTime** | str, datetime,  | str,  | Information when was the last time the job was successfully scheduled. | [optional] value must conform to RFC-3339 date-time
**lastSuccessfulTime** | str, datetime,  | str,  | Information when was the last time the job successfully completed. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# active

A list of pointers to currently running jobs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of pointers to currently running jobs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1ObjectReference**](V1ObjectReference.md) | [**V1ObjectReference**](V1ObjectReference.md) | [**V1ObjectReference**](V1ObjectReference.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

