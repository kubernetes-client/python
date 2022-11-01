# kubernetes.client.model.v1_condition.V1Condition

Condition contains details for one aspect of the current state of this API Resource.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Condition contains details for one aspect of the current state of this API Resource. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**reason** | str,  | str,  | reason contains a programmatic identifier indicating the reason for the condition&#x27;s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. | 
**lastTransitionTime** | str, datetime,  | str,  | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable. | value must conform to RFC-3339 date-time
**message** | str,  | str,  | message is a human readable message indicating details about the transition. This may be an empty string. | 
**type** | str,  | str,  | type of condition in CamelCase or in foo.example.com/CamelCase. | 
**status** | str,  | str,  | status of the condition, one of True, False, Unknown. | 
**observedGeneration** | decimal.Decimal, int,  | decimal.Decimal,  | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

