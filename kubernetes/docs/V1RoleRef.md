# V1RoleRef

RoleRef contains information that points to the role being used

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup is the group for the resource being referenced | 
**kind** | **str** | Kind is the type of resource being referenced | 
**name** | **str** | Name is the name of resource being referenced | 

## Example

```python
from kubernetes.client.models.v1_role_ref import V1RoleRef

# TODO update the JSON string below
json = "{}"
# create an instance of V1RoleRef from a JSON string
v1_role_ref_instance = V1RoleRef.from_json(json)
# print the JSON string representation of the object
print V1RoleRef.to_json()

# convert the object into a dict
v1_role_ref_dict = v1_role_ref_instance.to_dict()
# create an instance of V1RoleRef from a dict
v1_role_ref_form_dict = v1_role_ref.from_dict(v1_role_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


