# V1ShardInfo

ShardInfo describes the shard selector that was applied to produce a list response. Its presence on a list response indicates the list is a filtered subset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | **str** | selector is the shard selector string from the request, echoed back so clients can verify which shard they received and merge responses from multiple shards. |

## Example

```python
from kubernetes.client.models.v1_shard_info import V1ShardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V1ShardInfo from a JSON string
v1_shard_info_instance = V1ShardInfo.from_json(json)
# print the JSON string representation of the object
print(V1ShardInfo.to_json())

# convert the object into a dict
v1_shard_info_dict = v1_shard_info_instance.to_dict()
# create an instance of V1ShardInfo from a dict
v1_shard_info_from_dict = V1ShardInfo.from_dict(v1_shard_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
