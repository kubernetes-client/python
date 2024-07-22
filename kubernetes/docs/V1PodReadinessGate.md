# V1PodReadinessGate

PodReadinessGate contains the reference to a pod condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition_type** | **str** | ConditionType refers to a condition in the pod&#39;s condition list with matching type. | 

## Example

```python
from kubernetes.client.models.v1_pod_readiness_gate import V1PodReadinessGate

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodReadinessGate from a JSON string
v1_pod_readiness_gate_instance = V1PodReadinessGate.from_json(json)
# print the JSON string representation of the object
print V1PodReadinessGate.to_json()

# convert the object into a dict
v1_pod_readiness_gate_dict = v1_pod_readiness_gate_instance.to_dict()
# create an instance of V1PodReadinessGate from a dict
v1_pod_readiness_gate_form_dict = v1_pod_readiness_gate.from_dict(v1_pod_readiness_gate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


