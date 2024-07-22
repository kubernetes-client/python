# V1Scheduling

Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_selector** | **Dict[str, str]** | nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod&#39;s existing nodeSelector. Any conflicts will cause the pod to be rejected in admission. | [optional] 
**tolerations** | [**List[V1Toleration]**](V1Toleration.md) | tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass. | [optional] 

## Example

```python
from kubernetes.client.models.v1_scheduling import V1Scheduling

# TODO update the JSON string below
json = "{}"
# create an instance of V1Scheduling from a JSON string
v1_scheduling_instance = V1Scheduling.from_json(json)
# print the JSON string representation of the object
print V1Scheduling.to_json()

# convert the object into a dict
v1_scheduling_dict = v1_scheduling_instance.to_dict()
# create an instance of V1Scheduling from a dict
v1_scheduling_form_dict = v1_scheduling.from_dict(v1_scheduling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


