# V1SelfSubjectRulesReview

SelfSubjectRulesReview enumerates the set of actions the current user can perform within a namespace. The returned list of actions may be incomplete depending on the server's authorization mode, and any errors experienced during the evaluation. SelfSubjectRulesReview should be used by UIs to show/hide actions, or to quickly let an end user reason about their permissions. It should NOT Be used by external systems to drive authorization decisions as this raises confused deputy, cache lifetime/revocation, and correctness concerns. SubjectAccessReview, and LocalAccessReview are the correct way to defer authorization decisions to the API server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1SelfSubjectRulesReviewSpec**](V1SelfSubjectRulesReviewSpec.md) |  | 
**status** | [**V1SubjectRulesReviewStatus**](V1SubjectRulesReviewStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_self_subject_rules_review import V1SelfSubjectRulesReview

# TODO update the JSON string below
json = "{}"
# create an instance of V1SelfSubjectRulesReview from a JSON string
v1_self_subject_rules_review_instance = V1SelfSubjectRulesReview.from_json(json)
# print the JSON string representation of the object
print V1SelfSubjectRulesReview.to_json()

# convert the object into a dict
v1_self_subject_rules_review_dict = v1_self_subject_rules_review_instance.to_dict()
# create an instance of V1SelfSubjectRulesReview from a dict
v1_self_subject_rules_review_form_dict = v1_self_subject_rules_review.from_dict(v1_self_subject_rules_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


