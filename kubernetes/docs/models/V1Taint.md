# kubernetes.client.model.v1_taint.V1Taint

The node this Taint is attached to has the \"effect\" on any pod that does not tolerate the Taint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The node this Taint is attached to has the \&quot;effect\&quot; on any pod that does not tolerate the Taint. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**effect** | str,  | str,  | Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.   | 
**key** | str,  | str,  | Required. The taint key to be applied to a node. | 
**timeAdded** | str, datetime,  | str,  | TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints. | [optional] value must conform to RFC-3339 date-time
**value** | str,  | str,  | The taint value corresponding to the taint key. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

