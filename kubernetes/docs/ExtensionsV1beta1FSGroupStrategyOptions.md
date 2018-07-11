# ExtensionsV1beta1FSGroupStrategyOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ranges** | [**list[ExtensionsV1beta1IDRange]**](ExtensionsV1beta1IDRange.md) | ranges are the allowed ranges of fs groups.  If you would like to force a single fs group then supply a single range with the same start and end. Required for MustRunAs. | [optional] 
**rule** | **str** | rule is the strategy that will dictate what FSGroup is used in the SecurityContext. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


