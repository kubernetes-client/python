# kubernetes.client.model.v2_metric_value_status.V2MetricValueStatus

MetricValueStatus holds the current value for a metric

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | MetricValueStatus holds the current value for a metric | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**averageUtilization** | decimal.Decimal, int,  | decimal.Decimal,  | currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. | [optional] value must be a 32 bit integer
**averageValue** | str,  | str,  | averageValue is the current value of the average of the metric across all relevant pods (as a quantity) | [optional] 
**value** | str,  | str,  | value is the current value of the metric (as a quantity). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

