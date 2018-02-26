# V1CSIPersistentVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | Driver is the name of the driver to use for this volume. Required. | 
**read_only** | **bool** | Optional: The value to pass to ControllerPublishVolumeRequest. Defaults to false (read/write). | [optional] 
**volume_handle** | **str** | VolumeHandle is the unique volume name returned by the CSI volume plugin’s CreateVolume to refer to the volume on all subsequent calls. Required. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


