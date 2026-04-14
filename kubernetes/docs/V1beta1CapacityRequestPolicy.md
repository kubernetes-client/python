# V1beta1CapacityRequestPolicy

CapacityRequestPolicy defines how requests consume device capacity.  Must not set more than one ValidRequestValues.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Default specifies how much of this capacity is consumed by a request that does not contain an entry for it in DeviceRequest&#39;s Capacity. | [optional] 
**valid_range** | [**V1beta1CapacityRequestPolicyRange**](V1beta1CapacityRequestPolicyRange.md) |  | [optional] 
**valid_values** | **list[str]** | ValidValues defines a set of acceptable quantity values in consuming requests.  Must not contain more than 10 entries. Must be sorted in ascending order.  If this field is set, Default must be defined and it must be included in ValidValues list.  If the requested amount does not match any valid value but smaller than some valid values, the scheduler calculates the smallest valid value that is greater than or equal to the request. That is: min(ceil(requestedValue) ∈ validValues), where requestedValue ≤ max(validValues).  If the requested amount exceeds all valid values, the request violates the policy, and this device cannot be allocated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


