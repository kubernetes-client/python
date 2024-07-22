# V1APIServiceStatus

APIServiceStatus contains derived information about an API server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[V1APIServiceCondition]**](V1APIServiceCondition.md) | Current service state of apiService. | [optional] 

## Example

```python
from kubernetes.client.models.v1_api_service_status import V1APIServiceStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V1APIServiceStatus from a JSON string
v1_api_service_status_instance = V1APIServiceStatus.from_json(json)
# print the JSON string representation of the object
print V1APIServiceStatus.to_json()

# convert the object into a dict
v1_api_service_status_dict = v1_api_service_status_instance.to_dict()
# create an instance of V1APIServiceStatus from a dict
v1_api_service_status_form_dict = v1_api_service_status.from_dict(v1_api_service_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


