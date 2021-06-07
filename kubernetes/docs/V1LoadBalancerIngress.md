# V1LoadBalancerIngress

LoadBalancerIngress represents the status of a load-balancer ingress point: traffic intended for the service should be sent to an ingress point.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers) | [optional] 
**ip** | **str** | IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


