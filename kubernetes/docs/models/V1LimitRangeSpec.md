# kubernetes.client.model.v1_limit_range_spec.V1LimitRangeSpec

LimitRangeSpec defines a min/max usage limit for resources that match on kind.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | LimitRangeSpec defines a min/max usage limit for resources that match on kind. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[limits](#limits)** | list, tuple,  | tuple,  | Limits is the list of LimitRangeItem objects that are enforced. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# limits

Limits is the list of LimitRangeItem objects that are enforced.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Limits is the list of LimitRangeItem objects that are enforced. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1LimitRangeItem**](V1LimitRangeItem.md) | [**V1LimitRangeItem**](V1LimitRangeItem.md) | [**V1LimitRangeItem**](V1LimitRangeItem.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

