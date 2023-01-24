# V1beta3LimitResponse

LimitResponse defines how to handle requests that can not be executed right now.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queuing** | [**V1beta3QueuingConfiguration**](V1beta3QueuingConfiguration.md) |  | [optional] 
**type** | **str** | &#x60;type&#x60; is \&quot;Queue\&quot; or \&quot;Reject\&quot;. \&quot;Queue\&quot; means that requests that can not be executed upon arrival are held in a queue until they can be executed or a queuing limit is reached. \&quot;Reject\&quot; means that requests that can not be executed upon arrival are rejected. Required. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


