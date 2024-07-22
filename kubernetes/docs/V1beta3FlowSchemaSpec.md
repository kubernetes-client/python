# V1beta3FlowSchemaSpec

FlowSchemaSpec describes how the FlowSchema's specification looks like.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distinguisher_method** | [**V1beta3FlowDistinguisherMethod**](V1beta3FlowDistinguisherMethod.md) |  | [optional] 
**matching_precedence** | **int** | &#x60;matchingPrecedence&#x60; is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence.  Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default. | [optional] 
**priority_level_configuration** | [**V1beta3PriorityLevelConfigurationReference**](V1beta3PriorityLevelConfigurationReference.md) |  | 
**rules** | [**List[V1beta3PolicyRulesWithSubjects]**](V1beta3PolicyRulesWithSubjects.md) | &#x60;rules&#x60; describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema. | [optional] 

## Example

```python
from kubernetes.client.models.v1beta3_flow_schema_spec import V1beta3FlowSchemaSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta3FlowSchemaSpec from a JSON string
v1beta3_flow_schema_spec_instance = V1beta3FlowSchemaSpec.from_json(json)
# print the JSON string representation of the object
print V1beta3FlowSchemaSpec.to_json()

# convert the object into a dict
v1beta3_flow_schema_spec_dict = v1beta3_flow_schema_spec_instance.to_dict()
# create an instance of V1beta3FlowSchemaSpec from a dict
v1beta3_flow_schema_spec_form_dict = v1beta3_flow_schema_spec.from_dict(v1beta3_flow_schema_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


