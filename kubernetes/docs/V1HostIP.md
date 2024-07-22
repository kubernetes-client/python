# V1HostIP

HostIP represents a single IP address allocated to the host.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP is the IP address assigned to the host | [optional] 

## Example

```python
from kubernetes.client.models.v1_host_ip import V1HostIP

# TODO update the JSON string below
json = "{}"
# create an instance of V1HostIP from a JSON string
v1_host_ip_instance = V1HostIP.from_json(json)
# print the JSON string representation of the object
print V1HostIP.to_json()

# convert the object into a dict
v1_host_ip_dict = v1_host_ip_instance.to_dict()
# create an instance of V1HostIP from a dict
v1_host_ip_form_dict = v1_host_ip.from_dict(v1_host_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


