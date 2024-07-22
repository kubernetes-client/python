# V1beta3GroupSubject

GroupSubject holds detailed information for group-kind subject.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the user group that matches, or \&quot;*\&quot; to match all user groups. See https://github.com/kubernetes/apiserver/blob/master/pkg/authentication/user/user.go for some well-known group names. Required. | 

## Example

```python
from kubernetes.client.models.v1beta3_group_subject import V1beta3GroupSubject

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta3GroupSubject from a JSON string
v1beta3_group_subject_instance = V1beta3GroupSubject.from_json(json)
# print the JSON string representation of the object
print V1beta3GroupSubject.to_json()

# convert the object into a dict
v1beta3_group_subject_dict = v1beta3_group_subject_instance.to_dict()
# create an instance of V1beta3GroupSubject from a dict
v1beta3_group_subject_form_dict = v1beta3_group_subject.from_dict(v1beta3_group_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


