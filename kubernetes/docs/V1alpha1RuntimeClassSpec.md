# V1alpha1RuntimeClassSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overhead** | [**V1alpha1Overhead**](V1alpha1Overhead.md) |  | [optional] 
**runtime_handler** | **str** | RuntimeHandler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node &amp; CRI configuration.  It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called \&quot;runc\&quot; might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The RuntimeHandler must conform to the DNS Label (RFC 1123) requirements and is immutable. | 
**scheduling** | [**V1alpha1Scheduling**](V1alpha1Scheduling.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


