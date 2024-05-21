# V1alpha2StructuredResourceHandle

StructuredResourceHandle is the in-tree representation of the allocation result.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_name** | **str** | NodeName is the name of the node providing the necessary resources if the resources are local to a node. | [optional] 
**results** | [**list[V1alpha2DriverAllocationResult]**](V1alpha2DriverAllocationResult.md) | Results lists all allocated driver resources. | 
**vendor_claim_parameters** | [**object**](.md) | VendorClaimParameters are the per-claim configuration parameters from the resource claim parameters at the time that the claim was allocated. | [optional] 
**vendor_class_parameters** | [**object**](.md) | VendorClassParameters are the per-claim configuration parameters from the resource class at the time that the claim was allocated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


