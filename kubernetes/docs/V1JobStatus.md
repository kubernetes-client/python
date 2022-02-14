# V1JobStatus

JobStatus represents the current state of a Job.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** | The number of pending and running pods. | [optional] 
**completed_indexes** | **str** | CompletedIndexes holds the completed indexes when .spec.completionMode &#x3D; \&quot;Indexed\&quot; in a text format. The indexes are represented as decimal integers separated by commas. The numbers are listed in increasing order. Three or more consecutive numbers are compressed and represented by the first and last element of the series, separated by a hyphen. For example, if the completed indexes are 1, 3, 4, 5 and 7, they are represented as \&quot;1,3-5,7\&quot;. | [optional] 
**completion_time** | **datetime** | Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. The completion time is only set when the job finishes successfully. | [optional] 
**conditions** | [**list[V1JobCondition]**](V1JobCondition.md) | The latest available observations of an object&#39;s current state. When a Job fails, one of the conditions will have type \&quot;Failed\&quot; and status true. When a Job is suspended, one of the conditions will have type \&quot;Suspended\&quot; and status true; when the Job is resumed, the status of this condition will become false. When a Job is completed, one of the conditions will have type \&quot;Complete\&quot; and status true. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/ | [optional] 
**failed** | **int** | The number of pods which reached phase Failed. | [optional] 
**ready** | **int** | The number of pods which have a Ready condition.  This field is alpha-level. The job controller populates the field when the feature gate JobReadyPods is enabled (disabled by default). | [optional] 
**start_time** | **datetime** | Represents time when the job controller started processing a job. When a Job is created in the suspended state, this field is not set until the first time it is resumed. This field is reset every time a Job is resumed from suspension. It is represented in RFC3339 form and is in UTC. | [optional] 
**succeeded** | **int** | The number of pods which reached phase Succeeded. | [optional] 
**uncounted_terminated_pods** | [**V1UncountedTerminatedPods**](V1UncountedTerminatedPods.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


