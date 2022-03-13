# V1HorizontalPodAutoscalerStatus

current status of a horizontal pod autoscaler

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_replicas** | **int** | current number of replicas of pods managed by this autoscaler. | 
**desired_replicas** | **int** | desired number of replicas of pods managed by this autoscaler. | 
**current_cpu_utilization_percentage** | **int** | current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU. | [optional] 
**last_scale_time** | **datetime** | last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed. | [optional] 
**observed_generation** | **int** | most recent generation observed by this autoscaler. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


