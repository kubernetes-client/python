# V1HorizontalPodAutoscalerSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_replicas** | **int** | upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas. | 
**min_replicas** | **int** | minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available. | [optional] 
**scale_target_ref** | [**V1CrossVersionObjectReference**](V1CrossVersionObjectReference.md) |  | 
**target_cpu_utilization_percentage** | **int** | target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


