# kubernetes.client.model.v2beta2_metric_target.V2beta2MetricTarget

MetricTarget defines the target value, average value, or average utilization of a specific metric

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | MetricTarget defines the target value, average value, or average utilization of a specific metric | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | type represents whether the metric type is Utilization, Value, or AverageValue | 
**averageUtilization** | decimal.Decimal, int,  | decimal.Decimal,  | averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type | [optional] value must be a 32 bit integer
**averageValue** | str,  | str,  | averageValue is the target value of the average of the metric across all relevant pods (as a quantity) | [optional] 
**value** | str,  | str,  | value is the target value of the metric (as a quantity). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

