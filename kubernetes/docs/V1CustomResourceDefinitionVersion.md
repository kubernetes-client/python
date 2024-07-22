# V1CustomResourceDefinitionVersion

CustomResourceDefinitionVersion describes a version for CRD.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_printer_columns** | [**List[V1CustomResourceColumnDefinition]**](V1CustomResourceColumnDefinition.md) | additionalPrinterColumns specifies additional columns returned in Table output. See https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables for details. If no columns are specified, a single column displaying the age of the custom resource is used. | [optional] 
**deprecated** | **bool** | deprecated indicates this version of the custom resource API is deprecated. When set to true, API requests to this version receive a warning header in the server response. Defaults to false. | [optional] 
**deprecation_warning** | **str** | deprecationWarning overrides the default warning returned to API kubernetes.clients. May only be set when &#x60;deprecated&#x60; is true. The default warning indicates this version is deprecated and recommends use of the newest served version of equal or greater stability, if one exists. | [optional] 
**name** | **str** | name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at &#x60;/apis/&lt;group&gt;/&lt;version&gt;/...&#x60; if &#x60;served&#x60; is true. | 
**var_schema** | [**V1CustomResourceValidation**](V1CustomResourceValidation.md) |  | [optional] 
**selectable_fields** | [**List[V1SelectableField]**](V1SelectableField.md) | selectableFields specifies paths to fields that may be used as field selectors. A maximum of 8 selectable fields are allowed. See https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors | [optional] 
**served** | **bool** | served is a flag enabling/disabling this version from being served via REST APIs | 
**storage** | **bool** | storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage&#x3D;true. | 
**subresources** | [**V1CustomResourceSubresources**](V1CustomResourceSubresources.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_custom_resource_definition_version import V1CustomResourceDefinitionVersion

# TODO update the JSON string below
json = "{}"
# create an instance of V1CustomResourceDefinitionVersion from a JSON string
v1_custom_resource_definition_version_instance = V1CustomResourceDefinitionVersion.from_json(json)
# print the JSON string representation of the object
print V1CustomResourceDefinitionVersion.to_json()

# convert the object into a dict
v1_custom_resource_definition_version_dict = v1_custom_resource_definition_version_instance.to_dict()
# create an instance of V1CustomResourceDefinitionVersion from a dict
v1_custom_resource_definition_version_form_dict = v1_custom_resource_definition_version.from_dict(v1_custom_resource_definition_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


