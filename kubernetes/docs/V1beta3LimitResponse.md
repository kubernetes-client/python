# V1beta3LimitResponse

LimitResponse defines how to handle requests that can not be executed right now.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queuing** | [**V1beta3QueuingConfiguration**](V1beta3QueuingConfiguration.md) |  | [optional] 
**type** | **str** | &#x60;type&#x60; is \&quot;Queue\&quot; or \&quot;Reject\&quot;. \&quot;Queue\&quot; means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. \&quot;Reject\&quot; means that requests that can not be executed upon arrival are rejected. Required. | 

## Example

```python
from kubernetes.client.models.v1beta3_limit_response import V1beta3LimitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta3LimitResponse from a JSON string
v1beta3_limit_response_instance = V1beta3LimitResponse.from_json(json)
# print the JSON string representation of the object
print V1beta3LimitResponse.to_json()

# convert the object into a dict
v1beta3_limit_response_dict = v1beta3_limit_response_instance.to_dict()
# create an instance of V1beta3LimitResponse from a dict
v1beta3_limit_response_form_dict = v1beta3_limit_response.from_dict(v1beta3_limit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


