# V1VolumeHealthStatus

VolumeHealthStatus contains health information for a volume reported by the CSI controller plugin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_conditions** | [**List[V1VolumeHealthCondition]**](V1VolumeHealthCondition.md) | conditions is the set of adverse conditions reported by the CSI controller plugin. An empty list means no adverse condition. At most 16 conditions may be reported. | [optional]
**last_transition_time** | **datetime** | lastTransitionTime is when the current set of conditions first appeared. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1_volume_health_status import V1VolumeHealthStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1VolumeHealthStatus from a JSON string
v1_volume_health_status_instance = V1VolumeHealthStatus.from_json(json)
# print the JSON string representation of the object
print(V1VolumeHealthStatus.to_json())

# convert the object into a dict
v1_volume_health_status_dict = v1_volume_health_status_instance.to_dict()
# create an instance of V1VolumeHealthStatus from a dict
v1_volume_health_status_from_dict = V1VolumeHealthStatus.from_dict(v1_volume_health_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
