# V1VolumeMountStatus

VolumeMountStatus shows status of volume mounts.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_path** | **str** | MountPath corresponds to the original VolumeMount. | 
**name** | **str** | Name corresponds to the name of the original VolumeMount. | 
**read_only** | **bool** | ReadOnly corresponds to the original VolumeMount. | [optional] 
**recursive_read_only** | **str** | RecursiveReadOnly must be set to Disabled, Enabled, or unspecified (for non-readonly mounts). An IfPossible value in the original VolumeMount must be translated to Disabled or Enabled, depending on the mount result. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


