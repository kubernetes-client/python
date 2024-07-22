# V1beta3ServiceAccountSubject

ServiceAccountSubject holds detailed information for service-account-kind subject.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | &#x60;name&#x60; is the name of matching ServiceAccount objects, or \&quot;*\&quot; to match regardless of name. Required. | 
**namespace** | **str** | &#x60;namespace&#x60; is the namespace of matching ServiceAccount objects. Required. | 

## Example

```python
from kubernetes.client.models.v1beta3_service_account_subject import V1beta3ServiceAccountSubject

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta3ServiceAccountSubject from a JSON string
v1beta3_service_account_subject_instance = V1beta3ServiceAccountSubject.from_json(json)
# print the JSON string representation of the object
print V1beta3ServiceAccountSubject.to_json()

# convert the object into a dict
v1beta3_service_account_subject_dict = v1beta3_service_account_subject_instance.to_dict()
# create an instance of V1beta3ServiceAccountSubject from a dict
v1beta3_service_account_subject_form_dict = v1beta3_service_account_subject.from_dict(v1beta3_service_account_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


