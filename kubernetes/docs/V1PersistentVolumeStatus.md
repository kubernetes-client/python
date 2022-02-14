# V1PersistentVolumeStatus

PersistentVolumeStatus is the current status of a persistent volume.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A human-readable message indicating details about why the volume is in this state. | [optional] 
**phase** | **str** | Phase indicates if a volume is available, bound to a claim, or released by a claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#phase  Possible enum values:  - &#x60;\&quot;Available\&quot;&#x60; used for PersistentVolumes that are not yet bound Available volumes are held by the binder and matched to PersistentVolumeClaims  - &#x60;\&quot;Bound\&quot;&#x60; used for PersistentVolumes that are bound  - &#x60;\&quot;Failed\&quot;&#x60; used for PersistentVolumes that failed to be correctly recycled or deleted after being released from a claim  - &#x60;\&quot;Pending\&quot;&#x60; used for PersistentVolumes that are not available  - &#x60;\&quot;Released\&quot;&#x60; used for PersistentVolumes where the bound PersistentVolumeClaim was deleted released volumes must be recycled before becoming available again this phase is used by the persistent volume claim binder to signal to another process to reclaim the resource | [optional] 
**reason** | **str** | Reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


