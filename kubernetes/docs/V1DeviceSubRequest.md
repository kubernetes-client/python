# V1DeviceSubRequest

DeviceSubRequest describes a request for device provided in the claim.spec.devices.requests[].firstAvailable array. Each is typically a request for a single resource like a device, but can also ask for several identical devices.  DeviceSubRequest is similar to ExactDeviceRequest, but doesn't expose the AdminAccess field as that one is only supported when requesting a specific device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_mode** | **str** | AllocationMode and its related fields define how devices are allocated to satisfy this subrequest. Supported values are:  - ExactCount: This request is for a specific number of devices.   This is the default. The exact number is provided in the   count field.  - All: This subrequest is for all of the matching devices in a pool.   Allocation will fail if some devices are already allocated,   unless adminAccess is requested.  If AllocationMode is not specified, the default mode is ExactCount. If the mode is ExactCount and count is not specified, the default count is one. Any other subrequests must specify this field.  More modes may get added in the future. Clients must refuse to handle requests with unknown modes. | [optional]
**capacity** | [**V1CapacityRequirements**](V1CapacityRequirements.md) |  | [optional]
**count** | **int** | Count is used only when the count mode is \&quot;ExactCount\&quot;. Must be greater than zero. If AllocationMode is ExactCount and this field is not specified, the default is one. | [optional]
**derived_attributes** | [**List[V1DeviceDerivedAttribute]**](V1DeviceDerivedAttribute.md) | DerivedAttributes defines a set of virtual attributes computed via CEL expressions for each candidate device. These virtual attributes can be referenced in &#x60;.devices.constraints&#x60; to align and match different devices (e.g., co-allocating a GPU and a NIC on the same NUMA node) even if their drivers publish different attributes. Derived attributes are not available via &#x60;device.attributes&#x60; in the CEL environment when evaluating selector expressions.  Derived attributes allow you to extract, transform, or normalize topology information (such as extracting a NUMA index from a complex topology string or renaming a vendor-specific attribute) into a common virtual attribute name at scheduling time. The scheduler then evaluates these virtual attributes exactly like static attributes when matching constraints.  Every derived attribute defined in this list must be referenced by at least one MatchAttribute or DistinctAttribute constraint in the &#x60;.devices.constraints&#x60; list.  The maximum number of derived attributes is 32.  This is an alpha field and requires enabling the DRADerivedAttributes feature gate. | [optional]
**device_class_name** | **str** | DeviceClassName references a specific DeviceClass, which can define additional configuration and selectors to be inherited by this subrequest.  A class is required. Which classes are available depends on the cluster.  Administrators may use this to restrict which devices may get requested by only installing classes with selectors for permitted devices. If users are free to request anything without restrictions, then administrators can create an empty DeviceClass for users to reference. |
**name** | **str** | Name can be used to reference this subrequest in the list of constraints or the list of configurations for the claim. References must use the format &lt;main request&gt;/&lt;subrequest&gt;.  Must be a DNS label. |
**selectors** | [**List[V1DeviceSelector]**](V1DeviceSelector.md) | Selectors define criteria which must be satisfied by a specific device in order for that device to be considered for this subrequest. All selectors must be satisfied for a device to be considered. | [optional]
**tolerations** | [**List[V1DeviceToleration]**](V1DeviceToleration.md) | If specified, the request&#39;s tolerations.  Tolerations for NoSchedule are required to allocate a device which has a taint with that effect. The same applies to NoExecute.  In addition, should any of the allocated devices get tainted with NoExecute after allocation and that effect is not tolerated, then all pods consuming the ResourceClaim get deleted to evict them. The scheduler will not let new pods reserve the claim while it has these tainted devices. Once all pods are evicted, the claim will get deallocated.  The maximum number of tolerations is 16.  This is a beta field and requires enabling the DRADeviceTaints feature gate. | [optional]

## Example

```python
from kubernetes.client.models.v1_device_sub_request import V1DeviceSubRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V1DeviceSubRequest from a JSON string
v1_device_sub_request_instance = V1DeviceSubRequest.from_json(json)
# print the JSON string representation of the object
print(V1DeviceSubRequest.to_json())

# convert the object into a dict
v1_device_sub_request_dict = v1_device_sub_request_instance.to_dict()
# create an instance of V1DeviceSubRequest from a dict
v1_device_sub_request_from_dict = V1DeviceSubRequest.from_dict(v1_device_sub_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
