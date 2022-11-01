# kubernetes.client.model.v1_container_state_terminated.V1ContainerStateTerminated

ContainerStateTerminated is a terminated state of a container.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ContainerStateTerminated is a terminated state of a container. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**exitCode** | decimal.Decimal, int,  | decimal.Decimal,  | Exit status from the last termination of the container | value must be a 32 bit integer
**containerID** | str,  | str,  | Container&#x27;s ID in the format &#x27;&lt;type&gt;://&lt;container_id&gt;&#x27; | [optional] 
**finishedAt** | str, datetime,  | str,  | Time at which the container last terminated | [optional] value must conform to RFC-3339 date-time
**message** | str,  | str,  | Message regarding the last termination of the container | [optional] 
**reason** | str,  | str,  | (brief) reason from the last termination of the container | [optional] 
**signal** | decimal.Decimal, int,  | decimal.Decimal,  | Signal from the last termination of the container | [optional] value must be a 32 bit integer
**startedAt** | str, datetime,  | str,  | Time at which previous execution of the container started | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

