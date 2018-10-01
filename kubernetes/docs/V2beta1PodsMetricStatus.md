# V2beta1PodsMetricStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_average_value** | **str** | currentAverageValue is the current value of the average of the metric across all relevant pods (as a quantity) | 
**metric_name** | **str** | metricName is the name of the metric in question | 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) | selector is the string-encoded form of a standard kubernetes label selector for the given metric When set in the PodsMetricSource, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


