# V1alpha3ResourcePoolStatusRequestSpec

ResourcePoolStatusRequestSpec defines the filters for the pool status request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**driver** | **str** | Driver specifies the DRA driver name to filter pools. Only pools from ResourceSlices with this driver will be included. Must be a DNS subdomain (e.g., \&quot;gpu.example.com\&quot;). |
**limit** | **int** | Limit optionally specifies the maximum number of pools to return in the status. If more pools match the filter criteria, the response will be truncated (i.e., len(status.pools) &lt; status.poolCount).  Default: 100 Minimum: 1 Maximum: 1000 | [optional]
**pool_name** | **str** | PoolName optionally filters to a specific pool name. If not specified, all pools from the specified driver are included. When specified, must be a non-empty valid resource pool name (DNS subdomains separated by \&quot;/\&quot;). | [optional]

## Example

```python
from kubernetes.client.models.v1alpha3_resource_pool_status_request_spec import V1alpha3ResourcePoolStatusRequestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3ResourcePoolStatusRequestSpec from a JSON string
v1alpha3_resource_pool_status_request_spec_instance = V1alpha3ResourcePoolStatusRequestSpec.from_json(json)
# print the JSON string representation of the object
print(V1alpha3ResourcePoolStatusRequestSpec.to_json())

# convert the object into a dict
v1alpha3_resource_pool_status_request_spec_dict = v1alpha3_resource_pool_status_request_spec_instance.to_dict()
# create an instance of V1alpha3ResourcePoolStatusRequestSpec from a dict
v1alpha3_resource_pool_status_request_spec_from_dict = V1alpha3ResourcePoolStatusRequestSpec.from_dict(v1alpha3_resource_pool_status_request_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
