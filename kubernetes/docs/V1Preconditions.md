# V1Preconditions

Preconditions must be fulfilled before an operation (update, delete, etc.) is carried out.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_version** | **str** | Specifies the target ResourceVersion | [optional] 
**uid** | **str** | Specifies the target UID. | [optional] 

## Example

```python
from kubernetes.client.models.v1_preconditions import V1Preconditions

# TODO update the JSON string below
json = "{}"
# create an instance of V1Preconditions from a JSON string
v1_preconditions_instance = V1Preconditions.from_json(json)
# print the JSON string representation of the object
print V1Preconditions.to_json()

# convert the object into a dict
v1_preconditions_dict = v1_preconditions_instance.to_dict()
# create an instance of V1Preconditions from a dict
v1_preconditions_form_dict = v1_preconditions.from_dict(v1_preconditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


