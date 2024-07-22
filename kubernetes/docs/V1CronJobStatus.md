# V1CronJobStatus

CronJobStatus represents the current state of a cron job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**List[V1ObjectReference]**](V1ObjectReference.md) | A list of pointers to currently running jobs. | [optional] 
**last_schedule_time** | **datetime** | Information when was the last time the job was successfully scheduled. | [optional] 
**last_successful_time** | **datetime** | Information when was the last time the job successfully completed. | [optional] 

## Example

```python
from kubernetes.client.models.v1_cron_job_status import V1CronJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1CronJobStatus from a JSON string
v1_cron_job_status_instance = V1CronJobStatus.from_json(json)
# print the JSON string representation of the object
print V1CronJobStatus.to_json()

# convert the object into a dict
v1_cron_job_status_dict = v1_cron_job_status_instance.to_dict()
# create an instance of V1CronJobStatus from a dict
v1_cron_job_status_form_dict = v1_cron_job_status.from_dict(v1_cron_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


