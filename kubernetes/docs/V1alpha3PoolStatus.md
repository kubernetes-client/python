# V1alpha3PoolStatus

PoolStatus contains status information for a single resource pool.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_devices** | **int** | AllocatedDevices is the number of devices currently allocated to claims. A value of 0 means no devices are allocated. May be unset when validationError is set. | [optional] 
**available_devices** | **int** | AvailableDevices is the number of devices available for allocation. This equals TotalDevices - AllocatedDevices - UnavailableDevices. A value of 0 means no devices are currently available. May be unset when validationError is set. | [optional] 
**driver** | **str** | Driver is the DRA driver name for this pool. Must be a DNS subdomain (e.g., \&quot;gpu.example.com\&quot;). | 
**generation** | **int** | Generation is the pool generation observed across all ResourceSlices in this pool. Only the latest generation is reported. During a generation rollout, if not all slices at the latest generation have been published, the pool is included with a validationError and device counts unset. | 
**node_name** | **str** | NodeName is the node this pool is associated with. When omitted, the pool is not associated with a specific node. Must be a valid DNS subdomain name (RFC1123). | [optional] 
**pool_name** | **str** | PoolName is the name of the pool. Must be a valid resource pool name (DNS subdomains separated by \&quot;/\&quot;). | 
**resource_slice_count** | **int** | ResourceSliceCount is the number of ResourceSlices that make up this pool. May be unset when validationError is set. | [optional] 
**total_devices** | **int** | TotalDevices is the total number of devices in the pool across all slices. A value of 0 means the pool has no devices. May be unset when validationError is set. | [optional] 
**unavailable_devices** | **int** | UnavailableDevices is the number of devices that are not available due to taints or other conditions, but are not allocated. A value of 0 means all unallocated devices are available. May be unset when validationError is set. | [optional] 
**validation_error** | **str** | ValidationError is set when the pool&#39;s data could not be fully validated (e.g., incomplete slice publication). When set, device count fields and ResourceSliceCount may be unset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


