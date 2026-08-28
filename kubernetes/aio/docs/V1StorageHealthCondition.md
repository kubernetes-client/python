# V1StorageHealthCondition

StorageHealthCondition represents an adverse health condition reported by a CSI driver for its storage backend on a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_mode** | **str** | accessMode is the access mode affected. Nil means all access modes are affected. | [optional]
**last_transition_time** | **datetime** | lastTransitionTime is when this condition first appeared at its current state. | [optional]
**message** | **str** | message is a human-readable description. Maximum permitted length of a message is 1024 characters. | [optional]
**reason** | **str** | reason is a brief CamelCase machine-parseable reason. Maximum permitted length of a reason is 256 characters. |
**status** | **str** | status is the health status category. One of \&quot;StorageUnreachable\&quot;, \&quot;StorageDegraded\&quot;. |
**volume_mode** | **str** | volumeMode is the volume mode affected. Nil means both are affected. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1_storage_health_condition import V1StorageHealthCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1StorageHealthCondition from a JSON string
v1_storage_health_condition_instance = V1StorageHealthCondition.from_json(json)
# print the JSON string representation of the object
print(V1StorageHealthCondition.to_json())

# convert the object into a dict
v1_storage_health_condition_dict = v1_storage_health_condition_instance.to_dict()
# create an instance of V1StorageHealthCondition from a dict
v1_storage_health_condition_from_dict = V1StorageHealthCondition.from_dict(v1_storage_health_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
