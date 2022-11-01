# kubernetes.client.model.v1_service_backend_port.V1ServiceBackendPort

ServiceBackendPort is the service port being referenced.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ServiceBackendPort is the service port being referenced. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Name is the name of the port on the Service. This is a mutually exclusive setting with \&quot;Number\&quot;. | [optional] 
**number** | decimal.Decimal, int,  | decimal.Decimal,  | Number is the numerical port number (e.g. 80) on the Service. This is a mutually exclusive setting with \&quot;Name\&quot;. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

