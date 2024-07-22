# V1ContainerImage

Describe a container image

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | Names by which this image is known. e.g. [\&quot;kubernetes.example/hyperkube:v1.0.7\&quot;, \&quot;cloud-vendor.registry.example/cloud-vendor/hyperkube:v1.0.7\&quot;] | [optional] 
**size_bytes** | **int** | The size of the image in bytes. | [optional] 

## Example

```python
from kubernetes.client.models.v1_container_image import V1ContainerImage

# TODO update the JSON string below
json = "{}"
# create an instance of V1ContainerImage from a JSON string
v1_container_image_instance = V1ContainerImage.from_json(json)
# print the JSON string representation of the object
print V1ContainerImage.to_json()

# convert the object into a dict
v1_container_image_dict = v1_container_image_instance.to_dict()
# create an instance of V1ContainerImage from a dict
v1_container_image_form_dict = v1_container_image.from_dict(v1_container_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


