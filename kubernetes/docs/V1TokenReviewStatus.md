# V1TokenReviewStatus

TokenReviewStatus is the result of the token authentication request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **List[str]** | Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token&#39;s audiences. A kubernetes.client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is \&quot;true\&quot;, the token is valid against the audience of the Kubernetes API server. | [optional] 
**authenticated** | **bool** | Authenticated indicates that the token was associated with a known user. | [optional] 
**error** | **str** | Error indicates that the token couldn&#39;t be checked | [optional] 
**user** | [**V1UserInfo**](V1UserInfo.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_token_review_status import V1TokenReviewStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1TokenReviewStatus from a JSON string
v1_token_review_status_instance = V1TokenReviewStatus.from_json(json)
# print the JSON string representation of the object
print V1TokenReviewStatus.to_json()

# convert the object into a dict
v1_token_review_status_dict = v1_token_review_status_instance.to_dict()
# create an instance of V1TokenReviewStatus from a dict
v1_token_review_status_form_dict = v1_token_review_status.from_dict(v1_token_review_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


