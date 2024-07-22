# V1IngressStatus

IngressStatus describe the current state of the Ingress.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**load_balancer** | [**V1IngressLoadBalancerStatus**](V1IngressLoadBalancerStatus.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_ingress_status import V1IngressStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1IngressStatus from a JSON string
v1_ingress_status_instance = V1IngressStatus.from_json(json)
# print the JSON string representation of the object
print V1IngressStatus.to_json()

# convert the object into a dict
v1_ingress_status_dict = v1_ingress_status_instance.to_dict()
# create an instance of V1IngressStatus from a dict
v1_ingress_status_form_dict = v1_ingress_status.from_dict(v1_ingress_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


