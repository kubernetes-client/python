# V1beta1Subject

Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | &#x60;kind&#x60; indicates which one of the other fields is non-empty. Required | 
**group** | [**V1beta1GroupSubject**](V1beta1GroupSubject.md) |  | [optional] 
**service_account** | [**V1beta1ServiceAccountSubject**](V1beta1ServiceAccountSubject.md) |  | [optional] 
**user** | [**V1beta1UserSubject**](V1beta1UserSubject.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


