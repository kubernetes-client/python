# V1SelfSubjectRulesReviewSpec

SelfSubjectRulesReviewSpec defines the specification for SelfSubjectRulesReview.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** | Namespace to evaluate rules for. Required. | [optional] 

## Example

```python
from kubernetes.client.models.v1_self_subject_rules_review_spec import V1SelfSubjectRulesReviewSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1SelfSubjectRulesReviewSpec from a JSON string
v1_self_subject_rules_review_spec_instance = V1SelfSubjectRulesReviewSpec.from_json(json)
# print the JSON string representation of the object
print V1SelfSubjectRulesReviewSpec.to_json()

# convert the object into a dict
v1_self_subject_rules_review_spec_dict = v1_self_subject_rules_review_spec_instance.to_dict()
# create an instance of V1SelfSubjectRulesReviewSpec from a dict
v1_self_subject_rules_review_spec_form_dict = v1_self_subject_rules_review_spec.from_dict(v1_self_subject_rules_review_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


