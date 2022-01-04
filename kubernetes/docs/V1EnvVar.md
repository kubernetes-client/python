# V1EnvVar

EnvVar represents an environment variable present in a Container.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the environment variable. Must be a C_IDENTIFIER. | 
**value** | **str** | Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \&quot;$$(VAR_NAME)\&quot; will produce the string literal \&quot;$(VAR_NAME)\&quot;. Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to \&quot;\&quot;. | [optional] 
**value_from** | [**V1EnvVarSource**](V1EnvVarSource.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


