# V2beta1ExternalMetricSource

ExternalMetricSource indicates how to scale on a metric not associated with any Kubernetes object (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster). Exactly one \"target\" type should be set.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name** | **str** | metricName is the name of the metric in question. | 
**metric_selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**target_average_value** | **str** | targetAverageValue is the target per-pod value of global metric (as a quantity). Mutually exclusive with TargetValue. | [optional] 
**target_value** | **str** | targetValue is the target value of the metric (as a quantity). Mutually exclusive with TargetAverageValue. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


