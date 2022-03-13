# V1AggregationRule

AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_role_selectors** | [**[V1LabelSelector]**](V1LabelSelector.md) | ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole&#39;s permissions will be added | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


