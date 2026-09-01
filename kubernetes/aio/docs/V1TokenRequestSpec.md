# V1TokenRequestSpec

TokenRequestSpec contains client provided parameters of a token request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestations** | **Dict[str, List[str]]** | attestations is a map of well-known keys to string-slice values. The values for each key have a specific semantic meaning, which is documented on the key definition. Requesters of tokens may ask the Kubernetes API Server to attest to certain claims. The API Server may perform authorization checks depending on the key of this map. | [optional]
**audiences** | **List[str]** | audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences. | [optional]
**bound_object_ref** | [**V1BoundObjectReference**](V1BoundObjectReference.md) |  | [optional]
**expiration_seconds** | **int** | expirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the &#39;expiration&#39; field in a response. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1_token_request_spec import V1TokenRequestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1TokenRequestSpec from a JSON string
v1_token_request_spec_instance = V1TokenRequestSpec.from_json(json)
# print the JSON string representation of the object
print(V1TokenRequestSpec.to_json())

# convert the object into a dict
v1_token_request_spec_dict = v1_token_request_spec_instance.to_dict()
# create an instance of V1TokenRequestSpec from a dict
v1_token_request_spec_from_dict = V1TokenRequestSpec.from_dict(v1_token_request_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
