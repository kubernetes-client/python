# V1beta1RunAsUserStrategyOptions

RunAsUserStrategyOptions defines the strategy type and any options used to create the strategy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | **str** | rule is the strategy that will dictate the allowable RunAsUser values that may be set. | 
**ranges** | [**[V1beta1IDRange]**](V1beta1IDRange.md) | ranges are the allowed ranges of uids that may be used. If you would like to force a single uid then supply a single range with the same start and end. Required for MustRunAs. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


