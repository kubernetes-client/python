# V1SelfSubjectAccessReview

SelfSubjectAccessReview checks whether or the current user can perform an action.  Not filling in a spec.namespace means \"in all namespaces\".  Self is a special case, because users should always be able to check whether they can perform an action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1SelfSubjectAccessReviewSpec**](V1SelfSubjectAccessReviewSpec.md) |  | 
**status** | [**V1SubjectAccessReviewStatus**](V1SubjectAccessReviewStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_self_subject_access_review import V1SelfSubjectAccessReview

# TODO update the JSON string below
json = "{}"
# create an instance of V1SelfSubjectAccessReview from a JSON string
v1_self_subject_access_review_instance = V1SelfSubjectAccessReview.from_json(json)
# print the JSON string representation of the object
print V1SelfSubjectAccessReview.to_json()

# convert the object into a dict
v1_self_subject_access_review_dict = v1_self_subject_access_review_instance.to_dict()
# create an instance of V1SelfSubjectAccessReview from a dict
v1_self_subject_access_review_form_dict = v1_self_subject_access_review.from_dict(v1_self_subject_access_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


