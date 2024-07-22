# V1alpha1StorageVersionMigrationStatus

Status of the storage version migration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1alpha1MigrationCondition]**](V1alpha1MigrationCondition.md) | The latest available observations of the migration&#39;s current state. | [optional] 
**resource_version** | **str** | ResourceVersion to compare with the GC cache for performing the migration. This is the current resource version of given group, version and resource when kube-controller-manager first observes this StorageVersionMigration resource. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_storage_version_migration_status import V1alpha1StorageVersionMigrationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1StorageVersionMigrationStatus from a JSON string
v1alpha1_storage_version_migration_status_instance = V1alpha1StorageVersionMigrationStatus.from_json(json)
# print the JSON string representation of the object
print V1alpha1StorageVersionMigrationStatus.to_json()

# convert the object into a dict
v1alpha1_storage_version_migration_status_dict = v1alpha1_storage_version_migration_status_instance.to_dict()
# create an instance of V1alpha1StorageVersionMigrationStatus from a dict
v1alpha1_storage_version_migration_status_form_dict = v1alpha1_storage_version_migration_status.from_dict(v1alpha1_storage_version_migration_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


