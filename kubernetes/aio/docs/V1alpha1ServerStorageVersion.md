# V1alpha1ServerStorageVersion

An API server instance reports the version it can decode and the version it encodes objects to when persisting objects in the backend.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_server_id** | **str** | apiServerID is the ID of the reporting API server. | 
**decodable_versions** | **list[str]** | decodableVersions are the encoding versions the API server can handle to decode. The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions. | 
**encoding_version** | **str** | encodingVersion the API server encodes the object to when persisting it in the backend (e.g., etcd). | 
**served_versions** | **list[str]** | servedVersions lists all versions the API server can serve. DecodableVersions must include all ServedVersions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


