# V1ConfigMapVolumeSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_mode** | **int** | Optional: mode bits to use on created files by default. Must be a value between 0 and 0777. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. | [optional] 
**items** | [**list[V1KeyToPath]**](V1KeyToPath.md) | If unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error. Paths must be relative and may not contain the &#39;..&#39; path or start with &#39;..&#39;. | [optional] 
**name** | **str** | Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


