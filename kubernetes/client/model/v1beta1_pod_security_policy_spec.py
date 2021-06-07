"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.18
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from kubernetes.client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from kubernetes.client.model.v1beta1_allowed_csi_driver import V1beta1AllowedCSIDriver
    from kubernetes.client.model.v1beta1_allowed_flex_volume import V1beta1AllowedFlexVolume
    from kubernetes.client.model.v1beta1_allowed_host_path import V1beta1AllowedHostPath
    from kubernetes.client.model.v1beta1_fs_group_strategy_options import V1beta1FSGroupStrategyOptions
    from kubernetes.client.model.v1beta1_host_port_range import V1beta1HostPortRange
    from kubernetes.client.model.v1beta1_run_as_group_strategy_options import V1beta1RunAsGroupStrategyOptions
    from kubernetes.client.model.v1beta1_run_as_user_strategy_options import V1beta1RunAsUserStrategyOptions
    from kubernetes.client.model.v1beta1_runtime_class_strategy_options import V1beta1RuntimeClassStrategyOptions
    from kubernetes.client.model.v1beta1_se_linux_strategy_options import V1beta1SELinuxStrategyOptions
    from kubernetes.client.model.v1beta1_supplemental_groups_strategy_options import V1beta1SupplementalGroupsStrategyOptions
    globals()['V1beta1AllowedCSIDriver'] = V1beta1AllowedCSIDriver
    globals()['V1beta1AllowedFlexVolume'] = V1beta1AllowedFlexVolume
    globals()['V1beta1AllowedHostPath'] = V1beta1AllowedHostPath
    globals()['V1beta1FSGroupStrategyOptions'] = V1beta1FSGroupStrategyOptions
    globals()['V1beta1HostPortRange'] = V1beta1HostPortRange
    globals()['V1beta1RunAsGroupStrategyOptions'] = V1beta1RunAsGroupStrategyOptions
    globals()['V1beta1RunAsUserStrategyOptions'] = V1beta1RunAsUserStrategyOptions
    globals()['V1beta1RuntimeClassStrategyOptions'] = V1beta1RuntimeClassStrategyOptions
    globals()['V1beta1SELinuxStrategyOptions'] = V1beta1SELinuxStrategyOptions
    globals()['V1beta1SupplementalGroupsStrategyOptions'] = V1beta1SupplementalGroupsStrategyOptions


class V1beta1PodSecurityPolicySpec(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'fs_group': (V1beta1FSGroupStrategyOptions,),  # noqa: E501
            'run_as_user': (V1beta1RunAsUserStrategyOptions,),  # noqa: E501
            'se_linux': (V1beta1SELinuxStrategyOptions,),  # noqa: E501
            'supplemental_groups': (V1beta1SupplementalGroupsStrategyOptions,),  # noqa: E501
            'allow_privilege_escalation': (bool,),  # noqa: E501
            'allowed_csi_drivers': ([V1beta1AllowedCSIDriver],),  # noqa: E501
            'allowed_capabilities': ([str],),  # noqa: E501
            'allowed_flex_volumes': ([V1beta1AllowedFlexVolume],),  # noqa: E501
            'allowed_host_paths': ([V1beta1AllowedHostPath],),  # noqa: E501
            'allowed_proc_mount_types': ([str],),  # noqa: E501
            'allowed_unsafe_sysctls': ([str],),  # noqa: E501
            'default_add_capabilities': ([str],),  # noqa: E501
            'default_allow_privilege_escalation': (bool,),  # noqa: E501
            'forbidden_sysctls': ([str],),  # noqa: E501
            'host_ipc': (bool,),  # noqa: E501
            'host_network': (bool,),  # noqa: E501
            'host_pid': (bool,),  # noqa: E501
            'host_ports': ([V1beta1HostPortRange],),  # noqa: E501
            'privileged': (bool,),  # noqa: E501
            'read_only_root_filesystem': (bool,),  # noqa: E501
            'required_drop_capabilities': ([str],),  # noqa: E501
            'run_as_group': (V1beta1RunAsGroupStrategyOptions,),  # noqa: E501
            'runtime_class': (V1beta1RuntimeClassStrategyOptions,),  # noqa: E501
            'volumes': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'fs_group': 'fsGroup',  # noqa: E501
        'run_as_user': 'runAsUser',  # noqa: E501
        'se_linux': 'seLinux',  # noqa: E501
        'supplemental_groups': 'supplementalGroups',  # noqa: E501
        'allow_privilege_escalation': 'allowPrivilegeEscalation',  # noqa: E501
        'allowed_csi_drivers': 'allowedCSIDrivers',  # noqa: E501
        'allowed_capabilities': 'allowedCapabilities',  # noqa: E501
        'allowed_flex_volumes': 'allowedFlexVolumes',  # noqa: E501
        'allowed_host_paths': 'allowedHostPaths',  # noqa: E501
        'allowed_proc_mount_types': 'allowedProcMountTypes',  # noqa: E501
        'allowed_unsafe_sysctls': 'allowedUnsafeSysctls',  # noqa: E501
        'default_add_capabilities': 'defaultAddCapabilities',  # noqa: E501
        'default_allow_privilege_escalation': 'defaultAllowPrivilegeEscalation',  # noqa: E501
        'forbidden_sysctls': 'forbiddenSysctls',  # noqa: E501
        'host_ipc': 'hostIPC',  # noqa: E501
        'host_network': 'hostNetwork',  # noqa: E501
        'host_pid': 'hostPID',  # noqa: E501
        'host_ports': 'hostPorts',  # noqa: E501
        'privileged': 'privileged',  # noqa: E501
        'read_only_root_filesystem': 'readOnlyRootFilesystem',  # noqa: E501
        'required_drop_capabilities': 'requiredDropCapabilities',  # noqa: E501
        'run_as_group': 'runAsGroup',  # noqa: E501
        'runtime_class': 'runtimeClass',  # noqa: E501
        'volumes': 'volumes',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, fs_group, run_as_user, se_linux, supplemental_groups, *args, **kwargs):  # noqa: E501
        """V1beta1PodSecurityPolicySpec - a model defined in OpenAPI

        Args:
            fs_group (V1beta1FSGroupStrategyOptions):
            run_as_user (V1beta1RunAsUserStrategyOptions):
            se_linux (V1beta1SELinuxStrategyOptions):
            supplemental_groups (V1beta1SupplementalGroupsStrategyOptions):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            allow_privilege_escalation (bool): allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.. [optional]  # noqa: E501
            allowed_csi_drivers ([V1beta1AllowedCSIDriver]): AllowedCSIDrivers is a whitelist of inline CSI drivers that must be explicitly set to be embedded within a pod spec. An empty value indicates that any CSI driver can be used for inline ephemeral volumes. This is an alpha field, and is only honored if the API server enables the CSIInlineVolume feature gate.. [optional]  # noqa: E501
            allowed_capabilities ([str]): allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities.. [optional]  # noqa: E501
            allowed_flex_volumes ([V1beta1AllowedFlexVolume]): allowedFlexVolumes is a whitelist of allowed Flexvolumes.  Empty or nil indicates that all Flexvolumes may be used.  This parameter is effective only when the usage of the Flexvolumes is allowed in the \"volumes\" field.. [optional]  # noqa: E501
            allowed_host_paths ([V1beta1AllowedHostPath]): allowedHostPaths is a white list of allowed host paths. Empty indicates that all host paths may be used.. [optional]  # noqa: E501
            allowed_proc_mount_types ([str]): AllowedProcMountTypes is a whitelist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled.. [optional]  # noqa: E501
            allowed_unsafe_sysctls ([str]): allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \"*\" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to whitelist all allowed unsafe sysctls explicitly to avoid rejection.  Examples: e.g. \"foo/*\" allows \"foo/bar\", \"foo/baz\", etc. e.g. \"foo.*\" allows \"foo.bar\", \"foo.baz\", etc.. [optional]  # noqa: E501
            default_add_capabilities ([str]): defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list.. [optional]  # noqa: E501
            default_allow_privilege_escalation (bool): defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.. [optional]  # noqa: E501
            forbidden_sysctls ([str]): forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in \"*\" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.  Examples: e.g. \"foo/*\" forbids \"foo/bar\", \"foo/baz\", etc. e.g. \"foo.*\" forbids \"foo.bar\", \"foo.baz\", etc.. [optional]  # noqa: E501
            host_ipc (bool): hostIPC determines if the policy allows the use of HostIPC in the pod spec.. [optional]  # noqa: E501
            host_network (bool): hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.. [optional]  # noqa: E501
            host_pid (bool): hostPID determines if the policy allows the use of HostPID in the pod spec.. [optional]  # noqa: E501
            host_ports ([V1beta1HostPortRange]): hostPorts determines which host port ranges are allowed to be exposed.. [optional]  # noqa: E501
            privileged (bool): privileged determines if a pod can request to be run as privileged.. [optional]  # noqa: E501
            read_only_root_filesystem (bool): readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.. [optional]  # noqa: E501
            required_drop_capabilities ([str]): requiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.. [optional]  # noqa: E501
            run_as_group (V1beta1RunAsGroupStrategyOptions): [optional]  # noqa: E501
            runtime_class (V1beta1RuntimeClassStrategyOptions): [optional]  # noqa: E501
            volumes ([str]): volumes is a white list of allowed volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.fs_group = fs_group
        self.run_as_user = run_as_user
        self.se_linux = se_linux
        self.supplemental_groups = supplemental_groups
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)