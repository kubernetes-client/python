# V1FlowSchemaStatus

FlowSchemaStatus represents the current state of a FlowSchema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1FlowSchemaCondition]**](V1FlowSchemaCondition.md) | &#x60;conditions&#x60; is a list of the current states of FlowSchema. | [optional] 

## Example

```python
from kubernetes.client.models.v1_flow_schema_status import V1FlowSchemaStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowSchemaStatus from a JSON string
v1_flow_schema_status_instance = V1FlowSchemaStatus.from_json(json)
# print the JSON string representation of the object
print V1FlowSchemaStatus.to_json()

# convert the object into a dict
v1_flow_schema_status_dict = v1_flow_schema_status_instance.to_dict()
# create an instance of V1FlowSchemaStatus from a dict
v1_flow_schema_status_form_dict = v1_flow_schema_status.from_dict(v1_flow_schema_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


