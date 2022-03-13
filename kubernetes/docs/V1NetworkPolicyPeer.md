# V1NetworkPolicyPeer

NetworkPolicyPeer describes a peer to allow traffic to/from. Only certain combinations of fields are allowed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_block** | [**V1IPBlock**](V1IPBlock.md) |  | [optional] 
**namespace_selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**pod_selector** | [**V1LabelSelector**](V1LabelSelector.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


