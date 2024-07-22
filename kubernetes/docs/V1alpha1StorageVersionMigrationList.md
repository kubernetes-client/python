# V1alpha1StorageVersionMigrationList

StorageVersionMigrationList is a collection of storage version migrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[V1alpha1StorageVersionMigration]**](V1alpha1StorageVersionMigration.md) | Items is the list of StorageVersionMigration | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_storage_version_migration_list import V1alpha1StorageVersionMigrationList

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1StorageVersionMigrationList from a JSON string
v1alpha1_storage_version_migration_list_instance = V1alpha1StorageVersionMigrationList.from_json(json)
# print the JSON string representation of the object
print V1alpha1StorageVersionMigrationList.to_json()

# convert the object into a dict
v1alpha1_storage_version_migration_list_dict = v1alpha1_storage_version_migration_list_instance.to_dict()
# create an instance of V1alpha1StorageVersionMigrationList from a dict
v1alpha1_storage_version_migration_list_form_dict = v1alpha1_storage_version_migration_list.from_dict(v1alpha1_storage_version_migration_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


