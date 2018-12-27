# V1beta1CustomResourceDefinitionVersion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_printer_columns** | [**list[V1beta1CustomResourceColumnDefinition]**](V1beta1CustomResourceColumnDefinition.md) | AdditionalPrinterColumns are additional columns shown e.g. in kubectl next to the name. Defaults to a created-at column. Top-level and per-version columns are mutually exclusive. Per-version columns must not all be set to identical values (top-level columns should be used instead) This field is alpha-level and is only honored by servers that enable the CustomResourceWebhookConversion feature. NOTE: CRDs created prior to 1.13 populated the top-level additionalPrinterColumns field by default. To apply an update that changes to per-version additionalPrinterColumns, the top-level additionalPrinterColumns field must be explicitly set to null | [optional] 
**name** | **str** | Name is the version name, e.g. “v1”, “v2beta1”, etc. | 
**schema** | [**V1beta1CustomResourceValidation**](V1beta1CustomResourceValidation.md) | Schema describes the schema for CustomResource used in validation, pruning, and defaulting. Top-level and per-version schemas are mutually exclusive. Per-version schemas must not all be set to identical values (top-level validation schema should be used instead) This field is alpha-level and is only honored by servers that enable the CustomResourceWebhookConversion feature. | [optional] 
**served** | **bool** | Served is a flag enabling/disabling this version from being served via REST APIs | 
**storage** | **bool** | Storage flags the version as storage version. There must be exactly one flagged as storage version. | 
**subresources** | [**V1beta1CustomResourceSubresources**](V1beta1CustomResourceSubresources.md) | Subresources describes the subresources for CustomResource Top-level and per-version subresources are mutually exclusive. Per-version subresources must not all be set to identical values (top-level subresources should be used instead) This field is alpha-level and is only honored by servers that enable the CustomResourceWebhookConversion feature. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


