# V1FlowDistinguisherMethod

FlowDistinguisherMethod specifies the method of a flow distinguisher.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | &#x60;type&#x60; is the type of flow distinguisher method The supported types are \&quot;ByUser\&quot; and \&quot;ByNamespace\&quot;. Required. | 

## Example

```python
from kubernetes.client.models.v1_flow_distinguisher_method import V1FlowDistinguisherMethod

# TODO update the JSON string below
json = "{}"
# create an instance of V1FlowDistinguisherMethod from a JSON string
v1_flow_distinguisher_method_instance = V1FlowDistinguisherMethod.from_json(json)
# print the JSON string representation of the object
print V1FlowDistinguisherMethod.to_json()

# convert the object into a dict
v1_flow_distinguisher_method_dict = v1_flow_distinguisher_method_instance.to_dict()
# create an instance of V1FlowDistinguisherMethod from a dict
v1_flow_distinguisher_method_form_dict = v1_flow_distinguisher_method.from_dict(v1_flow_distinguisher_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


