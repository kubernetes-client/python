# V1LifecycleHandler

LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_exec** | [**V1ExecAction**](V1ExecAction.md) |  | [optional] 
**http_get** | [**V1HTTPGetAction**](V1HTTPGetAction.md) |  | [optional] 
**tcp_socket** | [**V1TCPSocketAction**](V1TCPSocketAction.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


