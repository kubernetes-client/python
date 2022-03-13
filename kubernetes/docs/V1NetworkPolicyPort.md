# V1NetworkPolicyPort

NetworkPolicyPort describes a port to allow traffic on

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_port** | **int** | If set, indicates that the range of ports from port to endPort, inclusive, should be allowed by the policy. This field cannot be defined if the port field is not defined or if the port field is defined as a named (string) port. The endPort must be equal or greater than port. This feature is in Beta state and is enabled by default. It can be disabled using the Feature Gate \&quot;NetworkPolicyEndPort\&quot;. | [optional] 
**port** | **bool, date, datetime, dict, float, int, list, str, none_type** | The port on the given protocol. This can either be a numerical or named port on a pod. If this field is not provided, this matches all port names and numbers. If present, only traffic on the specified protocol AND port will be matched. | [optional] 
**protocol** | **str** | The protocol (TCP, UDP, or SCTP) which traffic must match. If not specified, this field defaults to TCP. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


