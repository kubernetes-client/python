# V1UserSubject

UserSubject holds detailed information for user-kind subject.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | &#x60;name&#x60; is the username that matches, or \&quot;*\&quot; to match all usernames. Required. | 

## Example

```python
from kubernetes.client.models.v1_user_subject import V1UserSubject

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserSubject from a JSON string
v1_user_subject_instance = V1UserSubject.from_json(json)
# print the JSON string representation of the object
print V1UserSubject.to_json()

# convert the object into a dict
v1_user_subject_dict = v1_user_subject_instance.to_dict()
# create an instance of V1UserSubject from a dict
v1_user_subject_form_dict = v1_user_subject.from_dict(v1_user_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


