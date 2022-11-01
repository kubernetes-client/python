# kubernetes.client.model.v1_lifecycle_handler.V1LifecycleHandler

LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**exec** | [**V1ExecAction**](V1ExecAction.md) | [**V1ExecAction**](V1ExecAction.md) |  | [optional] 
**httpGet** | [**V1HTTPGetAction**](V1HTTPGetAction.md) | [**V1HTTPGetAction**](V1HTTPGetAction.md) |  | [optional] 
**tcpSocket** | [**V1TCPSocketAction**](V1TCPSocketAction.md) | [**V1TCPSocketAction**](V1TCPSocketAction.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

