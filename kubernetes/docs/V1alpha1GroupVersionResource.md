# V1alpha1GroupVersionResource

The names of the group, the version, and the resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | The name of the group. | [optional] 
**resource** | **str** | The name of the resource. | [optional] 
**version** | **str** | The name of the version. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha1_group_version_resource import V1alpha1GroupVersionResource

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1GroupVersionResource from a JSON string
v1alpha1_group_version_resource_instance = V1alpha1GroupVersionResource.from_json(json)
# print the JSON string representation of the object
print V1alpha1GroupVersionResource.to_json()

# convert the object into a dict
v1alpha1_group_version_resource_dict = v1alpha1_group_version_resource_instance.to_dict()
# create an instance of V1alpha1GroupVersionResource from a dict
v1alpha1_group_version_resource_form_dict = v1alpha1_group_version_resource.from_dict(v1alpha1_group_version_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


