# V1ResourceQuotaSpec

ResourceQuotaSpec defines the desired hard limits to enforce for Quota.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard** | **Dict[str, str]** | hard is the set of desired hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ | [optional] 
**scope_selector** | [**V1ScopeSelector**](V1ScopeSelector.md) |  | [optional] 
**scopes** | **List[str]** | A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. | [optional] 

## Example

```python
from kubernetes.client.models.v1_resource_quota_spec import V1ResourceQuotaSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceQuotaSpec from a JSON string
v1_resource_quota_spec_instance = V1ResourceQuotaSpec.from_json(json)
# print the JSON string representation of the object
print V1ResourceQuotaSpec.to_json()

# convert the object into a dict
v1_resource_quota_spec_dict = v1_resource_quota_spec_instance.to_dict()
# create an instance of V1ResourceQuotaSpec from a dict
v1_resource_quota_spec_form_dict = v1_resource_quota_spec.from_dict(v1_resource_quota_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


