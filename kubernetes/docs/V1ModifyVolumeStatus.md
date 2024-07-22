# V1ModifyVolumeStatus

ModifyVolumeStatus represents the status object of ControllerModifyVolume operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | status is the status of the ControllerModifyVolume operation. It can be in any of following states:  - Pending    Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as    the specified VolumeAttributesClass not existing.  - InProgress    InProgress indicates that the volume is being modified.  - Infeasible   Infeasible indicates that the request has been rejected as invalid by the CSI driver. To    resolve the error, a valid VolumeAttributesClass needs to be specified. Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately. | 
**target_volume_attributes_class_name** | **str** | targetVolumeAttributesClassName is the name of the VolumeAttributesClass the PVC currently being reconciled | [optional] 

## Example

```python
from kubernetes.client.models.v1_modify_volume_status import V1ModifyVolumeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1ModifyVolumeStatus from a JSON string
v1_modify_volume_status_instance = V1ModifyVolumeStatus.from_json(json)
# print the JSON string representation of the object
print V1ModifyVolumeStatus.to_json()

# convert the object into a dict
v1_modify_volume_status_dict = v1_modify_volume_status_instance.to_dict()
# create an instance of V1ModifyVolumeStatus from a dict
v1_modify_volume_status_form_dict = v1_modify_volume_status.from_dict(v1_modify_volume_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


