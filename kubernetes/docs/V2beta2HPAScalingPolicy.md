# V2beta2HPAScalingPolicy

HPAScalingPolicy is a single policy which must hold true for a specified past interval.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_seconds** | **int** | PeriodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). | 
**type** | **str** | Type is used to specify the scaling policy. | 
**value** | **int** | Value contains the amount of change which is permitted by the policy. It must be greater than zero | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


