# V1alpha1Requester

Requester allows you to identify the entity, that requested the eviction of the target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intent** | **str** | intent specifies the action that should be taken for the specified target.  - Eviction means that the requester is interested in the eviction of the target. - Withdrawn means that the requester is no longer interested in the eviction of the target.   If all requesters&#39; intents are withdrawn, the eviction will be canceled.   Cancellation consequences:   - Inactive responders will never run.   - Active responders are expected to cancel the eviction.   - Completed or Interrupted responders should not take any action. |
**name** | **str** | name allows you to identify the entity, that requested the eviction of the target.  It must be a valid domain-prefixed key (such as \&quot;acme.io/foo\&quot;). This field must be unique for each requester. This field is required. |

## Example

```python
from kubernetes.client.models.v1alpha1_requester import V1alpha1Requester

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1Requester from a JSON string
v1alpha1_requester_instance = V1alpha1Requester.from_json(json)
# print the JSON string representation of the object
print(V1alpha1Requester.to_json())

# convert the object into a dict
v1alpha1_requester_dict = v1alpha1_requester_instance.to_dict()
# create an instance of V1alpha1Requester from a dict
v1alpha1_requester_from_dict = V1alpha1Requester.from_dict(v1alpha1_requester_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
