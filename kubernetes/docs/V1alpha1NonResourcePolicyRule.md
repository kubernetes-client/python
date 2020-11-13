# V1alpha1NonResourcePolicyRule

NonResourcePolicyRule is a predicate that matches non-resource requests according to their verb and the target non-resource URL. A NonResourcePolicyRule matches a request if and only if both (a) at least one member of verbs matches the request and (b) at least one member of nonResourceURLs matches the request.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_resource_ur_ls** | **list[str]** | &#x60;nonResourceURLs&#x60; is a set of url prefixes that a user should have access to and may not be empty. For example:   - \&quot;/healthz\&quot; is legal   - \&quot;/hea*\&quot; is illegal   - \&quot;/hea\&quot; is legal but matches nothing   - \&quot;/hea/*\&quot; also matches nothing   - \&quot;/healthz/*\&quot; matches all per-component health checks. \&quot;*\&quot; matches all non-resource urls. if it is present, it must be the only entry. Required. | 
**verbs** | **list[str]** | &#x60;verbs&#x60; is a list of matching verbs and may not be empty. \&quot;*\&quot; matches all verbs. If it is present, it must be the only entry. Required. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


