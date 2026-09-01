# V1alpha3TypedLocalObjectReference

TypedLocalObjectReference allows to reference typed object inside the same namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | apiGroup is the group for the resource being referenced. If APIGroup is empty, the specified Kind must be in the core API group. For any other third-party types, setting APIGroup is required. It must be a DNS subdomain. | [optional]
**kind** | **str** | kind is the type of resource being referenced. It must be a path segment name. |
**name** | **str** | name is the name of resource being referenced. It must be a path segment name. |

## Example

```python
from kubernetes.aio.client.models.v1alpha3_typed_local_object_reference import V1alpha3TypedLocalObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3TypedLocalObjectReference from a JSON string
v1alpha3_typed_local_object_reference_instance = V1alpha3TypedLocalObjectReference.from_json(json)
# print the JSON string representation of the object
print(V1alpha3TypedLocalObjectReference.to_json())

# convert the object into a dict
v1alpha3_typed_local_object_reference_dict = v1alpha3_typed_local_object_reference_instance.to_dict()
# create an instance of V1alpha3TypedLocalObjectReference from a dict
v1alpha3_typed_local_object_reference_from_dict = V1alpha3TypedLocalObjectReference.from_dict(v1alpha3_typed_local_object_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
