# V1ReplicaSet

ReplicaSet ensures that a specified number of pod replicas are running at any given time.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the kubernetes.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**spec** | [**V1ReplicaSetSpec**](V1ReplicaSetSpec.md) |  | [optional] 
**status** | [**V1ReplicaSetStatus**](V1ReplicaSetStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_replica_set import V1ReplicaSet

# TODO update the JSON string below
json = "{}"
# create an instance of V1ReplicaSet from a JSON string
v1_replica_set_instance = V1ReplicaSet.from_json(json)
# print the JSON string representation of the object
print V1ReplicaSet.to_json()

# convert the object into a dict
v1_replica_set_dict = v1_replica_set_instance.to_dict()
# create an instance of V1ReplicaSet from a dict
v1_replica_set_form_dict = v1_replica_set.from_dict(v1_replica_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


