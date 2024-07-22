# V1RoleBinding

RoleBinding references a role, but does not contain it.  It can reference a Role in the same namespace or a ClusterRole in the global namespace. It adds who information via Subjects and namespace information by which namespace it exists in.  RoleBindings in a given namespace only have effect in that namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**role_ref** | [**V1RoleRef**](V1RoleRef.md) |  | 
**subjects** | [**List[RbacV1Subject]**](RbacV1Subject.md) | Subjects holds references to the objects the role applies to. | [optional] 

## Example

```python
from kubernetes.client.models.v1_role_binding import V1RoleBinding

# TODO update the JSON string below
json = "{}"
# create an instance of V1RoleBinding from a JSON string
v1_role_binding_instance = V1RoleBinding.from_json(json)
# print the JSON string representation of the object
print V1RoleBinding.to_json()

# convert the object into a dict
v1_role_binding_dict = v1_role_binding_instance.to_dict()
# create an instance of V1RoleBinding from a dict
v1_role_binding_form_dict = v1_role_binding.from_dict(v1_role_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


