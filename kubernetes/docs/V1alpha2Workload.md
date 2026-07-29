# V1alpha2Workload

Workload allows for expressing scheduling constraints that should be used when managing the lifecycle of workloads from the scheduling perspective, including scheduling, preemption, eviction and other phases. Workload API enablement is toggled by the GenericWorkload feature gate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional]
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional]
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional]
**spec** | [**V1alpha2WorkloadSpec**](V1alpha2WorkloadSpec.md) |  |

## Example

```python
from kubernetes.client.models.v1alpha2_workload import V1alpha2Workload

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha2Workload from a JSON string
v1alpha2_workload_instance = V1alpha2Workload.from_json(json)
# print the JSON string representation of the object
print(V1alpha2Workload.to_json())

# convert the object into a dict
v1alpha2_workload_dict = v1alpha2_workload_instance.to_dict()
# create an instance of V1alpha2Workload from a dict
v1alpha2_workload_from_dict = V1alpha2Workload.from_dict(v1alpha2_workload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
