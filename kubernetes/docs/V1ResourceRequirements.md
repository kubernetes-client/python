# V1ResourceRequirements

ResourceRequirements describes the compute resource requirements.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claims** | [**list[CoreV1ResourceClaim]**](CoreV1ResourceClaim.md) | Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This field depends on the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers. | [optional] 
**limits** | **dict(str, str)** | Limits describes the maximum amount of compute resources allowed. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 
**requests** | **dict(str, str)** | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


