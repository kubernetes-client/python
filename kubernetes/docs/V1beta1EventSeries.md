# V1beta1EventSeries

EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of occurrences in this series up to the last heartbeat time | 
**last_observed_time** | **datetime** | Time when last Event from the series was seen before last heartbeat. | 
**state** | **str** | Information whether this series is ongoing or finished. Deprecated. Planned removal for 1.18 | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


