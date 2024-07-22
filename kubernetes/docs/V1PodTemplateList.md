# V1PodTemplateList

PodTemplateList is a list of PodTemplates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[V1PodTemplate]**](V1PodTemplate.md) | List of pod templates | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_pod_template_list import V1PodTemplateList

# TODO update the JSON string below
json = "{}"
# create an instance of V1PodTemplateList from a JSON string
v1_pod_template_list_instance = V1PodTemplateList.from_json(json)
# print the JSON string representation of the object
print V1PodTemplateList.to_json()

# convert the object into a dict
v1_pod_template_list_dict = v1_pod_template_list_instance.to_dict()
# create an instance of V1PodTemplateList from a dict
v1_pod_template_list_form_dict = v1_pod_template_list.from_dict(v1_pod_template_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


