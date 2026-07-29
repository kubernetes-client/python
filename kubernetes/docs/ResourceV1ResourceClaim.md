# ResourceV1ResourceClaim

ResourceClaim describes a request for access to resources in the cluster, for use by workloads. For example, if a workload needs an accelerator device with specific properties, this is how that request is expressed. The status stanza tracks whether this claim has been satisfied and what specific resources have been allocated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1ResourceClaimSpec**](V1ResourceClaimSpec.md) |  |
**status** | [**V1ResourceClaimStatus**](V1ResourceClaimStatus.md) |  | [optional]

## Example

```python
from kubernetes.client.models.resource_v1_resource_claim import ResourceV1ResourceClaim

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceV1ResourceClaim from a JSON string
resource_v1_resource_claim_instance = ResourceV1ResourceClaim.from_json(json)
# print the JSON string representation of the object
print(ResourceV1ResourceClaim.to_json())

# convert the object into a dict
resource_v1_resource_claim_dict = resource_v1_resource_claim_instance.to_dict()
# create an instance of ResourceV1ResourceClaim from a dict
resource_v1_resource_claim_from_dict = ResourceV1ResourceClaim.from_dict(resource_v1_resource_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
