# V1LimitResponse

LimitResponse defines how to handle requests that can not be executed right now.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queuing** | [**V1QueuingConfiguration**](V1QueuingConfiguration.md) |  | [optional] 
**type** | **str** | &#x60;type&#x60; is \&quot;Queue\&quot; or \&quot;Reject\&quot;. \&quot;Queue\&quot; means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. \&quot;Reject\&quot; means that requests that can not be executed upon arrival are rejected. Required. | 

## Example

```python
from kubernetes.client.models.v1_limit_response import V1LimitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V1LimitResponse from a JSON string
v1_limit_response_instance = V1LimitResponse.from_json(json)
# print the JSON string representation of the object
print V1LimitResponse.to_json()

# convert the object into a dict
v1_limit_response_dict = v1_limit_response_instance.to_dict()
# create an instance of V1LimitResponse from a dict
v1_limit_response_form_dict = v1_limit_response.from_dict(v1_limit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


