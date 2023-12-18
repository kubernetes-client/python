# V1LoadBalancerIngress

LoadBalancerIngress represents the status of a load-balancer ingress point: traffic intended for the service should be sent to an ingress point.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers) | [optional] 
**ip** | **str** | IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers) | [optional] 
**ip_mode** | **str** | IPMode specifies how the load-balancer IP behaves, and may only be specified when the ip field is specified. Setting this to \&quot;VIP\&quot; indicates that traffic is delivered to the node with the destination set to the load-balancer&#39;s IP and port. Setting this to \&quot;Proxy\&quot; indicates that traffic is delivered to the node or pod with the destination set to the node&#39;s IP and node port or the pod&#39;s IP and port. Service implementations may use this information to adjust traffic routing. | [optional] 
**ports** | [**list[V1PortStatus]**](V1PortStatus.md) | Ports is a list of records of service ports If used, every port defined in the service should have an entry in it | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


