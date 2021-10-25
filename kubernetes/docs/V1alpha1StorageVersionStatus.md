# V1alpha1StorageVersionStatus

API server instances report the versions they can decode and the version they encode objects to when persisting objects in the backend.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_encoding_version** | **str** | If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality. | [optional] 
**conditions** | [**list[V1alpha1StorageVersionCondition]**](V1alpha1StorageVersionCondition.md) | The latest available observations of the storageVersion&#39;s state. | [optional] 
**storage_versions** | [**list[V1alpha1ServerStorageVersion]**](V1alpha1ServerStorageVersion.md) | The reported versions per API server instance. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


