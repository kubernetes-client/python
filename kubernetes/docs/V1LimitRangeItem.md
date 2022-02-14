# V1LimitRangeItem

LimitRangeItem defines a min/max usage limit for any resource that matches on kind.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **dict(str, str)** | Default resource requirement limit value by resource name if resource limit is omitted. | [optional] 
**default_request** | **dict(str, str)** | DefaultRequest is the default resource requirement request value by resource name if resource request is omitted. | [optional] 
**max** | **dict(str, str)** | Max usage constraints on this kind by resource name. | [optional] 
**max_limit_request_ratio** | **dict(str, str)** | MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource. | [optional] 
**min** | **dict(str, str)** | Min usage constraints on this kind by resource name. | [optional] 
**type** | **str** | Type of resource that this limit applies to.  Possible enum values:  - &#x60;\&quot;Container\&quot;&#x60; Limit that applies to all containers in a namespace  - &#x60;\&quot;PersistentVolumeClaim\&quot;&#x60; Limit that applies to all persistent volume claims in a namespace  - &#x60;\&quot;Pod\&quot;&#x60; Limit that applies to all pods in a namespace | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


