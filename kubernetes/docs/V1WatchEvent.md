# V1WatchEvent

Event represents a single event to a watched resource.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **bool, date, datetime, dict, float, int, list, str, none_type** | Object is:  * If Type is Added or Modified: the new state of the object.  * If Type is Deleted: the state of the object immediately before deletion.  * If Type is Error: *Status is recommended; other types may make sense    depending on context. | 
**type** | **str** |  | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


