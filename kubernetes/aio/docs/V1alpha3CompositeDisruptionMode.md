# V1alpha3CompositeDisruptionMode

CompositeDisruptionMode defines how individual entities within a composite pod group can be disrupted. Exactly one mode must be set.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **object** | all specifies that all children groups can only be disrupted together. | [optional]
**single** | **object** | single specifies that children groups can be disrupted independently from each other. | [optional]

## Example

```python
from kubernetes.aio.client.models.v1alpha3_composite_disruption_mode import V1alpha3CompositeDisruptionMode

# TODO update the JSON string below
json = "{}"
# create an instance of V1alpha3CompositeDisruptionMode from a JSON string
v1alpha3_composite_disruption_mode_instance = V1alpha3CompositeDisruptionMode.from_json(json)
# print the JSON string representation of the object
print(V1alpha3CompositeDisruptionMode.to_json())

# convert the object into a dict
v1alpha3_composite_disruption_mode_dict = v1alpha3_composite_disruption_mode_instance.to_dict()
# create an instance of V1alpha3CompositeDisruptionMode from a dict
v1alpha3_composite_disruption_mode_from_dict = V1alpha3CompositeDisruptionMode.from_dict(v1alpha3_composite_disruption_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
