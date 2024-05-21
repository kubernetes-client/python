# V1alpha2NamedResourcesAttribute

NamedResourcesAttribute is a combination of an attribute name and its value.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bool** | **bool** | BoolValue is a true/false value. | [optional] 
**int** | **int** | IntValue is a 64-bit integer. | [optional] 
**int_slice** | [**V1alpha2NamedResourcesIntSlice**](V1alpha2NamedResourcesIntSlice.md) |  | [optional] 
**name** | **str** | Name is unique identifier among all resource instances managed by the driver on the node. It must be a DNS subdomain. | 
**quantity** | **str** | QuantityValue is a quantity. | [optional] 
**string** | **str** | StringValue is a string. | [optional] 
**string_slice** | [**V1alpha2NamedResourcesStringSlice**](V1alpha2NamedResourcesStringSlice.md) |  | [optional] 
**version** | **str** | VersionValue is a semantic version according to semver.org spec 2.0.0. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


