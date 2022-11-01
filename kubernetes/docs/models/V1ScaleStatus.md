# kubernetes.client.model.v1_scale_status.V1ScaleStatus

ScaleStatus represents the current status of a scale subresource.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ScaleStatus represents the current status of a scale subresource. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**replicas** | decimal.Decimal, int,  | decimal.Decimal,  | actual number of observed instances of the scaled object. | value must be a 32 bit integer
**selector** | str,  | str,  | label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by kubernetes.clients. The string will be in the same format as the query-param syntax. More info about label selectors: http://kubernetes.io/docs/user-guide/labels#label-selectors | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

