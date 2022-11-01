# kubernetes.client.model.v1_preferred_scheduling_term.V1PreferredSchedulingTerm

An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it's a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it&#x27;s a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**preference** | [**V1NodeSelectorTerm**](V1NodeSelectorTerm.md) | [**V1NodeSelectorTerm**](V1NodeSelectorTerm.md) |  | 
**weight** | decimal.Decimal, int,  | decimal.Decimal,  | Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100. | value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

