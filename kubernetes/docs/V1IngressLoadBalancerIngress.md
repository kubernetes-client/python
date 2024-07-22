# V1IngressLoadBalancerIngress

IngressLoadBalancerIngress represents the status of a load-balancer ingress point.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | hostname is set for load-balancer ingress points that are DNS based. | [optional] 
**ip** | **str** | ip is set for load-balancer ingress points that are IP based. | [optional] 
**ports** | [**List[V1IngressPortStatus]**](V1IngressPortStatus.md) | ports provides information about the ports exposed by this LoadBalancer. | [optional] 

## Example

```python
from kubernetes.client.models.v1_ingress_load_balancer_ingress import V1IngressLoadBalancerIngress

# TODO update the JSON string below
json = "{}"
# create an instance of V1IngressLoadBalancerIngress from a JSON string
v1_ingress_load_balancer_ingress_instance = V1IngressLoadBalancerIngress.from_json(json)
# print the JSON string representation of the object
print V1IngressLoadBalancerIngress.to_json()

# convert the object into a dict
v1_ingress_load_balancer_ingress_dict = v1_ingress_load_balancer_ingress_instance.to_dict()
# create an instance of V1IngressLoadBalancerIngress from a dict
v1_ingress_load_balancer_ingress_form_dict = v1_ingress_load_balancer_ingress.from_dict(v1_ingress_load_balancer_ingress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


