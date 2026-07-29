# V1alpha3DeviceTaintSelector

DeviceTaintSelector defines which device(s) a DeviceTaintRule applies to. The empty selector matches all devices. Without a selector, no devices are matched.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | If device is set, only devices with that name are selected. This field corresponds to slice.spec.devices[].name.  Setting also driver and pool may be required to avoid ambiguity, but is not required. | [optional]
**driver** | **str** | If driver is set, only devices from that driver are selected. This fields corresponds to slice.spec.driver. | [optional]
**pool** | **str** | If pool is set, only devices in that pool are selected.  Also setting the driver name may be useful to avoid ambiguity when different drivers use the same pool name, but this is not required because selecting pools from different drivers may also be useful, for example when drivers with node-local devices use the node name as their pool name. | [optional]

## Example

```python
from kubernetes.client.models.v1alpha3_device_taint_selector import V1alpha3DeviceTaintSelector

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3DeviceTaintSelector from a JSON string
v1alpha3_device_taint_selector_instance = V1alpha3DeviceTaintSelector.from_json(json)
# print the JSON string representation of the object
print(V1alpha3DeviceTaintSelector.to_json())

# convert the object into a dict
v1alpha3_device_taint_selector_dict = v1alpha3_device_taint_selector_instance.to_dict()
# create an instance of V1alpha3DeviceTaintSelector from a dict
v1alpha3_device_taint_selector_from_dict = V1alpha3DeviceTaintSelector.from_dict(v1alpha3_device_taint_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
