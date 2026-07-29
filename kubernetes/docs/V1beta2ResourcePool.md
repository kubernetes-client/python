# V1beta2ResourcePool

ResourcePool describes the pool that ResourceSlices belong to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generation** | **int** | Generation tracks the change in a pool over time. Whenever a driver changes something about one or more of the resources in a pool, it must change the generation in all ResourceSlices which are part of that pool. Consumers of ResourceSlices should only consider resources from the pool with the highest generation number. The generation may be reset by drivers, which should be fine for consumers, assuming that all ResourceSlices in a pool are updated to match or deleted.  Combined with ResourceSliceCount, this mechanism enables consumers to detect pools which are comprised of multiple ResourceSlices and are in an incomplete state. |
**name** | **str** | Name is used to identify the pool. For node-local devices, this is often the node name, but this is not required.  It must not be longer than 253 characters and must consist of one or more DNS sub-domains separated by slashes. This field is immutable. |
**resource_slice_count** | **int** | ResourceSliceCount is the total number of ResourceSlices in the pool at this generation number. Must be greater than zero.  Consumers can use this to check whether they have seen all ResourceSlices belonging to the same pool. |

## Example

```python
from kubernetes.client.models.v1beta2_resource_pool import V1beta2ResourcePool

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta2ResourcePool from a JSON string
v1beta2_resource_pool_instance = V1beta2ResourcePool.from_json(json)
# print the JSON string representation of the object
print(V1beta2ResourcePool.to_json())

# convert the object into a dict
v1beta2_resource_pool_dict = v1beta2_resource_pool_instance.to_dict()
# create an instance of V1beta2ResourcePool from a dict
v1beta2_resource_pool_from_dict = V1beta2ResourcePool.from_dict(v1beta2_resource_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
