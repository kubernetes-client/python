# V1alpha1EvictionRequestTarget

EvictionRequestTarget contains a reference to an object that should be evicted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pod** | [**V1alpha1EvictionRequestPodReference**](V1alpha1EvictionRequestPodReference.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1alpha1_eviction_request_target import V1alpha1EvictionRequestTarget

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1EvictionRequestTarget from a JSON string
v1alpha1_eviction_request_target_instance = V1alpha1EvictionRequestTarget.from_json(json)
# print the JSON string representation of the object
print(V1alpha1EvictionRequestTarget.to_json())

# convert the object into a dict
v1alpha1_eviction_request_target_dict = v1alpha1_eviction_request_target_instance.to_dict()
# create an instance of V1alpha1EvictionRequestTarget from a dict
v1alpha1_eviction_request_target_from_dict = V1alpha1EvictionRequestTarget.from_dict(v1alpha1_eviction_request_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
