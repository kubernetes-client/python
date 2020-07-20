# V1beta2StatefulSetUpdateStrategy

StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform updates. It includes any additional parameters necessary to perform the update for the indicated strategy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rolling_update** | [**V1beta2RollingUpdateStatefulSetStrategy**](V1beta2RollingUpdateStatefulSetStrategy.md) |  | [optional] 
**type** | **str** | Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


