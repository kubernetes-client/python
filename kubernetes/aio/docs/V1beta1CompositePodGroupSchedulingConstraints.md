# V1beta1CompositePodGroupSchedulingConstraints

CompositePodGroupSchedulingConstraints defines scheduling constraints (e.g. topology) for a CompositePodGroup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topology** | [**List[V1beta1TopologyConstraint]**](V1beta1TopologyConstraint.md) | topology defines the topology constraints for the composite pod group. Currently only a single topology constraint can be specified. This may change in the future. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1beta1_composite_pod_group_scheduling_constraints import V1beta1CompositePodGroupSchedulingConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1CompositePodGroupSchedulingConstraints from a JSON string
v1beta1_composite_pod_group_scheduling_constraints_instance = V1beta1CompositePodGroupSchedulingConstraints.from_json(json)
# print the JSON string representation of the object
print(V1beta1CompositePodGroupSchedulingConstraints.to_json())

# convert the object into a dict
v1beta1_composite_pod_group_scheduling_constraints_dict = v1beta1_composite_pod_group_scheduling_constraints_instance.to_dict()
# create an instance of V1beta1CompositePodGroupSchedulingConstraints from a dict
v1beta1_composite_pod_group_scheduling_constraints_from_dict = V1beta1CompositePodGroupSchedulingConstraints.from_dict(v1beta1_composite_pod_group_scheduling_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
