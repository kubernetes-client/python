# V1TCPSocketAction

TCPSocketAction describes an action based on opening a socket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Optional: Host name to connect to, defaults to the pod IP. | [optional] 
**port** | **object** | Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. | 

## Example

```python
from kubernetes.client.models.v1_tcp_socket_action import V1TCPSocketAction

# TODO update the JSON string below
json = "{}"
# create an instance of V1TCPSocketAction from a JSON string
v1_tcp_socket_action_instance = V1TCPSocketAction.from_json(json)
# print the JSON string representation of the object
print V1TCPSocketAction.to_json()

# convert the object into a dict
v1_tcp_socket_action_dict = v1_tcp_socket_action_instance.to_dict()
# create an instance of V1TCPSocketAction from a dict
v1_tcp_socket_action_form_dict = v1_tcp_socket_action.from_dict(v1_tcp_socket_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


