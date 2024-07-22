# V1TokenReview

TokenReview attempts to authenticate a token to a known user. Note: TokenReview requests may be cached by the webhook token authenticator plugin in the kube-apiserver.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1TokenReviewSpec**](V1TokenReviewSpec.md) |  | 
**status** | [**V1TokenReviewStatus**](V1TokenReviewStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_token_review import V1TokenReview

# TODO update the JSON string below
json = "{}"
# create an instance of V1TokenReview from a JSON string
v1_token_review_instance = V1TokenReview.from_json(json)
# print the JSON string representation of the object
print V1TokenReview.to_json()

# convert the object into a dict
v1_token_review_dict = v1_token_review_instance.to_dict()
# create an instance of V1TokenReview from a dict
v1_token_review_form_dict = v1_token_review.from_dict(v1_token_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


