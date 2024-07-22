# V1PodSchedulingGate

PodSchedulingGate is associated to a Pod to guard its scheduling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the scheduling gate. Each scheduling gate must have a unique name field. | 

## Example

```python
from kubernetes.client.models.v1_pod_scheduling_gate import V1PodSchedulingGate

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodSchedulingGate from a JSON string
v1_pod_scheduling_gate_instance = V1PodSchedulingGate.from_json(json)
# print the JSON string representation of the object
print V1PodSchedulingGate.to_json()

# convert the object into a dict
v1_pod_scheduling_gate_dict = v1_pod_scheduling_gate_instance.to_dict()
# create an instance of V1PodSchedulingGate from a dict
v1_pod_scheduling_gate_form_dict = v1_pod_scheduling_gate.from_dict(v1_pod_scheduling_gate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


