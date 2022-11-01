# kubernetes.client.model.v1_weighted_pod_affinity_term.V1WeightedPodAffinityTerm

The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s) | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**podAffinityTerm** | [**V1PodAffinityTerm**](V1PodAffinityTerm.md) | [**V1PodAffinityTerm**](V1PodAffinityTerm.md) |  | 
**weight** | decimal.Decimal, int,  | decimal.Decimal,  | weight associated with matching the corresponding podAffinityTerm, in the range 1-100. | value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

