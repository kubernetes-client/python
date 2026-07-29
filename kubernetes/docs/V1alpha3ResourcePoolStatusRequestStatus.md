# V1alpha3ResourcePoolStatusRequestStatus

ResourcePoolStatusRequestStatus contains the calculated pool status information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1Condition]**](V1Condition.md) | Conditions provide information about the state of the request. A condition with type&#x3D;Complete or type&#x3D;Failed will always be set when the status is populated.  Known condition types: - \&quot;Complete\&quot;: True when the request has been processed successfully - \&quot;Failed\&quot;: True when the request could not be processed | [optional]
**pool_count** | **int** | PoolCount is the total number of pools that matched the filter criteria, regardless of truncation. This helps users understand how many pools exist even when the response is truncated. A value of 0 means no pools matched the filter criteria. |
**pools** | [**List[V1alpha3PoolStatus]**](V1alpha3PoolStatus.md) | Pools contains the first &#x60;spec.limit&#x60; matching pools, sorted by driver then pool name. If &#x60;len(pools) &lt; poolCount&#x60;, the list was truncated. When omitted, no pools matched the request filters. | [optional]

## Example

```python
from kubernetes.client.models.v1alpha3_resource_pool_status_request_status import V1alpha3ResourcePoolStatusRequestStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3ResourcePoolStatusRequestStatus from a JSON string
v1alpha3_resource_pool_status_request_status_instance = V1alpha3ResourcePoolStatusRequestStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha3ResourcePoolStatusRequestStatus.to_json())

# convert the object into a dict
v1alpha3_resource_pool_status_request_status_dict = v1alpha3_resource_pool_status_request_status_instance.to_dict()
# create an instance of V1alpha3ResourcePoolStatusRequestStatus from a dict
v1alpha3_resource_pool_status_request_status_from_dict = V1alpha3ResourcePoolStatusRequestStatus.from_dict(v1alpha3_resource_pool_status_request_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
