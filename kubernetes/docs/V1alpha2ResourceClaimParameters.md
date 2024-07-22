# V1alpha2ResourceClaimParameters

ResourceClaimParameters defines resource requests for a ResourceClaim in an in-tree format understood by Kubernetes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**driver_requests** | [**List[V1alpha2DriverRequests]**](V1alpha2DriverRequests.md) | DriverRequests describes all resources that are needed for the allocated claim. A single claim may use resources coming from different drivers. For each driver, this array has at most one entry which then may have one or more per-driver requests.  May be empty, in which case the claim can always be allocated. | [optional] 
**generated_from** | [**V1alpha2ResourceClaimParametersReference**](V1alpha2ResourceClaimParametersReference.md) |  | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**shareable** | **bool** | Shareable indicates whether the allocated claim is meant to be shareable by multiple consumers at the same time. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_claim_parameters import V1alpha2ResourceClaimParameters

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceClaimParameters from a JSON string
v1alpha2_resource_claim_parameters_instance = V1alpha2ResourceClaimParameters.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceClaimParameters.to_json()

# convert the object into a dict
v1alpha2_resource_claim_parameters_dict = v1alpha2_resource_claim_parameters_instance.to_dict()
# create an instance of V1alpha2ResourceClaimParameters from a dict
v1alpha2_resource_claim_parameters_form_dict = v1alpha2_resource_claim_parameters.from_dict(v1alpha2_resource_claim_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


