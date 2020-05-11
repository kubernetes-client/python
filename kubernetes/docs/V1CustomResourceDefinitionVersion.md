# V1CustomResourceDefinitionVersion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_printer_columns** | [**list[V1CustomResourceColumnDefinition]**](V1CustomResourceColumnDefinition.md) | additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used. | [optional] 
**name** | **str** | name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at &#x60;/apis/&lt;group&gt;/&lt;version&gt;/...&#x60; if &#x60;served&#x60; is true. | 
**schema** | [**V1CustomResourceValidation**](V1CustomResourceValidation.md) |  | [optional] 
**served** | **bool** | served is a flag enabling/disabling this version from being served via REST APIs | 
**storage** | **bool** | storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage&#x3D;true. | 
**subresources** | [**V1CustomResourceSubresources**](V1CustomResourceSubresources.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


