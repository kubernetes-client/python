# V1Sysctl

Sysctl defines a kernel parameter to be set

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of a property to set | 
**value** | **str** | Value of a property to set | 

## Example

```python
from kubernetes.client.models.v1_sysctl import V1Sysctl

# TODO update the JSON string below
json = "{}"
# create an instance of V1Sysctl from a JSON string
v1_sysctl_instance = V1Sysctl.from_json(json)
# print the JSON string representation of the object
print V1Sysctl.to_json()

# convert the object into a dict
v1_sysctl_dict = v1_sysctl_instance.to_dict()
# create an instance of V1Sysctl from a dict
v1_sysctl_form_dict = v1_sysctl.from_dict(v1_sysctl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


