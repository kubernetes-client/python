# V1WatchEvent

Event represents a single event to a watched resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **object** | Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *Status is recommended; other types may make sense    depending on context. | 
**type** | **str** |  | 

## Example

```python
from kubernetes.client.models.v1_watch_event import V1WatchEvent

# TODO update the JSON string below
json = "{}"
# create an instance of V1WatchEvent from a JSON string
v1_watch_event_instance = V1WatchEvent.from_json(json)
# print the JSON string representation of the object
print V1WatchEvent.to_json()

# convert the object into a dict
v1_watch_event_dict = v1_watch_event_instance.to_dict()
# create an instance of V1WatchEvent from a dict
v1_watch_event_form_dict = v1_watch_event.from_dict(v1_watch_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


