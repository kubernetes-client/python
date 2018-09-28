# V2beta1ObjectMetricSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_value** | **str** | averageValue is the target value of the average of the metric across all relevant pods (as a quantity) | [optional] 
**metric_name** | **str** | metricName is the name of the metric in question. | 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) | selector is the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping When unset, just the metricName will be used to gather metrics. | [optional] 
**target** | [**V2beta1CrossVersionObjectReference**](V2beta1CrossVersionObjectReference.md) | target is the described Kubernetes object. | 
**target_value** | **str** | targetValue is the target value of the metric (as a quantity). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


