# V1NamespaceStatus

NamespaceStatus is information about the current status of a Namespace.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**list[V1NamespaceCondition]**](V1NamespaceCondition.md) | Represents the latest available observations of a namespace&#39;s current state. | [optional] 
**phase** | **str** | Phase is the current lifecycle phase of the namespace. More info: https://kubernetes.io/docs/tasks/administer-cluster/namespaces/  Possible enum values:  - &#x60;\&quot;Active\&quot;&#x60; means the namespace is available for use in the system  - &#x60;\&quot;Terminating\&quot;&#x60; means the namespace is undergoing graceful termination | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


