# kubernetes.client.model.v1_ephemeral_container.V1EphemeralContainer

An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.  To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An EphemeralContainer is a temporary container that you may add to an existing Pod for user-initiated activities such as debugging. Ephemeral containers have no resource or scheduling guarantees, and they will not be restarted when they exit or when a Pod is removed or restarted. The kubelet may evict a Pod if an ephemeral container causes the Pod to exceed its resource allocation.  To add an ephemeral container, use the ephemeralcontainers subresource of an existing Pod. Ephemeral containers may not be removed or restarted. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Name of the ephemeral container specified as a DNS_LABEL. This name must be unique among all containers, init containers and ephemeral containers. | 
**[args](#args)** | list, tuple,  | tuple,  | Arguments to the entrypoint. The image&#x27;s CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container&#x27;s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \&quot;$$(VAR_NAME)\&quot; will produce the string literal \&quot;$(VAR_NAME)\&quot;. Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell | [optional] 
**[command](#command)** | list, tuple,  | tuple,  | Entrypoint array. Not executed within a shell. The image&#x27;s ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container&#x27;s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \&quot;$$(VAR_NAME)\&quot; will produce the string literal \&quot;$(VAR_NAME)\&quot;. Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell | [optional] 
**[env](#env)** | list, tuple,  | tuple,  | List of environment variables to set in the container. Cannot be updated. | [optional] 
**[envFrom](#envFrom)** | list, tuple,  | tuple,  | List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. | [optional] 
**image** | str,  | str,  | Container image name. More info: https://kubernetes.io/docs/concepts/containers/images | [optional] 
**imagePullPolicy** | str,  | str,  | Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images   | [optional] 
**lifecycle** | [**V1Lifecycle**](V1Lifecycle.md) | [**V1Lifecycle**](V1Lifecycle.md) |  | [optional] 
**livenessProbe** | [**V1Probe**](V1Probe.md) | [**V1Probe**](V1Probe.md) |  | [optional] 
**[ports](#ports)** | list, tuple,  | tuple,  | Ports are not allowed for ephemeral containers. | [optional] 
**readinessProbe** | [**V1Probe**](V1Probe.md) | [**V1Probe**](V1Probe.md) |  | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | [**V1ResourceRequirements**](V1ResourceRequirements.md) |  | [optional] 
**securityContext** | [**V1SecurityContext**](V1SecurityContext.md) | [**V1SecurityContext**](V1SecurityContext.md) |  | [optional] 
**startupProbe** | [**V1Probe**](V1Probe.md) | [**V1Probe**](V1Probe.md) |  | [optional] 
**stdin** | bool,  | BoolClass,  | Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false. | [optional] 
**stdinOnce** | bool,  | BoolClass,  | Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first kubernetes.client attaches to stdin, and then remains open and accepts data until the kubernetes.client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false | [optional] 
**targetContainerName** | str,  | str,  | If set, the name of the container from PodSpec that this ephemeral container targets. The ephemeral container will be run in the namespaces (IPC, PID, etc) of this container. If not set then the ephemeral container uses the namespaces configured in the Pod spec.  The container runtime must implement support for this feature. If the runtime does not support namespace targeting then the result of setting this field is undefined. | [optional] 
**terminationMessagePath** | str,  | str,  | Optional: Path at which the file to which the container&#x27;s termination message will be written is mounted into the container&#x27;s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated. | [optional] 
**terminationMessagePolicy** | str,  | str,  | Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.   | [optional] 
**tty** | bool,  | BoolClass,  | Whether this container should allocate a TTY for itself, also requires &#x27;stdin&#x27; to be true. Default is false. | [optional] 
**[volumeDevices](#volumeDevices)** | list, tuple,  | tuple,  | volumeDevices is the list of block devices to be used by the container. | [optional] 
**[volumeMounts](#volumeMounts)** | list, tuple,  | tuple,  | Pod volumes to mount into the container&#x27;s filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated. | [optional] 
**workingDir** | str,  | str,  | Container&#x27;s working directory. If not specified, the container runtime&#x27;s default will be used, which might be configured in the container image. Cannot be updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# args

Arguments to the entrypoint. The image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Arguments to the entrypoint. The image&#x27;s CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container&#x27;s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \&quot;$$(VAR_NAME)\&quot; will produce the string literal \&quot;$(VAR_NAME)\&quot;. Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# command

Entrypoint array. Not executed within a shell. The image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \"$$(VAR_NAME)\" will produce the string literal \"$(VAR_NAME)\". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Entrypoint array. Not executed within a shell. The image&#x27;s ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container&#x27;s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \&quot;$$(VAR_NAME)\&quot; will produce the string literal \&quot;$(VAR_NAME)\&quot;. Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# env

List of environment variables to set in the container. Cannot be updated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of environment variables to set in the container. Cannot be updated. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1EnvVar**](V1EnvVar.md) | [**V1EnvVar**](V1EnvVar.md) | [**V1EnvVar**](V1EnvVar.md) |  | 

# envFrom

List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of sources to populate environment variables in the container. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the container is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1EnvFromSource**](V1EnvFromSource.md) | [**V1EnvFromSource**](V1EnvFromSource.md) | [**V1EnvFromSource**](V1EnvFromSource.md) |  | 

# ports

Ports are not allowed for ephemeral containers.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Ports are not allowed for ephemeral containers. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1ContainerPort**](V1ContainerPort.md) | [**V1ContainerPort**](V1ContainerPort.md) | [**V1ContainerPort**](V1ContainerPort.md) |  | 

# volumeDevices

volumeDevices is the list of block devices to be used by the container.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | volumeDevices is the list of block devices to be used by the container. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1VolumeDevice**](V1VolumeDevice.md) | [**V1VolumeDevice**](V1VolumeDevice.md) | [**V1VolumeDevice**](V1VolumeDevice.md) |  | 

# volumeMounts

Pod volumes to mount into the container's filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Pod volumes to mount into the container&#x27;s filesystem. Subpath mounts are not allowed for ephemeral containers. Cannot be updated. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**V1VolumeMount**](V1VolumeMount.md) | [**V1VolumeMount**](V1VolumeMount.md) | [**V1VolumeMount**](V1VolumeMount.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

