# V1PersistentVolumeClaimCondition

PersistentVolumeClaimCondition contains details about state of pvc
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_probe_time** | **datetime** | lastProbeTime is the time we probed the condition. | [optional] 
**last_transition_time** | **datetime** | lastTransitionTime is the time the condition transitioned from one status to another. | [optional] 
**message** | **str** | message is the human-readable message indicating details about last transition. | [optional] 
**reason** | **str** | reason is a unique, this should be a short, machine understandable string that gives the reason for condition&#39;s last transition. If it reports \&quot;Resizing\&quot; that means the underlying persistent volume is being resized. | [optional] 
**status** | **str** |  | 
**type** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


