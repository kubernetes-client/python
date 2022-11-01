# kubernetes.client.model.v1_replica_set_spec.V1ReplicaSetSpec

ReplicaSetSpec is the specification of a ReplicaSet.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ReplicaSetSpec is the specification of a ReplicaSet. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**selector** | [**V1LabelSelector**](V1LabelSelector.md) | [**V1LabelSelector**](V1LabelSelector.md) |  | 
**minReadySeconds** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready) | [optional] value must be a 32 bit integer
**replicas** | decimal.Decimal, int,  | decimal.Decimal,  | Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller | [optional] value must be a 32 bit integer
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

