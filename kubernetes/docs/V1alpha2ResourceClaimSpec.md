# V1alpha2ResourceClaimSpec

ResourceClaimSpec defines how a resource is to be allocated.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_mode** | **str** | Allocation can start immediately or when a Pod wants to use the resource. \&quot;WaitForFirstConsumer\&quot; is the default. | [optional] 
**parameters_ref** | [**V1alpha2ResourceClaimParametersReference**](V1alpha2ResourceClaimParametersReference.md) |  | [optional] 
**resource_class_name** | **str** | ResourceClassName references the driver and additional parameters via the name of a ResourceClass that was created as part of the driver deployment. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


