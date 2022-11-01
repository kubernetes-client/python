# kubernetes.client.model.v1alpha1_storage_version_condition.V1alpha1StorageVersionCondition

Describes the state of the storageVersion at a certain point.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Describes the state of the storageVersion at a certain point. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**reason** | str,  | str,  | The reason for the condition&#x27;s last transition. | 
**type** | str,  | str,  | Type of the condition. | 
**status** | str,  | str,  | Status of the condition, one of True, False, Unknown. | 
**lastTransitionTime** | str, datetime,  | str,  | Last time the condition transitioned from one status to another. | [optional] value must conform to RFC-3339 date-time
**message** | str,  | str,  | A human readable message indicating details about the transition. | [optional] 
**observedGeneration** | decimal.Decimal, int,  | decimal.Decimal,  | If set, this represents the .metadata.generation that the condition was set based upon. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

