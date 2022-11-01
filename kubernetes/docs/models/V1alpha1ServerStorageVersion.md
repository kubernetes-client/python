# kubernetes.client.model.v1alpha1_server_storage_version.V1alpha1ServerStorageVersion

An API server instance reports the version it can decode and the version it encodes objects to when persisting objects in the backend.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An API server instance reports the version it can decode and the version it encodes objects to when persisting objects in the backend. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**apiServerID** | str,  | str,  | The ID of the reporting API server. | [optional] 
**[decodableVersions](#decodableVersions)** | list, tuple,  | tuple,  | The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions. | [optional] 
**encodingVersion** | str,  | str,  | The API server encodes the object to this version when persisting it in the backend (e.g., etcd). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# decodableVersions

The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

