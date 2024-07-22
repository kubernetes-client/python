# V1ScaleStatus

ScaleStatus represents the current status of a scale subresource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicas** | **int** | replicas is the actual number of observed instances of the scaled object. | 
**selector** | **str** | selector is the label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by kubernetes.clients. The string will be in the same format as the query-param syntax. More info about label selectors: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/ | [optional] 

## Example

```python
from kubernetes.client.models.v1_scale_status import V1ScaleStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1ScaleStatus from a JSON string
v1_scale_status_instance = V1ScaleStatus.from_json(json)
# print the JSON string representation of the object
print V1ScaleStatus.to_json()

# convert the object into a dict
v1_scale_status_dict = v1_scale_status_instance.to_dict()
# create an instance of V1ScaleStatus from a dict
v1_scale_status_form_dict = v1_scale_status.from_dict(v1_scale_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


