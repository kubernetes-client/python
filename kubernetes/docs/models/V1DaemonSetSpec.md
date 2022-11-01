# kubernetes.client.model.v1_daemon_set_spec.V1DaemonSetSpec

DaemonSetSpec is the specification of a daemon set.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DaemonSetSpec is the specification of a daemon set. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) |  | 
**selector** | [**V1LabelSelector**](V1LabelSelector.md) | [**V1LabelSelector**](V1LabelSelector.md) |  | 
**minReadySeconds** | decimal.Decimal, int,  | decimal.Decimal,  | The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready). | [optional] value must be a 32 bit integer
**revisionHistoryLimit** | decimal.Decimal, int,  | decimal.Decimal,  | The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10. | [optional] value must be a 32 bit integer
**updateStrategy** | [**V1DaemonSetUpdateStrategy**](V1DaemonSetUpdateStrategy.md) | [**V1DaemonSetUpdateStrategy**](V1DaemonSetUpdateStrategy.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

