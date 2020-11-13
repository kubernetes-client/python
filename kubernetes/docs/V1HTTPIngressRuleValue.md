# V1HTTPIngressRuleValue

HTTPIngressRuleValue is a list of http selectors pointing to backends. In the example: http://<host>/<path>?<searchpart> -> backend where where parts of the url correspond to RFC 3986, this resource will be used to match against everything after the last '/' and before the first '?' or '#'.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paths** | [**list[V1HTTPIngressPath]**](V1HTTPIngressPath.md) | A collection of paths that map requests to backends. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


