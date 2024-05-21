# V1alpha2ResourceClassParameters

ResourceClassParameters defines resource requests for a ResourceClass in an in-tree format understood by Kubernetes.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**filters** | [**list[V1alpha2ResourceFilter]**](V1alpha2ResourceFilter.md) | Filters describes additional contraints that must be met when using the class. | [optional] 
**generated_from** | [**V1alpha2ResourceClassParametersReference**](V1alpha2ResourceClassParametersReference.md) |  | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**vendor_parameters** | [**list[V1alpha2VendorParameters]**](V1alpha2VendorParameters.md) | VendorParameters are arbitrary setup parameters for all claims using this class. They are ignored while allocating the claim. There must not be more than one entry per driver. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


