# V1alpha1StorageVersionMigrationSpec

Spec of the storage version migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_token** | **str** | The token used in the list options to get the next chunk of objects to migrate. When the .status.conditions indicates the migration is \&quot;Running\&quot;, users can use this token to check the progress of the migration. | [optional] 
**resource** | [**V1alpha1GroupVersionResource**](V1alpha1GroupVersionResource.md) |  | 

## Example

```python
from kubernetes.client.models.v1alpha1_storage_version_migration_spec import V1alpha1StorageVersionMigrationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1StorageVersionMigrationSpec from a JSON string
v1alpha1_storage_version_migration_spec_instance = V1alpha1StorageVersionMigrationSpec.from_json(json)
# print the JSON string representation of the object
print V1alpha1StorageVersionMigrationSpec.to_json()

# convert the object into a dict
v1alpha1_storage_version_migration_spec_dict = v1alpha1_storage_version_migration_spec_instance.to_dict()
# create an instance of V1alpha1StorageVersionMigrationSpec from a dict
v1alpha1_storage_version_migration_spec_form_dict = v1alpha1_storage_version_migration_spec.from_dict(v1alpha1_storage_version_migration_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


