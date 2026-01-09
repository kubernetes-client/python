# V1LeaseSpec

LeaseSpec is a specification of a Lease.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acquire_time** | **datetime** | acquireTime is a time when the current lease was acquired. | [optional] 
**holder_identity** | **str** | holderIdentity contains the identity of the holder of a current lease. If Coordinated Leader Election is used, the holder identity must be equal to the elected LeaseCandidate.metadata.name field. | [optional] 
**lease_duration_seconds** | **int** | leaseDurationSeconds is a duration that candidates for a lease need to wait to force acquire it. This is measured against the time of last observed renewTime. | [optional] 
**lease_transitions** | **int** | leaseTransitions is the number of transitions of a lease between holders. | [optional] 
**preferred_holder** | **str** | PreferredHolder signals to a lease holder that the lease has a more optimal holder and should be given up. This field can only be set if Strategy is also set. | [optional] 
**renew_time** | **datetime** | renewTime is a time when the current holder of a lease has last updated the lease. | [optional] 
**strategy** | **str** | Strategy indicates the strategy for picking the leader for coordinated leader election. If the field is not specified, there is no active coordination for this lease. (Alpha) Using this field requires the CoordinatedLeaderElection feature gate to be enabled. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


