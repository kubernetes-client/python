# V1ScaleStatus

ScaleStatus represents the current status of a scale subresource.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicas** | **int** | replicas is the actual number of observed instances of the scaled object. | 
**selector** | **str** | selector is the label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by kubernetes.clients. The string will be in the same format as the query-param syntax. More info about label selectors: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


