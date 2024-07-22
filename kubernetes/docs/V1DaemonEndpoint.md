# V1DaemonEndpoint

DaemonEndpoint contains information about a single Daemon endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** | Port number of the given endpoint. | 

## Example

```python
from kubernetes.client.models.v1_daemon_endpoint import V1DaemonEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of V1DaemonEndpoint from a JSON string
v1_daemon_endpoint_instance = V1DaemonEndpoint.from_json(json)
# print the JSON string representation of the object
print V1DaemonEndpoint.to_json()

# convert the object into a dict
v1_daemon_endpoint_dict = v1_daemon_endpoint_instance.to_dict()
# create an instance of V1DaemonEndpoint from a dict
v1_daemon_endpoint_form_dict = v1_daemon_endpoint.from_dict(v1_daemon_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


