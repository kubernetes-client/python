# V1beta1HorizontalPodAutoscalerSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_utilization** | [**V1beta1CPUTargetUtilization**](V1beta1CPUTargetUtilization.md) | target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified it defaults to the target CPU utilization at 80% of the requested resources. | [optional] 
**max_replicas** | **int** | upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas. | 
**min_replicas** | **int** | lower limit for the number of pods that can be set by the autoscaler, default 1. | [optional] 
**scale_ref** | [**V1beta1SubresourceReference**](V1beta1SubresourceReference.md) | reference to Scale subresource; horizontal pod autoscaler will learn the current resource consumption from its status, and will set the desired number of pods by modifying its spec. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


