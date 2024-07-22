# V1WeightedPodAffinityTerm

The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod_affinity_term** | [**V1PodAffinityTerm**](V1PodAffinityTerm.md) |  | 
**weight** | **int** | weight associated with matching the corresponding podAffinityTerm, in the range 1-100. | 

## Example

```python
from kubernetes.client.models.v1_weighted_pod_affinity_term import V1WeightedPodAffinityTerm

# TODO update the JSON string below
json = "{}"
# create an instance of V1WeightedPodAffinityTerm from a JSON string
v1_weighted_pod_affinity_term_instance = V1WeightedPodAffinityTerm.from_json(json)
# print the JSON string representation of the object
print V1WeightedPodAffinityTerm.to_json()

# convert the object into a dict
v1_weighted_pod_affinity_term_dict = v1_weighted_pod_affinity_term_instance.to_dict()
# create an instance of V1WeightedPodAffinityTerm from a dict
v1_weighted_pod_affinity_term_form_dict = v1_weighted_pod_affinity_term.from_dict(v1_weighted_pod_affinity_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


