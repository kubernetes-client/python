# kubernetes.client.model.v1_bound_object_reference.V1BoundObjectReference

BoundObjectReference is a reference to an object that a token is bound to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | BoundObjectReference is a reference to an object that a token is bound to. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**apiVersion** | str,  | str,  | API version of the referent. | [optional] 
**kind** | str,  | str,  | Kind of the referent. Valid kinds are &#x27;Pod&#x27; and &#x27;Secret&#x27;. | [optional] 
**name** | str,  | str,  | Name of the referent. | [optional] 
**uid** | str,  | str,  | UID of the referent. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

