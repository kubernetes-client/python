# V1LoadBalancerIngress

LoadBalancerIngress represents the status of a load-balancer ingress point: traffic intended for the service should be sent to an ingress point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Hostname is set for load-balancer ingress points that are DNS based (typically AWS load-balancers) | [optional] 
**ip** | **str** | IP is set for load-balancer ingress points that are IP based (typically GCE or OpenStack load-balancers) | [optional] 
**ip_mode** | **str** | IPMode specifies how the load-balancer IP behaves, and may only be specified when the ip field is specified. Setting this to \&quot;VIP\&quot; indicates that traffic is delivered to the node with the destination set to the load-balancer&#39;s IP and port. Setting this to \&quot;Proxy\&quot; indicates that traffic is delivered to the node or pod with the destination set to the node&#39;s IP and node port or the pod&#39;s IP and port. Service implementations may use this information to adjust traffic routing. | [optional] 
**ports** | [**List[V1PortStatus]**](V1PortStatus.md) | Ports is a list of records of service ports If used, every port defined in the service should have an entry in it | [optional] 

## Example

```python
from kubernetes.client.models.v1_load_balancer_ingress import V1LoadBalancerIngress

# TODO update the JSON string below
json = "{}"
# create an instance of V1LoadBalancerIngress from a JSON string
v1_load_balancer_ingress_instance = V1LoadBalancerIngress.from_json(json)
# print the JSON string representation of the object
print V1LoadBalancerIngress.to_json()

# convert the object into a dict
v1_load_balancer_ingress_dict = v1_load_balancer_ingress_instance.to_dict()
# create an instance of V1LoadBalancerIngress from a dict
v1_load_balancer_ingress_form_dict = v1_load_balancer_ingress.from_dict(v1_load_balancer_ingress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


