# V1beta2DeviceAllocationResult

DeviceAllocationResult is the result of allocating devices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[V1beta2DeviceAllocationConfiguration]**](V1beta2DeviceAllocationConfiguration.md) | This field is a combination of all the claim and class configuration parameters. Drivers can distinguish between those based on a flag.  This includes configuration parameters for drivers which have no allocated devices in the result because it is up to the drivers which configuration parameters they support. They can silently ignore unknown configuration parameters. | [optional]
**results** | [**List[V1beta2DeviceRequestAllocationResult]**](V1beta2DeviceRequestAllocationResult.md) | Results lists all allocated devices. | [optional]

## Example

```python
from kubernetes.client.models.v1beta2_device_allocation_result import V1beta2DeviceAllocationResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2DeviceAllocationResult from a JSON string
v1beta2_device_allocation_result_instance = V1beta2DeviceAllocationResult.from_json(json)
# print the JSON string representation of the object
print(V1beta2DeviceAllocationResult.to_json())

# convert the object into a dict
v1beta2_device_allocation_result_dict = v1beta2_device_allocation_result_instance.to_dict()
# create an instance of V1beta2DeviceAllocationResult from a dict
v1beta2_device_allocation_result_from_dict = V1beta2DeviceAllocationResult.from_dict(v1beta2_device_allocation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
