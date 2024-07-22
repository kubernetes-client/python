# CoreV1EventSeries

EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of occurrences in this series up to the last heartbeat time | [optional] 
**last_observed_time** | **datetime** | Time of the last occurrence observed | [optional] 

## Example

```python
from kubernetes.client.models.core_v1_event_series import CoreV1EventSeries

# TODO update the JSON string below
json = "{}"
# create an instance of CoreV1EventSeries from a JSON string
core_v1_event_series_instance = CoreV1EventSeries.from_json(json)
# print the JSON string representation of the object
print CoreV1EventSeries.to_json()

# convert the object into a dict
core_v1_event_series_dict = core_v1_event_series_instance.to_dict()
# create an instance of CoreV1EventSeries from a dict
core_v1_event_series_form_dict = core_v1_event_series.from_dict(core_v1_event_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


