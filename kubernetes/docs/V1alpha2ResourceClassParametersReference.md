# V1alpha2ResourceClassParametersReference

ResourceClassParametersReference contains enough information to let you locate the parameters for a ResourceClass.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup is the group for the resource being referenced. It is empty for the core API. This matches the group in the APIVersion that is used when creating the resources. | [optional] 
**kind** | **str** | Kind is the type of resource being referenced. This is the same value as in the parameter object&#39;s metadata. | 
**name** | **str** | Name is the name of resource being referenced. | 
**namespace** | **str** | Namespace that contains the referenced resource. Must be empty for cluster-scoped resources and non-empty for namespaced resources. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_class_parameters_reference import V1alpha2ResourceClassParametersReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceClassParametersReference from a JSON string
v1alpha2_resource_class_parameters_reference_instance = V1alpha2ResourceClassParametersReference.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceClassParametersReference.to_json()

# convert the object into a dict
v1alpha2_resource_class_parameters_reference_dict = v1alpha2_resource_class_parameters_reference_instance.to_dict()
# create an instance of V1alpha2ResourceClassParametersReference from a dict
v1alpha2_resource_class_parameters_reference_form_dict = v1alpha2_resource_class_parameters_reference.from_dict(v1alpha2_resource_class_parameters_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


