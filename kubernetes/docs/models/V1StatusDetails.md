# kubernetes.client.model.v1_status_details.V1StatusDetails

StatusDetails is a set of additional properties that MAY be set by the server to provide additional information about a response. The Reason field of a Status object defines what attributes will be set. Clients must ignore fields that do not match the defined type of each attribute, and should assume that any attribute may be empty, invalid, or under defined.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | StatusDetails is a set of additional properties that MAY be set by the server to provide additional information about a response. The Reason field of a Status object defines what attributes will be set. Clients must ignore fields that do not match the defined type of each attribute, and should assume that any attribute may be empty, invalid, or under defined. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[causes](#causes)** | list, tuple,  | tuple,  | The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes. | [optional] 
**group** | str,  | str,  | The group attribute of the resource associated with the status StatusReason. | [optional] 
**kind** | str,  | str,  | The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**name** | str,  | str,  | The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described). | [optional] 
**retryAfterSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | If specified, the time in seconds before the operation should be retried. Some errors may indicate the kubernetes.client must take an alternate action - for those errors this field may indicate how long to wait before taking the alternate action. | [optional] value must be a 32 bit integer
**uid** | str,  | str,  | UID of the resource. (when there is a single resource which can be described). More info: http://kubernetes.io/docs/user-guide/identifiers#uids | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# causes

The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1StatusCause**](V1StatusCause.md) | [**V1StatusCause**](V1StatusCause.md) | [**V1StatusCause**](V1StatusCause.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

