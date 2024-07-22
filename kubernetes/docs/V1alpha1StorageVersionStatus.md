# V1alpha1StorageVersionStatus

API server instances report the versions they can decode and the version they encode objects to when persisting objects in the backend.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_encoding_version** | **str** | If all API server instances agree on the same encoding storage version, then this field is set to that version. Otherwise this field is left empty. API servers should finish updating its storageVersionStatus entry before serving write operations, so that this field will be in sync with the reality. | [optional] 
**conditions** | [**List[V1alpha1StorageVersionCondition]**](V1alpha1StorageVersionCondition.md) | The latest available observations of the storageVersion&#39;s state. | [optional] 
**storage_versions** | [**List[V1alpha1ServerStorageVersion]**](V1alpha1ServerStorageVersion.md) | The reported versions per API server instance. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_storage_version_status import V1alpha1StorageVersionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1StorageVersionStatus from a JSON string
v1alpha1_storage_version_status_instance = V1alpha1StorageVersionStatus.from_json(json)
# print the JSON string representation of the object
print V1alpha1StorageVersionStatus.to_json()

# convert the object into a dict
v1alpha1_storage_version_status_dict = v1alpha1_storage_version_status_instance.to_dict()
# create an instance of V1alpha1StorageVersionStatus from a dict
v1alpha1_storage_version_status_form_dict = v1alpha1_storage_version_status.from_dict(v1alpha1_storage_version_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


