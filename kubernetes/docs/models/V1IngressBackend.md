# kubernetes.client.model.v1_ingress_backend.V1IngressBackend

IngressBackend describes all endpoints for a given service and port.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | IngressBackend describes all endpoints for a given service and port. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resource** | [**V1TypedLocalObjectReference**](V1TypedLocalObjectReference.md) | [**V1TypedLocalObjectReference**](V1TypedLocalObjectReference.md) |  | [optional] 
**service** | [**V1IngressServiceBackend**](V1IngressServiceBackend.md) | [**V1IngressServiceBackend**](V1IngressServiceBackend.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

