# V2beta1HorizontalPodAutoscalerSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_replicas** | **int** | maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas. | 
**metrics** | [**list[V2beta1MetricSpec]**](V2beta1MetricSpec.md) | metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. | [optional] 
**min_replicas** | **int** | minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down. It defaults to 1 pod. | [optional] 
**scale_target_ref** | [**V2beta1CrossVersionObjectReference**](V2beta1CrossVersionObjectReference.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


