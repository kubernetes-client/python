# V1alpha3DeviceTaint

The device this taint is attached to has the \"effect\" on any claim which does not tolerate the taint and, through the claim, to pods using the claim.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | The effect of the taint on claims that do not tolerate the taint and through such claims on the pods using them.  Valid effects are None, NoSchedule and NoExecute. PreferNoSchedule as used for nodes is not valid here. More effects may get added in the future. Consumers must treat unknown effects like None. | 
**key** | **str** | The taint key to be applied to a device. Must be a label name. | 
**time_added** | **datetime** | TimeAdded represents the time at which the taint was added. Added automatically during create or update if not set. | [optional] 
**value** | **str** | The taint value corresponding to the taint key. Must be a label value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


