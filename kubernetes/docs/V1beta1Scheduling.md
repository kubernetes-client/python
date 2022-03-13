# V1beta1Scheduling

Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_selector** | **{str: (str,)}** | nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod&#39;s existing nodeSelector. Any conflicts will cause the pod to be rejected in admission. | [optional] 
**tolerations** | [**[V1Toleration]**](V1Toleration.md) | tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


