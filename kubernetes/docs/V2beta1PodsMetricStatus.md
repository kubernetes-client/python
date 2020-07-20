# V2beta1PodsMetricStatus

PodsMetricStatus indicates the current value of a metric describing each pod in the current scale target (for example, transactions-processed-per-second).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_average_value** | **str** | currentAverageValue is the current value of the average of the metric across all relevant pods (as a quantity) | 
**metric_name** | **str** | metricName is the name of the metric in question | 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


