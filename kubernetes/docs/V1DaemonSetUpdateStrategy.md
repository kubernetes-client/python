# V1DaemonSetUpdateStrategy

DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rolling_update** | [**V1RollingUpdateDaemonSet**](V1RollingUpdateDaemonSet.md) |  | [optional] 
**type** | **str** | Type of daemon set update. Can be \&quot;RollingUpdate\&quot; or \&quot;OnDelete\&quot;. Default is RollingUpdate.  Possible enum values:  - &#x60;\&quot;OnDelete\&quot;&#x60; Replace the old daemons only when it&#39;s killed  - &#x60;\&quot;RollingUpdate\&quot;&#x60; Replace the old daemons by new ones using rolling update i.e replace them on each node one after the other. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


