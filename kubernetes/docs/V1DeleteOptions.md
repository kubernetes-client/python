# V1DeleteOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_period_seconds** | **int** | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
**orphan_dependents** | **bool** | Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. | [optional] 
**preconditions** | [**V1Preconditions**](V1Preconditions.md) | Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status will be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


