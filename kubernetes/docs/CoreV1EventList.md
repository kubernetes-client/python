# CoreV1EventList

EventList is a list of events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[CoreV1Event]**](CoreV1Event.md) | List of events | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.core_v1_event_list import CoreV1EventList

# TODO update the JSON string below
json = "{}"
# create an instance of CoreV1EventList from a JSON string
core_v1_event_list_instance = CoreV1EventList.from_json(json)
# print the JSON string representation of the object
print CoreV1EventList.to_json()

# convert the object into a dict
core_v1_event_list_dict = core_v1_event_list_instance.to_dict()
# create an instance of CoreV1EventList from a dict
core_v1_event_list_form_dict = core_v1_event_list.from_dict(core_v1_event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


