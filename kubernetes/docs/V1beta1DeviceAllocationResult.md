# V1beta1DeviceAllocationResult

DeviceAllocationResult is the result of allocating devices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[V1beta1DeviceAllocationConfiguration]**](V1beta1DeviceAllocationConfiguration.md) | This field is a combination of all the claim and class configuration parameters. Drivers can distinguish between those based on a flag.  This includes configuration parameters for drivers which have no allocated devices in the result because it is up to the drivers which configuration parameters they support. They can silently ignore unknown configuration parameters. | [optional]
**results** | [**List[V1beta1DeviceRequestAllocationResult]**](V1beta1DeviceRequestAllocationResult.md) | Results lists all allocated devices. | [optional]

## Example

```python
from kubernetes.client.models.v1beta1_device_allocation_result import V1beta1DeviceAllocationResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1DeviceAllocationResult from a JSON string
v1beta1_device_allocation_result_instance = V1beta1DeviceAllocationResult.from_json(json)
# print the JSON string representation of the object
print(V1beta1DeviceAllocationResult.to_json())

# convert the object into a dict
v1beta1_device_allocation_result_dict = v1beta1_device_allocation_result_instance.to_dict()
# create an instance of V1beta1DeviceAllocationResult from a dict
v1beta1_device_allocation_result_from_dict = V1beta1DeviceAllocationResult.from_dict(v1beta1_device_allocation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
