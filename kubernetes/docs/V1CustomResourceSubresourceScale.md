# V1CustomResourceSubresourceScale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_selector_path** | **str** | labelSelectorPath defines the JSON path inside of a custom resource that corresponds to Scale &#x60;status.selector&#x60;. Only JSON paths without the array notation are allowed. Must be a JSON Path under &#x60;.status&#x60; or &#x60;.spec&#x60;. Must be set to work with HorizontalPodAutoscaler. The field pointed by this JSON path must be a string field (not a complex selector struct) which contains a serialized label selector in string form. More info: https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions#scale-subresource If there is no value under the given path in the custom resource, the &#x60;status.selector&#x60; value in the &#x60;/scale&#x60; subresource will default to the empty string. | [optional] 
**spec_replicas_path** | **str** | specReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale &#x60;spec.replicas&#x60;. Only JSON paths without the array notation are allowed. Must be a JSON Path under &#x60;.spec&#x60;. If there is no value under the given path in the custom resource, the &#x60;/scale&#x60; subresource will return an error on GET. | 
**status_replicas_path** | **str** | statusReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale &#x60;status.replicas&#x60;. Only JSON paths without the array notation are allowed. Must be a JSON Path under &#x60;.status&#x60;. If there is no value under the given path in the custom resource, the &#x60;status.replicas&#x60; value in the &#x60;/scale&#x60; subresource will default to 0. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


