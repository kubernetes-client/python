# V1HTTPHeader

HTTPHeader describes a custom header to be used in HTTP probes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header. | 
**value** | **str** | The header field value | 

## Example

```python
from kubernetes.client.models.v1_http_header import V1HTTPHeader

# TODO update the JSON string below
json = "{}"
# create an instance of V1HTTPHeader from a JSON string
v1_http_header_instance = V1HTTPHeader.from_json(json)
# print the JSON string representation of the object
print V1HTTPHeader.to_json()

# convert the object into a dict
v1_http_header_dict = v1_http_header_instance.to_dict()
# create an instance of V1HTTPHeader from a dict
v1_http_header_form_dict = v1_http_header.from_dict(v1_http_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


