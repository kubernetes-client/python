# V2APIResourceDiscovery

APIResourceDiscovery provides information about an API resource for discovery.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | resource is the plural name of the resource. | 
**response_kind** | [**IoK8sApimachineryPkgApisMetaV1GroupVersionKind**](IoK8sApimachineryPkgApisMetaV1GroupVersionKind.md) |  | [optional] 
**scope** | **str** | scope indicates the scope of a resource, either Cluster or Namespaced | 
**singular_resource** | **str** | singularResource is the singular name of the resource. | 
**verbs** | **list[str]** | verbs is a list of supported API operation types | 
**short_names** | **list[str]** | shortNames is a list of suggested short names of the resource. | [optional] 
**categories** | **list[str]** | categories is a list of the grouped resources this resource belongs to. | [optional] 
**subresources** | [**list[V2APISubresourceDiscovery]**](V2APISubresourceDiscovery.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


