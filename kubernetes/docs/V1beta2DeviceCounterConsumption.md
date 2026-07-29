# V1beta2DeviceCounterConsumption

DeviceCounterConsumption defines a set of counters that a device will consume from a CounterSet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter_set** | **str** | CounterSet is the name of the set from which the counters defined will be consumed. |
**counters** | [**Dict[str, V1beta2Counter]**](V1beta2Counter.md) | Counters defines the counters that will be consumed by the device.  The maximum number of counters is 32. |

## Example

```python
from kubernetes.client.models.v1beta2_device_counter_consumption import V1beta2DeviceCounterConsumption

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceCounterConsumption from a JSON string
v1beta2_device_counter_consumption_instance = V1beta2DeviceCounterConsumption.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceCounterConsumption.to_json())

# convert the object into a dict
v1beta2_device_counter_consumption_dict = v1beta2_device_counter_consumption_instance.to_dict()
# create an instance of V1beta2DeviceCounterConsumption from a dict
v1beta2_device_counter_consumption_from_dict = V1beta2DeviceCounterConsumption.from_dict(v1beta2_device_counter_consumption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
