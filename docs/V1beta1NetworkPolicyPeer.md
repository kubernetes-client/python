# V1beta1NetworkPolicyPeer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace_selector** | [**UnversionedLabelSelector**](UnversionedLabelSelector.md) | Selects Namespaces using cluster scoped-labels.  This matches all pods in all namespaces selected by this label selector. This field follows standard label selector semantics. If omitted, this selector selects no namespaces. If present but empty, this selector selects all namespaces. | [optional] 
**pod_selector** | [**UnversionedLabelSelector**](UnversionedLabelSelector.md) | This is a label selector which selects Pods in this namespace. This field follows standard label selector semantics. If not provided, this selector selects no pods. If present but empty, this selector selects all pods in this namespace. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


