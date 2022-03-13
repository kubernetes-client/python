# V1IngressServiceBackend

IngressServiceBackend references a Kubernetes Service as a Backend.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name is the referenced service. The service must exist in the same namespace as the Ingress object. | 
**port** | [**V1ServiceBackendPort**](V1ServiceBackendPort.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


