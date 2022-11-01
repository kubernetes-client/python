# kubernetes.client.model.v1_group_version_for_discovery.V1GroupVersionForDiscovery

GroupVersion contains the \"group/version\" and \"version\" string of a version. It is made a struct to keep extensibility.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | GroupVersion contains the \&quot;group/version\&quot; and \&quot;version\&quot; string of a version. It is made a struct to keep extensibility. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**groupVersion** | str,  | str,  | groupVersion specifies the API group and version in the form \&quot;group/version\&quot; | 
**version** | str,  | str,  | version specifies the version in the form of \&quot;version\&quot;. This is to save the kubernetes.clients the trouble of splitting the GroupVersion. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

