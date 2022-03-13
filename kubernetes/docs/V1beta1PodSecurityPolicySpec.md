# V1beta1PodSecurityPolicySpec

PodSecurityPolicySpec defines the policy enforced.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fs_group** | [**V1beta1FSGroupStrategyOptions**](V1beta1FSGroupStrategyOptions.md) |  | 
**run_as_user** | [**V1beta1RunAsUserStrategyOptions**](V1beta1RunAsUserStrategyOptions.md) |  | 
**se_linux** | [**V1beta1SELinuxStrategyOptions**](V1beta1SELinuxStrategyOptions.md) |  | 
**supplemental_groups** | [**V1beta1SupplementalGroupsStrategyOptions**](V1beta1SupplementalGroupsStrategyOptions.md) |  | 
**allow_privilege_escalation** | **bool** | allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true. | [optional] 
**allowed_csi_drivers** | [**[V1beta1AllowedCSIDriver]**](V1beta1AllowedCSIDriver.md) | AllowedCSIDrivers is an allowlist of inline CSI drivers that must be explicitly set to be embedded within a pod spec. An empty value indicates that any CSI driver can be used for inline ephemeral volumes. This is a beta field, and is only honored if the API server enables the CSIInlineVolume feature gate. | [optional] 
**allowed_capabilities** | **[str]** | allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author&#39;s discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities. | [optional] 
**allowed_flex_volumes** | [**[V1beta1AllowedFlexVolume]**](V1beta1AllowedFlexVolume.md) | allowedFlexVolumes is an allowlist of Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This parameter is effective only when the usage of the Flexvolumes is allowed in the \&quot;volumes\&quot; field. | [optional] 
**allowed_host_paths** | [**[V1beta1AllowedHostPath]**](V1beta1AllowedHostPath.md) | allowedHostPaths is an allowlist of host paths. Empty indicates that all host paths may be used. | [optional] 
**allowed_proc_mount_types** | **[str]** | AllowedProcMountTypes is an allowlist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled. | [optional] 
**allowed_unsafe_sysctls** | **[str]** | allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \&quot;*\&quot; in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to allowlist all allowed unsafe sysctls explicitly to avoid rejection.  Examples: e.g. \&quot;foo/*\&quot; allows \&quot;foo/bar\&quot;, \&quot;foo/baz\&quot;, etc. e.g. \&quot;foo.*\&quot; allows \&quot;foo.bar\&quot;, \&quot;foo.baz\&quot;, etc. | [optional] 
**default_add_capabilities** | **[str]** | defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list. | [optional] 
**default_allow_privilege_escalation** | **bool** | defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process. | [optional] 
**forbidden_sysctls** | **[str]** | forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \&quot;*\&quot; in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.  Examples: e.g. \&quot;foo/*\&quot; forbids \&quot;foo/bar\&quot;, \&quot;foo/baz\&quot;, etc. e.g. \&quot;foo.*\&quot; forbids \&quot;foo.bar\&quot;, \&quot;foo.baz\&quot;, etc. | [optional] 
**host_ipc** | **bool** | hostIPC determines if the policy allows the use of HostIPC in the pod spec. | [optional] 
**host_network** | **bool** | hostNetwork determines if the policy allows the use of HostNetwork in the pod spec. | [optional] 
**host_pid** | **bool** | hostPID determines if the policy allows the use of HostPID in the pod spec. | [optional] 
**host_ports** | [**[V1beta1HostPortRange]**](V1beta1HostPortRange.md) | hostPorts determines which host port ranges are allowed to be exposed. | [optional] 
**privileged** | **bool** | privileged determines if a pod can request to be run as privileged. | [optional] 
**read_only_root_filesystem** | **bool** | readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to. | [optional] 
**required_drop_capabilities** | **[str]** | requiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added. | [optional] 
**run_as_group** | [**V1beta1RunAsGroupStrategyOptions**](V1beta1RunAsGroupStrategyOptions.md) |  | [optional] 
**runtime_class** | [**V1beta1RuntimeClassStrategyOptions**](V1beta1RuntimeClassStrategyOptions.md) |  | [optional] 
**volumes** | **[str]** | volumes is an allowlist of volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use &#39;*&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


