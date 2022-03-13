# V1LimitRangeItem

LimitRangeItem defines a min/max usage limit for any resource that matches on kind.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of resource that this limit applies to.  Possible enum values:  - &#x60;\&quot;Container\&quot;&#x60; Limit that applies to all containers in a namespace  - &#x60;\&quot;PersistentVolumeClaim\&quot;&#x60; Limit that applies to all persistent volume claims in a namespace  - &#x60;\&quot;Pod\&quot;&#x60; Limit that applies to all pods in a namespace | 
**default** | **{str: (str,)}** | Default resource requirement limit value by resource name if resource limit is omitted. | [optional] 
**default_request** | **{str: (str,)}** | DefaultRequest is the default resource requirement request value by resource name if resource request is omitted. | [optional] 
**max** | **{str: (str,)}** | Max usage constraints on this kind by resource name. | [optional] 
**max_limit_request_ratio** | **{str: (str,)}** | MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource. | [optional] 
**min** | **{str: (str,)}** | Min usage constraints on this kind by resource name. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


