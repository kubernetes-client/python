# V1SubjectRulesReviewStatus

SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it's safe to assume the subject has that permission, even if that list is incomplete.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**incomplete** | **bool** | Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn&#39;t support rules evaluation. | 
**non_resource_rules** | [**[V1NonResourceRule]**](V1NonResourceRule.md) | NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn&#39;t significant, may contain duplicates, and possibly be incomplete. | 
**resource_rules** | [**[V1ResourceRule]**](V1ResourceRule.md) | ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn&#39;t significant, may contain duplicates, and possibly be incomplete. | 
**evaluation_error** | **str** | EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn&#39;t support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


