# V1alpha1StorageVersionMigrationSpec

Spec of the storage version migration.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_token** | **str** | The token used in the list options to get the next chunk of objects to migrate. When the .status.conditions indicates the migration is \&quot;Running\&quot;, users can use this token to check the progress of the migration. | [optional] 
**resource** | [**V1alpha1GroupVersionResource**](V1alpha1GroupVersionResource.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


