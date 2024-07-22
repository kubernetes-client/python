# V1SubjectAccessReviewSpec

SubjectAccessReviewSpec is a description of the access request.  Exactly one of ResourceAuthorizationAttributes and NonResourceAuthorizationAttributes must be set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **Dict[str, List[str]]** | Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here. | [optional] 
**groups** | **List[str]** | Groups is the groups you&#39;re testing for. | [optional] 
**non_resource_attributes** | [**V1NonResourceAttributes**](V1NonResourceAttributes.md) |  | [optional] 
**resource_attributes** | [**V1ResourceAttributes**](V1ResourceAttributes.md) |  | [optional] 
**uid** | **str** | UID information about the requesting user. | [optional] 
**user** | **str** | User is the user you&#39;re testing for. If you specify \&quot;User\&quot; but not \&quot;Groups\&quot;, then is it interpreted as \&quot;What if User were not a member of any groups | [optional] 

## Example

```python
from kubernetes.client.models.v1_subject_access_review_spec import V1SubjectAccessReviewSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1SubjectAccessReviewSpec from a JSON string
v1_subject_access_review_spec_instance = V1SubjectAccessReviewSpec.from_json(json)
# print the JSON string representation of the object
print V1SubjectAccessReviewSpec.to_json()

# convert the object into a dict
v1_subject_access_review_spec_dict = v1_subject_access_review_spec_instance.to_dict()
# create an instance of V1SubjectAccessReviewSpec from a dict
v1_subject_access_review_spec_form_dict = v1_subject_access_review_spec.from_dict(v1_subject_access_review_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


