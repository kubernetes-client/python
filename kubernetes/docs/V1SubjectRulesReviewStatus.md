# V1SubjectRulesReviewStatus

SubjectRulesReviewStatus contains the result of a rules check. This check can be incomplete depending on the set of authorizers the server is configured with and any errors experienced during evaluation. Because authorization rules are additive, if a rule appears in a list it's safe to assume the subject has that permission, even if that list is incomplete.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**evaluation_error** | **str** | EvaluationError can appear in combination with Rules. It indicates an error occurred during rule evaluation, such as an authorizer that doesn&#39;t support rule evaluation, and that ResourceRules and/or NonResourceRules may be incomplete. | [optional] 
**incomplete** | **bool** | Incomplete is true when the rules returned by this call are incomplete. This is most commonly encountered when an authorizer, such as an external authorizer, doesn&#39;t support rules evaluation. | 
**non_resource_rules** | [**List[V1NonResourceRule]**](V1NonResourceRule.md) | NonResourceRules is the list of actions the subject is allowed to perform on non-resources. The list ordering isn&#39;t significant, may contain duplicates, and possibly be incomplete. | 
**resource_rules** | [**List[V1ResourceRule]**](V1ResourceRule.md) | ResourceRules is the list of actions the subject is allowed to perform on resources. The list ordering isn&#39;t significant, may contain duplicates, and possibly be incomplete. | 

## Example

```python
from kubernetes.client.models.v1_subject_rules_review_status import V1SubjectRulesReviewStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1SubjectRulesReviewStatus from a JSON string
v1_subject_rules_review_status_instance = V1SubjectRulesReviewStatus.from_json(json)
# print the JSON string representation of the object
print V1SubjectRulesReviewStatus.to_json()

# convert the object into a dict
v1_subject_rules_review_status_dict = v1_subject_rules_review_status_instance.to_dict()
# create an instance of V1SubjectRulesReviewStatus from a dict
v1_subject_rules_review_status_form_dict = v1_subject_rules_review_status.from_dict(v1_subject_rules_review_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


