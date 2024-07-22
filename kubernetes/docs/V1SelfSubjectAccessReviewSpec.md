# V1SelfSubjectAccessReviewSpec

SelfSubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_resource_attributes** | [**V1NonResourceAttributes**](V1NonResourceAttributes.md) |  | [optional] 
**resource_attributes** | [**V1ResourceAttributes**](V1ResourceAttributes.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_self_subject_access_review_spec import V1SelfSubjectAccessReviewSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1SelfSubjectAccessReviewSpec from a JSON string
v1_self_subject_access_review_spec_instance = V1SelfSubjectAccessReviewSpec.from_json(json)
# print the JSON string representation of the object
print V1SelfSubjectAccessReviewSpec.to_json()

# convert the object into a dict
v1_self_subject_access_review_spec_dict = v1_self_subject_access_review_spec_instance.to_dict()
# create an instance of V1SelfSubjectAccessReviewSpec from a dict
v1_self_subject_access_review_spec_form_dict = v1_self_subject_access_review_spec.from_dict(v1_self_subject_access_review_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


