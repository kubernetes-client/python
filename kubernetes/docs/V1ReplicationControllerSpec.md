# V1ReplicationControllerSpec

ReplicationControllerSpec is the specification of a replication controller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_ready_seconds** | **int** | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) | [optional] 
**replicas** | **int** | Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller | [optional] 
**selector** | **Dict[str, str]** | Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors | [optional] 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_replication_controller_spec import V1ReplicationControllerSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1ReplicationControllerSpec from a JSON string
v1_replication_controller_spec_instance = V1ReplicationControllerSpec.from_json(json)
# print the JSON string representation of the object
print V1ReplicationControllerSpec.to_json()

# convert the object into a dict
v1_replication_controller_spec_dict = v1_replication_controller_spec_instance.to_dict()
# create an instance of V1ReplicationControllerSpec from a dict
v1_replication_controller_spec_form_dict = v1_replication_controller_spec.from_dict(v1_replication_controller_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


