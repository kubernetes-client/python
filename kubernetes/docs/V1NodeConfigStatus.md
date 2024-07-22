# V1NodeConfigStatus

NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | [**V1NodeConfigSource**](V1NodeConfigSource.md) |  | [optional] 
**assigned** | [**V1NodeConfigSource**](V1NodeConfigSource.md) |  | [optional] 
**error** | **str** | Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions. | [optional] 
**last_known_good** | [**V1NodeConfigSource**](V1NodeConfigSource.md) |  | [optional] 

## Example

```python
from kubernetes.client.models.v1_node_config_status import V1NodeConfigStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1NodeConfigStatus from a JSON string
v1_node_config_status_instance = V1NodeConfigStatus.from_json(json)
# print the JSON string representation of the object
print V1NodeConfigStatus.to_json()

# convert the object into a dict
v1_node_config_status_dict = v1_node_config_status_instance.to_dict()
# create an instance of V1NodeConfigStatus from a dict
v1_node_config_status_form_dict = v1_node_config_status.from_dict(v1_node_config_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


