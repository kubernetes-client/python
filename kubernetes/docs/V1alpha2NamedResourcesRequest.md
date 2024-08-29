# V1alpha2NamedResourcesRequest

NamedResourcesRequest is used in ResourceRequestModel.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | **str** | Selector is a CEL expression which must evaluate to true if a resource instance is suitable. The language is as defined in https://kubernetes.io/docs/reference/using-api/cel/  In addition, for each type NamedResourcesin AttributeValue there is a map that resolves to the corresponding value of the instance under evaluation. For example:     attributes.quantity[\&quot;a\&quot;].isGreaterThan(quantity(\&quot;0\&quot;)) &amp;&amp;    attributes.stringslice[\&quot;b\&quot;].isSorted() | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


