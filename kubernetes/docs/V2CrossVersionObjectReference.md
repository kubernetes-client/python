# V2CrossVersionObjectReference

CrossVersionObjectReference contains enough information to let you identify the referred resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | apiVersion is the API version of the referent | [optional] 
**kind** | **str** | kind is the kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds | 
**name** | **str** | name is the name of the referent; More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names | 

## Example

```python
from kubernetes.client.models.v2_cross_version_object_reference import V2CrossVersionObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of V2CrossVersionObjectReference from a JSON string
v2_cross_version_object_reference_instance = V2CrossVersionObjectReference.from_json(json)
# print the JSON string representation of the object
print V2CrossVersionObjectReference.to_json()

# convert the object into a dict
v2_cross_version_object_reference_dict = v2_cross_version_object_reference_instance.to_dict()
# create an instance of V2CrossVersionObjectReference from a dict
v2_cross_version_object_reference_form_dict = v2_cross_version_object_reference.from_dict(v2_cross_version_object_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


