# V1alpha2PodSchedulingContextSpec

PodSchedulingContextSpec describes where resources for the Pod are needed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**potential_nodes** | **list[str]** | PotentialNodes lists nodes where the Pod might be able to run.  The size of this field is limited to 128. This is large enough for many clusters. Larger clusters may need more attempts to find a node that suits all pending resources. This may get increased in the future, but not reduced. | [optional] 
**selected_node** | **str** | SelectedNode is the node for which allocation of ResourceClaims that are referenced by the Pod and that use \&quot;WaitForFirstConsumer\&quot; allocation is to be attempted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


