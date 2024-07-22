# V2HorizontalPodAutoscalerList

HorizontalPodAutoscalerList is a list of horizontal pod autoscaler objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**items** | [**List[V2HorizontalPodAutoscaler]**](V2HorizontalPodAutoscaler.md) | items is the list of horizontal pod autoscaler objects. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v2_horizontal_pod_autoscaler_list import V2HorizontalPodAutoscalerList

# TODO update the JSON string below
json = "{}"
# create an instance of V2HorizontalPodAutoscalerList from a JSON string
v2_horizontal_pod_autoscaler_list_instance = V2HorizontalPodAutoscalerList.from_json(json)
# print the JSON string representation of the object
print V2HorizontalPodAutoscalerList.to_json()

# convert the object into a dict
v2_horizontal_pod_autoscaler_list_dict = v2_horizontal_pod_autoscaler_list_instance.to_dict()
# create an instance of V2HorizontalPodAutoscalerList from a dict
v2_horizontal_pod_autoscaler_list_form_dict = v2_horizontal_pod_autoscaler_list.from_dict(v2_horizontal_pod_autoscaler_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


