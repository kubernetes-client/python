# V1beta1SubjectAccessReviewSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra** | **dict(str, list[str])** | Extra corresponds to the user.Info.GetExtra() method from the authenticator.  Since that is input to the authorizer it needs a reflection here. | [optional] 
**group** | **list[str]** | Groups is the groups you&#39;re testing for. | [optional] 
**non_resource_attributes** | [**V1beta1NonResourceAttributes**](V1beta1NonResourceAttributes.md) |  | [optional] 
**resource_attributes** | [**V1beta1ResourceAttributes**](V1beta1ResourceAttributes.md) |  | [optional] 
**uid** | **str** | UID information about the requesting user. | [optional] 
**user** | **str** | User is the user you&#39;re testing for. If you specify \&quot;User\&quot; but not \&quot;Group\&quot;, then is it interpreted as \&quot;What if User were not a member of any groups | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


