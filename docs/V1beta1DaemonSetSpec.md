# V1beta1DaemonSetSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | [**UnversionedLabelSelector**](UnversionedLabelSelector.md) | Selector is a label query over pods that are managed by the daemon set. Must match in order to be controlled. If empty, defaulted to labels on Pod template. More info: http://kubernetes.io/docs/user-guide/labels#label-selectors | [optional] 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | Template is the object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template&#39;s node selector (or on every node if no node selector is specified). More info: http://kubernetes.io/docs/user-guide/replication-controller#pod-template | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


