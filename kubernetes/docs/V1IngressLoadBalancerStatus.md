# V1IngressLoadBalancerStatus

IngressLoadBalancerStatus represents the status of a load-balancer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingress** | [**List[V1IngressLoadBalancerIngress]**](V1IngressLoadBalancerIngress.md) | ingress is a list containing ingress points for the load-balancer. | [optional] 

## Example

```python
from kubernetes.client.models.v1_ingress_load_balancer_status import V1IngressLoadBalancerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1IngressLoadBalancerStatus from a JSON string
v1_ingress_load_balancer_status_instance = V1IngressLoadBalancerStatus.from_json(json)
# print the JSON string representation of the object
print V1IngressLoadBalancerStatus.to_json()

# convert the object into a dict
v1_ingress_load_balancer_status_dict = v1_ingress_load_balancer_status_instance.to_dict()
# create an instance of V1IngressLoadBalancerStatus from a dict
v1_ingress_load_balancer_status_form_dict = v1_ingress_load_balancer_status.from_dict(v1_ingress_load_balancer_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


