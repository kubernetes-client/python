# V1beta2CounterSet

CounterSet defines a named set of counters that are available to be used by devices defined in the ResourceSlice.  The counters are not allocatable by themselves, but can be referenced by devices. When a device is allocated, the portion of counters it uses will no longer be available for use by other devices.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counters** | [**dict(str, V1beta2Counter)**](V1beta2Counter.md) | Counters defines the set of counters for this CounterSet The name of each counter must be unique in that set and must be a DNS label.  The maximum number of counters in all sets is 32. | 
**name** | **str** | Name defines the name of the counter set. It must be a DNS label. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


