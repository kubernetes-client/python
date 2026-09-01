# V1alpha3DisruptionMode

DisruptionMode defines how individual entities within a group can be disrupted. Exactly one mode can be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **object** | all specifies that all children can only be disrupted together. | [optional]
**single** | **object** | single specifies that children can be disrupted independently from each other. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1alpha3_disruption_mode import V1alpha3DisruptionMode

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3DisruptionMode from a JSON string
v1alpha3_disruption_mode_instance = V1alpha3DisruptionMode.from_json(json)
# print the JSON string representation of the object
print(V1alpha3DisruptionMode.to_json())

# convert the object into a dict
v1alpha3_disruption_mode_dict = v1alpha3_disruption_mode_instance.to_dict()
# create an instance of V1alpha3DisruptionMode from a dict
v1alpha3_disruption_mode_from_dict = V1alpha3DisruptionMode.from_dict(v1alpha3_disruption_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
