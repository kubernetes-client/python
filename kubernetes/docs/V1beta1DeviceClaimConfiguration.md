# V1beta1DeviceClaimConfiguration

DeviceClaimConfiguration is used for configuration parameters in DeviceClaim.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opaque** | [**V1beta1OpaqueDeviceConfiguration**](V1beta1OpaqueDeviceConfiguration.md) |  | [optional]
**requests** | **List[str]** | Requests lists the names of requests where the configuration applies. If empty, it applies to all requests.  References to subrequests must include the name of the main request and may include the subrequest using the format &lt;main request&gt;[/&lt;subrequest&gt;]. If just the main request is given, the configuration applies to all subrequests. | [optional]

## Example

```python
from kubernetes.client.models.v1beta1_device_claim_configuration import V1beta1DeviceClaimConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1DeviceClaimConfiguration from a JSON string
v1beta1_device_claim_configuration_instance = V1beta1DeviceClaimConfiguration.from_json(json)
# print the JSON string representation of the object
print(V1beta1DeviceClaimConfiguration.to_json())

# convert the object into a dict
v1beta1_device_claim_configuration_dict = v1beta1_device_claim_configuration_instance.to_dict()
# create an instance of V1beta1DeviceClaimConfiguration from a dict
v1beta1_device_claim_configuration_from_dict = V1beta1DeviceClaimConfiguration.from_dict(v1beta1_device_claim_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
