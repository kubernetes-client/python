# V1TokenRequestStatus

TokenRequestStatus is the result of a token request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiration_timestamp** | **datetime** | ExpirationTimestamp is the time of expiration of the returned token. | 
**token** | **str** | Token is the opaque bearer token. | 

## Example

```python
from kubernetes.client.models.v1_token_request_status import V1TokenRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1TokenRequestStatus from a JSON string
v1_token_request_status_instance = V1TokenRequestStatus.from_json(json)
# print the JSON string representation of the object
print V1TokenRequestStatus.to_json()

# convert the object into a dict
v1_token_request_status_dict = v1_token_request_status_instance.to_dict()
# create an instance of V1TokenRequestStatus from a dict
v1_token_request_status_form_dict = v1_token_request_status.from_dict(v1_token_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


