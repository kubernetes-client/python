# V1beta1ParamKind

ParamKind is a tuple of Group Kind and Version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion is the API group version the resources belong to. In format of \&quot;group/version\&quot;. Required. | [optional] 
**kind** | **str** | Kind is the API kind the resources belong to. Required. | [optional] 

## Example

```python
from kubernetes.client.models.v1beta1_param_kind import V1beta1ParamKind

# TODO update the JSON string below
json = "{}"
# create an instance of V1beta1ParamKind from a JSON string
v1beta1_param_kind_instance = V1beta1ParamKind.from_json(json)
# print the JSON string representation of the object
print V1beta1ParamKind.to_json()

# convert the object into a dict
v1beta1_param_kind_dict = v1beta1_param_kind_instance.to_dict()
# create an instance of V1beta1ParamKind from a dict
v1beta1_param_kind_form_dict = v1beta1_param_kind.from_dict(v1beta1_param_kind_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


