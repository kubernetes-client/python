# V1beta3Subject

Subject matches the originator of a request, as identified by the request authentication system. There are three ways of matching an originator; by user, group, or service account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**V1beta3GroupSubject**](V1beta3GroupSubject.md) |  | [optional] 
**kind** | **str** | &#x60;kind&#x60; indicates which one of the other fields is non-empty. Required | 
**service_account** | [**V1beta3ServiceAccountSubject**](V1beta3ServiceAccountSubject.md) |  | [optional] 
**user** | [**V1beta3UserSubject**](V1beta3UserSubject.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1beta3_subject import V1beta3Subject

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta3Subject from a JSON string
v1beta3_subject_instance = V1beta3Subject.from_json(json)
# print the JSON string representation of the object
print V1beta3Subject.to_json()

# convert the object into a dict
v1beta3_subject_dict = v1beta3_subject_instance.to_dict()
# create an instance of V1beta3Subject from a dict
v1beta3_subject_form_dict = v1beta3_subject.from_dict(v1beta3_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


