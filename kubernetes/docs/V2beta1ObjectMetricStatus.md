# V2beta1ObjectMetricStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_value** | **str** | averageValue is the current value of the average of the metric across all relevant pods (as a quantity) | [optional] 
**current_value** | **str** | currentValue is the current value of the metric (as a quantity). | 
**metric_name** | **str** | metricName is the name of the metric in question. | 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) | selector is the string-encoded form of a standard kubernetes label selector for the given metric When set in the ObjectMetricSource, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics. | [optional] 
**target** | [**V2beta1CrossVersionObjectReference**](V2beta1CrossVersionObjectReference.md) | target is the described Kubernetes object. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


