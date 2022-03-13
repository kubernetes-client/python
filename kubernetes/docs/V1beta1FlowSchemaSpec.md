# V1beta1FlowSchemaSpec

FlowSchemaSpec describes how the FlowSchema's specification looks like.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority_level_configuration** | [**V1beta1PriorityLevelConfigurationReference**](V1beta1PriorityLevelConfigurationReference.md) |  | 
**distinguisher_method** | [**V1beta1FlowDistinguisherMethod**](V1beta1FlowDistinguisherMethod.md) |  | [optional] 
**matching_precedence** | **int** | &#x60;matchingPrecedence&#x60; is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence.  Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default. | [optional] 
**rules** | [**[V1beta1PolicyRulesWithSubjects]**](V1beta1PolicyRulesWithSubjects.md) | &#x60;rules&#x60; describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


