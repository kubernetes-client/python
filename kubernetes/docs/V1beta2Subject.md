# V1beta2Subject

Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**V1beta2GroupSubject**](V1beta2GroupSubject.md) |  | [optional] 
**kind** | **str** | &#x60;kind&#x60; indicates which one of the other fields is non-empty. Required | 
**service_account** | [**V1beta2ServiceAccountSubject**](V1beta2ServiceAccountSubject.md) |  | [optional] 
**user** | [**V1beta2UserSubject**](V1beta2UserSubject.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


