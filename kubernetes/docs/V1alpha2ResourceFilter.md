# V1alpha2ResourceFilter

ResourceFilter is a filter for resources from one particular driver.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver_name** | **str** | DriverName is the name used by the DRA driver kubelet plugin. | [optional] 
**named_resources** | [**V1alpha2NamedResourcesFilter**](V1alpha2NamedResourcesFilter.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_filter import V1alpha2ResourceFilter

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceFilter from a JSON string
v1alpha2_resource_filter_instance = V1alpha2ResourceFilter.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceFilter.to_json()

# convert the object into a dict
v1alpha2_resource_filter_dict = v1alpha2_resource_filter_instance.to_dict()
# create an instance of V1alpha2ResourceFilter from a dict
v1alpha2_resource_filter_form_dict = v1alpha2_resource_filter.from_dict(v1alpha2_resource_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


