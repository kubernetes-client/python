# EventsV1EventList

EventList is a list of Event objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[EventsV1Event]**](EventsV1Event.md) | items is a list of schema objects. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.events_v1_event_list import EventsV1EventList

# TODO update the JSON string below
json = "{}"
# create an instance of EventsV1EventList from a JSON string
events_v1_event_list_instance = EventsV1EventList.from_json(json)
# print the JSON string representation of the object
print EventsV1EventList.to_json()

# convert the object into a dict
events_v1_event_list_dict = events_v1_event_list_instance.to_dict()
# create an instance of EventsV1EventList from a dict
events_v1_event_list_form_dict = events_v1_event_list.from_dict(events_v1_event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


