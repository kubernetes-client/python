# V1OwnerReference

OwnerReference contains enough information to let you identify an owning object. An owning object must be in the same namespace as the dependent, or be cluster-scoped, so there is no namespace field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | API version of the referent. | 
**block_owner_deletion** | **bool** | If true, AND if the owner has the \&quot;foregroundDeletion\&quot; finalizer, then the owner cannot be deleted from the key-value store until this reference is removed. See https://kubernetes.io/docs/concepts/architecture/garbage-collection/#foreground-deletion for how the garbage collector interacts with this field and enforces the foreground deletion. Defaults to false. To set this field, a user needs \&quot;delete\&quot; permission of the owner, otherwise 422 (Unprocessable Entity) will be returned. | [optional] 
**controller** | **bool** | If true, this reference points to the managing controller. | [optional] 
**kind** | **str** | Kind of the referent. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | 
**name** | **str** | Name of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names | 
**uid** | **str** | UID of the referent. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids | 

## Example

```python
from kubernetes.client.models.v1_owner_reference import V1OwnerReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1OwnerReference from a JSON string
v1_owner_reference_instance = V1OwnerReference.from_json(json)
# print the JSON string representation of the object
print V1OwnerReference.to_json()

# convert the object into a dict
v1_owner_reference_dict = v1_owner_reference_instance.to_dict()
# create an instance of V1OwnerReference from a dict
v1_owner_reference_form_dict = v1_owner_reference.from_dict(v1_owner_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


