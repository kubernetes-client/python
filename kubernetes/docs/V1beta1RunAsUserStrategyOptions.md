# V1beta1RunAsUserStrategyOptions

RunAsUserStrategyOptions defines the strategy type and any options used to create the strategy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ranges** | [**list[V1beta1IDRange]**](V1beta1IDRange.md) | ranges are the allowed ranges of uids that may be used. If you would like to force a single uid then supply a single range with the same start and end. Required for MustRunAs. | [optional] 
**rule** | **str** | rule is the strategy that will dictate the allowable RunAsUser values that may be set. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


