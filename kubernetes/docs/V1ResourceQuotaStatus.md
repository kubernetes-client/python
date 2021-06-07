# V1ResourceQuotaStatus

ResourceQuotaStatus defines the enforced hard limits and observed use.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard** | **{str: (str,)}** | Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ | [optional] 
**used** | **{str: (str,)}** | Used is the current observed total usage of the resource in the namespace. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


