# V1beta1OpaqueDeviceConfiguration

OpaqueDeviceConfiguration contains configuration parameters for a driver in a format defined by the driver vendor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | Driver is used to determine which kubelet plugin needs to be passed these configuration parameters.  An admission policy provided by the driver developer could use this to decide whether it needs to validate them.  Must be a DNS subdomain and should end with a DNS domain owned by the vendor of the driver. It should use only lower case characters. |
**parameters** | **object** | Parameters can contain arbitrary data. It is the responsibility of the driver developer to handle validation and versioning. Typically this includes self-identification and a version (\&quot;kind\&quot; + \&quot;apiVersion\&quot; for Kubernetes types), with conversion between different versions.  The length of the raw data must be smaller or equal to 10 Ki. |

## Example

```python
from kubernetes.client.models.v1beta1_opaque_device_configuration import V1beta1OpaqueDeviceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1OpaqueDeviceConfiguration from a JSON string
v1beta1_opaque_device_configuration_instance = V1beta1OpaqueDeviceConfiguration.from_json(json)
# print the JSON string representation of the object
print(V1beta1OpaqueDeviceConfiguration.to_json())

# convert the object into a dict
v1beta1_opaque_device_configuration_dict = v1beta1_opaque_device_configuration_instance.to_dict()
# create an instance of V1beta1OpaqueDeviceConfiguration from a dict
v1beta1_opaque_device_configuration_from_dict = V1beta1OpaqueDeviceConfiguration.from_dict(v1beta1_opaque_device_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
