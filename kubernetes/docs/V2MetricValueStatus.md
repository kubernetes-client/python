# V2MetricValueStatus

MetricValueStatus holds the current value for a metric

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_utilization** | **int** | currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. | [optional] 
**average_value** | **str** | averageValue is the current value of the average of the metric across all relevant pods (as a quantity) | [optional] 
**value** | **str** | value is the current value of the metric (as a quantity). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


