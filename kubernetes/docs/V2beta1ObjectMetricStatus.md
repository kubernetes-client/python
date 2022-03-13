# V2beta1ObjectMetricStatus

ObjectMetricStatus indicates the current value of a metric describing a kubernetes object (for example, hits-per-second on an Ingress object).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_value** | **str** | currentValue is the current value of the metric (as a quantity). | 
**metric_name** | **str** | metricName is the name of the metric in question. | 
**target** | [**V2beta1CrossVersionObjectReference**](V2beta1CrossVersionObjectReference.md) |  | 
**average_value** | **str** | averageValue is the current value of the average of the metric across all relevant pods (as a quantity) | [optional] 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


