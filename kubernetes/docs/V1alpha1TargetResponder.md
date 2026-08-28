# V1alpha1TargetResponder

TargetResponder allows you to specify the responder reacting to the Eviction. Responders should observe and communicate through the Eviction API (see .state) to help with the graceful eviction of a target (e.g. termination of a pod).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name allows you to identify the responder reacting to the Eviction.  It must be a valid domain-prefixed key (such as \&quot;acme.io/foo\&quot;). This field must be unique for each responder. This field is required. |
**priority** | **int** | priority for this responder. Higher priorities are selected first by the evictionrequest-controller. If there are responders with the same priority, the responder whose domain name comes first in the alphabetical higher domain order, will be picked. This means that the top domain labels are compared alphabetically first, followed by the lower domain labels. The key is compared last.  The responder that is the managing controller of the pod should set the value of this field to 10000 to allow both for preemption or fallback registration by other responders.  The minimum value is 0 and the maximum value is 100000. The interval 0-999 is reserved for responders with *.k8s.io suffix. This field is required and immutable. |
**state** | **str** | state specifies a state that is assigned by the evictionrequest-controller. Responders should observe this state in order to navigate their lifecycle. - Inactive means that the responder should not yet process this eviction request. - Active means that the responder is either running or expected to start soon.   Also, startTime has been set in the ResponderStatus by the evictionrequest-controller.    An active responder should currently interact with the eviction process by updating   .status.responders, where .name is the active responder name. ResponderStatus fields   should be periodically updated to indicate the progress or completion of the eviction process.   If .status.responders[].heartbeatTime field is not updated within the heartbeat deadline defined   by the Eviction API (currently 20 minutes), the eviction is passed over to the next responder   with a lower priority. Only one responder can be active at a time. - Interrupted means that the responder has failed to start or failed to update   heartbeatTime in ResponderStatus in a timely manner. - Canceled means that the responder has been canceled. In other words, there is no   EvictionRequest with the same target and Eviction intent in .spec.intent. - Completed means that the responder has successfully completed and set completionTime   in ResponderStatus.  Please refer to the ResponderStatus in .status.responders for more details on each responder. |

## Example

```python
from kubernetes.client.models.v1alpha1_target_responder import V1alpha1TargetResponder

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1TargetResponder from a JSON string
v1alpha1_target_responder_instance = V1alpha1TargetResponder.from_json(json)
# print the JSON string representation of the object
print(V1alpha1TargetResponder.to_json())

# convert the object into a dict
v1alpha1_target_responder_dict = v1alpha1_target_responder_instance.to_dict()
# create an instance of V1alpha1TargetResponder from a dict
v1alpha1_target_responder_from_dict = V1alpha1TargetResponder.from_dict(v1alpha1_target_responder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
