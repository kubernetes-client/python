# StorageV1TokenRequest

TokenRequest contains parameters of a service account token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** | audience is the intended audience of the token in \&quot;TokenRequestSpec\&quot;. It will default to the audiences of kube apiserver. | 
**expiration_seconds** | **int** | expirationSeconds is the duration of validity of the token in \&quot;TokenRequestSpec\&quot;. It has the same default value of \&quot;ExpirationSeconds\&quot; in \&quot;TokenRequestSpec\&quot;. | [optional] 

## Example

```python
from kubernetes.client.models.storage_v1_token_request import StorageV1TokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StorageV1TokenRequest from a JSON string
storage_v1_token_request_instance = StorageV1TokenRequest.from_json(json)
# print the JSON string representation of the object
print StorageV1TokenRequest.to_json()

# convert the object into a dict
storage_v1_token_request_dict = storage_v1_token_request_instance.to_dict()
# create an instance of StorageV1TokenRequest from a dict
storage_v1_token_request_form_dict = storage_v1_token_request.from_dict(storage_v1_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


