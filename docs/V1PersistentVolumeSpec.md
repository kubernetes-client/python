# V1PersistentVolumeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | **list[str]** | AccessModes contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes | [optional] 
**capacity** | [**dict(str, ResourceQuantity)**](ResourceQuantity.md) | A description of the persistent volume&#39;s resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity | [optional] 
**claim_ref** | [**V1ObjectReference**](V1ObjectReference.md) | ClaimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#binding | [optional] 
**persistent_volume_reclaim_policy** | **str** | What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


