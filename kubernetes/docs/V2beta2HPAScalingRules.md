# V2beta2HPAScalingRules

HPAScalingRules configures the scaling behavior for one direction. These Rules are applied after calculating DesiredReplicas from metrics for the HPA. They can limit the scaling velocity by specifying scaling policies. They can prevent flapping by specifying the stabilization window, so that the number of replicas is not set instantly, instead, the safest value from the stabilization window is chosen.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**list[V2beta2HPAScalingPolicy]**](V2beta2HPAScalingPolicy.md) | policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the HPAScalingRules will be discarded as invalid | [optional] 
**select_policy** | **str** | selectPolicy is used to specify which policy should be used. If not set, the default value MaxPolicySelect is used. | [optional] 
**stabilization_window_seconds** | **int** | StabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


