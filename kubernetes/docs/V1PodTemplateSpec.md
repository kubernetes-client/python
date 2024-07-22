# V1PodTemplateSpec

PodTemplateSpec describes the data a pod should have when created from a template

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1PodSpec**](V1PodSpec.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_pod_template_spec import V1PodTemplateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodTemplateSpec from a JSON string
v1_pod_template_spec_instance = V1PodTemplateSpec.from_json(json)
# print the JSON string representation of the object
print V1PodTemplateSpec.to_json()

# convert the object into a dict
v1_pod_template_spec_dict = v1_pod_template_spec_instance.to_dict()
# create an instance of V1PodTemplateSpec from a dict
v1_pod_template_spec_form_dict = v1_pod_template_spec.from_dict(v1_pod_template_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


