# V1CronJobStatus

CronJobStatus represents the current state of a cron job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**[V1ObjectReference]**](V1ObjectReference.md) | A list of pointers to currently running jobs. | [optional] 
**last_schedule_time** | **datetime** | Information when was the last time the job was successfully scheduled. | [optional] 
**last_successful_time** | **datetime** | Information when was the last time the job successfully completed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


