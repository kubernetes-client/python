# V1alpha2TopologyConstraint

TopologyConstraint defines a topology constraint for a PodGroup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key specifies the key of the node label representing the topology domain. All pods within the PodGroup must be colocated within the same domain instance. Different PodGroups can land on different domain instances even if they derive from the same PodGroupTemplate. Examples: \&quot;topology.kubernetes.io/rack\&quot; |

## Example

```python
from kubernetes.client.models.v1alpha2_topology_constraint import V1alpha2TopologyConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2TopologyConstraint from a JSON string
v1alpha2_topology_constraint_instance = V1alpha2TopologyConstraint.from_json(json)
# print the JSON string representation of the object
print(V1alpha2TopologyConstraint.to_json())

# convert the object into a dict
v1alpha2_topology_constraint_dict = v1alpha2_topology_constraint_instance.to_dict()
# create an instance of V1alpha2TopologyConstraint from a dict
v1alpha2_topology_constraint_from_dict = V1alpha2TopologyConstraint.from_dict(v1alpha2_topology_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
