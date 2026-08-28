# V1alpha1EvictionRequestPodReference

EvictionRequestPodReference contains enough information to locate the referenced pod inside the same namespace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the target. This field is required. |
**uid** | **str** | uid of the target. It can be found in .metadata.uid of the target and is a lowercase UUID in 8-4-4-4-12 format. This field is required. |

## Example

```python
from kubernetes.aio.client.models.v1alpha1_eviction_request_pod_reference import V1alpha1EvictionRequestPodReference

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1EvictionRequestPodReference from a JSON string
v1alpha1_eviction_request_pod_reference_instance = V1alpha1EvictionRequestPodReference.from_json(json)
# print the JSON string representation of the object
print(V1alpha1EvictionRequestPodReference.to_json())

# convert the object into a dict
v1alpha1_eviction_request_pod_reference_dict = v1alpha1_eviction_request_pod_reference_instance.to_dict()
# create an instance of V1alpha1EvictionRequestPodReference from a dict
v1alpha1_eviction_request_pod_reference_from_dict = V1alpha1EvictionRequestPodReference.from_dict(v1alpha1_eviction_request_pod_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
