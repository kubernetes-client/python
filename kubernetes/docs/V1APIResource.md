# V1APIResource

APIResource specifies the name of a resource and whether it is namespaced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **List[str]** | categories is a list of the grouped resources this resource belongs to (e.g. &#39;all&#39;) | [optional] 
**group** | **str** | group is the preferred group of the resource.  Empty implies the group of the containing resource list. For subresources, this may have a different value, for example: Scale\&quot;. | [optional] 
**kind** | **str** | kind is the kind for the resource (e.g. &#39;Foo&#39; is the kind for a resource &#39;foo&#39;) | 
**name** | **str** | name is the plural name of the resource. | 
**namespaced** | **bool** | namespaced indicates if a resource is namespaced or not. | 
**short_names** | **List[str]** | shortNames is a list of suggested short names of the resource. | [optional] 
**singular_name** | **str** | singularName is the singular name of the resource.  This allows kubernetes.clients to handle plural and singular opaquely. The singularName is more correct for reporting status on a single item and both singular and plural are allowed from the kubectl CLI interface. | 
**storage_version_hash** | **str** | The hash value of the storage version, the version this resource is converted to when written to the data store. Value must be treated as opaque by kubernetes.clients. Only equality comparison on the value is valid. This is an alpha feature and may change or be removed in the future. The field is populated by the apiserver only if the StorageVersionHash feature gate is enabled. This field will remain optional even if it graduates. | [optional] 
**verbs** | **List[str]** | verbs is a list of supported kube verbs (this includes get, list, watch, create, update, patch, delete, deletecollection, and proxy) | 
**version** | **str** | version is the preferred version of the resource.  Empty implies the version of the containing resource list For subresources, this may have a different value, for example: v1 (while inside a v1beta1 version of the core resource&#39;s group)\&quot;. | [optional] 

## Example

```python
from kubernetes.client.models.v1_api_resource import V1APIResource

# TODO update the JSON string below
json = "{}"
# create an instance of V1APIResource from a JSON string
v1_api_resource_instance = V1APIResource.from_json(json)
# print the JSON string representation of the object
print V1APIResource.to_json()

# convert the object into a dict
v1_api_resource_dict = v1_api_resource_instance.to_dict()
# create an instance of V1APIResource from a dict
v1_api_resource_form_dict = v1_api_resource.from_dict(v1_api_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


