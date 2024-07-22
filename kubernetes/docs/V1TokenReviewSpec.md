# V1TokenReviewSpec

TokenReviewSpec is a description of the token authentication request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **List[str]** | Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver. | [optional] 
**token** | **str** | Token is the opaque bearer token. | [optional] 

## Example

```python
from kubernetes.client.models.v1_token_review_spec import V1TokenReviewSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1TokenReviewSpec from a JSON string
v1_token_review_spec_instance = V1TokenReviewSpec.from_json(json)
# print the JSON string representation of the object
print V1TokenReviewSpec.to_json()

# convert the object into a dict
v1_token_review_spec_dict = v1_token_review_spec_instance.to_dict()
# create an instance of V1TokenReviewSpec from a dict
v1_token_review_spec_form_dict = v1_token_review_spec.from_dict(v1_token_review_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


