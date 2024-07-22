# V1StatefulSetUpdateStrategy

StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform updates. It includes any additional parameters necessary to perform the update for the indicated strategy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rolling_update** | [**V1RollingUpdateStatefulSetStrategy**](V1RollingUpdateStatefulSetStrategy.md) |  | [optional] 
**type** | **str** | Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate. | [optional] 

## Example

```python
from kubernetes.client.models.v1_stateful_set_update_strategy import V1StatefulSetUpdateStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of V1StatefulSetUpdateStrategy from a JSON string
v1_stateful_set_update_strategy_instance = V1StatefulSetUpdateStrategy.from_json(json)
# print the JSON string representation of the object
print V1StatefulSetUpdateStrategy.to_json()

# convert the object into a dict
v1_stateful_set_update_strategy_dict = v1_stateful_set_update_strategy_instance.to_dict()
# create an instance of V1StatefulSetUpdateStrategy from a dict
v1_stateful_set_update_strategy_form_dict = v1_stateful_set_update_strategy.from_dict(v1_stateful_set_update_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


