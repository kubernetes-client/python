# V1alpha2ResourceHandle

ResourceHandle holds opaque resource data for processing by a specific kubelet plugin.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Data contains the opaque data associated with this ResourceHandle. It is set by the controller component of the resource driver whose name matches the DriverName set in the ResourceClaimStatus this ResourceHandle is embedded in. It is set at allocation time and is intended for processing by the kubelet plugin whose name matches the DriverName set in this ResourceHandle.  The maximum size of this field is 16KiB. This may get increased in the future, but not reduced. | [optional] 
**driver_name** | **str** | DriverName specifies the name of the resource driver whose kubelet plugin should be invoked to process this ResourceHandle&#39;s data once it lands on a node. This may differ from the DriverName set in ResourceClaimStatus this ResourceHandle is embedded in. | [optional] 
**structured_data** | [**V1alpha2StructuredResourceHandle**](V1alpha2StructuredResourceHandle.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_handle import V1alpha2ResourceHandle

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceHandle from a JSON string
v1alpha2_resource_handle_instance = V1alpha2ResourceHandle.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceHandle.to_json()

# convert the object into a dict
v1alpha2_resource_handle_dict = v1alpha2_resource_handle_instance.to_dict()
# create an instance of V1alpha2ResourceHandle from a dict
v1alpha2_resource_handle_form_dict = v1alpha2_resource_handle.from_dict(v1alpha2_resource_handle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


