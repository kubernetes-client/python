# kubernetes.client.model.v1_deployment_strategy.V1DeploymentStrategy

DeploymentStrategy describes how to replace existing pods with new ones.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | DeploymentStrategy describes how to replace existing pods with new ones. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**rollingUpdate** | [**V1RollingUpdateDeployment**](V1RollingUpdateDeployment.md) | [**V1RollingUpdateDeployment**](V1RollingUpdateDeployment.md) |  | [optional] 
**type** | str,  | str,  | Type of deployment. Can be \&quot;Recreate\&quot; or \&quot;RollingUpdate\&quot;. Default is RollingUpdate.   | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

