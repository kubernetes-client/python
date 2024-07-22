# V1IngressServiceBackend

IngressServiceBackend references a Kubernetes Service as a Backend.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the referenced service. The service must exist in the same namespace as the Ingress object. | 
**port** | [**V1ServiceBackendPort**](V1ServiceBackendPort.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_ingress_service_backend import V1IngressServiceBackend

# TODO update the JSON string below
json = "{}"
# create an instance of V1IngressServiceBackend from a JSON string
v1_ingress_service_backend_instance = V1IngressServiceBackend.from_json(json)
# print the JSON string representation of the object
print V1IngressServiceBackend.to_json()

# convert the object into a dict
v1_ingress_service_backend_dict = v1_ingress_service_backend_instance.to_dict()
# create an instance of V1IngressServiceBackend from a dict
v1_ingress_service_backend_form_dict = v1_ingress_service_backend.from_dict(v1_ingress_service_backend_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


