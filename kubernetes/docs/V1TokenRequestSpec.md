# V1TokenRequestSpec

TokenRequestSpec contains kubernetes.client provided parameters of a token request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **List[str]** | Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences. | 
**bound_object_ref** | [**V1BoundObjectReference**](V1BoundObjectReference.md) |  | [optional] 
**expiration_seconds** | **int** | ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a kubernetes.client needs to check the &#39;expiration&#39; field in a response. | [optional] 

## Example

```python
from kubernetes.client.models.v1_token_request_spec import V1TokenRequestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1TokenRequestSpec from a JSON string
v1_token_request_spec_instance = V1TokenRequestSpec.from_json(json)
# print the JSON string representation of the object
print V1TokenRequestSpec.to_json()

# convert the object into a dict
v1_token_request_spec_dict = v1_token_request_spec_instance.to_dict()
# create an instance of V1TokenRequestSpec from a dict
v1_token_request_spec_form_dict = v1_token_request_spec.from_dict(v1_token_request_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


