# V1PodIP

PodIP represents a single IP address allocated to the pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP is the IP address assigned to the pod | [optional] 

## Example

```python
from kubernetes.client.models.v1_pod_ip import V1PodIP

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodIP from a JSON string
v1_pod_ip_instance = V1PodIP.from_json(json)
# print the JSON string representation of the object
print V1PodIP.to_json()

# convert the object into a dict
v1_pod_ip_dict = v1_pod_ip_instance.to_dict()
# create an instance of V1PodIP from a dict
v1_pod_ip_form_dict = v1_pod_ip.from_dict(v1_pod_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


