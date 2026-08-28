# V1alpha3CompositePodGroup

CompositePodGroup represents a runtime instance of pod groups grouped together. CompositePodGroups are created by workload controllers (LWS, JobSet, etc...) from Workload.compositePodGroupTemplates. CompositePodGroup API enablement is toggled by the CompositePodGroup feature gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1alpha3CompositePodGroupSpec**](V1alpha3CompositePodGroupSpec.md) |  |
**status** | [**V1alpha3CompositePodGroupStatus**](V1alpha3CompositePodGroupStatus.md) |  | [optional]

## Example

```python
from kubernetes.client.models.v1alpha3_composite_pod_group import V1alpha3CompositePodGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3CompositePodGroup from a JSON string
v1alpha3_composite_pod_group_instance = V1alpha3CompositePodGroup.from_json(json)
# print the JSON string representation of the object
print(V1alpha3CompositePodGroup.to_json())

# convert the object into a dict
v1alpha3_composite_pod_group_dict = v1alpha3_composite_pod_group_instance.to_dict()
# create an instance of V1alpha3CompositePodGroup from a dict
v1alpha3_composite_pod_group_from_dict = V1alpha3CompositePodGroup.from_dict(v1alpha3_composite_pod_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
