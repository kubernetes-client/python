# V1beta2CounterSet

CounterSet defines a named set of counters that are available to be used by devices defined in the ResourcePool.  The counters are not allocatable by themselves, but can be referenced by devices. When a device is allocated, the portion of counters it uses will no longer be available for use by other devices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counters** | [**Dict[str, V1beta2Counter]**](V1beta2Counter.md) | Counters defines the set of counters for this CounterSet The name of each counter must be unique in that set and must be a DNS label.  The maximum number of counters is 32. |
**name** | **str** | Name defines the name of the counter set. It must be a DNS label. |

## Example

```python
from kubernetes.client.models.v1beta2_counter_set import V1beta2CounterSet

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2CounterSet from a JSON string
v1beta2_counter_set_instance = V1beta2CounterSet.from_json(json)
# print the JSON string representation of the object
print(V1beta2CounterSet.to_json())

# convert the object into a dict
v1beta2_counter_set_dict = v1beta2_counter_set_instance.to_dict()
# create an instance of V1beta2CounterSet from a dict
v1beta2_counter_set_from_dict = V1beta2CounterSet.from_dict(v1beta2_counter_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
