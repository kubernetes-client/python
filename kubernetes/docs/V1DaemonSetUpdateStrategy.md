# V1DaemonSetUpdateStrategy

DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rolling_update** | [**V1RollingUpdateDaemonSet**](V1RollingUpdateDaemonSet.md) |  | [optional] 
**type** | **str** | Type of daemon set update. Can be \&quot;RollingUpdate\&quot; or \&quot;OnDelete\&quot;. Default is RollingUpdate. | [optional] 

## Example

```python
from kubernetes.client.models.v1_daemon_set_update_strategy import V1DaemonSetUpdateStrategy

# TODO update the JSON string below
json = "{}"
# create an instance of V1DaemonSetUpdateStrategy from a JSON string
v1_daemon_set_update_strategy_instance = V1DaemonSetUpdateStrategy.from_json(json)
# print the JSON string representation of the object
print V1DaemonSetUpdateStrategy.to_json()

# convert the object into a dict
v1_daemon_set_update_strategy_dict = v1_daemon_set_update_strategy_instance.to_dict()
# create an instance of V1DaemonSetUpdateStrategy from a dict
v1_daemon_set_update_strategy_form_dict = v1_daemon_set_update_strategy.from_dict(v1_daemon_set_update_strategy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


