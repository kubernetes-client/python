# V1alpha1ServerStorageVersion

An API server instance reports the version it can decode and the version it encodes objects to when persisting objects in the backend.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_server_id** | **str** | The ID of the reporting API server. | [optional] 
**decodable_versions** | **List[str]** | The API server can decode objects encoded in these versions. The encodingVersion must be included in the decodableVersions. | [optional] 
**encoding_version** | **str** | The API server encodes the object to this version when persisting it in the backend (e.g., etcd). | [optional] 
**served_versions** | **List[str]** | The API server can serve these versions. DecodableVersions must include all ServedVersions. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_server_storage_version import V1alpha1ServerStorageVersion

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ServerStorageVersion from a JSON string
v1alpha1_server_storage_version_instance = V1alpha1ServerStorageVersion.from_json(json)
# print the JSON string representation of the object
print V1alpha1ServerStorageVersion.to_json()

# convert the object into a dict
v1alpha1_server_storage_version_dict = v1alpha1_server_storage_version_instance.to_dict()
# create an instance of V1alpha1ServerStorageVersion from a dict
v1alpha1_server_storage_version_form_dict = v1alpha1_server_storage_version.from_dict(v1alpha1_server_storage_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


