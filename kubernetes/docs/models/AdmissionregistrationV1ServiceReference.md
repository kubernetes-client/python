# kubernetes.client.model.admissionregistration_v1_service_reference.AdmissionregistrationV1ServiceReference

ServiceReference holds a reference to Service.legacy.k8s.io

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ServiceReference holds a reference to Service.legacy.k8s.io | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | &#x60;name&#x60; is the name of the service. Required | 
**namespace** | str,  | str,  | &#x60;namespace&#x60; is the namespace of the service. Required | 
**path** | str,  | str,  | &#x60;path&#x60; is an optional URL path which will be sent in any request to this service. | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. &#x60;port&#x60; should be a valid port number (1-65535, inclusive). | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

