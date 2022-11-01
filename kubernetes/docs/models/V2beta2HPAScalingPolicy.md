# kubernetes.client.model.v2beta2_hpa_scaling_policy.V2beta2HPAScalingPolicy

HPAScalingPolicy is a single policy which must hold true for a specified past interval.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | HPAScalingPolicy is a single policy which must hold true for a specified past interval. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**periodSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | PeriodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). | value must be a 32 bit integer
**type** | str,  | str,  | Type is used to specify the scaling policy. | 
**value** | decimal.Decimal, int,  | decimal.Decimal,  | Value contains the amount of change which is permitted by the policy. It must be greater than zero | value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

