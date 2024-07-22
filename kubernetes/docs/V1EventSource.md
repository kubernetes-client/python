# V1EventSource

EventSource contains information for an event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | Component from which the event is generated. | [optional] 
**host** | **str** | Node name on which the event is generated. | [optional] 

## Example

```python
from kubernetes.client.models.v1_event_source import V1EventSource

# TODO update the JSON string below
json = "{}"
# create an instance of V1EventSource from a JSON string
v1_event_source_instance = V1EventSource.from_json(json)
# print the JSON string representation of the object
print V1EventSource.to_json()

# convert the object into a dict
v1_event_source_dict = v1_event_source_instance.to_dict()
# create an instance of V1EventSource from a dict
v1_event_source_form_dict = v1_event_source.from_dict(v1_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


