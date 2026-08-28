# V1PodVolumeHealth

PodVolumeHealth contains health information for a volume used by a pod, reported by the CSI node plugin via the kubelet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**health_conditions** | [**List[V1VolumeHealthCondition]**](V1VolumeHealthCondition.md) | conditions is the set of adverse conditions reported by the CSI node plugin for this volume on this node. At most 16 conditions may be reported. | [optional]
**last_transition_time** | **datetime** | lastTransitionTime is when the current set of conditions first appeared. | [optional]
**name** | **str** | name matches an entry in pod.spec.volumes. |

## Example

```python
from kubernetes.aio.client.models.v1_pod_volume_health import V1PodVolumeHealth

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodVolumeHealth from a JSON string
v1_pod_volume_health_instance = V1PodVolumeHealth.from_json(json)
# print the JSON string representation of the object
print(V1PodVolumeHealth.to_json())

# convert the object into a dict
v1_pod_volume_health_dict = v1_pod_volume_health_instance.to_dict()
# create an instance of V1PodVolumeHealth from a dict
v1_pod_volume_health_from_dict = V1PodVolumeHealth.from_dict(v1_pod_volume_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
