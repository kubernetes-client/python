# V1alpha2PodGroup

PodGroup represents a runtime instance of pods grouped together. PodGroups are created by workload controllers (Job, LWS, JobSet, etc...) from Workload.podGroupTemplates. PodGroup API enablement is toggled by the GenericWorkload feature gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1alpha2PodGroupSpec**](V1alpha2PodGroupSpec.md) |  |
**status** | [**V1alpha2PodGroupStatus**](V1alpha2PodGroupStatus.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1alpha2_pod_group import V1alpha2PodGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2PodGroup from a JSON string
v1alpha2_pod_group_instance = V1alpha2PodGroup.from_json(json)
# print the JSON string representation of the object
print(V1alpha2PodGroup.to_json())

# convert the object into a dict
v1alpha2_pod_group_dict = v1alpha2_pod_group_instance.to_dict()
# create an instance of V1alpha2PodGroup from a dict
v1alpha2_pod_group_from_dict = V1alpha2PodGroup.from_dict(v1alpha2_pod_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
