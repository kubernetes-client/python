# V1ResourceQuotaSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard** | **dict(str, str)** | hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ | [optional] 
**scope_selector** | [**V1ScopeSelector**](V1ScopeSelector.md) |  | [optional] 
**scopes** | **list[str]** | A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


