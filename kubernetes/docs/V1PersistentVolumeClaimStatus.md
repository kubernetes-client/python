# V1PersistentVolumeClaimStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **list[str]** | AccessModes contains the actual access modes the volume backing the PVC has. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes-1 | [optional] 
**capacity** | [**dict(str, ResourceQuantity)**](ResourceQuantity.md) | Represents the actual resources of the underlying volume. | [optional] 
**phase** | **str** | Phase represents the current phase of PersistentVolumeClaim. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


