# V1alpha1ServerStorageVersion

An API server instance reports the version it can decode and the version it encodes objects to when persisting objects in the backend.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_server_id** | **str** | apiServerID is the ID of the reporting API server. |
**decodable_versions** | **List[str]** | decodableVersions are the encoding versions the API server can handle to decode. The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions. |
**encoding_version** | **str** | encodingVersion the API server encodes the object to when persisting it in the backend (e.g., etcd). |
**served_versions** | **List[str]** | servedVersions lists all versions the API server can serve. DecodableVersions must include all ServedVersions. | [optional]

## Example

```python
from kubernetes.client.models.v1alpha1_server_storage_version import V1alpha1ServerStorageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ServerStorageVersion from a JSON string
v1alpha1_server_storage_version_instance = V1alpha1ServerStorageVersion.from_json(json)
# print the JSON string representation of the object
print(V1alpha1ServerStorageVersion.to_json())

# convert the object into a dict
v1alpha1_server_storage_version_dict = v1alpha1_server_storage_version_instance.to_dict()
# create an instance of V1alpha1ServerStorageVersion from a dict
v1alpha1_server_storage_version_from_dict = V1alpha1ServerStorageVersion.from_dict(v1alpha1_server_storage_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
