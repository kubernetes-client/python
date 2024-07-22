# ApiregistrationV1ServiceReference

ServiceReference holds a reference to Service.legacy.k8s.io

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the name of the service | [optional] 
**namespace** | **str** | Namespace is the namespace of the service | [optional] 
**port** | **int** | If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. &#x60;port&#x60; should be a valid port number (1-65535, inclusive). | [optional] 

## Example

```python
from kubernetes.client.models.apiregistration_v1_service_reference import ApiregistrationV1ServiceReference

# TODO update the JSON string below
json = "{}"
# create an instance of ApiregistrationV1ServiceReference from a JSON string
apiregistration_v1_service_reference_instance = ApiregistrationV1ServiceReference.from_json(json)
# print the JSON string representation of the object
print ApiregistrationV1ServiceReference.to_json()

# convert the object into a dict
apiregistration_v1_service_reference_dict = apiregistration_v1_service_reference_instance.to_dict()
# create an instance of ApiregistrationV1ServiceReference from a dict
apiregistration_v1_service_reference_form_dict = apiregistration_v1_service_reference.from_dict(apiregistration_v1_service_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


