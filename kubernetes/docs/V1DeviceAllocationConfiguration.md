# V1DeviceAllocationConfiguration

DeviceAllocationConfiguration gets embedded in an AllocationResult.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opaque** | [**V1OpaqueDeviceConfiguration**](V1OpaqueDeviceConfiguration.md) |  | [optional]
**requests** | **List[str]** | Requests lists the names of requests where the configuration applies. If empty, its applies to all requests.  References to subrequests must include the name of the main request and may include the subrequest using the format &lt;main request&gt;[/&lt;subrequest&gt;]. If just the main request is given, the configuration applies to all subrequests. | [optional]
**source** | **str** | Source records whether the configuration comes from a class and thus is not something that a normal user would have been able to set or from a claim. |

## Example

```python
from kubernetes.client.models.v1_device_allocation_configuration import V1DeviceAllocationConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceAllocationConfiguration from a JSON string
v1_device_allocation_configuration_instance = V1DeviceAllocationConfiguration.from_json(json)
# print the JSON string representation of the object
print(V1DeviceAllocationConfiguration.to_json())

# convert the object into a dict
v1_device_allocation_configuration_dict = v1_device_allocation_configuration_instance.to_dict()
# create an instance of V1DeviceAllocationConfiguration from a dict
v1_device_allocation_configuration_from_dict = V1DeviceAllocationConfiguration.from_dict(v1_device_allocation_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
