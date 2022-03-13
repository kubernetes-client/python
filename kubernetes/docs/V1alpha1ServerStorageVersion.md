# V1alpha1ServerStorageVersion

An API server instance reports the version it can decode and the version it encodes objects to when persisting objects in the backend.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_server_id** | **str** | The ID of the reporting API server. | [optional] 
**decodable_versions** | **[str]** | The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions. | [optional] 
**encoding_version** | **str** | The API server encodes the object to this version when persisting it in the backend (e.g., etcd). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


