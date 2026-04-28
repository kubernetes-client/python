# V1alpha2LeaseCandidateSpec

LeaseCandidateSpec is a specification of a Lease.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_version** | **str** | BinaryVersion is the binary version. It must be in a semver format without leading &#x60;v&#x60;. This field is required. | 
**emulation_version** | **str** | EmulationVersion is the emulation version. It must be in a semver format without leading &#x60;v&#x60;. EmulationVersion must be less than or equal to BinaryVersion. This field is required when strategy is \&quot;OldestEmulationVersion\&quot; | [optional] 
**lease_name** | **str** | LeaseName is the name of the lease for which this candidate is contending. This field is immutable. | 
**ping_time** | **datetime** | PingTime is the last time that the server has requested the LeaseCandidate to renew. It is only done during leader election to check if any LeaseCandidates have become ineligible. When PingTime is updated, the LeaseCandidate will respond by updating RenewTime. | [optional] 
**renew_time** | **datetime** | RenewTime is the time that the LeaseCandidate was last updated. Any time a Lease needs to do leader election, the PingTime field is updated to signal to the LeaseCandidate that they should update the RenewTime. Old LeaseCandidate objects are also garbage collected if it has been hours since the last renew. The PingTime field is updated regularly to prevent garbage collection for still active LeaseCandidates. | [optional] 
**strategy** | **str** | Strategy is the strategy that coordinated leader election will use for picking the leader. If multiple candidates for the same Lease return different strategies, the strategy provided by the candidate with the latest BinaryVersion will be used. If there is still conflict, this is a user error and coordinated leader election will not operate the Lease until resolved. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


