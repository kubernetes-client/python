# V1PersistentVolumeStatus

PersistentVolumeStatus is the current status of a persistent volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_phase_transition_time** | **datetime** | lastPhaseTransitionTime is the time the phase transitioned from one to another and automatically resets to current time everytime a volume phase transitions. This is a beta field and requires the PersistentVolumeLastPhaseTransitionTime feature to be enabled (enabled by default). | [optional] 
**message** | **str** | message is a human-readable message indicating details about why the volume is in this state. | [optional] 
**phase** | **str** | phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase | [optional] 
**reason** | **str** | reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI. | [optional] 

## Example

```python
from kubernetes.client.models.v1_persistent_volume_status import V1PersistentVolumeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1PersistentVolumeStatus from a JSON string
v1_persistent_volume_status_instance = V1PersistentVolumeStatus.from_json(json)
# print the JSON string representation of the object
print V1PersistentVolumeStatus.to_json()

# convert the object into a dict
v1_persistent_volume_status_dict = v1_persistent_volume_status_instance.to_dict()
# create an instance of V1PersistentVolumeStatus from a dict
v1_persistent_volume_status_form_dict = v1_persistent_volume_status.from_dict(v1_persistent_volume_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


