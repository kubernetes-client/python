# V2APIVersionDiscovery

APIVersionDiscovery holds a list of APIResourceDiscovery types that are served for a particular version within an API Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | version is the name of the version within a group version. | 
**resources** | [**list[V2APIResourceDiscovery]**](V2APIResourceDiscovery.md) |  | [optional] 
**freshness** | **str** | freshness marks whether a group version&#39;s discovery document is up to date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


