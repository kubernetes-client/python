# kubernetes.client.model.v1_component_condition.V1ComponentCondition

Information about the condition of a component.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the condition of a component. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Type of condition for a component. Valid value: \&quot;Healthy\&quot; | 
**status** | str,  | str,  | Status of the condition for a component. Valid values for \&quot;Healthy\&quot;: \&quot;True\&quot;, \&quot;False\&quot;, or \&quot;Unknown\&quot;. | 
**error** | str,  | str,  | Condition error code for a component. For example, a health check error code. | [optional] 
**message** | str,  | str,  | Message about the condition for a component. For example, information about a health check. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

