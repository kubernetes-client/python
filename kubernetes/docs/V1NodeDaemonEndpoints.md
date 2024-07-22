# V1NodeDaemonEndpoints

NodeDaemonEndpoints lists ports opened by daemons running on the Node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubelet_endpoint** | [**V1DaemonEndpoint**](V1DaemonEndpoint.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_node_daemon_endpoints import V1NodeDaemonEndpoints

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeDaemonEndpoints from a JSON string
v1_node_daemon_endpoints_instance = V1NodeDaemonEndpoints.from_json(json)
# print the JSON string representation of the object
print V1NodeDaemonEndpoints.to_json()

# convert the object into a dict
v1_node_daemon_endpoints_dict = v1_node_daemon_endpoints_instance.to_dict()
# create an instance of V1NodeDaemonEndpoints from a dict
v1_node_daemon_endpoints_form_dict = v1_node_daemon_endpoints.from_dict(v1_node_daemon_endpoints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


