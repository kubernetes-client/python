# V1beta1StorageVersionMigrationSpec

Spec of the storage version migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**V1GroupResource**](V1GroupResource.md) |  |

## Example

```python
from kubernetes.client.models.v1beta1_storage_version_migration_spec import V1beta1StorageVersionMigrationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1StorageVersionMigrationSpec from a JSON string
v1beta1_storage_version_migration_spec_instance = V1beta1StorageVersionMigrationSpec.from_json(json)
# print the JSON string representation of the object
print(V1beta1StorageVersionMigrationSpec.to_json())

# convert the object into a dict
v1beta1_storage_version_migration_spec_dict = v1beta1_storage_version_migration_spec_instance.to_dict()
# create an instance of V1beta1StorageVersionMigrationSpec from a dict
v1beta1_storage_version_migration_spec_from_dict = V1beta1StorageVersionMigrationSpec.from_dict(v1beta1_storage_version_migration_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
