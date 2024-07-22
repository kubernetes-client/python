# V1NamespaceSpec

NamespaceSpec describes the attributes on a Namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finalizers** | **List[str]** | Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/ | [optional] 

## Example

```python
from kubernetes.client.models.v1_namespace_spec import V1NamespaceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1NamespaceSpec from a JSON string
v1_namespace_spec_instance = V1NamespaceSpec.from_json(json)
# print the JSON string representation of the object
print V1NamespaceSpec.to_json()

# convert the object into a dict
v1_namespace_spec_dict = v1_namespace_spec_instance.to_dict()
# create an instance of V1NamespaceSpec from a dict
v1_namespace_spec_form_dict = v1_namespace_spec.from_dict(v1_namespace_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


