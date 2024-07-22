# V1alpha2NamedResourcesStringSlice

NamedResourcesStringSlice contains a slice of strings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strings** | **List[str]** | Strings is the slice of strings. | 

## Example

```python
from kubernetes.client.models.v1alpha2_named_resources_string_slice import V1alpha2NamedResourcesStringSlice

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2NamedResourcesStringSlice from a JSON string
v1alpha2_named_resources_string_slice_instance = V1alpha2NamedResourcesStringSlice.from_json(json)
# print the JSON string representation of the object
print V1alpha2NamedResourcesStringSlice.to_json()

# convert the object into a dict
v1alpha2_named_resources_string_slice_dict = v1alpha2_named_resources_string_slice_instance.to_dict()
# create an instance of V1alpha2NamedResourcesStringSlice from a dict
v1alpha2_named_resources_string_slice_form_dict = v1alpha2_named_resources_string_slice.from_dict(v1alpha2_named_resources_string_slice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


