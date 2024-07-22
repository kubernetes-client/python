# V1StatefulSet

StatefulSet represents a set of pods with consistent identities. Identities are defined as:   - Network: A single stable DNS and hostname.   - Storage: As many VolumeClaims as requested.  The StatefulSet guarantees that a given network identity will always map to the same storage identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1StatefulSetSpec**](V1StatefulSetSpec.md) |  | [optional] 
**status** | [**V1StatefulSetStatus**](V1StatefulSetStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_stateful_set import V1StatefulSet

# TODO update the JSON string below
json = "{}"
# create an instance of V1StatefulSet from a JSON string
v1_stateful_set_instance = V1StatefulSet.from_json(json)
# print the JSON string representation of the object
print V1StatefulSet.to_json()

# convert the object into a dict
v1_stateful_set_dict = v1_stateful_set_instance.to_dict()
# create an instance of V1StatefulSet from a dict
v1_stateful_set_form_dict = v1_stateful_set.from_dict(v1_stateful_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


