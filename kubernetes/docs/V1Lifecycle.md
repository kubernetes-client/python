# V1Lifecycle

Lifecycle describes actions that the management system should take in response to container lifecycle events. For the PostStart and PreStop lifecycle handlers, management of the container blocks until the action is complete, unless the container process fails, in which case the handler is aborted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_start** | [**V1LifecycleHandler**](V1LifecycleHandler.md) |  | [optional] 
**pre_stop** | [**V1LifecycleHandler**](V1LifecycleHandler.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_lifecycle import V1Lifecycle

# TODO update the JSON string below
json = "{}"
# create an instance of V1Lifecycle from a JSON string
v1_lifecycle_instance = V1Lifecycle.from_json(json)
# print the JSON string representation of the object
print V1Lifecycle.to_json()

# convert the object into a dict
v1_lifecycle_dict = v1_lifecycle_instance.to_dict()
# create an instance of V1Lifecycle from a dict
v1_lifecycle_form_dict = v1_lifecycle.from_dict(v1_lifecycle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


