# V1LifecycleHandler

LifecycleHandler defines a specific action that should be taken in a lifecycle hook. One and only one of the fields, except TCPSocket must be specified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_exec** | [**V1ExecAction**](V1ExecAction.md) |  | [optional] 
**http_get** | [**V1HTTPGetAction**](V1HTTPGetAction.md) |  | [optional] 
**sleep** | [**V1SleepAction**](V1SleepAction.md) |  | [optional] 
**tcp_socket** | [**V1TCPSocketAction**](V1TCPSocketAction.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_lifecycle_handler import V1LifecycleHandler

# TODO update the JSON string below
json = "{}"
# create an instance of V1LifecycleHandler from a JSON string
v1_lifecycle_handler_instance = V1LifecycleHandler.from_json(json)
# print the JSON string representation of the object
print V1LifecycleHandler.to_json()

# convert the object into a dict
v1_lifecycle_handler_dict = v1_lifecycle_handler_instance.to_dict()
# create an instance of V1LifecycleHandler from a dict
v1_lifecycle_handler_form_dict = v1_lifecycle_handler.from_dict(v1_lifecycle_handler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


