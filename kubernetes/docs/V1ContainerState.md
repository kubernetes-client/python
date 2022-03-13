# V1ContainerState

ContainerState holds a possible state of container. Only one of its members may be specified. If none of them is specified, the default one is ContainerStateWaiting.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**running** | [**V1ContainerStateRunning**](V1ContainerStateRunning.md) |  | [optional] 
**terminated** | [**V1ContainerStateTerminated**](V1ContainerStateTerminated.md) |  | [optional] 
**waiting** | [**V1ContainerStateWaiting**](V1ContainerStateWaiting.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


