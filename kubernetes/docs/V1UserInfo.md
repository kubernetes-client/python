# V1UserInfo

UserInfo holds the information about the user needed to implement the user.Info interface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **Dict[str, List[str]]** | Any additional information provided by the authenticator. | [optional] 
**groups** | **List[str]** | The names of groups this user is a part of. | [optional] 
**uid** | **str** | A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs. | [optional] 
**username** | **str** | The name that uniquely identifies this user among all active users. | [optional] 

## Example

```python
from kubernetes.client.models.v1_user_info import V1UserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V1UserInfo from a JSON string
v1_user_info_instance = V1UserInfo.from_json(json)
# print the JSON string representation of the object
print V1UserInfo.to_json()

# convert the object into a dict
v1_user_info_dict = v1_user_info_instance.to_dict()
# create an instance of V1UserInfo from a dict
v1_user_info_form_dict = v1_user_info.from_dict(v1_user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


