# kubernetes.client.model.core_v1_event.CoreV1Event

Event is a report of an event somewhere in the cluster.  Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Event is a report of an event somewhere in the cluster.  Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | [**V1ObjectMeta**](V1ObjectMeta.md) |  | 
**involvedObject** | [**V1ObjectReference**](V1ObjectReference.md) | [**V1ObjectReference**](V1ObjectReference.md) |  | 
**action** | str,  | str,  | What action was taken/failed regarding to the Regarding object. | [optional] 
**apiVersion** | str,  | str,  | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of times this event has occurred. | [optional] value must be a 32 bit integer
**eventTime** | str, datetime,  | str,  | Time when this Event was first observed. | [optional] value must conform to RFC-3339 date-time
**firstTimestamp** | str, datetime,  | str,  | The time at which the event was first recorded. (Time of server receipt is in TypeMeta.) | [optional] value must conform to RFC-3339 date-time
**kind** | str,  | str,  | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**lastTimestamp** | str, datetime,  | str,  | The time at which the most recent occurrence of this event was recorded. | [optional] value must conform to RFC-3339 date-time
**message** | str,  | str,  | A human-readable description of the status of this operation. | [optional] 
**reason** | str,  | str,  | This should be a short, machine understandable string that gives the reason for the transition into the object&#x27;s current status. | [optional] 
**related** | [**V1ObjectReference**](V1ObjectReference.md) | [**V1ObjectReference**](V1ObjectReference.md) |  | [optional] 
**reportingComponent** | str,  | str,  | Name of the controller that emitted this Event, e.g. &#x60;kubernetes.io/kubelet&#x60;. | [optional] 
**reportingInstance** | str,  | str,  | ID of the controller instance, e.g. &#x60;kubelet-xyzf&#x60;. | [optional] 
**series** | [**CoreV1EventSeries**](CoreV1EventSeries.md) | [**CoreV1EventSeries**](CoreV1EventSeries.md) |  | [optional] 
**source** | [**V1EventSource**](V1EventSource.md) | [**V1EventSource**](V1EventSource.md) |  | [optional] 
**type** | str,  | str,  | Type of this event (Normal, Warning), new types could be added in the future | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

