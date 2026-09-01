# V1alpha3CompositePodGroupSchedulingConstraints

CompositePodGroupSchedulingConstraints defines scheduling constraints (e.g. topology) for a CompositePodGroup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topology** | [**List[V1alpha3TopologyConstraint]**](V1alpha3TopologyConstraint.md) | topology defines the topology constraints for the composite pod group. Currently only a single topology constraint can be specified. This may change in the future. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1alpha3_composite_pod_group_scheduling_constraints import V1alpha3CompositePodGroupSchedulingConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3CompositePodGroupSchedulingConstraints from a JSON string
v1alpha3_composite_pod_group_scheduling_constraints_instance = V1alpha3CompositePodGroupSchedulingConstraints.from_json(json)
# print the JSON string representation of the object
print(V1alpha3CompositePodGroupSchedulingConstraints.to_json())

# convert the object into a dict
v1alpha3_composite_pod_group_scheduling_constraints_dict = v1alpha3_composite_pod_group_scheduling_constraints_instance.to_dict()
# create an instance of V1alpha3CompositePodGroupSchedulingConstraints from a dict
v1alpha3_composite_pod_group_scheduling_constraints_from_dict = V1alpha3CompositePodGroupSchedulingConstraints.from_dict(v1alpha3_composite_pod_group_scheduling_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
