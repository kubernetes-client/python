# V1beta1PodGroup

PodGroup represents a runtime instance of pods grouped together. PodGroups are created by workload controllers (Job, LWS, JobSet, etc...) from Workload.podGroupTemplates. PodGroup API enablement is toggled by the GenericWorkload feature gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1beta1PodGroupSpec**](V1beta1PodGroupSpec.md) |  |
**status** | [**V1beta1PodGroupStatus**](V1beta1PodGroupStatus.md) |  | [optional]

## Example

```python
from kubernetes.aio.client.models.v1beta1_pod_group import V1beta1PodGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1PodGroup from a JSON string
v1beta1_pod_group_instance = V1beta1PodGroup.from_json(json)
# print the JSON string representation of the object
print(V1beta1PodGroup.to_json())

# convert the object into a dict
v1beta1_pod_group_dict = v1beta1_pod_group_instance.to_dict()
# create an instance of V1beta1PodGroup from a dict
v1beta1_pod_group_from_dict = V1beta1PodGroup.from_dict(v1beta1_pod_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
