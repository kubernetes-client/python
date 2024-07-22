# RbacV1Subject

Subject contains a reference to the object or user identities a role binding applies to.  This can either hold a direct API object reference, or a value for non-objects such as user and group names.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_group** | **str** | APIGroup holds the API group of the referenced subject. Defaults to \&quot;\&quot; for ServiceAccount subjects. Defaults to \&quot;rbac.authorization.k8s.io\&quot; for User and Group subjects. | [optional] 
**kind** | **str** | Kind of object being referenced. Values defined by this API group are \&quot;User\&quot;, \&quot;Group\&quot;, and \&quot;ServiceAccount\&quot;. If the Authorizer does not recognized the kind value, the Authorizer should report an error. | 
**name** | **str** | Name of the object being referenced. | 
**namespace** | **str** | Namespace of the referenced object.  If the object kind is non-namespace, such as \&quot;User\&quot; or \&quot;Group\&quot;, and this value is not empty the Authorizer should report an error. | [optional] 

## Example

```python
from kubernetes.client.models.rbac_v1_subject import RbacV1Subject

# TODO update the JSON string below
json = "{}"
# create an instance of RbacV1Subject from a JSON string
rbac_v1_subject_instance = RbacV1Subject.from_json(json)
# print the JSON string representation of the object
print RbacV1Subject.to_json()

# convert the object into a dict
rbac_v1_subject_dict = rbac_v1_subject_instance.to_dict()
# create an instance of RbacV1Subject from a dict
rbac_v1_subject_form_dict = rbac_v1_subject.from_dict(rbac_v1_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


