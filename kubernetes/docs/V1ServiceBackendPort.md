# V1ServiceBackendPort

ServiceBackendPort is the service port being referenced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the name of the port on the Service. This is a mutually exclusive setting with \&quot;Number\&quot;. | [optional] 
**number** | **int** | number is the numerical port number (e.g. 80) on the Service. This is a mutually exclusive setting with \&quot;Name\&quot;. | [optional] 

## Example

```python
from kubernetes.client.models.v1_service_backend_port import V1ServiceBackendPort

# TODO update the JSON string below
json = "{}"
# create an instance of V1ServiceBackendPort from a JSON string
v1_service_backend_port_instance = V1ServiceBackendPort.from_json(json)
# print the JSON string representation of the object
print V1ServiceBackendPort.to_json()

# convert the object into a dict
v1_service_backend_port_dict = v1_service_backend_port_instance.to_dict()
# create an instance of V1ServiceBackendPort from a dict
v1_service_backend_port_form_dict = v1_service_backend_port.from_dict(v1_service_backend_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


