# V1alpha2ResourceClass

ResourceClass is used by administrators to influence how resources are allocated.  This is an alpha type and requires enabling the DynamicResourceAllocation feature gate.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**driver_name** | **str** | DriverName defines the name of the dynamic resource driver that is used for allocation of a ResourceClaim that uses this class.  Resource drivers have a unique name in forward domain order (acme.example.com). | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**parameters_ref** | [**V1alpha2ResourceClassParametersReference**](V1alpha2ResourceClassParametersReference.md) |  | [optional] 
**structured_parameters** | **bool** | If and only if allocation of claims using this class is handled via structured parameters, then StructuredParameters must be set to true. | [optional] 
**suitable_nodes** | [**V1NodeSelector**](V1NodeSelector.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


