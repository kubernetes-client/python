# V1PersistentVolumeClaimCondition

PersistentVolumeClaimCondition contains details about state of pvc

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | **datetime** | lastProbeTime is the time we probed the condition. | [optional]
**last_transition_time** | **datetime** | lastTransitionTime is the time the condition transitioned from one status to another. | [optional]
**message** | **str** | message is the human-readable message indicating details about last transition. | [optional]
**reason** | **str** | reason is a unique, this should be a short, machine understandable string that gives the reason for condition&#39;s last transition. If it reports \&quot;Resizing\&quot; that means the underlying persistent volume is being resized. | [optional]
**status** | **str** | Status is the status of the condition. Can be True, False, Unknown. More info: https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text&#x3D;state%20of%20pvc-,conditions.status,-(string)%2C%20required |
**type** | **str** | Type is the type of the condition. More info: https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text&#x3D;set%20to%20%27ResizeStarted%27.-,PersistentVolumeClaimCondition,-contains%20details%20about |

## Example

```python
from kubernetes.client.models.v1_persistent_volume_claim_condition import V1PersistentVolumeClaimCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1PersistentVolumeClaimCondition from a JSON string
v1_persistent_volume_claim_condition_instance = V1PersistentVolumeClaimCondition.from_json(json)
# print the JSON string representation of the object
print(V1PersistentVolumeClaimCondition.to_json())

# convert the object into a dict
v1_persistent_volume_claim_condition_dict = v1_persistent_volume_claim_condition_instance.to_dict()
# create an instance of V1PersistentVolumeClaimCondition from a dict
v1_persistent_volume_claim_condition_from_dict = V1PersistentVolumeClaimCondition.from_dict(v1_persistent_volume_claim_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
