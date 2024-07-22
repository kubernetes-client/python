# V1FlowSchemaSpec

FlowSchemaSpec describes how the FlowSchema's specification looks like.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distinguisher_method** | [**V1FlowDistinguisherMethod**](V1FlowDistinguisherMethod.md) |  | [optional] 
**matching_precedence** | **int** | &#x60;matchingPrecedence&#x60; is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence.  Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default. | [optional] 
**priority_level_configuration** | [**V1PriorityLevelConfigurationReference**](V1PriorityLevelConfigurationReference.md) |  | 
**rules** | [**List[V1PolicyRulesWithSubjects]**](V1PolicyRulesWithSubjects.md) | &#x60;rules&#x60; describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema. | [optional] 

## Example

```python
from kubernetes.client.models.v1_flow_schema_spec import V1FlowSchemaSpec

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowSchemaSpec from a JSON string
v1_flow_schema_spec_instance = V1FlowSchemaSpec.from_json(json)
# print the JSON string representation of the object
print V1FlowSchemaSpec.to_json()

# convert the object into a dict
v1_flow_schema_spec_dict = v1_flow_schema_spec_instance.to_dict()
# create an instance of V1FlowSchemaSpec from a dict
v1_flow_schema_spec_form_dict = v1_flow_schema_spec.from_dict(v1_flow_schema_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


