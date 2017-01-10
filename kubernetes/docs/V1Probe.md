# V1Probe

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_exec** | [**V1ExecAction**](V1ExecAction.md) | One and only one of the following should be specified. Exec specifies the action to take. | [optional] 
**failure_threshold** | **int** | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. | [optional] 
**http_get** | [**V1HTTPGetAction**](V1HTTPGetAction.md) | HTTPGet specifies the http request to perform. | [optional] 
**initial_delay_seconds** | **int** | Number of seconds after the container has started before liveness probes are initiated. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes | [optional] 
**period_seconds** | **int** | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. | [optional] 
**success_threshold** | **int** | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness. Minimum value is 1. | [optional] 
**tcp_socket** | [**V1TCPSocketAction**](V1TCPSocketAction.md) | TCPSocket specifies an action involving a TCP port. TCP hooks not yet supported | [optional] 
**timeout_seconds** | **int** | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: http://kubernetes.io/docs/user-guide/pod-states#container-probes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


