# V1beta1CertificateSigningRequestCondition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_transition_time** | **datetime** | lastTransitionTime is the time the condition last transitioned from one status to another. If unset, when a new condition type is added or an existing condition&#39;s status is changed, the server defaults this to the current time. | [optional] 
**last_update_time** | **datetime** | timestamp for the last update to this condition | [optional] 
**message** | **str** | human readable message with details about the request state | [optional] 
**reason** | **str** | brief reason for the request state | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. Approved, Denied, and Failed conditions may not be \&quot;False\&quot; or \&quot;Unknown\&quot;. Defaults to \&quot;True\&quot;. If unset, should be treated as \&quot;True\&quot;. | [optional] 
**type** | **str** | type of the condition. Known conditions include \&quot;Approved\&quot;, \&quot;Denied\&quot;, and \&quot;Failed\&quot;. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


