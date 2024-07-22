# V1SubjectAccessReviewStatus

SubjectAccessReviewStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** | Allowed is required. True if the action would be allowed, false otherwise. | 
**denied** | **bool** | Denied is optional. True if the action would be denied, otherwise false. If both allowed is false and denied is false, then the authorizer has no opinion on whether to authorize the action. Denied may not be true if Allowed is true. | [optional] 
**evaluation_error** | **str** | EvaluationError is an indication that some error occurred during the authorization check. It is entirely possible to get an error and be able to continue determine authorization status in spite of it. For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request. | [optional] 
**reason** | **str** | Reason is optional.  It indicates why a request was allowed or denied. | [optional] 

## Example

```python
from kubernetes.client.models.v1_subject_access_review_status import V1SubjectAccessReviewStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1SubjectAccessReviewStatus from a JSON string
v1_subject_access_review_status_instance = V1SubjectAccessReviewStatus.from_json(json)
# print the JSON string representation of the object
print V1SubjectAccessReviewStatus.to_json()

# convert the object into a dict
v1_subject_access_review_status_dict = v1_subject_access_review_status_instance.to_dict()
# create an instance of V1SubjectAccessReviewStatus from a dict
v1_subject_access_review_status_form_dict = v1_subject_access_review_status.from_dict(v1_subject_access_review_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


