# V1alpha2ResourceSlice

ResourceSlice provides information about available resources on individual nodes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**driver_name** | **str** | DriverName identifies the DRA driver providing the capacity information. A field selector can be used to list only ResourceSlice objects with a certain driver name. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**named_resources** | [**V1alpha2NamedResourcesResources**](V1alpha2NamedResourcesResources.md) |  | [optional] 
**node_name** | **str** | NodeName identifies the node which provides the resources if they are local to a node.  A field selector can be used to list only ResourceSlice objects with a certain node name. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_slice import V1alpha2ResourceSlice

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceSlice from a JSON string
v1alpha2_resource_slice_instance = V1alpha2ResourceSlice.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceSlice.to_json()

# convert the object into a dict
v1alpha2_resource_slice_dict = v1alpha2_resource_slice_instance.to_dict()
# create an instance of V1alpha2ResourceSlice from a dict
v1alpha2_resource_slice_form_dict = v1alpha2_resource_slice.from_dict(v1alpha2_resource_slice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


