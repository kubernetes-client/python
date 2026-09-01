# V1DeviceCounterConsumption

DeviceCounterConsumption defines a set of counters that a device will consume from a CounterSet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compatibility_groups** | **List[str]** | CompatibilityGroups is a list of opaque group names for this counter set consumption.  Devices that consume counters from the same counter set may only be allocated at the same time (\&quot;co-allocated\&quot;) if they all share at least one common group: the intersection of the CompatibilityGroups of all co-allocated devices on that counter set must be non-empty. Devices that consume from different counter sets are never compared via this field.  An unset field, an explicit nil, and an empty list are equivalent and mean \&quot;no groups\&quot;: such a device is only co-allocatable with sibling devices on the same counter set that also have no groups, and is never co-allocatable with a device that declares one or more groups.  Group names are opaque and meaningful only within the publishing driver&#39;s pool.  The maximum number of groups is 2, and the names must be unique. | [optional]
**counter_set** | **str** | CounterSet is the name of the set from which the counters defined will be consumed. |
**counters** | [**Dict[str, V1Counter]**](V1Counter.md) | Counters defines the counters that will be consumed by the device.  The maximum number of counters is 32. |

## Example

```python
from kubernetes.aio.client.models.v1_device_counter_consumption import V1DeviceCounterConsumption

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceCounterConsumption from a JSON string
v1_device_counter_consumption_instance = V1DeviceCounterConsumption.from_json(json)
# print the JSON string representation of the object
print(V1DeviceCounterConsumption.to_json())

# convert the object into a dict
v1_device_counter_consumption_dict = v1_device_counter_consumption_instance.to_dict()
# create an instance of V1DeviceCounterConsumption from a dict
v1_device_counter_consumption_from_dict = V1DeviceCounterConsumption.from_dict(v1_device_counter_consumption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
