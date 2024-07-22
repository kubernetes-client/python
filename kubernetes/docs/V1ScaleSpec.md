# V1ScaleSpec

ScaleSpec describes the attributes of a scale subresource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicas** | **int** | replicas is the desired number of instances for the scaled object. | [optional] 

## Example

```python
from kubernetes.client.models.v1_scale_spec import V1ScaleSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1ScaleSpec from a JSON string
v1_scale_spec_instance = V1ScaleSpec.from_json(json)
# print the JSON string representation of the object
print V1ScaleSpec.to_json()

# convert the object into a dict
v1_scale_spec_dict = v1_scale_spec_instance.to_dict()
# create an instance of V1ScaleSpec from a dict
v1_scale_spec_form_dict = v1_scale_spec.from_dict(v1_scale_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


