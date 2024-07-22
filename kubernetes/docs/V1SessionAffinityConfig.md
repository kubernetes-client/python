# V1SessionAffinityConfig

SessionAffinityConfig represents the configurations of session affinity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubernetes.client_ip** | [**V1ClientIPConfig**](V1ClientIPConfig.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_session_affinity_config import V1SessionAffinityConfig

# TODO update the JSON string below
json = "{}"
# create an instance of V1SessionAffinityConfig from a JSON string
v1_session_affinity_config_instance = V1SessionAffinityConfig.from_json(json)
# print the JSON string representation of the object
print V1SessionAffinityConfig.to_json()

# convert the object into a dict
v1_session_affinity_config_dict = v1_session_affinity_config_instance.to_dict()
# create an instance of V1SessionAffinityConfig from a dict
v1_session_affinity_config_form_dict = v1_session_affinity_config.from_dict(v1_session_affinity_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


