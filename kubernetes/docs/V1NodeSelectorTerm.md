# V1NodeSelectorTerm

A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_expressions** | [**[V1NodeSelectorRequirement]**](V1NodeSelectorRequirement.md) | A list of node selector requirements by node&#39;s labels. | [optional] 
**match_fields** | [**[V1NodeSelectorRequirement]**](V1NodeSelectorRequirement.md) | A list of node selector requirements by node&#39;s fields. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


