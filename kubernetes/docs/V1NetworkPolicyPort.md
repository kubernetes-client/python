# V1NetworkPolicyPort

NetworkPolicyPort describes a port to allow traffic on
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_port** | **int** | If set, indicates that the range of ports from port to endPort, inclusive, should be allowed by the policy. This field cannot be defined if the port field is not defined or if the port field is defined as a named (string) port. The endPort must be equal or greater than port. This feature is in Alpha state and should be enabled using the Feature Gate \&quot;NetworkPolicyEndPort\&quot;. | [optional] 
**port** | [**object**](.md) | The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched. | [optional] 
**protocol** | **str** | The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


