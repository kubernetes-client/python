# V2beta1APIGroupDiscovery

APIGroupDiscovery holds information about which resources are being served for all version of the API Group. It contains a list of APIVersionDiscovery that holds a list of APIResourceDiscovery types served for a version. Versions are in descending order of preference, with the first version being the preferred entry.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**versions** | [**list[V2beta1APIVersionDiscovery]**](V2beta1APIVersionDiscovery.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


