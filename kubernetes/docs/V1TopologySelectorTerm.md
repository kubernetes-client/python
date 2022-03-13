# V1TopologySelectorTerm

A topology selector term represents the result of label queries. A null or empty topology selector term matches no objects. The requirements of them are ANDed. It provides a subset of functionality as NodeSelectorTerm. This is an alpha feature and may change in the future.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_label_expressions** | [**[V1TopologySelectorLabelRequirement]**](V1TopologySelectorLabelRequirement.md) | A list of topology selector requirements by labels. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


