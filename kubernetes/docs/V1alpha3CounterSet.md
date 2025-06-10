# V1alpha3CounterSet

CounterSet defines a named set of counters that are available to be used by devices defined in the ResourceSlice.  The counters are not allocatable by themselves, but can be referenced by devices. When a device is allocated, the portion of counters it uses will no longer be available for use by other devices.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counters** | [**dict(str, V1alpha3Counter)**](V1alpha3Counter.md) | Counters defines the counters that will be consumed by the device. The name of each counter must be unique in that set and must be a DNS label.  To ensure this uniqueness, capacities defined by the vendor must be listed without the driver name as domain prefix in their name. All others must be listed with their domain prefix.  The maximum number of counters is 32. | 
**name** | **str** | CounterSet is the name of the set from which the counters defined will be consumed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


