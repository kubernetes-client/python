# V1RollingUpdateStatefulSetStrategy

RollingUpdateStatefulSetStrategy is used to communicate parameter for RollingUpdateStatefulSetStrategyType.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_unavailable** | **object** | The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0. Defaults to 1. This field is alpha-level and is only honored by servers that enable the MaxUnavailableStatefulSet feature. The field applies to all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0 to Replicas-1, it will be counted towards MaxUnavailable. | [optional] 
**partition** | **int** | Partition indicates the ordinal at which the StatefulSet should be partitioned for updates. During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based deployment. The default value is 0. | [optional] 

## Example

```python
from kubernetes.client.models.v1_rolling_update_stateful_set_strategy import V1RollingUpdateStatefulSetStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of V1RollingUpdateStatefulSetStrategy from a JSON string
v1_rolling_update_stateful_set_strategy_instance = V1RollingUpdateStatefulSetStrategy.from_json(json)
# print the JSON string representation of the object
print V1RollingUpdateStatefulSetStrategy.to_json()

# convert the object into a dict
v1_rolling_update_stateful_set_strategy_dict = v1_rolling_update_stateful_set_strategy_instance.to_dict()
# create an instance of V1RollingUpdateStatefulSetStrategy from a dict
v1_rolling_update_stateful_set_strategy_form_dict = v1_rolling_update_stateful_set_strategy.from_dict(v1_rolling_update_stateful_set_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


