# V1alpha3DeviceTaintRuleStatus

DeviceTaintRuleStatus provides information about an on-going pod eviction.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1Condition]**](V1Condition.md) | Conditions provide information about the state of the DeviceTaintRule and the cluster at some point in time, in a machine-readable and human-readable format.  The following condition is currently defined as part of this API, more may get added: - Type: EvictionInProgress - Status: True if there are currently pods which need to be evicted, False otherwise   (includes the effects which don&#39;t cause eviction). - Reason: not specified, may change - Message: includes information about number of pending pods and already evicted pods   in a human-readable format, updated periodically, may change  For &#x60;effect: None&#x60;, the condition above gets set once for each change to the spec, with the message containing information about what would happen if the effect was &#x60;NoExecute&#x60;. This feedback can be used to decide whether changing the effect to &#x60;NoExecute&#x60; will work as intended. It only gets set once to avoid having to constantly update the status.  Must have 8 or fewer entries. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


