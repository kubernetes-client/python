# V1PortStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error is to record the problem with the service port The format of the error shall comply with the following rules: - built-in error values shall be specified in this file and those shall use   CamelCase names - cloud provider specific error values must have names that comply with the   format foo.example.com/CamelCase. | [optional] 
**port** | **int** | Port is the port number of the service port of which status is recorded here | 
**protocol** | **str** | Protocol is the protocol of the service port of which status is recorded here The supported values are: \&quot;TCP\&quot;, \&quot;UDP\&quot;, \&quot;SCTP\&quot; | 

## Example

```python
from kubernetes.client.models.v1_port_status import V1PortStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1PortStatus from a JSON string
v1_port_status_instance = V1PortStatus.from_json(json)
# print the JSON string representation of the object
print V1PortStatus.to_json()

# convert the object into a dict
v1_port_status_dict = v1_port_status_instance.to_dict()
# create an instance of V1PortStatus from a dict
v1_port_status_form_dict = v1_port_status.from_dict(v1_port_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


