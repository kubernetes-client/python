# V1ScaleStatus

ScaleStatus represents the current status of a scale subresource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicas** | **int** | actual number of observed instances of the scaled object. | 
**selector** | **str** | label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by kubernetes.clients. The string will be in the same format as the query-param syntax. More info about label selectors: http://kubernetes.io/docs/user-guide/labels#label-selectors | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


