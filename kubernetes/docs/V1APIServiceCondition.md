# V1APIServiceCondition

APIServiceCondition describes the state of an APIService at a particular point

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | Last time the condition transitioned from one status to another. | [optional] 
**message** | **str** | Human-readable message indicating details about last transition. | [optional] 
**reason** | **str** | Unique, one-word, CamelCase reason for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status is the status of the condition. Can be True, False, Unknown. | 
**type** | **str** | Type is the type of the condition. | 

## Example

```python
from kubernetes.client.models.v1_api_service_condition import V1APIServiceCondition

# TODO update the JSON string below
json = "{}"
# create an instance of V1APIServiceCondition from a JSON string
v1_api_service_condition_instance = V1APIServiceCondition.from_json(json)
# print the JSON string representation of the object
print V1APIServiceCondition.to_json()

# convert the object into a dict
v1_api_service_condition_dict = v1_api_service_condition_instance.to_dict()
# create an instance of V1APIServiceCondition from a dict
v1_api_service_condition_form_dict = v1_api_service_condition.from_dict(v1_api_service_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


