# V1DeviceAttribute

DeviceAttribute must have exactly one field set.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bool** | **bool** | BoolValue is a true/false value. | [optional] 
**bools** | **list[bool]** | BoolValues is a non-empty list of true/false values. | [optional] 
**int** | **int** | IntValue is a number. | [optional] 
**ints** | **list[int]** | IntValues is a non-empty list of numbers.  This is an alpha field and requires enabling the DRAListTypeAttributes feature gate. | [optional] 
**string** | **str** | StringValue is a string. Must not be longer than 64 characters. | [optional] 
**strings** | **list[str]** | StringValues is a non-empty list of strings. Each string must not be longer than 64 characters.  This is an alpha field and requires enabling the DRAListTypeAttributes feature gate. | [optional] 
**version** | **str** | VersionValue is a semantic version according to semver.org spec 2.0.0. Must not be longer than 64 characters. | [optional] 
**versions** | **list[str]** | VersionValues is a non-empty list of semantic versions according to semver.org spec 2.0.0. Each version string must not be longer than 64 characters.  This is an alpha field and requires enabling the DRAListTypeAttributes feature gate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


