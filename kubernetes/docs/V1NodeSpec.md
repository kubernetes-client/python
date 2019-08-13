# V1NodeSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_source** | [**V1NodeConfigSource**](V1NodeConfigSource.md) |  | [optional] 
**external_id** | **str** | Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966 | [optional] 
**pod_cidr** | **str** | PodCIDR represents the pod IP range assigned to the node. | [optional] 
**provider_id** | **str** | ID of the node assigned by the cloud provider in the format: &lt;ProviderName&gt;://&lt;ProviderSpecificNodeID&gt; | [optional] 
**taints** | [**list[V1Taint]**](V1Taint.md) | If specified, the node&#39;s taints. | [optional] 
**unschedulable** | **bool** | Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


