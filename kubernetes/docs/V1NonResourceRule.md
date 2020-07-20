# V1NonResourceRule

NonResourceRule holds information that describes a rule for the non-resource
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_resource_ur_ls** | **list[str]** | NonResourceURLs is a set of partial urls that a user should have access to.  *s are allowed, but only as the full, final step in the path.  \&quot;*\&quot; means all. | [optional] 
**verbs** | **list[str]** | Verb is a list of kubernetes non-resource API verbs, like: get, post, put, delete, patch, head, options.  \&quot;*\&quot; means all. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


