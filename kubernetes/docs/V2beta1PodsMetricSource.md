# V2beta1PodsMetricSource

PodsMetricSource indicates how to scale on a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_name** | **str** | metricName is the name of the metric in question | 
**target_average_value** | **str** | targetAverageValue is the target value of the average of the metric across all relevant pods (as a quantity) | 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


