# kubernetes.client.model.v1_http_get_action.V1HTTPGetAction

HTTPGetAction describes an action based on HTTP Get requests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | HTTPGetAction describes an action based on HTTP Get requests. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[port](#port)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. | 
**host** | str,  | str,  | Host name to connect to, defaults to the pod IP. You probably want to set \&quot;Host\&quot; in httpHeaders instead. | [optional] 
**[httpHeaders](#httpHeaders)** | list, tuple,  | tuple,  | Custom headers to set in the request. HTTP allows repeated headers. | [optional] 
**path** | str,  | str,  | Path to access on the HTTP server. | [optional] 
**scheme** | str,  | str,  | Scheme to use for connecting to the host. Defaults to HTTP.   | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# port

Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. | 

# httpHeaders

Custom headers to set in the request. HTTP allows repeated headers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Custom headers to set in the request. HTTP allows repeated headers. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1HTTPHeader**](V1HTTPHeader.md) | [**V1HTTPHeader**](V1HTTPHeader.md) | [**V1HTTPHeader**](V1HTTPHeader.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

