# V1beta1RuntimeClassStrategyOptions

RuntimeClassStrategyOptions define the strategy that will dictate the allowable RuntimeClasses for a pod.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_runtime_class_names** | **list[str]** | allowedRuntimeClassNames is a whitelist of RuntimeClass names that may be specified on a pod. A value of \&quot;*\&quot; means that any RuntimeClass name is allowed, and must be the only item in the list. An empty list requires the RuntimeClassName field to be unset. | 
**default_runtime_class_name** | **str** | defaultRuntimeClassName is the default RuntimeClassName to set on the pod. The default MUST be allowed by the allowedRuntimeClassNames list. A value of nil does not mutate the Pod. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


