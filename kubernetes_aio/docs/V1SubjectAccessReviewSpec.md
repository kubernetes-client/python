# V1SubjectAccessReviewSpec

SubjectAccessReviewSpec is a description of the access request.  Exactly one of resourceAttributes and nonResourceAttributes must be set

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **dict[str, list[str]]** | extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here. | [optional] 
**groups** | **list[str]** | groups is the groups you&#39;re testing for. | [optional] 
**non_resource_attributes** | [**V1NonResourceAttributes**](V1NonResourceAttributes.md) |  | [optional] 
**resource_attributes** | [**V1ResourceAttributes**](V1ResourceAttributes.md) |  | [optional] 
**uid** | **str** | uid information about the requesting user. | [optional] 
**user** | **str** | user is the user you&#39;re testing for. If you specify \&quot;User\&quot; but not \&quot;Groups\&quot;, then is it interpreted as \&quot;What if User were not a member of any groups | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


