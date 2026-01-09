# V1beta2CapacityRequirements

CapacityRequirements defines the capacity requirements for a specific device request.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | **dict(str, str)** | Requests represent individual device resource requests for distinct resources, all of which must be provided by the device.  This value is used as an additional filtering condition against the available capacity on the device. This is semantically equivalent to a CEL selector with &#x60;device.capacity[&lt;domain&gt;].&lt;name&gt;.compareTo(quantity(&lt;request quantity&gt;)) &gt;&#x3D; 0&#x60;. For example, device.capacity[&#39;test-driver.cdi.k8s.io&#39;].counters.compareTo(quantity(&#39;2&#39;)) &gt;&#x3D; 0.  When a requestPolicy is defined, the requested amount is adjusted upward to the nearest valid value based on the policy. If the requested amount cannot be adjusted to a valid value—because it exceeds what the requestPolicy allows— the device is considered ineligible for allocation.  For any capacity that is not explicitly requested: - If no requestPolicy is set, the default consumed capacity is equal to the full device capacity   (i.e., the whole device is claimed). - If a requestPolicy is set, the default consumed capacity is determined according to that policy.  If the device allows multiple allocation, the aggregated amount across all requests must not exceed the capacity value. The consumed capacity, which may be adjusted based on the requestPolicy if defined, is recorded in the resource claim’s status.devices[*].consumedCapacity field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


