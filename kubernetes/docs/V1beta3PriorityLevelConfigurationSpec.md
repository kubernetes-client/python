# V1beta3PriorityLevelConfigurationSpec

PriorityLevelConfigurationSpec specifies the configuration of a priority level.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exempt** | [**V1beta3ExemptPriorityLevelConfiguration**](V1beta3ExemptPriorityLevelConfiguration.md) |  | [optional] 
**limited** | [**V1beta3LimitedPriorityLevelConfiguration**](V1beta3LimitedPriorityLevelConfiguration.md) |  | [optional] 
**type** | **str** | &#x60;type&#x60; indicates whether this priority level is subject to limitation on request execution.  A value of &#x60;\&quot;Exempt\&quot;&#x60; means that requests of this priority level are not subject to a limit (and thus are never queued) and do not detract from the capacity made available to other priority levels.  A value of &#x60;\&quot;Limited\&quot;&#x60; means that (a) requests of this priority level _are_ subject to limits and (b) some of the server&#39;s limited capacity is made available exclusively to this priority level. Required. | 

## Example

```python
from kubernetes.client.models.v1beta3_priority_level_configuration_spec import V1beta3PriorityLevelConfigurationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta3PriorityLevelConfigurationSpec from a JSON string
v1beta3_priority_level_configuration_spec_instance = V1beta3PriorityLevelConfigurationSpec.from_json(json)
# print the JSON string representation of the object
print V1beta3PriorityLevelConfigurationSpec.to_json()

# convert the object into a dict
v1beta3_priority_level_configuration_spec_dict = v1beta3_priority_level_configuration_spec_instance.to_dict()
# create an instance of V1beta3PriorityLevelConfigurationSpec from a dict
v1beta3_priority_level_configuration_spec_form_dict = v1beta3_priority_level_configuration_spec.from_dict(v1beta3_priority_level_configuration_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


