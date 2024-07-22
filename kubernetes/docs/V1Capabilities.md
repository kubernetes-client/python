# V1Capabilities

Adds and removes POSIX capabilities from running containers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add** | **List[str]** | Added capabilities | [optional] 
**drop** | **List[str]** | Removed capabilities | [optional] 

## Example

```python
from kubernetes.client.models.v1_capabilities import V1Capabilities

# TODO update the JSON string below
json = "{}"
# create an instance of V1Capabilities from a JSON string
v1_capabilities_instance = V1Capabilities.from_json(json)
# print the JSON string representation of the object
print V1Capabilities.to_json()

# convert the object into a dict
v1_capabilities_dict = v1_capabilities_instance.to_dict()
# create an instance of V1Capabilities from a dict
v1_capabilities_form_dict = v1_capabilities.from_dict(v1_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


