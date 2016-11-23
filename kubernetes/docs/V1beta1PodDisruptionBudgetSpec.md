# V1beta1PodDisruptionBudgetSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_available** | [**IntstrIntOrString**](IntstrIntOrString.md) | An eviction is allowed if at least \&quot;minAvailable\&quot; pods selected by \&quot;selector\&quot; will still be available after the eviction, i.e. even in the absence of the evicted pod.  So for example you can prevent all voluntary evictions by specifying \&quot;100%\&quot;. | [optional] 
**selector** | [**UnversionedLabelSelector**](UnversionedLabelSelector.md) | Label query over pods whose evictions are managed by the disruption budget. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


