# V2beta1APIGroupDiscoveryList

APIGroupDiscoveryList is a resource containing a list of APIGroupDiscovery. This is one of the types able to be returned from the /api and /apis endpoint and contains an aggregated list of API resources (built-ins, Custom Resource Definitions, resources from aggregated servers) that a cluster supports.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**metadata** | [**V1ListMeta**](V1ListMeta.md) |  | [optional] 
**items** | [**list[V2beta1APIGroupDiscovery]**](V2beta1APIGroupDiscovery.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


