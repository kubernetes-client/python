# V1alpha1EvictionRequestStatus

EvictionRequestStatus represents the last observed status of the eviction request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1Condition]**](V1Condition.md) | conditions contain information about the eviction request.  EvictionRequest specific conditions are: TargetEvicted or Failed (managed by evictionrequest-controller). - Failed means that the eviction request is no longer being processed   by any eviction responder. This can happen if the request is canceled or if no responder   managed to evict the target (e.g. terminate or delete a pod). - TargetEvicted means that the target has been evicted (e.g. a pod has been terminated or deleted).  These conditions can be reset if the eviction was unsuccessful and a new Eviction intent has been submitted.  The maximum length of the conditions list is 100. | [optional]
**observed_generation** | **int** | observedGeneration is EvictionRequest&#39;s .metadata.generation observed by the evictionrequest-controller. The observed generation value cannot be negative and can only be incremented. The minimum value is 1. This field is managed by evictionrequest-controller. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1alpha1_eviction_request_status import V1alpha1EvictionRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1EvictionRequestStatus from a JSON string
v1alpha1_eviction_request_status_instance = V1alpha1EvictionRequestStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha1EvictionRequestStatus.to_json())

# convert the object into a dict
v1alpha1_eviction_request_status_dict = v1alpha1_eviction_request_status_instance.to_dict()
# create an instance of V1alpha1EvictionRequestStatus from a dict
v1alpha1_eviction_request_status_from_dict = V1alpha1EvictionRequestStatus.from_dict(v1alpha1_eviction_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
