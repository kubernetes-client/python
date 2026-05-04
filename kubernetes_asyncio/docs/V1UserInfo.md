# V1UserInfo

UserInfo holds the information about the user needed to implement the user.Info interface.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **dict[str, list[str]]** | extra is any additional information provided by the authenticator. | [optional] 
**groups** | **list[str]** | groups is the names of groups this user is a part of. | [optional] 
**uid** | **str** | uid is a unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs. | [optional] 
**username** | **str** | username is the name that uniquely identifies this user among all active users. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


