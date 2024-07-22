# V1ResourceQuotaStatus

ResourceQuotaStatus defines the enforced hard limits and observed use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hard** | **Dict[str, str]** | Hard is the set of enforced hard limits for each named resource. More info: https://kubernetes.io/docs/concepts/policy/resource-quotas/ | [optional] 
**used** | **Dict[str, str]** | Used is the current observed total usage of the resource in the namespace. | [optional] 

## Example

```python
from kubernetes.client.models.v1_resource_quota_status import V1ResourceQuotaStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceQuotaStatus from a JSON string
v1_resource_quota_status_instance = V1ResourceQuotaStatus.from_json(json)
# print the JSON string representation of the object
print V1ResourceQuotaStatus.to_json()

# convert the object into a dict
v1_resource_quota_status_dict = v1_resource_quota_status_instance.to_dict()
# create an instance of V1ResourceQuotaStatus from a dict
v1_resource_quota_status_form_dict = v1_resource_quota_status.from_dict(v1_resource_quota_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


