# V1alpha2NamedResourcesIntSlice

NamedResourcesIntSlice contains a slice of 64-bit integers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ints** | **List[int]** | Ints is the slice of 64-bit integers. | 

## Example

```python
from kubernetes.client.models.v1alpha2_named_resources_int_slice import V1alpha2NamedResourcesIntSlice

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2NamedResourcesIntSlice from a JSON string
v1alpha2_named_resources_int_slice_instance = V1alpha2NamedResourcesIntSlice.from_json(json)
# print the JSON string representation of the object
print V1alpha2NamedResourcesIntSlice.to_json()

# convert the object into a dict
v1alpha2_named_resources_int_slice_dict = v1alpha2_named_resources_int_slice_instance.to_dict()
# create an instance of V1alpha2NamedResourcesIntSlice from a dict
v1alpha2_named_resources_int_slice_form_dict = v1alpha2_named_resources_int_slice.from_dict(v1alpha2_named_resources_int_slice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


