# kubernetes.client.model.v1_ingress_service_backend.V1IngressServiceBackend

IngressServiceBackend references a Kubernetes Service as a Backend.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | IngressServiceBackend references a Kubernetes Service as a Backend. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Name is the referenced service. The service must exist in the same namespace as the Ingress object. | 
**port** | [**V1ServiceBackendPort**](V1ServiceBackendPort.md) | [**V1ServiceBackendPort**](V1ServiceBackendPort.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

