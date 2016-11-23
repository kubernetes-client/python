# V2alpha1JobStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** | Active is the number of actively running pods. | [optional] 
**completion_time** | [**UnversionedTime**](UnversionedTime.md) | CompletionTime represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. | [optional] 
**conditions** | [**list[V2alpha1JobCondition]**](V2alpha1JobCondition.md) | Conditions represent the latest available observations of an object&#39;s current state. More info: http://kubernetes.io/docs/user-guide/jobs | [optional] 
**failed** | **int** | Failed is the number of pods which reached Phase Failed. | [optional] 
**start_time** | [**UnversionedTime**](UnversionedTime.md) | StartTime represents time when the job was acknowledged by the Job Manager. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. | [optional] 
**succeeded** | **int** | Succeeded is the number of pods which reached Phase Succeeded. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


