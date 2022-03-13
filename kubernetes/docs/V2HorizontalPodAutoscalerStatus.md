# V2HorizontalPodAutoscalerStatus

HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desired_replicas** | **int** | desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler. | 
**conditions** | [**[V2HorizontalPodAutoscalerCondition]**](V2HorizontalPodAutoscalerCondition.md) | conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met. | [optional] 
**current_metrics** | [**[V2MetricStatus]**](V2MetricStatus.md) | currentMetrics is the last read state of the metrics used by this autoscaler. | [optional] 
**current_replicas** | **int** | currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler. | [optional] 
**last_scale_time** | **datetime** | lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed. | [optional] 
**observed_generation** | **int** | observedGeneration is the most recent generation observed by this autoscaler. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


