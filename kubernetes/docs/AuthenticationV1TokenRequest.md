# AuthenticationV1TokenRequest

TokenRequest requests a token for a given service account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1TokenRequestSpec**](V1TokenRequestSpec.md) |  | 
**status** | [**V1TokenRequestStatus**](V1TokenRequestStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.authentication_v1_token_request import AuthenticationV1TokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationV1TokenRequest from a JSON string
authentication_v1_token_request_instance = AuthenticationV1TokenRequest.from_json(json)
# print the JSON string representation of the object
print AuthenticationV1TokenRequest.to_json()

# convert the object into a dict
authentication_v1_token_request_dict = authentication_v1_token_request_instance.to_dict()
# create an instance of AuthenticationV1TokenRequest from a dict
authentication_v1_token_request_form_dict = authentication_v1_token_request.from_dict(authentication_v1_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


