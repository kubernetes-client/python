# V1ContainerStateTerminated

ContainerStateTerminated is a terminated state of a container.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exit_code** | **int** | Exit status from the last termination of the container | 
**container_id** | **str** | Container&#39;s ID in the format &#39;docker://&lt;container_id&gt;&#39; | [optional] 
**finished_at** | **datetime** | Time at which the container last terminated | [optional] 
**message** | **str** | Message regarding the last termination of the container | [optional] 
**reason** | **str** | (brief) reason from the last termination of the container | [optional] 
**signal** | **int** | Signal from the last termination of the container | [optional] 
**started_at** | **datetime** | Time at which previous execution of the container started | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


