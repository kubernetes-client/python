# kubernetes.client.model.v1_cron_job_spec.V1CronJobSpec

CronJobSpec describes how the job execution will look like and when it will actually run.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CronJobSpec describes how the job execution will look like and when it will actually run. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**schedule** | str,  | str,  | The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron. | 
**jobTemplate** | [**V1JobTemplateSpec**](V1JobTemplateSpec.md) | [**V1JobTemplateSpec**](V1JobTemplateSpec.md) |  | 
**concurrencyPolicy** | str,  | str,  | Specifies how to treat concurrent executions of a Job. Valid values are: - \&quot;Allow\&quot; (default): allows CronJobs to run concurrently; - \&quot;Forbid\&quot;: forbids concurrent runs, skipping next run if previous run hasn&#x27;t finished yet; - \&quot;Replace\&quot;: cancels currently running job and replaces it with a new one   | [optional] 
**failedJobsHistoryLimit** | decimal.Decimal, int,  | decimal.Decimal,  | The number of failed finished jobs to retain. Value must be non-negative integer. Defaults to 1. | [optional] value must be a 32 bit integer
**startingDeadlineSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones. | [optional] value must be a 64 bit integer
**successfulJobsHistoryLimit** | decimal.Decimal, int,  | decimal.Decimal,  | The number of successful finished jobs to retain. Value must be non-negative integer. Defaults to 3. | [optional] value must be a 32 bit integer
**suspend** | bool,  | BoolClass,  | This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false. | [optional] 
**timeZone** | str,  | str,  | The time zone name for the given schedule, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. If not specified, this will default to the time zone of the kube-controller-manager process. The set of valid time zone names and the time zone offset is loaded from the system-wide time zone database by the API server during CronJob validation and the controller manager during execution. If no system-wide time zone database can be found a bundled version of the database is used instead. If the time zone name becomes invalid during the lifetime of a CronJob or due to a change in host configuration, the controller will stop creating new new Jobs and will create a system event with the reason UnknownTimeZone. More information can be found in https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones This is beta field and must be enabled via the &#x60;CronJobTimeZone&#x60; feature gate. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

