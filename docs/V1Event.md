# V1Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of times this event has occurred. | [optional] 
**first_timestamp** | [**UnversionedTime**](UnversionedTime.md) | The time at which the event was first recorded. (Time of server receipt is in TypeMeta.) | [optional] 
**involved_object** | [**V1ObjectReference**](V1ObjectReference.md) | The object that this event is about. | 
**last_timestamp** | [**UnversionedTime**](UnversionedTime.md) | The time at which the most recent occurrence of this event was recorded. | [optional] 
**message** | **str** | A human-readable description of the status of this operation. | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata | 
**reason** | **str** | This should be a short, machine understandable string that gives the reason for the transition into the object&#39;s current status. | [optional] 
**source** | [**V1EventSource**](V1EventSource.md) | The component reporting this event. Should be a short machine understandable string. | [optional] 
**type** | **str** | Type of this event (Normal, Warning), new types could be added in the future | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


