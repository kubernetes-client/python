# V1ResourceQuotaSpec

ResourceQuotaSpec defines the desired hard limits to enforce for Quota.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard** | **{str: (str,)}** | hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ | [optional] 
**scope_selector** | [**V1ScopeSelector**](V1ScopeSelector.md) |  | [optional] 
**scopes** | **[str]** | A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


