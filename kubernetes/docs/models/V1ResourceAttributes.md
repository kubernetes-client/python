# kubernetes.client.model.v1_resource_attributes.V1ResourceAttributes

ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**group** | str,  | str,  | Group is the API Group of the Resource.  \&quot;*\&quot; means all. | [optional] 
**name** | str,  | str,  | Name is the name of the resource being requested for a \&quot;get\&quot; or deleted for a \&quot;delete\&quot;. \&quot;\&quot; (empty) means all. | [optional] 
**namespace** | str,  | str,  | Namespace is the namespace of the action being requested.  Currently, there is no distinction between no namespace and all namespaces \&quot;\&quot; (empty) is defaulted for LocalSubjectAccessReviews \&quot;\&quot; (empty) is empty for cluster-scoped resources \&quot;\&quot; (empty) means \&quot;all\&quot; for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview | [optional] 
**resource** | str,  | str,  | Resource is one of the existing resource types.  \&quot;*\&quot; means all. | [optional] 
**subresource** | str,  | str,  | Subresource is one of the existing resource types.  \&quot;\&quot; means none. | [optional] 
**verb** | str,  | str,  | Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  \&quot;*\&quot; means all. | [optional] 
**version** | str,  | str,  | Version is the API Version of the Resource.  \&quot;*\&quot; means all. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

