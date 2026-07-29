# V1beta1Mutation

Mutation specifies the CEL expression which is used to apply the Mutation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_configuration** | [**V1beta1ApplyConfiguration**](V1beta1ApplyConfiguration.md) |  | [optional]
**json_patch** | [**V1beta1JSONPatch**](V1beta1JSONPatch.md) |  | [optional]
**patch_type** | **str** | patchType indicates the patch strategy used. Allowed values are \&quot;ApplyConfiguration\&quot; and \&quot;JSONPatch\&quot;. Required. |

## Example

```python
from kubernetes.client.models.v1beta1_mutation import V1beta1Mutation

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1Mutation from a JSON string
v1beta1_mutation_instance = V1beta1Mutation.from_json(json)
# print the JSON string representation of the object
print(V1beta1Mutation.to_json())

# convert the object into a dict
v1beta1_mutation_dict = v1beta1_mutation_instance.to_dict()
# create an instance of V1beta1Mutation from a dict
v1beta1_mutation_from_dict = V1beta1Mutation.from_dict(v1beta1_mutation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
