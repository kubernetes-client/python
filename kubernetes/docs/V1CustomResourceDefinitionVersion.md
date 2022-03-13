# V1CustomResourceDefinitionVersion

CustomResourceDefinitionVersion describes a version for CRD.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at &#x60;/apis/&lt;group&gt;/&lt;version&gt;/...&#x60; if &#x60;served&#x60; is true. | 
**served** | **bool** | served is a flag enabling/disabling this version from being served via REST APIs | 
**storage** | **bool** | storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage&#x3D;true. | 
**additional_printer_columns** | [**[V1CustomResourceColumnDefinition]**](V1CustomResourceColumnDefinition.md) | additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used. | [optional] 
**deprecated** | **bool** | deprecated indicates this version of the custom resource API is deprecated. When set to true, API requests to this version receive a warning header in the server response. Defaults to false. | [optional] 
**deprecation_warning** | **str** | deprecationWarning overrides the default warning returned to API kubernetes.clients. May only be set when &#x60;deprecated&#x60; is true. The default warning indicates this version is deprecated and recommends use of the newest served version of equal or greater stability, if one exists. | [optional] 
**schema** | [**V1CustomResourceValidation**](V1CustomResourceValidation.md) |  | [optional] 
**subresources** | [**V1CustomResourceSubresources**](V1CustomResourceSubresources.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


