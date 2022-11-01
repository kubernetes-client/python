# kubernetes.client.model.v1_custom_resource_definition_version.V1CustomResourceDefinitionVersion

CustomResourceDefinitionVersion describes a version for CRD.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | CustomResourceDefinitionVersion describes a version for CRD. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**served** | bool,  | BoolClass,  | served is a flag enabling/disabling this version from being served via REST APIs | 
**name** | str,  | str,  | name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at &#x60;/apis/&lt;group&gt;/&lt;version&gt;/...&#x60; if &#x60;served&#x60; is true. | 
**storage** | bool,  | BoolClass,  | storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage&#x3D;true. | 
**[additionalPrinterColumns](#additionalPrinterColumns)** | list, tuple,  | tuple,  | additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used. | [optional] 
**deprecated** | bool,  | BoolClass,  | deprecated indicates this version of the custom resource API is deprecated. When set to true, API requests to this version receive a warning header in the server response. Defaults to false. | [optional] 
**deprecationWarning** | str,  | str,  | deprecationWarning overrides the default warning returned to API kubernetes.clients. May only be set when &#x60;deprecated&#x60; is true. The default warning indicates this version is deprecated and recommends use of the newest served version of equal or greater stability, if one exists. | [optional] 
**schema** | [**V1CustomResourceValidation**](V1CustomResourceValidation.md) | [**V1CustomResourceValidation**](V1CustomResourceValidation.md) |  | [optional] 
**subresources** | [**V1CustomResourceSubresources**](V1CustomResourceSubresources.md) | [**V1CustomResourceSubresources**](V1CustomResourceSubresources.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# additionalPrinterColumns

additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1CustomResourceColumnDefinition**](V1CustomResourceColumnDefinition.md) | [**V1CustomResourceColumnDefinition**](V1CustomResourceColumnDefinition.md) | [**V1CustomResourceColumnDefinition**](V1CustomResourceColumnDefinition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

