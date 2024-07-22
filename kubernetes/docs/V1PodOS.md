# V1PodOS

PodOS defines the OS parameters of a pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the name of the operating system. The currently supported values are linux and windows. Additional value may be defined in future and can be one of: https://github.com/opencontainers/runtime-spec/blob/master/config.md#platform-specific-configuration Clients should expect to handle additional values and treat unrecognized values in this field as os: null | 

## Example

```python
from kubernetes.client.models.v1_pod_os import V1PodOS

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodOS from a JSON string
v1_pod_os_instance = V1PodOS.from_json(json)
# print the JSON string representation of the object
print V1PodOS.to_json()

# convert the object into a dict
v1_pod_os_dict = v1_pod_os_instance.to_dict()
# create an instance of V1PodOS from a dict
v1_pod_os_form_dict = v1_pod_os.from_dict(v1_pod_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


