# kubernetes.client.model.v1_subject_rules_review_status.V1SubjectRulesReviewStatus

SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it's safe to assume the subject has that permission, even if that list is incomplete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it&#x27;s safe to assume the subject has that permission, even if that list is incomplete. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**incomplete** | bool,  | BoolClass,  | Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn&#x27;t support rules evaluation. | 
**[nonResourceRules](#nonResourceRules)** | list, tuple,  | tuple,  | NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn&#x27;t significant, may contain duplicates, and possibly be incomplete. | 
**[resourceRules](#resourceRules)** | list, tuple,  | tuple,  | ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn&#x27;t significant, may contain duplicates, and possibly be incomplete. | 
**evaluationError** | str,  | str,  | EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn&#x27;t support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# nonResourceRules

NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn&#x27;t significant, may contain duplicates, and possibly be incomplete. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1NonResourceRule**](V1NonResourceRule.md) | [**V1NonResourceRule**](V1NonResourceRule.md) | [**V1NonResourceRule**](V1NonResourceRule.md) |  | 

# resourceRules

ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn't significant, may contain duplicates, and possibly be incomplete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn&#x27;t significant, may contain duplicates, and possibly be incomplete. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1ResourceRule**](V1ResourceRule.md) | [**V1ResourceRule**](V1ResourceRule.md) | [**V1ResourceRule**](V1ResourceRule.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

