# V1UncountedTerminatedPods

UncountedTerminatedPods holds UIDs of Pods that have terminated but haven't been accounted in Job status counters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed** | **List[str]** | failed holds UIDs of failed Pods. | [optional] 
**succeeded** | **List[str]** | succeeded holds UIDs of succeeded Pods. | [optional] 

## Example

```python
from kubernetes.client.models.v1_uncounted_terminated_pods import V1UncountedTerminatedPods

# TODO update the JSON string below
json = "{}"
# create an instance of V1UncountedTerminatedPods from a JSON string
v1_uncounted_terminated_pods_instance = V1UncountedTerminatedPods.from_json(json)
# print the JSON string representation of the object
print V1UncountedTerminatedPods.to_json()

# convert the object into a dict
v1_uncounted_terminated_pods_dict = v1_uncounted_terminated_pods_instance.to_dict()
# create an instance of V1UncountedTerminatedPods from a dict
v1_uncounted_terminated_pods_form_dict = v1_uncounted_terminated_pods.from_dict(v1_uncounted_terminated_pods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


