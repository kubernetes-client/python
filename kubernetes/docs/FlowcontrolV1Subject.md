# FlowcontrolV1Subject

Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**V1GroupSubject**](V1GroupSubject.md) |  | [optional] 
**kind** | **str** | &#x60;kind&#x60; indicates which one of the other fields is non-empty. Required | 
**service_account** | [**V1ServiceAccountSubject**](V1ServiceAccountSubject.md) |  | [optional] 
**user** | [**V1UserSubject**](V1UserSubject.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


