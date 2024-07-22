# V1HTTPGetAction

HTTPGetAction describes an action based on HTTP Get requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str** | Host name to connect to, defaults to the pod IP. You probably want to set \&quot;Host\&quot; in httpHeaders instead. | [optional] 
**http_headers** | [**List[V1HTTPHeader]**](V1HTTPHeader.md) | Custom headers to set in the request. HTTP allows repeated headers. | [optional] 
**path** | **str** | Path to access on the HTTP server. | [optional] 
**port** | **object** | Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME. | 
**scheme** | **str** | Scheme to use for connecting to the host. Defaults to HTTP. | [optional] 

## Example

```python
from kubernetes.client.models.v1_http_get_action import V1HTTPGetAction

# TODO update the JSON string below
json = "{}"
# create an instance of V1HTTPGetAction from a JSON string
v1_http_get_action_instance = V1HTTPGetAction.from_json(json)
# print the JSON string representation of the object
print V1HTTPGetAction.to_json()

# convert the object into a dict
v1_http_get_action_dict = v1_http_get_action_instance.to_dict()
# create an instance of V1HTTPGetAction from a dict
v1_http_get_action_form_dict = v1_http_get_action.from_dict(v1_http_get_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


