# V1PersistentVolumeClaimSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **list[str]** | AccessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources represents the minimum resources the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources | [optional] 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) | A label query over volumes to consider for binding. | [optional] 
**storage_class_name** | **str** | Name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 | [optional] 
**volume_name** | **str** | VolumeName is the binding reference to the PersistentVolume backing this claim. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


