# V1JobSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_deadline_seconds** | **int** | Specifies the duration in seconds relative to the startTime that the job may be active before the system tries to terminate it; value must be positive integer | [optional] 
**backoff_limit** | **int** | Specifies the number of retries before marking this job failed. Defaults to 6 | [optional] 
**completions** | **int** | Specifies the desired number of successfully finished pods the job should be run with.  Setting to nil means that the success of any pod signals the success of all pods, and allows parallelism to have any positive value.  Setting to 1 means that parallelism is limited to 1 and the success of that pod signals the success of the job. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ | [optional] 
**manual_selector** | **bool** | manualSelector controls generation of pod labels and pod selectors. Leave &#x60;manualSelector&#x60; unset unless you are certain what you are doing. When false or unset, the system pick labels unique to this job and appends those labels to the pod template.  When true, the user is responsible for picking unique labels and specifying the selector.  Failure to pick a unique label may cause this and other jobs to not function correctly.  However, You may see &#x60;manualSelector&#x3D;true&#x60; in jobs that were created with the old &#x60;extensions/v1beta1&#x60; API. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/#specifying-your-own-pod-selector | [optional] 
**parallelism** | **int** | Specifies the maximum desired number of pods the job should run at any given time. The actual number of pods running in steady state will be less than this number when ((.spec.completions - .status.successful) &lt; .spec.parallelism), i.e. when the work left to do is less than max parallelism. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ | [optional] 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) |  | 
**ttl_seconds_after_finished** | **int** | ttlSecondsAfterFinished limits the lifetime of a Job that has finished execution (either Complete or Failed). If this field is set, ttlSecondsAfterFinished after the Job finishes, it is eligible to be automatically deleted. When the Job is being deleted, its lifecycle guarantees (e.g. finalizers) will be honored. If this field is unset, the Job won&#39;t be automatically deleted. If this field is set to zero, the Job becomes eligible to be deleted immediately after it finishes. This field is alpha-level and is only honored by servers that enable the TTLAfterFinished feature. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


