# kubernetes.client.model.v1beta1_subject.V1beta1Subject

Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**kind** | str,  | str,  | &#x60;kind&#x60; indicates which one of the other fields is non-empty. Required | 
**group** | [**V1beta1GroupSubject**](V1beta1GroupSubject.md) | [**V1beta1GroupSubject**](V1beta1GroupSubject.md) |  | [optional] 
**serviceAccount** | [**V1beta1ServiceAccountSubject**](V1beta1ServiceAccountSubject.md) | [**V1beta1ServiceAccountSubject**](V1beta1ServiceAccountSubject.md) |  | [optional] 
**user** | [**V1beta1UserSubject**](V1beta1UserSubject.md) | [**V1beta1UserSubject**](V1beta1UserSubject.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

