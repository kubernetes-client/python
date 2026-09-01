# V1alpha1ResponderStatus

ResponderStatus represents the last observed status of the eviction process of the responder. It should be only updated by the designated responder whose name is .name field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_time** | **datetime** | completionTime tracks the time at which the Responder stopped processing the eviction request. Completion means that the responders has either fully or partially completed the eviction process, which may have resulted in target eviction (e.g. pod termination). It should reflect the present time when set. This field becomes immutable once set. | [optional]
**expected_completion_time** | **datetime** | expectedCompletionTime is the time at which the eviction process step is expected to end for the responder. The time cannot be set to the past. May be omitted if no estimate can be made. | [optional]
**heartbeat_time** | **datetime** | heartbeatTime is the last time at which the eviction process was reported to be in progress by the responder. It should reflect the present time when set. Responders should avoid heartbeats more frequent than 20 seconds to avoid overloading the control-plane. | [optional]
**message** | **str** | message provides human-readable details about the state of the responder and the eviction process. Maximum length is 4000 characters. | [optional]
**name** | **str** | name allows you to identify the responder reacting to the Eviction.  It must be a valid domain-prefixed key (such as \&quot;acme.io/foo\&quot;). This field is initialized by Kubernetes and must be unique for each responder. This field is required. |
**start_time** | **datetime** | startTime tracks the time at which this responder was designated as active and should start processing the eviction request. It should reflect the present time when set. This field is initialized by Kubernetes when this responder becomes active. This field becomes immutable once set. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1alpha1_responder_status import V1alpha1ResponderStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1ResponderStatus from a JSON string
v1alpha1_responder_status_instance = V1alpha1ResponderStatus.from_json(json)
# print the JSON string representation of the object
print(V1alpha1ResponderStatus.to_json())

# convert the object into a dict
v1alpha1_responder_status_dict = v1alpha1_responder_status_instance.to_dict()
# create an instance of V1alpha1ResponderStatus from a dict
v1alpha1_responder_status_from_dict = V1alpha1ResponderStatus.from_dict(v1alpha1_responder_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
