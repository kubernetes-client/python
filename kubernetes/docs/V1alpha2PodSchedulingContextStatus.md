# V1alpha2PodSchedulingContextStatus

PodSchedulingContextStatus describes where resources for the Pod can be allocated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_claims** | [**List[V1alpha2ResourceClaimSchedulingStatus]**](V1alpha2ResourceClaimSchedulingStatus.md) | ResourceClaims describes resource availability for each pod.spec.resourceClaim entry where the corresponding ResourceClaim uses \&quot;WaitForFirstConsumer\&quot; allocation mode. | [optional] 

## Example

```python
from kubernetes.client.models.v1alpha2_pod_scheduling_context_status import V1alpha2PodSchedulingContextStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2PodSchedulingContextStatus from a JSON string
v1alpha2_pod_scheduling_context_status_instance = V1alpha2PodSchedulingContextStatus.from_json(json)
# print the JSON string representation of the object
print V1alpha2PodSchedulingContextStatus.to_json()

# convert the object into a dict
v1alpha2_pod_scheduling_context_status_dict = v1alpha2_pod_scheduling_context_status_instance.to_dict()
# create an instance of V1alpha2PodSchedulingContextStatus from a dict
v1alpha2_pod_scheduling_context_status_form_dict = v1alpha2_pod_scheduling_context_status.from_dict(v1alpha2_pod_scheduling_context_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


