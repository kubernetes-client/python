# V1beta1ResourceSliceList

ResourceSliceList is a collection of ResourceSlices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**items** | [**List[V1beta1ResourceSlice]**](V1beta1ResourceSlice.md) | Items is the list of resource ResourceSlices. |
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1beta1_resource_slice_list import V1beta1ResourceSliceList

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ResourceSliceList from a JSON string
v1beta1_resource_slice_list_instance = V1beta1ResourceSliceList.from_json(json)
# print the JSON string representation of the object
print(V1beta1ResourceSliceList.to_json())

# convert the object into a dict
v1beta1_resource_slice_list_dict = v1beta1_resource_slice_list_instance.to_dict()
# create an instance of V1beta1ResourceSliceList from a dict
v1beta1_resource_slice_list_from_dict = V1beta1ResourceSliceList.from_dict(v1beta1_resource_slice_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
