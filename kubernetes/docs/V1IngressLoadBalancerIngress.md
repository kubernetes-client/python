# V1IngressLoadBalancerIngress

IngressLoadBalancerIngress represents the status of a load-balancer ingress point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | hostname is set for load-balancer ingress points that are DNS based. | [optional] 
**ip** | **str** | ip is set for load-balancer ingress points that are IP based. | [optional] 
**ports** | [**list[V1IngressPortStatus]**](V1IngressPortStatus.md) | ports provides information about the ports exposed by this LoadBalancer. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


