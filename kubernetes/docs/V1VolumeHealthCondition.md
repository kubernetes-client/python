# V1VolumeHealthCondition

VolumeHealthCondition represents an adverse health condition reported for a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | message is a human-readable description. Maximum permitted length of a message is 1024 bytes. | [optional]
**reason** | **str** | reason is a brief CamelCase machine-parseable reason. Together with status it forms the unique identity of a condition entry. Maximum permitted length of a reason is 256 bytes. |
**status** | **str** | status is the machine-parseable health category. Possible values: - \&quot;Inaccessible\&quot;: the volume cannot be accessed. - \&quot;DataLoss\&quot;: data loss has been detected on the volume. - \&quot;Degraded\&quot;: the volume is functioning with reduced capability. |

## Example

```python
from kubernetes.client.models.v1_volume_health_condition import V1VolumeHealthCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeHealthCondition from a JSON string
v1_volume_health_condition_instance = V1VolumeHealthCondition.from_json(json)
# print the JSON string representation of the object
print(V1VolumeHealthCondition.to_json())

# convert the object into a dict
v1_volume_health_condition_dict = v1_volume_health_condition_instance.to_dict()
# create an instance of V1VolumeHealthCondition from a dict
v1_volume_health_condition_from_dict = V1VolumeHealthCondition.from_dict(v1_volume_health_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
