# V1GroupVersionForDiscovery

GroupVersion contains the \"group/version\" and \"version\" string of a version. It is made a struct to keep extensibility.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_version** | **str** | groupVersion specifies the API group and version in the form \&quot;group/version\&quot; | 
**version** | **str** | version specifies the version in the form of \&quot;version\&quot;. This is to save the kubernetes.clients the trouble of splitting the GroupVersion. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


