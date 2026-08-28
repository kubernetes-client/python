# V1JobSchedulingConfiguration

JobSchedulingConfiguration composes the reusable workload-aware scheduling building blocks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disruption_mode** | [**V1alpha3WorkloadPodGroupDisruptionMode**](V1alpha3WorkloadPodGroupDisruptionMode.md) |  | [optional]
**resource_claims** | [**List[V1alpha3WorkloadPodGroupResourceClaim]**](V1alpha3WorkloadPodGroupResourceClaim.md) | ResourceClaims defines which ResourceClaims may be shared among Pods in the Job. Pods consume the devices allocated to a PodGroup&#39;s claim by defining a claim in its own Spec.ResourceClaims that matches the PodGroup&#39;s claim exactly. The claim must have the same name and refer to the same ResourceClaim or ResourceClaimTemplate. At most 4 claims may be set, matching the limit on the resulting PodGroup. This list is immutable after creation: entries may neither be added, removed, nor modified. | [optional]
**scheduling_constraints** | [**V1alpha3WorkloadPodGroupSchedulingConstraints**](V1alpha3WorkloadPodGroupSchedulingConstraints.md) |  | [optional]
**scheduling_policy** | [**V1alpha3WorkloadPodGroupSchedulingPolicy**](V1alpha3WorkloadPodGroupSchedulingPolicy.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1_job_scheduling_configuration import V1JobSchedulingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of V1JobSchedulingConfiguration from a JSON string
v1_job_scheduling_configuration_instance = V1JobSchedulingConfiguration.from_json(json)
# print the JSON string representation of the object
print(V1JobSchedulingConfiguration.to_json())

# convert the object into a dict
v1_job_scheduling_configuration_dict = v1_job_scheduling_configuration_instance.to_dict()
# create an instance of V1JobSchedulingConfiguration from a dict
v1_job_scheduling_configuration_from_dict = V1JobSchedulingConfiguration.from_dict(v1_job_scheduling_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
