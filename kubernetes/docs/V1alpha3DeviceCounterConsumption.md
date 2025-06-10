# V1alpha3DeviceCounterConsumption

DeviceCounterConsumption defines a set of counters that a device will consume from a CounterSet.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter_set** | **str** | CounterSet defines the set from which the counters defined will be consumed. | 
**counters** | [**dict(str, V1alpha3Counter)**](V1alpha3Counter.md) | Counters defines the Counter that will be consumed by the device.  The maximum number counters in a device is 32. In addition, the maximum number of all counters in all devices is 1024 (for example, 64 devices with 16 counters each). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


