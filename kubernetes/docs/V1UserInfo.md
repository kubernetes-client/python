# V1UserInfo

UserInfo holds the information about the user needed to implement the user.Info interface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **{str: ([str],)}** | Any additional information provided by the authenticator. | [optional] 
**groups** | **[str]** | The names of groups this user is a part of. | [optional] 
**uid** | **str** | A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs. | [optional] 
**username** | **str** | The name that uniquely identifies this user among all active users. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


