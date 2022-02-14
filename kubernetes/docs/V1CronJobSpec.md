# V1CronJobSpec

CronJobSpec describes how the job execution will look like and when it will actually run.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency_policy** | **str** | Specifies how to treat concurrent executions of a Job. Valid values are: - \&quot;Allow\&quot; (default): allows CronJobs to run concurrently; - \&quot;Forbid\&quot;: forbids concurrent runs, skipping next run if previous run hasn&#39;t finished yet; - \&quot;Replace\&quot;: cancels currently running job and replaces it with a new one  Possible enum values:  - &#x60;\&quot;Allow\&quot;&#x60; allows CronJobs to run concurrently.  - &#x60;\&quot;Forbid\&quot;&#x60; forbids concurrent runs, skipping next run if previous hasn&#39;t finished yet.  - &#x60;\&quot;Replace\&quot;&#x60; cancels currently running job and replaces it with a new one. | [optional] 
**failed_jobs_history_limit** | **int** | The number of failed finished jobs to retain. Value must be non-negative integer. Defaults to 1. | [optional] 
**job_template** | [**V1JobTemplateSpec**](V1JobTemplateSpec.md) |  | 
**schedule** | **str** | The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron. | 
**starting_deadline_seconds** | **int** | Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones. | [optional] 
**successful_jobs_history_limit** | **int** | The number of successful finished jobs to retain. Value must be non-negative integer. Defaults to 3. | [optional] 
**suspend** | **bool** | This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


