# V1Affinity

Affinity is a group of affinity scheduling rules.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_affinity** | [**V1NodeAffinity**](V1NodeAffinity.md) |  | [optional] 
**pod_affinity** | [**V1PodAffinity**](V1PodAffinity.md) |  | [optional] 
**pod_anti_affinity** | [**V1PodAntiAffinity**](V1PodAntiAffinity.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_affinity import V1Affinity

# TODO update the JSON string below
json = "{}"
# create an instance of V1Affinity from a JSON string
v1_affinity_instance = V1Affinity.from_json(json)
# print the JSON string representation of the object
print V1Affinity.to_json()

# convert the object into a dict
v1_affinity_dict = v1_affinity_instance.to_dict()
# create an instance of V1Affinity from a dict
v1_affinity_form_dict = v1_affinity.from_dict(v1_affinity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


