# V1alpha1EvictionSpec

EvictionSpec is a specification of an Eviction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**V1alpha1EvictionTarget**](V1alpha1EvictionTarget.md) |  |

## Example

```python
from kubernetes.client.models.v1alpha1_eviction_spec import V1alpha1EvictionSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1EvictionSpec from a JSON string
v1alpha1_eviction_spec_instance = V1alpha1EvictionSpec.from_json(json)
# print the JSON string representation of the object
print(V1alpha1EvictionSpec.to_json())

# convert the object into a dict
v1alpha1_eviction_spec_dict = v1alpha1_eviction_spec_instance.to_dict()
# create an instance of V1alpha1EvictionSpec from a dict
v1alpha1_eviction_spec_from_dict = V1alpha1EvictionSpec.from_dict(v1alpha1_eviction_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
