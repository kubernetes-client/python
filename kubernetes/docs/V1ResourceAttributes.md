# V1ResourceAttributes

ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** | Group is the API Group of the Resource.  \&quot;*\&quot; means all. | [optional] 
**name** | **str** | Name is the name of the resource being requested for a \&quot;get\&quot; or deleted for a \&quot;delete\&quot;. \&quot;\&quot; (empty) means all. | [optional] 
**namespace** | **str** | Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces \&quot;\&quot; (empty) is defaulted for LocalSubjectAccessReviews \&quot;\&quot; (empty) is empty for cluster-scoped resources \&quot;\&quot; (empty) means \&quot;all\&quot; for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview | [optional] 
**resource** | **str** | Resource is one of the existing resource types.  \&quot;*\&quot; means all. | [optional] 
**subresource** | **str** | Subresource is one of the existing resource types.  \&quot;\&quot; means none. | [optional] 
**verb** | **str** | Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  \&quot;*\&quot; means all. | [optional] 
**version** | **str** | Version is the API Version of the Resource.  \&quot;*\&quot; means all. | [optional] 

## Example

```python
from kubernetes.client.models.v1_resource_attributes import V1ResourceAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of V1ResourceAttributes from a JSON string
v1_resource_attributes_instance = V1ResourceAttributes.from_json(json)
# print the JSON string representation of the object
print V1ResourceAttributes.to_json()

# convert the object into a dict
v1_resource_attributes_dict = v1_resource_attributes_instance.to_dict()
# create an instance of V1ResourceAttributes from a dict
v1_resource_attributes_form_dict = v1_resource_attributes.from_dict(v1_resource_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


