# V2beta1ExternalMetricStatus

ExternalMetricStatus indicates the current value of a global metric not associated with any Kubernetes object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_value** | **str** | currentValue is the current value of the metric (as a quantity) | 
**metric_name** | **str** | metricName is the name of a metric used for autoscaling in metric system. | 
**current_average_value** | **str** | currentAverageValue is the current value of metric averaged over autoscaled pods. | [optional] 
**metric_selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


