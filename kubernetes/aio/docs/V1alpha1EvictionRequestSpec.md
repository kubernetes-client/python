# V1alpha1EvictionRequestSpec

EvictionRequestSpec is a specification of an EvictionRequest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intent** | **str** | intent specifies the action that should be taken for the specified target.  - Eviction means that the requester is interested in the eviction of the target. - Withdrawn means that the requester is no longer interested in the eviction of the target.   If all requesters&#39; intents are withdrawn for a common target, the eviction will be canceled.   Cancellation consequences:   - Inactive responders will never run.   - Active responders are expected to cancel the eviction.   - Completed or Interrupted responders should not take any action. |
**requester** | **str** | requester allows you to identify the entity, that requested the eviction of the target.  It must be a valid domain-prefixed key (such as \&quot;acme.io/foo\&quot;). Domain names *.k8s.io and *.kubernetes.io are reserved. This field is required and immutable. |
**target** | [**V1alpha1EvictionRequestTarget**](V1alpha1EvictionRequestTarget.md) |  |

## Example

```python
from kubernetes.aio.client.models.v1alpha1_eviction_request_spec import V1alpha1EvictionRequestSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha1EvictionRequestSpec from a JSON string
v1alpha1_eviction_request_spec_instance = V1alpha1EvictionRequestSpec.from_json(json)
# print the JSON string representation of the object
print(V1alpha1EvictionRequestSpec.to_json())

# convert the object into a dict
v1alpha1_eviction_request_spec_dict = v1alpha1_eviction_request_spec_instance.to_dict()
# create an instance of V1alpha1EvictionRequestSpec from a dict
v1alpha1_eviction_request_spec_from_dict = V1alpha1EvictionRequestSpec.from_dict(v1alpha1_eviction_request_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
