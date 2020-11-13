# EventsV1EventSeries

EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in \"k8s.io/kubernetes.client-go/tools/events/event_broadcaster.go\" shows how this struct is updated on heartbeats and can guide customized reporter implementations.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | count is the number of occurrences in this series up to the last heartbeat time. | 
**last_observed_time** | **datetime** | lastObservedTime is the time when last Event from the series was seen before last heartbeat. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


