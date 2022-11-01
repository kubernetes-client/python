# kubernetes.client.model.v1_persistent_volume_claim_spec.V1PersistentVolumeClaimSpec

PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[accessModes](#accessModes)** | list, tuple,  | tuple,  | accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 | [optional] 
**dataSource** | [**V1TypedLocalObjectReference**](V1TypedLocalObjectReference.md) | [**V1TypedLocalObjectReference**](V1TypedLocalObjectReference.md) |  | [optional] 
**dataSourceRef** | [**V1TypedLocalObjectReference**](V1TypedLocalObjectReference.md) | [**V1TypedLocalObjectReference**](V1TypedLocalObjectReference.md) |  | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**storageClassName** | str,  | str,  | storageClassName is the name of the StorageClass required by the claim. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1 | [optional] 
**volumeMode** | str,  | str,  | volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec. | [optional] 
**volumeName** | str,  | str,  | volumeName is the binding reference to the PersistentVolume backing this claim. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accessModes

accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | accessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1 | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

