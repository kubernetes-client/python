# V1LimitRangeItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | [**dict(str, ResourceQuantity)**](ResourceQuantity.md) | Default resource requirement limit value by resource name if resource limit is omitted. | [optional] 
**default_request** | [**dict(str, ResourceQuantity)**](ResourceQuantity.md) | DefaultRequest is the default resource requirement request value by resource name if resource request is omitted. | [optional] 
**max** | [**dict(str, ResourceQuantity)**](ResourceQuantity.md) | Max usage constraints on this kind by resource name. | [optional] 
**max_limit_request_ratio** | [**dict(str, ResourceQuantity)**](ResourceQuantity.md) | MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource. | [optional] 
**min** | [**dict(str, ResourceQuantity)**](ResourceQuantity.md) | Min usage constraints on this kind by resource name. | [optional] 
**type** | **str** | Type of resource that this limit applies to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


