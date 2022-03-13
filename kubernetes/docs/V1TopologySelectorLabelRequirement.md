# V1TopologySelectorLabelRequirement

A topology selector requirement is a selector that matches given label. This is an alpha feature and may change in the future.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The label key that the selector applies to. | 
**values** | **[str]** | An array of string values. One value must match the label to be selected. Each entry in Values is ORed. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


