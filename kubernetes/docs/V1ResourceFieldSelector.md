# V1ResourceFieldSelector

ResourceFieldSelector represents container resources (cpu, memory) and their output format

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Required: resource to select | 
**container_name** | **str** | Container name: required for volumes, optional for env vars | [optional] 
**divisor** | **str** | Specifies the output format of the exposed resources, defaults to \&quot;1\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


