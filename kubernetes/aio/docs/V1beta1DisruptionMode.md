# V1beta1DisruptionMode

DisruptionMode defines how individual entities within a group can be disrupted. Exactly one mode can be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **object** | all specifies that all children can only be disrupted together. | [optional]
**single** | **object** | single specifies that children can be disrupted independently from each other. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1beta1_disruption_mode import V1beta1DisruptionMode

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1DisruptionMode from a JSON string
v1beta1_disruption_mode_instance = V1beta1DisruptionMode.from_json(json)
# print the JSON string representation of the object
print(V1beta1DisruptionMode.to_json())

# convert the object into a dict
v1beta1_disruption_mode_dict = v1beta1_disruption_mode_instance.to_dict()
# create an instance of V1beta1DisruptionMode from a dict
v1beta1_disruption_mode_from_dict = V1beta1DisruptionMode.from_dict(v1beta1_disruption_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
