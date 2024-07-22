# V1RollingUpdateDeployment

Spec to control the desired behavior of rolling update.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_surge** | **object** | The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods. | [optional] 
**max_unavailable** | **object** | The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods. | [optional] 

## Example

```python
from kubernetes.client.models.v1_rolling_update_deployment import V1RollingUpdateDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of V1RollingUpdateDeployment from a JSON string
v1_rolling_update_deployment_instance = V1RollingUpdateDeployment.from_json(json)
# print the JSON string representation of the object
print V1RollingUpdateDeployment.to_json()

# convert the object into a dict
v1_rolling_update_deployment_dict = v1_rolling_update_deployment_instance.to_dict()
# create an instance of V1RollingUpdateDeployment from a dict
v1_rolling_update_deployment_form_dict = v1_rolling_update_deployment.from_dict(v1_rolling_update_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


