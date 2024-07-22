# V1Namespace

Namespace provides a scope for Names. Use of multiple namespaces is optional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1NamespaceSpec**](V1NamespaceSpec.md) |  | [optional] 
**status** | [**V1NamespaceStatus**](V1NamespaceStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_namespace import V1Namespace

# TODO update the JSON string below
json = "{}"
# create an instance of V1Namespace from a JSON string
v1_namespace_instance = V1Namespace.from_json(json)
# print the JSON string representation of the object
print V1Namespace.to_json()

# convert the object into a dict
v1_namespace_dict = v1_namespace_instance.to_dict()
# create an instance of V1Namespace from a dict
v1_namespace_form_dict = v1_namespace.from_dict(v1_namespace_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


