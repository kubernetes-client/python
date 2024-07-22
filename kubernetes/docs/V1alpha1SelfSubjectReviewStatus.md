# V1alpha1SelfSubjectReviewStatus

SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_info** | [**V1UserInfo**](V1UserInfo.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_self_subject_review_status import V1alpha1SelfSubjectReviewStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1SelfSubjectReviewStatus from a JSON string
v1alpha1_self_subject_review_status_instance = V1alpha1SelfSubjectReviewStatus.from_json(json)
# print the JSON string representation of the object
print V1alpha1SelfSubjectReviewStatus.to_json()

# convert the object into a dict
v1alpha1_self_subject_review_status_dict = v1alpha1_self_subject_review_status_instance.to_dict()
# create an instance of V1alpha1SelfSubjectReviewStatus from a dict
v1alpha1_self_subject_review_status_form_dict = v1alpha1_self_subject_review_status.from_dict(v1alpha1_self_subject_review_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


