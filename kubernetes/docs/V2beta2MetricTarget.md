# V2beta2MetricTarget

MetricTarget defines the target value, average value, or average utilization of a specific metric

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | type represents whether the metric type is Utilization, Value, or AverageValue | 
**average_utilization** | **int** | averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type | [optional] 
**average_value** | **str** | averageValue is the target value of the average of the metric across all relevant pods (as a quantity) | [optional] 
**value** | **str** | value is the target value of the metric (as a quantity). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


