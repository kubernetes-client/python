# V1alpha1Mutation

Mutation specifies the CEL expression which is used to apply the Mutation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_configuration** | [**V1alpha1ApplyConfiguration**](V1alpha1ApplyConfiguration.md) |  | [optional]
**json_patch** | [**V1alpha1JSONPatch**](V1alpha1JSONPatch.md) |  | [optional]
**patch_type** | **str** | patchType indicates the patch strategy used. Allowed values are \&quot;ApplyConfiguration\&quot; and \&quot;JSONPatch\&quot;. Required. |

## Example

```python
from kubernetes.client.models.v1alpha1_mutation import V1alpha1Mutation

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1Mutation from a JSON string
v1alpha1_mutation_instance = V1alpha1Mutation.from_json(json)
# print the JSON string representation of the object
print(V1alpha1Mutation.to_json())

# convert the object into a dict
v1alpha1_mutation_dict = v1alpha1_mutation_instance.to_dict()
# create an instance of V1alpha1Mutation from a dict
v1alpha1_mutation_from_dict = V1alpha1Mutation.from_dict(v1alpha1_mutation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
