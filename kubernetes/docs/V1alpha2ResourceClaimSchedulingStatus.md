# V1alpha2ResourceClaimSchedulingStatus

ResourceClaimSchedulingStatus contains information about one particular ResourceClaim with \"WaitForFirstConsumer\" allocation mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name matches the pod.spec.resourceClaims[*].Name field. | [optional] 
**unsuitable_nodes** | **List[str]** | UnsuitableNodes lists nodes that the ResourceClaim cannot be allocated for.  The size of this field is limited to 128, the same as for PodSchedulingSpec.PotentialNodes. This may get increased in the future, but not reduced. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_resource_claim_scheduling_status import V1alpha2ResourceClaimSchedulingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2ResourceClaimSchedulingStatus from a JSON string
v1alpha2_resource_claim_scheduling_status_instance = V1alpha2ResourceClaimSchedulingStatus.from_json(json)
# print the JSON string representation of the object
print V1alpha2ResourceClaimSchedulingStatus.to_json()

# convert the object into a dict
v1alpha2_resource_claim_scheduling_status_dict = v1alpha2_resource_claim_scheduling_status_instance.to_dict()
# create an instance of V1alpha2ResourceClaimSchedulingStatus from a dict
v1alpha2_resource_claim_scheduling_status_form_dict = v1alpha2_resource_claim_scheduling_status.from_dict(v1alpha2_resource_claim_scheduling_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


