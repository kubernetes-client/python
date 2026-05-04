# V1ShardInfo

ShardInfo describes the shard selector that was applied to produce a list response. Its presence on a list response indicates the list is a filtered subset.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | **str** | selector is the shard selector string from the request, echoed back so kubernetes.clients can verify which shard they received and merge responses from multiple shards. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


