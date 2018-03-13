# V1beta1CustomResourceDefinitionNames

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **list[str]** | Categories is a list of grouped resources custom resources belong to (e.g. &#39;all&#39;) | [optional] 
**kind** | **str** | Kind is the serialized kind of the resource.  It is normally CamelCase and singular. | 
**list_kind** | **str** | ListKind is the serialized kind of the list for this resource.  Defaults to &lt;kind&gt;List. | [optional] 
**plural** | **str** | Plural is the plural name of the resource to serve.  It must match the name of the CustomResourceDefinition-registration too: plural.group and it must be all lowercase. | 
**short_names** | **list[str]** | ShortNames are short names for the resource.  It must be all lowercase. | [optional] 
**singular** | **str** | Singular is the singular name of the resource.  It must be all lowercase  Defaults to lowercased &lt;kind&gt; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


