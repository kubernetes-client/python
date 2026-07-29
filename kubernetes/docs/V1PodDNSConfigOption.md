# V1PodDNSConfigOption

PodDNSConfigOption defines DNS resolver options of a pod.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is this DNS resolver option&#39;s name. Required. | [optional]
**value** | **str** | Value is this DNS resolver option&#39;s value. | [optional]

## Example

```python
from kubernetes.client.models.v1_pod_dns_config_option import V1PodDNSConfigOption

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodDNSConfigOption from a JSON string
v1_pod_dns_config_option_instance = V1PodDNSConfigOption.from_json(json)
# print the JSON string representation of the object
print(V1PodDNSConfigOption.to_json())

# convert the object into a dict
v1_pod_dns_config_option_dict = v1_pod_dns_config_option_instance.to_dict()
# create an instance of V1PodDNSConfigOption from a dict
v1_pod_dns_config_option_from_dict = V1PodDNSConfigOption.from_dict(v1_pod_dns_config_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
