# kubernetes.client.model.v1beta1_flow_schema_spec.V1beta1FlowSchemaSpec

FlowSchemaSpec describes how the FlowSchema's specification looks like.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | FlowSchemaSpec describes how the FlowSchema&#x27;s specification looks like. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**priorityLevelConfiguration** | [**V1beta1PriorityLevelConfigurationReference**](V1beta1PriorityLevelConfigurationReference.md) | [**V1beta1PriorityLevelConfigurationReference**](V1beta1PriorityLevelConfigurationReference.md) |  | 
**distinguisherMethod** | [**V1beta1FlowDistinguisherMethod**](V1beta1FlowDistinguisherMethod.md) | [**V1beta1FlowDistinguisherMethod**](V1beta1FlowDistinguisherMethod.md) |  | [optional] 
**matchingPrecedence** | decimal.Decimal, int,  | decimal.Decimal,  | &#x60;matchingPrecedence&#x60; is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence.  Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default. | [optional] value must be a 32 bit integer
**[rules](#rules)** | list, tuple,  | tuple,  | &#x60;rules&#x60; describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# rules

`rules` describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | &#x60;rules&#x60; describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1beta1PolicyRulesWithSubjects**](V1beta1PolicyRulesWithSubjects.md) | [**V1beta1PolicyRulesWithSubjects**](V1beta1PolicyRulesWithSubjects.md) | [**V1beta1PolicyRulesWithSubjects**](V1beta1PolicyRulesWithSubjects.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

