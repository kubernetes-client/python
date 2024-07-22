# V1IngressClassParametersReference

IngressClassParametersReference identifies an API object. This can be used to specify a cluster or namespace-scoped resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | apiGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. | [optional] 
**kind** | **str** | kind is the type of resource being referenced. | 
**name** | **str** | name is the name of resource being referenced. | 
**namespace** | **str** | namespace is the namespace of the resource being referenced. This field is required when scope is set to \&quot;Namespace\&quot; and must be unset when scope is set to \&quot;Cluster\&quot;. | [optional] 
**scope** | **str** | scope represents if this refers to a cluster or namespace scoped resource. This may be set to \&quot;Cluster\&quot; (default) or \&quot;Namespace\&quot;. | [optional] 

## Example

```python
from kubernetes.client.models.v1_ingress_class_parameters_reference import V1IngressClassParametersReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1IngressClassParametersReference from a JSON string
v1_ingress_class_parameters_reference_instance = V1IngressClassParametersReference.from_json(json)
# print the JSON string representation of the object
print V1IngressClassParametersReference.to_json()

# convert the object into a dict
v1_ingress_class_parameters_reference_dict = v1_ingress_class_parameters_reference_instance.to_dict()
# create an instance of V1IngressClassParametersReference from a dict
v1_ingress_class_parameters_reference_form_dict = v1_ingress_class_parameters_reference.from_dict(v1_ingress_class_parameters_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


