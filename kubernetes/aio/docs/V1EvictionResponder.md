# V1EvictionResponder

EvictionResponder allows you to specify the responder reacting to an Eviction. Responders should observe and communicate through the Eviction Resource API to help with the graceful eviction of a target (e.g. termination of a pod).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name allows you to identify the responder responding to the Eviction.  It must be a valid domain-prefixed key (such as \&quot;acme.io/foo\&quot;). Domain names *.k8s.io and *.kubernetes.io are reserved. This field must be unique for each responder. This field is required. |
**priority** | **int** | priority for this responder. Higher priorities are selected first by the evictionrequest-controller. If there are responders with the same priority, the responder whose domain name comes first in the alphabetical higher domain order, will be picked. This means that the top domain labels are compared alphabetically first, followed by the lower domain labels. The key is compared last.  The responder that is the managing controller of the pod should set the value of this field to 10000 to allow both for preemption or fallback registration by other responders.  The minimum value is 0 and the maximum value is 100000. The interval 0-999 is reserved for responders with *.k8s.io suffix. This field is required. |

## Example

```python
from kubernetes.aio.client.models.v1_eviction_responder import V1EvictionResponder

# TODO update the JSON string below
json = "{}"
# create an instance of V1EvictionResponder from a JSON string
v1_eviction_responder_instance = V1EvictionResponder.from_json(json)
# print the JSON string representation of the object
print(V1EvictionResponder.to_json())

# convert the object into a dict
v1_eviction_responder_dict = v1_eviction_responder_instance.to_dict()
# create an instance of V1EvictionResponder from a dict
v1_eviction_responder_from_dict = V1EvictionResponder.from_dict(v1_eviction_responder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
