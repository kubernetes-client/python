# V1ContainerRestartRuleOnExitCodes

ContainerRestartRuleOnExitCodes describes the condition for handling an exited container based on its exit codes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** | Represents the relationship between the container exit code(s) and the specified values. Possible values are: - In: the requirement is satisfied if the container exit code is in the   set of specified values. - NotIn: the requirement is satisfied if the container exit code is   not in the set of specified values. | 
**values** | **list[int]** | Specifies the set of values to check for container exit codes. At most 255 elements are allowed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


