# V1beta1AllocationResult

AllocationResult contains attributes of an allocated resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_timestamp** | **datetime** | AllocationTimestamp stores the time when the resources were allocated. This field is not guaranteed to be set, in which case that time is unknown.  This is a beta field and requires enabling the DRADeviceBindingConditions and DRAResourceClaimDeviceStatus feature gate. | [optional]
**devices** | [**V1beta1DeviceAllocationResult**](V1beta1DeviceAllocationResult.md) |  | [optional]
**node_selector** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1beta1_allocation_result import V1beta1AllocationResult

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1AllocationResult from a JSON string
v1beta1_allocation_result_instance = V1beta1AllocationResult.from_json(json)
# print the JSON string representation of the object
print(V1beta1AllocationResult.to_json())

# convert the object into a dict
v1beta1_allocation_result_dict = v1beta1_allocation_result_instance.to_dict()
# create an instance of V1beta1AllocationResult from a dict
v1beta1_allocation_result_from_dict = V1beta1AllocationResult.from_dict(v1beta1_allocation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
