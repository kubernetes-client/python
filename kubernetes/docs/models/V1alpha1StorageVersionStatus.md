# kubernetes.client.model.v1alpha1_storage_version_status.V1alpha1StorageVersionStatus

API server instances report the versions they can decode and the version they encode objects to when persisting objects in the backend.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | API server instances report the versions they can decode and the version they encode objects to when persisting objects in the backend. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**commonEncodingVersion** | str,  | str,  | If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality. | [optional] 
**[conditions](#conditions)** | list, tuple,  | tuple,  | The latest available observations of the storageVersion&#x27;s state. | [optional] 
**[storageVersions](#storageVersions)** | list, tuple,  | tuple,  | The reported versions per API server instance. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

The latest available observations of the storageVersion's state.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The latest available observations of the storageVersion&#x27;s state. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1alpha1StorageVersionCondition**](V1alpha1StorageVersionCondition.md) | [**V1alpha1StorageVersionCondition**](V1alpha1StorageVersionCondition.md) | [**V1alpha1StorageVersionCondition**](V1alpha1StorageVersionCondition.md) |  | 

# storageVersions

The reported versions per API server instance.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The reported versions per API server instance. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1alpha1ServerStorageVersion**](V1alpha1ServerStorageVersion.md) | [**V1alpha1ServerStorageVersion**](V1alpha1ServerStorageVersion.md) | [**V1alpha1ServerStorageVersion**](V1alpha1ServerStorageVersion.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

