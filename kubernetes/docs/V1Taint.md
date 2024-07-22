# V1Taint

The node this Taint is attached to has the \"effect\" on any pod that does not tolerate the Taint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute. | 
**key** | **str** | Required. The taint key to be applied to a node. | 
**time_added** | **datetime** | TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints. | [optional] 
**value** | **str** | The taint value corresponding to the taint key. | [optional] 

## Example

```python
from kubernetes.client.models.v1_taint import V1Taint

# TODO update the JSON string below
json = "{}"
# create an instance of V1Taint from a JSON string
v1_taint_instance = V1Taint.from_json(json)
# print the JSON string representation of the object
print V1Taint.to_json()

# convert the object into a dict
v1_taint_dict = v1_taint_instance.to_dict()
# create an instance of V1Taint from a dict
v1_taint_form_dict = v1_taint.from_dict(v1_taint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


