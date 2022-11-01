# kubernetes.client.model.v1_probe.V1Probe

Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Probe describes a health check to be performed against a container to determine whether it is alive or ready to receive traffic. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**exec** | [**V1ExecAction**](V1ExecAction.md) | [**V1ExecAction**](V1ExecAction.md) |  | [optional] 
**failureThreshold** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1. | [optional] value must be a 32 bit integer
**grpc** | [**V1GRPCAction**](V1GRPCAction.md) | [**V1GRPCAction**](V1GRPCAction.md) |  | [optional] 
**httpGet** | [**V1HTTPGetAction**](V1HTTPGetAction.md) | [**V1HTTPGetAction**](V1HTTPGetAction.md) |  | [optional] 
**initialDelaySeconds** | decimal.Decimal, int,  | decimal.Decimal,  | Number of seconds after the container has started before liveness probes are initiated. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] value must be a 32 bit integer
**periodSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1. | [optional] value must be a 32 bit integer
**successThreshold** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1. | [optional] value must be a 32 bit integer
**tcpSocket** | [**V1TCPSocketAction**](V1TCPSocketAction.md) | [**V1TCPSocketAction**](V1TCPSocketAction.md) |  | [optional] 
**terminationGracePeriodSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod&#x27;s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset. | [optional] value must be a 64 bit integer
**timeoutSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

