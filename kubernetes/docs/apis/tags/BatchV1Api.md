<a name="__pageTop"></a>
# kubernetes.client.apis.tags.batch_v1_api.BatchV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_cron_job**](#create_namespaced_cron_job) | **post** /apis/batch/v1/namespaces/{namespace}/cronjobs | 
[**create_namespaced_job**](#create_namespaced_job) | **post** /apis/batch/v1/namespaces/{namespace}/jobs | 
[**delete_collection_namespaced_cron_job**](#delete_collection_namespaced_cron_job) | **delete** /apis/batch/v1/namespaces/{namespace}/cronjobs | 
[**delete_collection_namespaced_job**](#delete_collection_namespaced_job) | **delete** /apis/batch/v1/namespaces/{namespace}/jobs | 
[**delete_namespaced_cron_job**](#delete_namespaced_cron_job) | **delete** /apis/batch/v1/namespaces/{namespace}/cronjobs/{name} | 
[**delete_namespaced_job**](#delete_namespaced_job) | **delete** /apis/batch/v1/namespaces/{namespace}/jobs/{name} | 
[**get_api_resources**](#get_api_resources) | **get** /apis/batch/v1/ | 
[**list_cron_job_for_all_namespaces**](#list_cron_job_for_all_namespaces) | **get** /apis/batch/v1/cronjobs | 
[**list_job_for_all_namespaces**](#list_job_for_all_namespaces) | **get** /apis/batch/v1/jobs | 
[**list_namespaced_cron_job**](#list_namespaced_cron_job) | **get** /apis/batch/v1/namespaces/{namespace}/cronjobs | 
[**list_namespaced_job**](#list_namespaced_job) | **get** /apis/batch/v1/namespaces/{namespace}/jobs | 
[**patch_namespaced_cron_job**](#patch_namespaced_cron_job) | **patch** /apis/batch/v1/namespaces/{namespace}/cronjobs/{name} | 
[**patch_namespaced_cron_job_status**](#patch_namespaced_cron_job_status) | **patch** /apis/batch/v1/namespaces/{namespace}/cronjobs/{name}/status | 
[**patch_namespaced_job**](#patch_namespaced_job) | **patch** /apis/batch/v1/namespaces/{namespace}/jobs/{name} | 
[**patch_namespaced_job_status**](#patch_namespaced_job_status) | **patch** /apis/batch/v1/namespaces/{namespace}/jobs/{name}/status | 
[**read_namespaced_cron_job**](#read_namespaced_cron_job) | **get** /apis/batch/v1/namespaces/{namespace}/cronjobs/{name} | 
[**read_namespaced_cron_job_status**](#read_namespaced_cron_job_status) | **get** /apis/batch/v1/namespaces/{namespace}/cronjobs/{name}/status | 
[**read_namespaced_job**](#read_namespaced_job) | **get** /apis/batch/v1/namespaces/{namespace}/jobs/{name} | 
[**read_namespaced_job_status**](#read_namespaced_job_status) | **get** /apis/batch/v1/namespaces/{namespace}/jobs/{name}/status | 
[**replace_namespaced_cron_job**](#replace_namespaced_cron_job) | **put** /apis/batch/v1/namespaces/{namespace}/cronjobs/{name} | 
[**replace_namespaced_cron_job_status**](#replace_namespaced_cron_job_status) | **put** /apis/batch/v1/namespaces/{namespace}/cronjobs/{name}/status | 
[**replace_namespaced_job**](#replace_namespaced_job) | **put** /apis/batch/v1/namespaces/{namespace}/jobs/{name} | 
[**replace_namespaced_job_status**](#replace_namespaced_job_status) | **put** /apis/batch/v1/namespaces/{namespace}/jobs/{name}/status | 

# **create_namespaced_cron_job**
<a name="create_namespaced_cron_job"></a>
> V1CronJob create_namespaced_cron_job(namespacebody)



create a CronJob

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_cron_job import V1CronJob
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = V1CronJob(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1CronJobSpec(
            concurrency_policy="concurrency_policy_example",
            failed_jobs_history_limit=1,
            job_template=V1JobTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1JobSpec(
                    active_deadline_seconds=1,
                    backoff_limit=1,
                    completion_mode="completion_mode_example",
                    completions=1,
                    manual_selector=True,
                    parallelism=1,
                    pod_failure_policy=V1PodFailurePolicy(
                        rules=[
                            V1PodFailurePolicyRule(
                                action="action_example",
                                on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                                    container_name="container_name_example",
                                    operator="operator_example",
                                    values=[
                                        1
                                    ],
                                ),
                                on_pod_conditions=[
                                    V1PodFailurePolicyOnPodConditionsPattern(
                                        status="status_example",
                                        type="type_example",
                                    )
                                ],
                            )
                        ],
                    ),
                    selector=V1LabelSelector(
                        match_expressions=[
                            V1LabelSelectorRequirement(
                                key="key_example",
                                operator="operator_example",
                                values=[
                                    "values_example"
                                ],
                            )
                        ],
                        match_labels=dict(
                            "key": "key_example",
                        ),
                    ),
                    suspend=True,
                    template=V1PodTemplateSpec(
                        metadata=V1ObjectMeta(),
                        spec=V1PodSpec(
                            active_deadline_seconds=1,
                            affinity=V1Affinity(
                                node_affinity=V1NodeAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1PreferredSchedulingTerm(
                                            preference=V1NodeSelectorTerm(
                                                match_expressions=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example"
                                                        ],
                                                    )
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement()
                                                ],
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                        node_selector_terms=[
                                            V1NodeSelectorTerm()
                                        ],
                                    ),
                                ),
                                pod_affinity=V1PodAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(),
                                                namespace_selector=V1LabelSelector(),
                                                namespaces=[
                                                    "namespaces_example"
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                                pod_anti_affinity=V1PodAntiAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm()
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                            ),
                            automount_service_account_token=True,
                            containers=[
                                V1Container(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
                                    env=[
                                        V1EnvVar(
                                            name="name_example",
                                            value="value_example",
                                            value_from=V1EnvVarSource(
                                                config_map_key_ref=V1ConfigMapKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                field_ref=V1ObjectFieldSelector(
                                                    api_version="api_version_example",
                                                    field_path="field_path_example",
                                                ),
                                                resource_field_ref=V1ResourceFieldSelector(
                                                    container_name="container_name_example",
                                                    divisor="divisor_example",
                                                    resource="resource_example",
                                                ),
                                                secret_key_ref=V1SecretKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                            ),
                                        )
                                    ],
                                    env_from=[
                                        V1EnvFromSource(
                                            config_map_ref=V1ConfigMapEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                            prefix="prefix_example",
                                            secret_ref=V1SecretEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                        )
                                    ],
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example"
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    )
                                                ],
                                                path="path_example",
                                                port=dict(),
                                                scheme="scheme_example",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port=dict(),
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort(
                                            container_port=1,
                                            host_ip="host_ip_example",
                                            host_port=1,
                                            name="name_example",
                                            protocol="protocol_example",
                                        )
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(
                                        limits=dict(
                                            "key": "key_example",
                                        ),
                                        requests=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example"
                                            ],
                                            drop=[
                                                "drop_example"
                                            ],
                                        ),
                                        privileged=True,
                                        proc_mount="proc_mount_example",
                                        read_only_root_filesystem=True,
                                        run_as_group=1,
                                        run_as_non_root=True,
                                        run_as_user=1,
                                        se_linux_options=V1SELinuxOptions(
                                            level="level_example",
                                            role="role_example",
                                            type="type_example",
                                            user="user_example",
                                        ),
                                        seccomp_profile=V1SeccompProfile(
                                            localhost_profile="localhost_profile_example",
                                            type="type_example",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        )
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        )
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            dns_config=V1PodDNSConfig(
                                nameservers=[
                                    "nameservers_example"
                                ],
                                options=[
                                    V1PodDNSConfigOption(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                searches=[
                                    "searches_example"
                                ],
                            ),
                            dns_policy="dns_policy_example",
                            enable_service_links=True,
                            ephemeral_containers=[
                                V1EphemeralContainer(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
,
,
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(),
                                    liveness_probe=V1Probe(),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort()
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(),
                                    security_context=V1SecurityContext(),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    target_container_name="target_container_name_example",
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
,
                                    volume_mounts=[
                                        V1VolumeMount()
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            host_aliases=[
                                V1HostAlias(
                                    hostnames=[
                                        "hostnames_example"
                                    ],
                                    ip="ip_example",
                                )
                            ],
                            host_ipc=True,
                            host_network=True,
                            host_pid=True,
                            host_users=True,
                            hostname="hostname_example",
                            image_pull_secrets=[
                                V1LocalObjectReference(
                                    name="name_example",
                                )
                            ],
                            init_containers=[
                                V1Container()
                            ],
                            node_name="node_name_example",
                            node_selector=dict(
                                "key": "key_example",
                            ),
                            os=V1PodOS(
                                name="name_example",
                            ),
                            overhead=dict(
                                "key": "key_example",
                            ),
                            preemption_policy="preemption_policy_example",
                            priority=1,
                            priority_class_name="priority_class_name_example",
                            readiness_gates=[
                                V1PodReadinessGate(
                                    condition_type="condition_type_example",
                                )
                            ],
                            restart_policy="restart_policy_example",
                            runtime_class_name="runtime_class_name_example",
                            scheduler_name="scheduler_name_example",
                            security_context=V1PodSecurityContext(
                                fs_group=1,
                                fs_group_change_policy="fs_group_change_policy_example",
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(),
                                seccomp_profile=V1SeccompProfile(),
                                supplemental_groups=[
                                    1
                                ],
                                sysctls=[
                                    V1Sysctl(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                windows_options=V1WindowsSecurityContextOptions(),
                            ),
                            service_account="service_account_example",
                            service_account_name="service_account_name_example",
                            set_hostname_as_fqdn=True,
                            share_process_namespace=True,
                            subdomain="subdomain_example",
                            termination_grace_period_seconds=1,
                            tolerations=[
                                V1Toleration(
                                    effect="effect_example",
                                    key="key_example",
                                    operator="operator_example",
                                    toleration_seconds=1,
                                    value="value_example",
                                )
                            ],
                            topology_spread_constraints=[
                                V1TopologySpreadConstraint(
                                    label_selector=V1LabelSelector(),
                                    match_label_keys=[
                                        "match_label_keys_example"
                                    ],
                                    max_skew=1,
                                    min_domains=1,
                                    node_affinity_policy="node_affinity_policy_example",
                                    node_taints_policy="node_taints_policy_example",
                                    topology_key="topology_key_example",
                                    when_unsatisfiable="when_unsatisfiable_example",
                                )
                            ],
                            volumes=[
                                V1Volume(
                                    aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    azure_disk=V1AzureDiskVolumeSource(
                                        caching_mode="caching_mode_example",
                                        disk_name="disk_name_example",
                                        disk_uri="disk_uri_example",
                                        fs_type="fs_type_example",
                                        kind="kind_example",
                                        read_only=True,
                                    ),
                                    azure_file=V1AzureFileVolumeSource(
                                        read_only=True,
                                        secret_name="secret_name_example",
                                        share_name="share_name_example",
                                    ),
                                    cephfs=V1CephFSVolumeSource(
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        path="path_example",
                                        read_only=True,
                                        secret_file="secret_file_example",
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    cinder=V1CinderVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_id="volume_id_example",
                                    ),
                                    config_map=V1ConfigMapVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            )
                                        ],
                                        name="name_example",
                                        optional=True,
                                    ),
                                    csi=V1CSIVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        node_publish_secret_ref=V1LocalObjectReference(),
                                        read_only=True,
                                        volume_attributes=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    downward_api=V1DownwardAPIVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1DownwardAPIVolumeFile(
                                                field_ref=V1ObjectFieldSelector(),
                                                mode=1,
                                                path="path_example",
                                                resource_field_ref=V1ResourceFieldSelector(),
                                            )
                                        ],
                                    ),
                                    empty_dir=V1EmptyDirVolumeSource(
                                        medium="medium_example",
                                        size_limit="size_limit_example",
                                    ),
                                    ephemeral=V1EphemeralVolumeSource(
                                        volume_claim_template=V1PersistentVolumeClaimTemplate(
                                            metadata=V1ObjectMeta(),
                                            spec=V1PersistentVolumeClaimSpec(
                                                access_modes=[
                                                    "access_modes_example"
                                                ],
                                                data_source=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
,
                                                resources=V1ResourceRequirements(),
                                                selector=V1LabelSelector(),
                                                storage_class_name="storage_class_name_example",
                                                volume_mode="volume_mode_example",
                                                volume_name="volume_name_example",
                                            ),
                                        ),
                                    ),
                                    fc=V1FCVolumeSource(
                                        fs_type="fs_type_example",
                                        lun=1,
                                        read_only=True,
                                        target_wwns=[
                                            "target_wwns_example"
                                        ],
                                        wwids=[
                                            "wwids_example"
                                        ],
                                    ),
                                    flex_volume=V1FlexVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        options=dict(
                                            "key": "key_example",
                                        ),
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                    ),
                                    flocker=V1FlockerVolumeSource(
                                        dataset_name="dataset_name_example",
                                        dataset_uuid="dataset_uuid_example",
                                    ),
                                    gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        pd_name="pd_name_example",
                                        read_only=True,
                                    ),
                                    git_repo=V1GitRepoVolumeSource(
                                        directory="directory_example",
                                        repository="repository_example",
                                        revision="revision_example",
                                    ),
                                    glusterfs=V1GlusterfsVolumeSource(
                                        endpoints="endpoints_example",
                                        path="path_example",
                                        read_only=True,
                                    ),
                                    host_path=V1HostPathVolumeSource(
                                        path="path_example",
                                        type="type_example",
                                    ),
                                    iscsi=V1ISCSIVolumeSource(
                                        chap_auth_discovery=True,
                                        chap_auth_session=True,
                                        fs_type="fs_type_example",
                                        initiator_name="initiator_name_example",
                                        iqn="iqn_example",
                                        iscsi_interface="iscsi_interface_example",
                                        lun=1,
                                        portals=[
                                            "portals_example"
                                        ],
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        target_portal="target_portal_example",
                                    ),
                                    name="name_example",
                                    nfs=V1NFSVolumeSource(
                                        path="path_example",
                                        read_only=True,
                                        server="server_example",
                                    ),
                                    persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                        claim_name="claim_name_example",
                                        read_only=True,
                                    ),
                                    photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        pd_id="pd_id_example",
                                    ),
                                    portworx_volume=V1PortworxVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    projected=V1ProjectedVolumeSource(
                                        default_mode=1,
                                        sources=[
                                            V1VolumeProjection(
                                                config_map=V1ConfigMapProjection(
,
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                downward_api=V1DownwardAPIProjection(
                                                    items=[
                                                        V1DownwardAPIVolumeFile()
                                                    ],
                                                ),
                                                secret=V1SecretProjection(
                                                    items=[
                                                        V1KeyToPath()
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                service_account_token=V1ServiceAccountTokenProjection(
                                                    audience="audience_example",
                                                    expiration_seconds=1,
                                                    path="path_example",
                                                ),
                                            )
                                        ],
                                    ),
                                    quobyte=V1QuobyteVolumeSource(
                                        group="group_example",
                                        read_only=True,
                                        registry="registry_example",
                                        tenant="tenant_example",
                                        user="user_example",
                                        volume="volume_example",
                                    ),
                                    rbd=V1RBDVolumeSource(
                                        fs_type="fs_type_example",
                                        image="image_example",
                                        keyring="keyring_example",
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        pool="pool_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    scale_io=V1ScaleIOVolumeSource(
                                        fs_type="fs_type_example",
                                        gateway="gateway_example",
                                        protection_domain="protection_domain_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        ssl_enabled=True,
                                        storage_mode="storage_mode_example",
                                        storage_pool="storage_pool_example",
                                        system="system_example",
                                        volume_name="volume_name_example",
                                    ),
                                    secret=V1SecretVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath()
                                        ],
                                        optional=True,
                                        secret_name="secret_name_example",
                                    ),
                                    storageos=V1StorageOSVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_name="volume_name_example",
                                        volume_namespace="volume_namespace_example",
                                    ),
                                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        storage_policy_id="storage_policy_id_example",
                                        storage_policy_name="storage_policy_name_example",
                                        volume_path="volume_path_example",
                                    ),
                                )
                            ],
                        ),
                    ),
                    ttl_seconds_after_finished=1,
                ),
            ),
            schedule="schedule_example",
            starting_deadline_seconds=1,
            successful_jobs_history_limit=1,
            suspend=True,
            time_zone="time_zone_example",
        ),
        status=V1CronJobStatus(
            active=[
                V1ObjectReference(
                    api_version="api_version_example",
                    field_path="field_path_example",
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    resource_version="resource_version_example",
                    uid="uid_example",
                )
            ],
            last_schedule_time="1970-01-01T00:00:00.00Z",
            last_successful_time="1970-01-01T00:00:00.00Z",
        ),
    )
    try:
        api_response = api_instance.create_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->create_namespaced_cron_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1CronJob(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1CronJobSpec(
            concurrency_policy="concurrency_policy_example",
            failed_jobs_history_limit=1,
            job_template=V1JobTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1JobSpec(
                    active_deadline_seconds=1,
                    backoff_limit=1,
                    completion_mode="completion_mode_example",
                    completions=1,
                    manual_selector=True,
                    parallelism=1,
                    pod_failure_policy=V1PodFailurePolicy(
                        rules=[
                            V1PodFailurePolicyRule(
                                action="action_example",
                                on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                                    container_name="container_name_example",
                                    operator="operator_example",
                                    values=[
                                        1
                                    ],
                                ),
                                on_pod_conditions=[
                                    V1PodFailurePolicyOnPodConditionsPattern(
                                        status="status_example",
                                        type="type_example",
                                    )
                                ],
                            )
                        ],
                    ),
                    selector=V1LabelSelector(
                        match_expressions=[
                            V1LabelSelectorRequirement(
                                key="key_example",
                                operator="operator_example",
                                values=[
                                    "values_example"
                                ],
                            )
                        ],
                        match_labels=dict(
                            "key": "key_example",
                        ),
                    ),
                    suspend=True,
                    template=V1PodTemplateSpec(
                        metadata=V1ObjectMeta(),
                        spec=V1PodSpec(
                            active_deadline_seconds=1,
                            affinity=V1Affinity(
                                node_affinity=V1NodeAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1PreferredSchedulingTerm(
                                            preference=V1NodeSelectorTerm(
                                                match_expressions=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example"
                                                        ],
                                                    )
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement()
                                                ],
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                        node_selector_terms=[
                                            V1NodeSelectorTerm()
                                        ],
                                    ),
                                ),
                                pod_affinity=V1PodAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(),
                                                namespace_selector=V1LabelSelector(),
                                                namespaces=[
                                                    "namespaces_example"
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                                pod_anti_affinity=V1PodAntiAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm()
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                            ),
                            automount_service_account_token=True,
                            containers=[
                                V1Container(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
                                    env=[
                                        V1EnvVar(
                                            name="name_example",
                                            value="value_example",
                                            value_from=V1EnvVarSource(
                                                config_map_key_ref=V1ConfigMapKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                field_ref=V1ObjectFieldSelector(
                                                    api_version="api_version_example",
                                                    field_path="field_path_example",
                                                ),
                                                resource_field_ref=V1ResourceFieldSelector(
                                                    container_name="container_name_example",
                                                    divisor="divisor_example",
                                                    resource="resource_example",
                                                ),
                                                secret_key_ref=V1SecretKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                            ),
                                        )
                                    ],
                                    env_from=[
                                        V1EnvFromSource(
                                            config_map_ref=V1ConfigMapEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                            prefix="prefix_example",
                                            secret_ref=V1SecretEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                        )
                                    ],
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example"
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    )
                                                ],
                                                path="path_example",
                                                port=dict(),
                                                scheme="scheme_example",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port=dict(),
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort(
                                            container_port=1,
                                            host_ip="host_ip_example",
                                            host_port=1,
                                            name="name_example",
                                            protocol="protocol_example",
                                        )
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(
                                        limits=dict(
                                            "key": "key_example",
                                        ),
                                        requests=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example"
                                            ],
                                            drop=[
                                                "drop_example"
                                            ],
                                        ),
                                        privileged=True,
                                        proc_mount="proc_mount_example",
                                        read_only_root_filesystem=True,
                                        run_as_group=1,
                                        run_as_non_root=True,
                                        run_as_user=1,
                                        se_linux_options=V1SELinuxOptions(
                                            level="level_example",
                                            role="role_example",
                                            type="type_example",
                                            user="user_example",
                                        ),
                                        seccomp_profile=V1SeccompProfile(
                                            localhost_profile="localhost_profile_example",
                                            type="type_example",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        )
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        )
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            dns_config=V1PodDNSConfig(
                                nameservers=[
                                    "nameservers_example"
                                ],
                                options=[
                                    V1PodDNSConfigOption(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                searches=[
                                    "searches_example"
                                ],
                            ),
                            dns_policy="dns_policy_example",
                            enable_service_links=True,
                            ephemeral_containers=[
                                V1EphemeralContainer(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
,
,
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(),
                                    liveness_probe=V1Probe(),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort()
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(),
                                    security_context=V1SecurityContext(),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    target_container_name="target_container_name_example",
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
,
                                    volume_mounts=[
                                        V1VolumeMount()
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            host_aliases=[
                                V1HostAlias(
                                    hostnames=[
                                        "hostnames_example"
                                    ],
                                    ip="ip_example",
                                )
                            ],
                            host_ipc=True,
                            host_network=True,
                            host_pid=True,
                            host_users=True,
                            hostname="hostname_example",
                            image_pull_secrets=[
                                V1LocalObjectReference(
                                    name="name_example",
                                )
                            ],
                            init_containers=[
                                V1Container()
                            ],
                            node_name="node_name_example",
                            node_selector=dict(
                                "key": "key_example",
                            ),
                            os=V1PodOS(
                                name="name_example",
                            ),
                            overhead=dict(
                                "key": "key_example",
                            ),
                            preemption_policy="preemption_policy_example",
                            priority=1,
                            priority_class_name="priority_class_name_example",
                            readiness_gates=[
                                V1PodReadinessGate(
                                    condition_type="condition_type_example",
                                )
                            ],
                            restart_policy="restart_policy_example",
                            runtime_class_name="runtime_class_name_example",
                            scheduler_name="scheduler_name_example",
                            security_context=V1PodSecurityContext(
                                fs_group=1,
                                fs_group_change_policy="fs_group_change_policy_example",
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(),
                                seccomp_profile=V1SeccompProfile(),
                                supplemental_groups=[
                                    1
                                ],
                                sysctls=[
                                    V1Sysctl(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                windows_options=V1WindowsSecurityContextOptions(),
                            ),
                            service_account="service_account_example",
                            service_account_name="service_account_name_example",
                            set_hostname_as_fqdn=True,
                            share_process_namespace=True,
                            subdomain="subdomain_example",
                            termination_grace_period_seconds=1,
                            tolerations=[
                                V1Toleration(
                                    effect="effect_example",
                                    key="key_example",
                                    operator="operator_example",
                                    toleration_seconds=1,
                                    value="value_example",
                                )
                            ],
                            topology_spread_constraints=[
                                V1TopologySpreadConstraint(
                                    label_selector=V1LabelSelector(),
                                    match_label_keys=[
                                        "match_label_keys_example"
                                    ],
                                    max_skew=1,
                                    min_domains=1,
                                    node_affinity_policy="node_affinity_policy_example",
                                    node_taints_policy="node_taints_policy_example",
                                    topology_key="topology_key_example",
                                    when_unsatisfiable="when_unsatisfiable_example",
                                )
                            ],
                            volumes=[
                                V1Volume(
                                    aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    azure_disk=V1AzureDiskVolumeSource(
                                        caching_mode="caching_mode_example",
                                        disk_name="disk_name_example",
                                        disk_uri="disk_uri_example",
                                        fs_type="fs_type_example",
                                        kind="kind_example",
                                        read_only=True,
                                    ),
                                    azure_file=V1AzureFileVolumeSource(
                                        read_only=True,
                                        secret_name="secret_name_example",
                                        share_name="share_name_example",
                                    ),
                                    cephfs=V1CephFSVolumeSource(
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        path="path_example",
                                        read_only=True,
                                        secret_file="secret_file_example",
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    cinder=V1CinderVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_id="volume_id_example",
                                    ),
                                    config_map=V1ConfigMapVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            )
                                        ],
                                        name="name_example",
                                        optional=True,
                                    ),
                                    csi=V1CSIVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        node_publish_secret_ref=V1LocalObjectReference(),
                                        read_only=True,
                                        volume_attributes=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    downward_api=V1DownwardAPIVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1DownwardAPIVolumeFile(
                                                field_ref=V1ObjectFieldSelector(),
                                                mode=1,
                                                path="path_example",
                                                resource_field_ref=V1ResourceFieldSelector(),
                                            )
                                        ],
                                    ),
                                    empty_dir=V1EmptyDirVolumeSource(
                                        medium="medium_example",
                                        size_limit="size_limit_example",
                                    ),
                                    ephemeral=V1EphemeralVolumeSource(
                                        volume_claim_template=V1PersistentVolumeClaimTemplate(
                                            metadata=V1ObjectMeta(),
                                            spec=V1PersistentVolumeClaimSpec(
                                                access_modes=[
                                                    "access_modes_example"
                                                ],
                                                data_source=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
,
                                                resources=V1ResourceRequirements(),
                                                selector=V1LabelSelector(),
                                                storage_class_name="storage_class_name_example",
                                                volume_mode="volume_mode_example",
                                                volume_name="volume_name_example",
                                            ),
                                        ),
                                    ),
                                    fc=V1FCVolumeSource(
                                        fs_type="fs_type_example",
                                        lun=1,
                                        read_only=True,
                                        target_wwns=[
                                            "target_wwns_example"
                                        ],
                                        wwids=[
                                            "wwids_example"
                                        ],
                                    ),
                                    flex_volume=V1FlexVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        options=dict(
                                            "key": "key_example",
                                        ),
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                    ),
                                    flocker=V1FlockerVolumeSource(
                                        dataset_name="dataset_name_example",
                                        dataset_uuid="dataset_uuid_example",
                                    ),
                                    gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        pd_name="pd_name_example",
                                        read_only=True,
                                    ),
                                    git_repo=V1GitRepoVolumeSource(
                                        directory="directory_example",
                                        repository="repository_example",
                                        revision="revision_example",
                                    ),
                                    glusterfs=V1GlusterfsVolumeSource(
                                        endpoints="endpoints_example",
                                        path="path_example",
                                        read_only=True,
                                    ),
                                    host_path=V1HostPathVolumeSource(
                                        path="path_example",
                                        type="type_example",
                                    ),
                                    iscsi=V1ISCSIVolumeSource(
                                        chap_auth_discovery=True,
                                        chap_auth_session=True,
                                        fs_type="fs_type_example",
                                        initiator_name="initiator_name_example",
                                        iqn="iqn_example",
                                        iscsi_interface="iscsi_interface_example",
                                        lun=1,
                                        portals=[
                                            "portals_example"
                                        ],
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        target_portal="target_portal_example",
                                    ),
                                    name="name_example",
                                    nfs=V1NFSVolumeSource(
                                        path="path_example",
                                        read_only=True,
                                        server="server_example",
                                    ),
                                    persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                        claim_name="claim_name_example",
                                        read_only=True,
                                    ),
                                    photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        pd_id="pd_id_example",
                                    ),
                                    portworx_volume=V1PortworxVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    projected=V1ProjectedVolumeSource(
                                        default_mode=1,
                                        sources=[
                                            V1VolumeProjection(
                                                config_map=V1ConfigMapProjection(
,
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                downward_api=V1DownwardAPIProjection(
                                                    items=[
                                                        V1DownwardAPIVolumeFile()
                                                    ],
                                                ),
                                                secret=V1SecretProjection(
                                                    items=[
                                                        V1KeyToPath()
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                service_account_token=V1ServiceAccountTokenProjection(
                                                    audience="audience_example",
                                                    expiration_seconds=1,
                                                    path="path_example",
                                                ),
                                            )
                                        ],
                                    ),
                                    quobyte=V1QuobyteVolumeSource(
                                        group="group_example",
                                        read_only=True,
                                        registry="registry_example",
                                        tenant="tenant_example",
                                        user="user_example",
                                        volume="volume_example",
                                    ),
                                    rbd=V1RBDVolumeSource(
                                        fs_type="fs_type_example",
                                        image="image_example",
                                        keyring="keyring_example",
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        pool="pool_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    scale_io=V1ScaleIOVolumeSource(
                                        fs_type="fs_type_example",
                                        gateway="gateway_example",
                                        protection_domain="protection_domain_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        ssl_enabled=True,
                                        storage_mode="storage_mode_example",
                                        storage_pool="storage_pool_example",
                                        system="system_example",
                                        volume_name="volume_name_example",
                                    ),
                                    secret=V1SecretVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath()
                                        ],
                                        optional=True,
                                        secret_name="secret_name_example",
                                    ),
                                    storageos=V1StorageOSVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_name="volume_name_example",
                                        volume_namespace="volume_namespace_example",
                                    ),
                                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        storage_policy_id="storage_policy_id_example",
                                        storage_policy_name="storage_policy_name_example",
                                        volume_path="volume_path_example",
                                    ),
                                )
                            ],
                        ),
                    ),
                    ttl_seconds_after_finished=1,
                ),
            ),
            schedule="schedule_example",
            starting_deadline_seconds=1,
            successful_jobs_history_limit=1,
            suspend=True,
            time_zone="time_zone_example",
        ),
        status=V1CronJobStatus(
            active=[
                V1ObjectReference(
                    api_version="api_version_example",
                    field_path="field_path_example",
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    resource_version="resource_version_example",
                    uid="uid_example",
                )
            ],
            last_schedule_time="1970-01-01T00:00:00.00Z",
            last_successful_time="1970-01-01T00:00:00.00Z",
        ),
    )
    try:
        api_response = api_instance.create_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->create_namespaced_cron_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_namespaced_cron_job.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_namespaced_cron_job.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_namespaced_cron_job.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_namespaced_cron_job.ApiResponseFor401) | Unauthorized

#### create_namespaced_cron_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### create_namespaced_cron_job.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### create_namespaced_cron_job.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### create_namespaced_cron_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_namespaced_job**
<a name="create_namespaced_job"></a>
> V1Job create_namespaced_job(namespacebody)



create a Job

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_job import V1Job
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = V1Job(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1JobSpec(
            active_deadline_seconds=1,
            backoff_limit=1,
            completion_mode="completion_mode_example",
            completions=1,
            manual_selector=True,
            parallelism=1,
            pod_failure_policy=V1PodFailurePolicy(
                rules=[
                    V1PodFailurePolicyRule(
                        action="action_example",
                        on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                            container_name="container_name_example",
                            operator="operator_example",
                            values=[
                                1
                            ],
                        ),
                        on_pod_conditions=[
                            V1PodFailurePolicyOnPodConditionsPattern(
                                status="status_example",
                                type="type_example",
                            )
                        ],
                    )
                ],
            ),
            selector=V1LabelSelector(
                match_expressions=[
                    V1LabelSelectorRequirement(
                        key="key_example",
                        operator="operator_example",
                        values=[
                            "values_example"
                        ],
                    )
                ],
                match_labels=dict(
                    "key": "key_example",
                ),
            ),
            suspend=True,
            template=V1PodTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1PodSpec(
                    active_deadline_seconds=1,
                    affinity=V1Affinity(
                        node_affinity=V1NodeAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1PreferredSchedulingTerm(
                                    preference=V1NodeSelectorTerm(
                                        match_expressions=[
                                            V1NodeSelectorRequirement(
                                                key="key_example",
                                                operator="operator_example",
                                                values=[
                                                    "values_example"
                                                ],
                                            )
                                        ],
                                        match_fields=[
                                            V1NodeSelectorRequirement()
                                        ],
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                node_selector_terms=[
                                    V1NodeSelectorTerm()
                                ],
                            ),
                        ),
                        pod_affinity=V1PodAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm(
                                    pod_affinity_term=V1PodAffinityTerm(
                                        label_selector=V1LabelSelector(),
                                        namespace_selector=V1LabelSelector(),
                                        namespaces=[
                                            "namespaces_example"
                                        ],
                                        topology_key="topology_key_example",
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                        pod_anti_affinity=V1PodAntiAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm()
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                    ),
                    automount_service_account_token=True,
                    containers=[
                        V1Container(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
                            env=[
                                V1EnvVar(
                                    name="name_example",
                                    value="value_example",
                                    value_from=V1EnvVarSource(
                                        config_map_key_ref=V1ConfigMapKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                        field_ref=V1ObjectFieldSelector(
                                            api_version="api_version_example",
                                            field_path="field_path_example",
                                        ),
                                        resource_field_ref=V1ResourceFieldSelector(
                                            container_name="container_name_example",
                                            divisor="divisor_example",
                                            resource="resource_example",
                                        ),
                                        secret_key_ref=V1SecretKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                    ),
                                )
                            ],
                            env_from=[
                                V1EnvFromSource(
                                    config_map_ref=V1ConfigMapEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                    prefix="prefix_example",
                                    secret_ref=V1SecretEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                )
                            ],
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(
                                post_start=V1LifecycleHandler(
                                    _exec=V1ExecAction(
                                        command=[
                                            "command_example"
                                        ],
                                    ),
                                    http_get=V1HTTPGetAction(
                                        host="host_example",
                                        http_headers=[
                                            V1HTTPHeader(
                                                name="name_example",
                                                value="value_example",
                                            )
                                        ],
                                        path="path_example",
                                        port=dict(),
                                        scheme="scheme_example",
                                    ),
                                    tcp_socket=V1TCPSocketAction(
                                        host="host_example",
                                        port=dict(),
                                    ),
                                ),
                                pre_stop=V1LifecycleHandler(),
                            ),
                            liveness_probe=V1Probe(
                                _exec=V1ExecAction(),
                                failure_threshold=1,
                                grpc=V1GRPCAction(
                                    port=1,
                                    service="service_example",
                                ),
                                http_get=V1HTTPGetAction(),
                                initial_delay_seconds=1,
                                period_seconds=1,
                                success_threshold=1,
                                tcp_socket=V1TCPSocketAction(),
                                termination_grace_period_seconds=1,
                                timeout_seconds=1,
                            ),
                            name="name_example",
                            ports=[
                                V1ContainerPort(
                                    container_port=1,
                                    host_ip="host_ip_example",
                                    host_port=1,
                                    name="name_example",
                                    protocol="protocol_example",
                                )
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(
                                limits=dict(
                                    "key": "key_example",
                                ),
                                requests=dict(
                                    "key": "key_example",
                                ),
                            ),
                            security_context=V1SecurityContext(
                                allow_privilege_escalation=True,
                                capabilities=V1Capabilities(
                                    add=[
                                        "add_example"
                                    ],
                                    drop=[
                                        "drop_example"
                                    ],
                                ),
                                privileged=True,
                                proc_mount="proc_mount_example",
                                read_only_root_filesystem=True,
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(
                                    level="level_example",
                                    role="role_example",
                                    type="type_example",
                                    user="user_example",
                                ),
                                seccomp_profile=V1SeccompProfile(
                                    localhost_profile="localhost_profile_example",
                                    type="type_example",
                                ),
                                windows_options=V1WindowsSecurityContextOptions(
                                    gmsa_credential_spec="gmsa_credential_spec_example",
                                    gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                    host_process=True,
                                    run_as_user_name="run_as_user_name_example",
                                ),
                            ),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
                            volume_devices=[
                                V1VolumeDevice(
                                    device_path="device_path_example",
                                    name="name_example",
                                )
                            ],
                            volume_mounts=[
                                V1VolumeMount(
                                    mount_path="mount_path_example",
                                    mount_propagation="mount_propagation_example",
                                    name="name_example",
                                    read_only=True,
                                    sub_path="sub_path_example",
                                    sub_path_expr="sub_path_expr_example",
                                )
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    dns_config=V1PodDNSConfig(
                        nameservers=[
                            "nameservers_example"
                        ],
                        options=[
                            V1PodDNSConfigOption(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        searches=[
                            "searches_example"
                        ],
                    ),
                    dns_policy="dns_policy_example",
                    enable_service_links=True,
                    ephemeral_containers=[
                        V1EphemeralContainer(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
,
,
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(),
                            liveness_probe=V1Probe(),
                            name="name_example",
                            ports=[
                                V1ContainerPort()
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(),
                            security_context=V1SecurityContext(),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            target_container_name="target_container_name_example",
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
,
                            volume_mounts=[
                                V1VolumeMount()
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    host_aliases=[
                        V1HostAlias(
                            hostnames=[
                                "hostnames_example"
                            ],
                            ip="ip_example",
                        )
                    ],
                    host_ipc=True,
                    host_network=True,
                    host_pid=True,
                    host_users=True,
                    hostname="hostname_example",
                    image_pull_secrets=[
                        V1LocalObjectReference(
                            name="name_example",
                        )
                    ],
                    init_containers=[
                        V1Container()
                    ],
                    node_name="node_name_example",
                    node_selector=dict(
                        "key": "key_example",
                    ),
                    os=V1PodOS(
                        name="name_example",
                    ),
                    overhead=dict(
                        "key": "key_example",
                    ),
                    preemption_policy="preemption_policy_example",
                    priority=1,
                    priority_class_name="priority_class_name_example",
                    readiness_gates=[
                        V1PodReadinessGate(
                            condition_type="condition_type_example",
                        )
                    ],
                    restart_policy="restart_policy_example",
                    runtime_class_name="runtime_class_name_example",
                    scheduler_name="scheduler_name_example",
                    security_context=V1PodSecurityContext(
                        fs_group=1,
                        fs_group_change_policy="fs_group_change_policy_example",
                        run_as_group=1,
                        run_as_non_root=True,
                        run_as_user=1,
                        se_linux_options=V1SELinuxOptions(),
                        seccomp_profile=V1SeccompProfile(),
                        supplemental_groups=[
                            1
                        ],
                        sysctls=[
                            V1Sysctl(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        windows_options=V1WindowsSecurityContextOptions(),
                    ),
                    service_account="service_account_example",
                    service_account_name="service_account_name_example",
                    set_hostname_as_fqdn=True,
                    share_process_namespace=True,
                    subdomain="subdomain_example",
                    termination_grace_period_seconds=1,
                    tolerations=[
                        V1Toleration(
                            effect="effect_example",
                            key="key_example",
                            operator="operator_example",
                            toleration_seconds=1,
                            value="value_example",
                        )
                    ],
                    topology_spread_constraints=[
                        V1TopologySpreadConstraint(
                            label_selector=V1LabelSelector(),
                            match_label_keys=[
                                "match_label_keys_example"
                            ],
                            max_skew=1,
                            min_domains=1,
                            node_affinity_policy="node_affinity_policy_example",
                            node_taints_policy="node_taints_policy_example",
                            topology_key="topology_key_example",
                            when_unsatisfiable="when_unsatisfiable_example",
                        )
                    ],
                    volumes=[
                        V1Volume(
                            aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            azure_disk=V1AzureDiskVolumeSource(
                                caching_mode="caching_mode_example",
                                disk_name="disk_name_example",
                                disk_uri="disk_uri_example",
                                fs_type="fs_type_example",
                                kind="kind_example",
                                read_only=True,
                            ),
                            azure_file=V1AzureFileVolumeSource(
                                read_only=True,
                                secret_name="secret_name_example",
                                share_name="share_name_example",
                            ),
                            cephfs=V1CephFSVolumeSource(
                                monitors=[
                                    "monitors_example"
                                ],
                                path="path_example",
                                read_only=True,
                                secret_file="secret_file_example",
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            cinder=V1CinderVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_id="volume_id_example",
                            ),
                            config_map=V1ConfigMapVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath(
                                        key="key_example",
                                        mode=1,
                                        path="path_example",
                                    )
                                ],
                                name="name_example",
                                optional=True,
                            ),
                            csi=V1CSIVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                node_publish_secret_ref=V1LocalObjectReference(),
                                read_only=True,
                                volume_attributes=dict(
                                    "key": "key_example",
                                ),
                            ),
                            downward_api=V1DownwardAPIVolumeSource(
                                default_mode=1,
                                items=[
                                    V1DownwardAPIVolumeFile(
                                        field_ref=V1ObjectFieldSelector(),
                                        mode=1,
                                        path="path_example",
                                        resource_field_ref=V1ResourceFieldSelector(),
                                    )
                                ],
                            ),
                            empty_dir=V1EmptyDirVolumeSource(
                                medium="medium_example",
                                size_limit="size_limit_example",
                            ),
                            ephemeral=V1EphemeralVolumeSource(
                                volume_claim_template=V1PersistentVolumeClaimTemplate(
                                    metadata=V1ObjectMeta(),
                                    spec=V1PersistentVolumeClaimSpec(
                                        access_modes=[
                                            "access_modes_example"
                                        ],
                                        data_source=V1TypedLocalObjectReference(
                                            api_group="api_group_example",
                                            kind="kind_example",
                                            name="name_example",
                                        ),
,
                                        resources=V1ResourceRequirements(),
                                        selector=V1LabelSelector(),
                                        storage_class_name="storage_class_name_example",
                                        volume_mode="volume_mode_example",
                                        volume_name="volume_name_example",
                                    ),
                                ),
                            ),
                            fc=V1FCVolumeSource(
                                fs_type="fs_type_example",
                                lun=1,
                                read_only=True,
                                target_wwns=[
                                    "target_wwns_example"
                                ],
                                wwids=[
                                    "wwids_example"
                                ],
                            ),
                            flex_volume=V1FlexVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                options=dict(
                                    "key": "key_example",
                                ),
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                            ),
                            flocker=V1FlockerVolumeSource(
                                dataset_name="dataset_name_example",
                                dataset_uuid="dataset_uuid_example",
                            ),
                            gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                pd_name="pd_name_example",
                                read_only=True,
                            ),
                            git_repo=V1GitRepoVolumeSource(
                                directory="directory_example",
                                repository="repository_example",
                                revision="revision_example",
                            ),
                            glusterfs=V1GlusterfsVolumeSource(
                                endpoints="endpoints_example",
                                path="path_example",
                                read_only=True,
                            ),
                            host_path=V1HostPathVolumeSource(
                                path="path_example",
                                type="type_example",
                            ),
                            iscsi=V1ISCSIVolumeSource(
                                chap_auth_discovery=True,
                                chap_auth_session=True,
                                fs_type="fs_type_example",
                                initiator_name="initiator_name_example",
                                iqn="iqn_example",
                                iscsi_interface="iscsi_interface_example",
                                lun=1,
                                portals=[
                                    "portals_example"
                                ],
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                target_portal="target_portal_example",
                            ),
                            name="name_example",
                            nfs=V1NFSVolumeSource(
                                path="path_example",
                                read_only=True,
                                server="server_example",
                            ),
                            persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                claim_name="claim_name_example",
                                read_only=True,
                            ),
                            photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                pd_id="pd_id_example",
                            ),
                            portworx_volume=V1PortworxVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            projected=V1ProjectedVolumeSource(
                                default_mode=1,
                                sources=[
                                    V1VolumeProjection(
                                        config_map=V1ConfigMapProjection(
,
                                            name="name_example",
                                            optional=True,
                                        ),
                                        downward_api=V1DownwardAPIProjection(
                                            items=[
                                                V1DownwardAPIVolumeFile()
                                            ],
                                        ),
                                        secret=V1SecretProjection(
                                            items=[
                                                V1KeyToPath()
                                            ],
                                            name="name_example",
                                            optional=True,
                                        ),
                                        service_account_token=V1ServiceAccountTokenProjection(
                                            audience="audience_example",
                                            expiration_seconds=1,
                                            path="path_example",
                                        ),
                                    )
                                ],
                            ),
                            quobyte=V1QuobyteVolumeSource(
                                group="group_example",
                                read_only=True,
                                registry="registry_example",
                                tenant="tenant_example",
                                user="user_example",
                                volume="volume_example",
                            ),
                            rbd=V1RBDVolumeSource(
                                fs_type="fs_type_example",
                                image="image_example",
                                keyring="keyring_example",
                                monitors=[
                                    "monitors_example"
                                ],
                                pool="pool_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            scale_io=V1ScaleIOVolumeSource(
                                fs_type="fs_type_example",
                                gateway="gateway_example",
                                protection_domain="protection_domain_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                ssl_enabled=True,
                                storage_mode="storage_mode_example",
                                storage_pool="storage_pool_example",
                                system="system_example",
                                volume_name="volume_name_example",
                            ),
                            secret=V1SecretVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath()
                                ],
                                optional=True,
                                secret_name="secret_name_example",
                            ),
                            storageos=V1StorageOSVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_name="volume_name_example",
                                volume_namespace="volume_namespace_example",
                            ),
                            vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                fs_type="fs_type_example",
                                storage_policy_id="storage_policy_id_example",
                                storage_policy_name="storage_policy_name_example",
                                volume_path="volume_path_example",
                            ),
                        )
                    ],
                ),
            ),
            ttl_seconds_after_finished=1,
        ),
        status=V1JobStatus(
            active=1,
            completed_indexes="completed_indexes_example",
            completion_time="1970-01-01T00:00:00.00Z",
            conditions=[
                V1JobCondition(
                    last_probe_time="1970-01-01T00:00:00.00Z",
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            failed=1,
            ready=1,
            start_time="1970-01-01T00:00:00.00Z",
            succeeded=1,
            uncounted_terminated_pods=V1UncountedTerminatedPods(
                failed=[
                    "failed_example"
                ],
                succeeded=[
                    "succeeded_example"
                ],
            ),
        ),
    )
    try:
        api_response = api_instance.create_namespaced_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1Job(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1JobSpec(
            active_deadline_seconds=1,
            backoff_limit=1,
            completion_mode="completion_mode_example",
            completions=1,
            manual_selector=True,
            parallelism=1,
            pod_failure_policy=V1PodFailurePolicy(
                rules=[
                    V1PodFailurePolicyRule(
                        action="action_example",
                        on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                            container_name="container_name_example",
                            operator="operator_example",
                            values=[
                                1
                            ],
                        ),
                        on_pod_conditions=[
                            V1PodFailurePolicyOnPodConditionsPattern(
                                status="status_example",
                                type="type_example",
                            )
                        ],
                    )
                ],
            ),
            selector=V1LabelSelector(
                match_expressions=[
                    V1LabelSelectorRequirement(
                        key="key_example",
                        operator="operator_example",
                        values=[
                            "values_example"
                        ],
                    )
                ],
                match_labels=dict(
                    "key": "key_example",
                ),
            ),
            suspend=True,
            template=V1PodTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1PodSpec(
                    active_deadline_seconds=1,
                    affinity=V1Affinity(
                        node_affinity=V1NodeAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1PreferredSchedulingTerm(
                                    preference=V1NodeSelectorTerm(
                                        match_expressions=[
                                            V1NodeSelectorRequirement(
                                                key="key_example",
                                                operator="operator_example",
                                                values=[
                                                    "values_example"
                                                ],
                                            )
                                        ],
                                        match_fields=[
                                            V1NodeSelectorRequirement()
                                        ],
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                node_selector_terms=[
                                    V1NodeSelectorTerm()
                                ],
                            ),
                        ),
                        pod_affinity=V1PodAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm(
                                    pod_affinity_term=V1PodAffinityTerm(
                                        label_selector=V1LabelSelector(),
                                        namespace_selector=V1LabelSelector(),
                                        namespaces=[
                                            "namespaces_example"
                                        ],
                                        topology_key="topology_key_example",
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                        pod_anti_affinity=V1PodAntiAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm()
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                    ),
                    automount_service_account_token=True,
                    containers=[
                        V1Container(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
                            env=[
                                V1EnvVar(
                                    name="name_example",
                                    value="value_example",
                                    value_from=V1EnvVarSource(
                                        config_map_key_ref=V1ConfigMapKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                        field_ref=V1ObjectFieldSelector(
                                            api_version="api_version_example",
                                            field_path="field_path_example",
                                        ),
                                        resource_field_ref=V1ResourceFieldSelector(
                                            container_name="container_name_example",
                                            divisor="divisor_example",
                                            resource="resource_example",
                                        ),
                                        secret_key_ref=V1SecretKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                    ),
                                )
                            ],
                            env_from=[
                                V1EnvFromSource(
                                    config_map_ref=V1ConfigMapEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                    prefix="prefix_example",
                                    secret_ref=V1SecretEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                )
                            ],
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(
                                post_start=V1LifecycleHandler(
                                    _exec=V1ExecAction(
                                        command=[
                                            "command_example"
                                        ],
                                    ),
                                    http_get=V1HTTPGetAction(
                                        host="host_example",
                                        http_headers=[
                                            V1HTTPHeader(
                                                name="name_example",
                                                value="value_example",
                                            )
                                        ],
                                        path="path_example",
                                        port=dict(),
                                        scheme="scheme_example",
                                    ),
                                    tcp_socket=V1TCPSocketAction(
                                        host="host_example",
                                        port=dict(),
                                    ),
                                ),
                                pre_stop=V1LifecycleHandler(),
                            ),
                            liveness_probe=V1Probe(
                                _exec=V1ExecAction(),
                                failure_threshold=1,
                                grpc=V1GRPCAction(
                                    port=1,
                                    service="service_example",
                                ),
                                http_get=V1HTTPGetAction(),
                                initial_delay_seconds=1,
                                period_seconds=1,
                                success_threshold=1,
                                tcp_socket=V1TCPSocketAction(),
                                termination_grace_period_seconds=1,
                                timeout_seconds=1,
                            ),
                            name="name_example",
                            ports=[
                                V1ContainerPort(
                                    container_port=1,
                                    host_ip="host_ip_example",
                                    host_port=1,
                                    name="name_example",
                                    protocol="protocol_example",
                                )
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(
                                limits=dict(
                                    "key": "key_example",
                                ),
                                requests=dict(
                                    "key": "key_example",
                                ),
                            ),
                            security_context=V1SecurityContext(
                                allow_privilege_escalation=True,
                                capabilities=V1Capabilities(
                                    add=[
                                        "add_example"
                                    ],
                                    drop=[
                                        "drop_example"
                                    ],
                                ),
                                privileged=True,
                                proc_mount="proc_mount_example",
                                read_only_root_filesystem=True,
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(
                                    level="level_example",
                                    role="role_example",
                                    type="type_example",
                                    user="user_example",
                                ),
                                seccomp_profile=V1SeccompProfile(
                                    localhost_profile="localhost_profile_example",
                                    type="type_example",
                                ),
                                windows_options=V1WindowsSecurityContextOptions(
                                    gmsa_credential_spec="gmsa_credential_spec_example",
                                    gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                    host_process=True,
                                    run_as_user_name="run_as_user_name_example",
                                ),
                            ),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
                            volume_devices=[
                                V1VolumeDevice(
                                    device_path="device_path_example",
                                    name="name_example",
                                )
                            ],
                            volume_mounts=[
                                V1VolumeMount(
                                    mount_path="mount_path_example",
                                    mount_propagation="mount_propagation_example",
                                    name="name_example",
                                    read_only=True,
                                    sub_path="sub_path_example",
                                    sub_path_expr="sub_path_expr_example",
                                )
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    dns_config=V1PodDNSConfig(
                        nameservers=[
                            "nameservers_example"
                        ],
                        options=[
                            V1PodDNSConfigOption(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        searches=[
                            "searches_example"
                        ],
                    ),
                    dns_policy="dns_policy_example",
                    enable_service_links=True,
                    ephemeral_containers=[
                        V1EphemeralContainer(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
,
,
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(),
                            liveness_probe=V1Probe(),
                            name="name_example",
                            ports=[
                                V1ContainerPort()
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(),
                            security_context=V1SecurityContext(),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            target_container_name="target_container_name_example",
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
,
                            volume_mounts=[
                                V1VolumeMount()
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    host_aliases=[
                        V1HostAlias(
                            hostnames=[
                                "hostnames_example"
                            ],
                            ip="ip_example",
                        )
                    ],
                    host_ipc=True,
                    host_network=True,
                    host_pid=True,
                    host_users=True,
                    hostname="hostname_example",
                    image_pull_secrets=[
                        V1LocalObjectReference(
                            name="name_example",
                        )
                    ],
                    init_containers=[
                        V1Container()
                    ],
                    node_name="node_name_example",
                    node_selector=dict(
                        "key": "key_example",
                    ),
                    os=V1PodOS(
                        name="name_example",
                    ),
                    overhead=dict(
                        "key": "key_example",
                    ),
                    preemption_policy="preemption_policy_example",
                    priority=1,
                    priority_class_name="priority_class_name_example",
                    readiness_gates=[
                        V1PodReadinessGate(
                            condition_type="condition_type_example",
                        )
                    ],
                    restart_policy="restart_policy_example",
                    runtime_class_name="runtime_class_name_example",
                    scheduler_name="scheduler_name_example",
                    security_context=V1PodSecurityContext(
                        fs_group=1,
                        fs_group_change_policy="fs_group_change_policy_example",
                        run_as_group=1,
                        run_as_non_root=True,
                        run_as_user=1,
                        se_linux_options=V1SELinuxOptions(),
                        seccomp_profile=V1SeccompProfile(),
                        supplemental_groups=[
                            1
                        ],
                        sysctls=[
                            V1Sysctl(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        windows_options=V1WindowsSecurityContextOptions(),
                    ),
                    service_account="service_account_example",
                    service_account_name="service_account_name_example",
                    set_hostname_as_fqdn=True,
                    share_process_namespace=True,
                    subdomain="subdomain_example",
                    termination_grace_period_seconds=1,
                    tolerations=[
                        V1Toleration(
                            effect="effect_example",
                            key="key_example",
                            operator="operator_example",
                            toleration_seconds=1,
                            value="value_example",
                        )
                    ],
                    topology_spread_constraints=[
                        V1TopologySpreadConstraint(
                            label_selector=V1LabelSelector(),
                            match_label_keys=[
                                "match_label_keys_example"
                            ],
                            max_skew=1,
                            min_domains=1,
                            node_affinity_policy="node_affinity_policy_example",
                            node_taints_policy="node_taints_policy_example",
                            topology_key="topology_key_example",
                            when_unsatisfiable="when_unsatisfiable_example",
                        )
                    ],
                    volumes=[
                        V1Volume(
                            aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            azure_disk=V1AzureDiskVolumeSource(
                                caching_mode="caching_mode_example",
                                disk_name="disk_name_example",
                                disk_uri="disk_uri_example",
                                fs_type="fs_type_example",
                                kind="kind_example",
                                read_only=True,
                            ),
                            azure_file=V1AzureFileVolumeSource(
                                read_only=True,
                                secret_name="secret_name_example",
                                share_name="share_name_example",
                            ),
                            cephfs=V1CephFSVolumeSource(
                                monitors=[
                                    "monitors_example"
                                ],
                                path="path_example",
                                read_only=True,
                                secret_file="secret_file_example",
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            cinder=V1CinderVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_id="volume_id_example",
                            ),
                            config_map=V1ConfigMapVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath(
                                        key="key_example",
                                        mode=1,
                                        path="path_example",
                                    )
                                ],
                                name="name_example",
                                optional=True,
                            ),
                            csi=V1CSIVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                node_publish_secret_ref=V1LocalObjectReference(),
                                read_only=True,
                                volume_attributes=dict(
                                    "key": "key_example",
                                ),
                            ),
                            downward_api=V1DownwardAPIVolumeSource(
                                default_mode=1,
                                items=[
                                    V1DownwardAPIVolumeFile(
                                        field_ref=V1ObjectFieldSelector(),
                                        mode=1,
                                        path="path_example",
                                        resource_field_ref=V1ResourceFieldSelector(),
                                    )
                                ],
                            ),
                            empty_dir=V1EmptyDirVolumeSource(
                                medium="medium_example",
                                size_limit="size_limit_example",
                            ),
                            ephemeral=V1EphemeralVolumeSource(
                                volume_claim_template=V1PersistentVolumeClaimTemplate(
                                    metadata=V1ObjectMeta(),
                                    spec=V1PersistentVolumeClaimSpec(
                                        access_modes=[
                                            "access_modes_example"
                                        ],
                                        data_source=V1TypedLocalObjectReference(
                                            api_group="api_group_example",
                                            kind="kind_example",
                                            name="name_example",
                                        ),
,
                                        resources=V1ResourceRequirements(),
                                        selector=V1LabelSelector(),
                                        storage_class_name="storage_class_name_example",
                                        volume_mode="volume_mode_example",
                                        volume_name="volume_name_example",
                                    ),
                                ),
                            ),
                            fc=V1FCVolumeSource(
                                fs_type="fs_type_example",
                                lun=1,
                                read_only=True,
                                target_wwns=[
                                    "target_wwns_example"
                                ],
                                wwids=[
                                    "wwids_example"
                                ],
                            ),
                            flex_volume=V1FlexVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                options=dict(
                                    "key": "key_example",
                                ),
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                            ),
                            flocker=V1FlockerVolumeSource(
                                dataset_name="dataset_name_example",
                                dataset_uuid="dataset_uuid_example",
                            ),
                            gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                pd_name="pd_name_example",
                                read_only=True,
                            ),
                            git_repo=V1GitRepoVolumeSource(
                                directory="directory_example",
                                repository="repository_example",
                                revision="revision_example",
                            ),
                            glusterfs=V1GlusterfsVolumeSource(
                                endpoints="endpoints_example",
                                path="path_example",
                                read_only=True,
                            ),
                            host_path=V1HostPathVolumeSource(
                                path="path_example",
                                type="type_example",
                            ),
                            iscsi=V1ISCSIVolumeSource(
                                chap_auth_discovery=True,
                                chap_auth_session=True,
                                fs_type="fs_type_example",
                                initiator_name="initiator_name_example",
                                iqn="iqn_example",
                                iscsi_interface="iscsi_interface_example",
                                lun=1,
                                portals=[
                                    "portals_example"
                                ],
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                target_portal="target_portal_example",
                            ),
                            name="name_example",
                            nfs=V1NFSVolumeSource(
                                path="path_example",
                                read_only=True,
                                server="server_example",
                            ),
                            persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                claim_name="claim_name_example",
                                read_only=True,
                            ),
                            photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                pd_id="pd_id_example",
                            ),
                            portworx_volume=V1PortworxVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            projected=V1ProjectedVolumeSource(
                                default_mode=1,
                                sources=[
                                    V1VolumeProjection(
                                        config_map=V1ConfigMapProjection(
,
                                            name="name_example",
                                            optional=True,
                                        ),
                                        downward_api=V1DownwardAPIProjection(
                                            items=[
                                                V1DownwardAPIVolumeFile()
                                            ],
                                        ),
                                        secret=V1SecretProjection(
                                            items=[
                                                V1KeyToPath()
                                            ],
                                            name="name_example",
                                            optional=True,
                                        ),
                                        service_account_token=V1ServiceAccountTokenProjection(
                                            audience="audience_example",
                                            expiration_seconds=1,
                                            path="path_example",
                                        ),
                                    )
                                ],
                            ),
                            quobyte=V1QuobyteVolumeSource(
                                group="group_example",
                                read_only=True,
                                registry="registry_example",
                                tenant="tenant_example",
                                user="user_example",
                                volume="volume_example",
                            ),
                            rbd=V1RBDVolumeSource(
                                fs_type="fs_type_example",
                                image="image_example",
                                keyring="keyring_example",
                                monitors=[
                                    "monitors_example"
                                ],
                                pool="pool_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            scale_io=V1ScaleIOVolumeSource(
                                fs_type="fs_type_example",
                                gateway="gateway_example",
                                protection_domain="protection_domain_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                ssl_enabled=True,
                                storage_mode="storage_mode_example",
                                storage_pool="storage_pool_example",
                                system="system_example",
                                volume_name="volume_name_example",
                            ),
                            secret=V1SecretVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath()
                                ],
                                optional=True,
                                secret_name="secret_name_example",
                            ),
                            storageos=V1StorageOSVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_name="volume_name_example",
                                volume_namespace="volume_namespace_example",
                            ),
                            vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                fs_type="fs_type_example",
                                storage_policy_id="storage_policy_id_example",
                                storage_policy_name="storage_policy_name_example",
                                volume_path="volume_path_example",
                            ),
                        )
                    ],
                ),
            ),
            ttl_seconds_after_finished=1,
        ),
        status=V1JobStatus(
            active=1,
            completed_indexes="completed_indexes_example",
            completion_time="1970-01-01T00:00:00.00Z",
            conditions=[
                V1JobCondition(
                    last_probe_time="1970-01-01T00:00:00.00Z",
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            failed=1,
            ready=1,
            start_time="1970-01-01T00:00:00.00Z",
            succeeded=1,
            uncounted_terminated_pods=V1UncountedTerminatedPods(
                failed=[
                    "failed_example"
                ],
                succeeded=[
                    "succeeded_example"
                ],
            ),
        ),
    )
    try:
        api_response = api_instance.create_namespaced_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->create_namespaced_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_namespaced_job.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_namespaced_job.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_namespaced_job.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_namespaced_job.ApiResponseFor401) | Unauthorized

#### create_namespaced_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### create_namespaced_job.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### create_namespaced_job.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### create_namespaced_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_collection_namespaced_cron_job**
<a name="delete_collection_namespaced_cron_job"></a>
> V1Status delete_collection_namespaced_cron_job(namespace)



delete collection of CronJob

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_delete_options import V1DeleteOptions
from kubernetes.client.model.v1_status import V1Status
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_collection_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->delete_collection_namespaced_cron_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'continue': "continue_example",
        'dryRun': "dryRun_example",
        'fieldSelector': "fieldSelector_example",
        'gracePeriodSeconds': 1,
        'labelSelector': "labelSelector_example",
        'limit': 1,
        'orphanDependents': True,
        'propagationPolicy': "propagationPolicy_example",
        'resourceVersion': "resourceVersion_example",
        'resourceVersionMatch': "resourceVersionMatch_example",
        'timeoutSeconds': 1,
    }
    body = V1DeleteOptions(
        api_version="api_version_example",
        dry_run=[
            "dry_run_example"
        ],
        grace_period_seconds=1,
        kind="kind_example",
        orphan_dependents=True,
        preconditions=V1Preconditions(
            resource_version="resource_version_example",
            uid="uid_example",
        ),
        propagation_policy="propagation_policy_example",
    )
    try:
        api_response = api_instance.delete_collection_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->delete_collection_namespaced_cron_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1DeleteOptions**](../../models/V1DeleteOptions.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
continue | ModelContinueSchema | | optional
dryRun | DryRunSchema | | optional
fieldSelector | FieldSelectorSchema | | optional
gracePeriodSeconds | GracePeriodSecondsSchema | | optional
labelSelector | LabelSelectorSchema | | optional
limit | LimitSchema | | optional
orphanDependents | OrphanDependentsSchema | | optional
propagationPolicy | PropagationPolicySchema | | optional
resourceVersion | ResourceVersionSchema | | optional
resourceVersionMatch | ResourceVersionMatchSchema | | optional
timeoutSeconds | TimeoutSecondsSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModelContinueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GracePeriodSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LabelSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OrphanDependentsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PropagationPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionMatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeoutSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_collection_namespaced_cron_job.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#delete_collection_namespaced_cron_job.ApiResponseFor401) | Unauthorized

#### delete_collection_namespaced_cron_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


#### delete_collection_namespaced_cron_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_collection_namespaced_job**
<a name="delete_collection_namespaced_job"></a>
> V1Status delete_collection_namespaced_job(namespace)



delete collection of Job

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_delete_options import V1DeleteOptions
from kubernetes.client.model.v1_status import V1Status
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_collection_namespaced_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->delete_collection_namespaced_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'continue': "continue_example",
        'dryRun': "dryRun_example",
        'fieldSelector': "fieldSelector_example",
        'gracePeriodSeconds': 1,
        'labelSelector': "labelSelector_example",
        'limit': 1,
        'orphanDependents': True,
        'propagationPolicy': "propagationPolicy_example",
        'resourceVersion': "resourceVersion_example",
        'resourceVersionMatch': "resourceVersionMatch_example",
        'timeoutSeconds': 1,
    }
    body = V1DeleteOptions(
        api_version="api_version_example",
        dry_run=[
            "dry_run_example"
        ],
        grace_period_seconds=1,
        kind="kind_example",
        orphan_dependents=True,
        preconditions=V1Preconditions(
            resource_version="resource_version_example",
            uid="uid_example",
        ),
        propagation_policy="propagation_policy_example",
    )
    try:
        api_response = api_instance.delete_collection_namespaced_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->delete_collection_namespaced_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1DeleteOptions**](../../models/V1DeleteOptions.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
continue | ModelContinueSchema | | optional
dryRun | DryRunSchema | | optional
fieldSelector | FieldSelectorSchema | | optional
gracePeriodSeconds | GracePeriodSecondsSchema | | optional
labelSelector | LabelSelectorSchema | | optional
limit | LimitSchema | | optional
orphanDependents | OrphanDependentsSchema | | optional
propagationPolicy | PropagationPolicySchema | | optional
resourceVersion | ResourceVersionSchema | | optional
resourceVersionMatch | ResourceVersionMatchSchema | | optional
timeoutSeconds | TimeoutSecondsSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ModelContinueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GracePeriodSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LabelSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OrphanDependentsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PropagationPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionMatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeoutSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_collection_namespaced_job.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#delete_collection_namespaced_job.ApiResponseFor401) | Unauthorized

#### delete_collection_namespaced_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


#### delete_collection_namespaced_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_namespaced_cron_job**
<a name="delete_namespaced_cron_job"></a>
> V1Status delete_namespaced_cron_job(namenamespace)



delete a CronJob

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_delete_options import V1DeleteOptions
from kubernetes.client.model.v1_status import V1Status
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->delete_namespaced_cron_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'gracePeriodSeconds': 1,
        'orphanDependents': True,
        'propagationPolicy': "propagationPolicy_example",
    }
    body = V1DeleteOptions(
        api_version="api_version_example",
        dry_run=[
            "dry_run_example"
        ],
        grace_period_seconds=1,
        kind="kind_example",
        orphan_dependents=True,
        preconditions=V1Preconditions(
            resource_version="resource_version_example",
            uid="uid_example",
        ),
        propagation_policy="propagation_policy_example",
    )
    try:
        api_response = api_instance.delete_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->delete_namespaced_cron_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1DeleteOptions**](../../models/V1DeleteOptions.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
gracePeriodSeconds | GracePeriodSecondsSchema | | optional
orphanDependents | OrphanDependentsSchema | | optional
propagationPolicy | PropagationPolicySchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GracePeriodSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OrphanDependentsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PropagationPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_namespaced_cron_job.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#delete_namespaced_cron_job.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#delete_namespaced_cron_job.ApiResponseFor401) | Unauthorized

#### delete_namespaced_cron_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


#### delete_namespaced_cron_job.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


#### delete_namespaced_cron_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_namespaced_job**
<a name="delete_namespaced_job"></a>
> V1Status delete_namespaced_job(namenamespace)



delete a Job

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_delete_options import V1DeleteOptions
from kubernetes.client.model.v1_status import V1Status
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_namespaced_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->delete_namespaced_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'gracePeriodSeconds': 1,
        'orphanDependents': True,
        'propagationPolicy': "propagationPolicy_example",
    }
    body = V1DeleteOptions(
        api_version="api_version_example",
        dry_run=[
            "dry_run_example"
        ],
        grace_period_seconds=1,
        kind="kind_example",
        orphan_dependents=True,
        preconditions=V1Preconditions(
            resource_version="resource_version_example",
            uid="uid_example",
        ),
        propagation_policy="propagation_policy_example",
    )
    try:
        api_response = api_instance.delete_namespaced_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->delete_namespaced_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1DeleteOptions**](../../models/V1DeleteOptions.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
gracePeriodSeconds | GracePeriodSecondsSchema | | optional
orphanDependents | OrphanDependentsSchema | | optional
propagationPolicy | PropagationPolicySchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GracePeriodSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# OrphanDependentsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# PropagationPolicySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_namespaced_job.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#delete_namespaced_job.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#delete_namespaced_job.ApiResponseFor401) | Unauthorized

#### delete_namespaced_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


#### delete_namespaced_job.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Status**](../../models/V1Status.md) |  | 


#### delete_namespaced_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_api_resources**
<a name="get_api_resources"></a>
> V1APIResourceList get_api_resources()



get available resources

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_api_resource_list import V1APIResourceList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_api_resources()
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->get_api_resources: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_api_resources.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_api_resources.ApiResponseFor401) | Unauthorized

#### get_api_resources.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1APIResourceList**](../../models/V1APIResourceList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1APIResourceList**](../../models/V1APIResourceList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1APIResourceList**](../../models/V1APIResourceList.md) |  | 


#### get_api_resources.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_cron_job_for_all_namespaces**
<a name="list_cron_job_for_all_namespaces"></a>
> V1CronJobList list_cron_job_for_all_namespaces()



list or watch objects of kind CronJob

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_cron_job_list import V1CronJobList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only optional values
    query_params = {
        'allowWatchBookmarks': True,
        'continue': "continue_example",
        'fieldSelector': "fieldSelector_example",
        'labelSelector': "labelSelector_example",
        'limit': 1,
        'pretty': "pretty_example",
        'resourceVersion': "resourceVersion_example",
        'resourceVersionMatch': "resourceVersionMatch_example",
        'timeoutSeconds': 1,
        'watch': True,
    }
    try:
        api_response = api_instance.list_cron_job_for_all_namespaces(
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->list_cron_job_for_all_namespaces: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', 'application/json;stream&#x3D;watch', 'application/vnd.kubernetes.protobuf;stream&#x3D;watch', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
allowWatchBookmarks | AllowWatchBookmarksSchema | | optional
continue | ModelContinueSchema | | optional
fieldSelector | FieldSelectorSchema | | optional
labelSelector | LabelSelectorSchema | | optional
limit | LimitSchema | | optional
pretty | PrettySchema | | optional
resourceVersion | ResourceVersionSchema | | optional
resourceVersionMatch | ResourceVersionMatchSchema | | optional
timeoutSeconds | TimeoutSecondsSchema | | optional
watch | WatchSchema | | optional


# AllowWatchBookmarksSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ModelContinueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LabelSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionMatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeoutSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_cron_job_for_all_namespaces.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_cron_job_for_all_namespaces.ApiResponseFor401) | Unauthorized

#### list_cron_job_for_all_namespaces.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJobList**](../../models/V1CronJobList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJobList**](../../models/V1CronJobList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJobList**](../../models/V1CronJobList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJobList**](../../models/V1CronJobList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJobList**](../../models/V1CronJobList.md) |  | 


#### list_cron_job_for_all_namespaces.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_job_for_all_namespaces**
<a name="list_job_for_all_namespaces"></a>
> V1JobList list_job_for_all_namespaces()



list or watch objects of kind Job

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_job_list import V1JobList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only optional values
    query_params = {
        'allowWatchBookmarks': True,
        'continue': "continue_example",
        'fieldSelector': "fieldSelector_example",
        'labelSelector': "labelSelector_example",
        'limit': 1,
        'pretty': "pretty_example",
        'resourceVersion': "resourceVersion_example",
        'resourceVersionMatch': "resourceVersionMatch_example",
        'timeoutSeconds': 1,
        'watch': True,
    }
    try:
        api_response = api_instance.list_job_for_all_namespaces(
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->list_job_for_all_namespaces: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', 'application/json;stream&#x3D;watch', 'application/vnd.kubernetes.protobuf;stream&#x3D;watch', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
allowWatchBookmarks | AllowWatchBookmarksSchema | | optional
continue | ModelContinueSchema | | optional
fieldSelector | FieldSelectorSchema | | optional
labelSelector | LabelSelectorSchema | | optional
limit | LimitSchema | | optional
pretty | PrettySchema | | optional
resourceVersion | ResourceVersionSchema | | optional
resourceVersionMatch | ResourceVersionMatchSchema | | optional
timeoutSeconds | TimeoutSecondsSchema | | optional
watch | WatchSchema | | optional


# AllowWatchBookmarksSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ModelContinueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LabelSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionMatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeoutSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_job_for_all_namespaces.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_job_for_all_namespaces.ApiResponseFor401) | Unauthorized

#### list_job_for_all_namespaces.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1JobList**](../../models/V1JobList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1JobList**](../../models/V1JobList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1JobList**](../../models/V1JobList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1JobList**](../../models/V1JobList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1JobList**](../../models/V1JobList.md) |  | 


#### list_job_for_all_namespaces.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_namespaced_cron_job**
<a name="list_namespaced_cron_job"></a>
> V1CronJobList list_namespaced_cron_job(namespace)



list or watch objects of kind CronJob

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_cron_job_list import V1CronJobList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.list_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->list_namespaced_cron_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'allowWatchBookmarks': True,
        'continue': "continue_example",
        'fieldSelector': "fieldSelector_example",
        'labelSelector': "labelSelector_example",
        'limit': 1,
        'resourceVersion': "resourceVersion_example",
        'resourceVersionMatch': "resourceVersionMatch_example",
        'timeoutSeconds': 1,
        'watch': True,
    }
    try:
        api_response = api_instance.list_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->list_namespaced_cron_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', 'application/json;stream&#x3D;watch', 'application/vnd.kubernetes.protobuf;stream&#x3D;watch', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
allowWatchBookmarks | AllowWatchBookmarksSchema | | optional
continue | ModelContinueSchema | | optional
fieldSelector | FieldSelectorSchema | | optional
labelSelector | LabelSelectorSchema | | optional
limit | LimitSchema | | optional
resourceVersion | ResourceVersionSchema | | optional
resourceVersionMatch | ResourceVersionMatchSchema | | optional
timeoutSeconds | TimeoutSecondsSchema | | optional
watch | WatchSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AllowWatchBookmarksSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ModelContinueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LabelSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ResourceVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionMatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeoutSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_namespaced_cron_job.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_namespaced_cron_job.ApiResponseFor401) | Unauthorized

#### list_namespaced_cron_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJobList**](../../models/V1CronJobList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJobList**](../../models/V1CronJobList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJobList**](../../models/V1CronJobList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJobList**](../../models/V1CronJobList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJobList**](../../models/V1CronJobList.md) |  | 


#### list_namespaced_cron_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_namespaced_job**
<a name="list_namespaced_job"></a>
> V1JobList list_namespaced_job(namespace)



list or watch objects of kind Job

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_job_list import V1JobList
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.list_namespaced_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->list_namespaced_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'allowWatchBookmarks': True,
        'continue': "continue_example",
        'fieldSelector': "fieldSelector_example",
        'labelSelector': "labelSelector_example",
        'limit': 1,
        'resourceVersion': "resourceVersion_example",
        'resourceVersionMatch': "resourceVersionMatch_example",
        'timeoutSeconds': 1,
        'watch': True,
    }
    try:
        api_response = api_instance.list_namespaced_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->list_namespaced_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', 'application/json;stream&#x3D;watch', 'application/vnd.kubernetes.protobuf;stream&#x3D;watch', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
allowWatchBookmarks | AllowWatchBookmarksSchema | | optional
continue | ModelContinueSchema | | optional
fieldSelector | FieldSelectorSchema | | optional
labelSelector | LabelSelectorSchema | | optional
limit | LimitSchema | | optional
resourceVersion | ResourceVersionSchema | | optional
resourceVersionMatch | ResourceVersionMatchSchema | | optional
timeoutSeconds | TimeoutSecondsSchema | | optional
watch | WatchSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AllowWatchBookmarksSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

# ModelContinueSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LabelSelectorSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ResourceVersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResourceVersionMatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TimeoutSecondsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# WatchSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
namespace | NamespaceSchema | | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_namespaced_job.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_namespaced_job.ApiResponseFor401) | Unauthorized

#### list_namespaced_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1JobList**](../../models/V1JobList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1JobList**](../../models/V1JobList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1JobList**](../../models/V1JobList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1JobList**](../../models/V1JobList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1JobList**](../../models/V1JobList.md) |  | 


#### list_namespaced_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_namespaced_cron_job**
<a name="patch_namespaced_cron_job"></a>
> V1CronJob patch_namespaced_cron_job(namenamespacebody)



partially update the specified CronJob

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_cron_job import V1CronJob
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->patch_namespaced_cron_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
        'force': True,
    }
    body = dict()
    try:
        api_response = api_instance.patch_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->patch_namespaced_cron_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationMergePatchjson, SchemaForRequestBodyApplicationStrategicMergePatchjson, SchemaForRequestBodyApplicationApplyPatchyaml] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationMergePatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationStrategicMergePatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationApplyPatchyaml

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional
force | ForceSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ForceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_namespaced_cron_job.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_namespaced_cron_job.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_namespaced_cron_job.ApiResponseFor401) | Unauthorized

#### patch_namespaced_cron_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### patch_namespaced_cron_job.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### patch_namespaced_cron_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_namespaced_cron_job_status**
<a name="patch_namespaced_cron_job_status"></a>
> V1CronJob patch_namespaced_cron_job_status(namenamespacebody)



partially update status of the specified CronJob

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_cron_job import V1CronJob
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_namespaced_cron_job_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->patch_namespaced_cron_job_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
        'force': True,
    }
    body = dict()
    try:
        api_response = api_instance.patch_namespaced_cron_job_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->patch_namespaced_cron_job_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationMergePatchjson, SchemaForRequestBodyApplicationStrategicMergePatchjson, SchemaForRequestBodyApplicationApplyPatchyaml] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationMergePatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationStrategicMergePatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationApplyPatchyaml

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional
force | ForceSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ForceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_namespaced_cron_job_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_namespaced_cron_job_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_namespaced_cron_job_status.ApiResponseFor401) | Unauthorized

#### patch_namespaced_cron_job_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### patch_namespaced_cron_job_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### patch_namespaced_cron_job_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_namespaced_job**
<a name="patch_namespaced_job"></a>
> V1Job patch_namespaced_job(namenamespacebody)



partially update the specified Job

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_job import V1Job
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_namespaced_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->patch_namespaced_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
        'force': True,
    }
    body = dict()
    try:
        api_response = api_instance.patch_namespaced_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->patch_namespaced_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationMergePatchjson, SchemaForRequestBodyApplicationStrategicMergePatchjson, SchemaForRequestBodyApplicationApplyPatchyaml] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationMergePatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationStrategicMergePatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationApplyPatchyaml

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional
force | ForceSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ForceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_namespaced_job.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_namespaced_job.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_namespaced_job.ApiResponseFor401) | Unauthorized

#### patch_namespaced_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### patch_namespaced_job.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### patch_namespaced_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_namespaced_job_status**
<a name="patch_namespaced_job_status"></a>
> V1Job patch_namespaced_job_status(namenamespacebody)



partially update status of the specified Job

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_job import V1Job
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_namespaced_job_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->patch_namespaced_job_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
        'force': True,
    }
    body = dict()
    try:
        api_response = api_instance.patch_namespaced_job_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->patch_namespaced_job_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJsonPatchjson, SchemaForRequestBodyApplicationMergePatchjson, SchemaForRequestBodyApplicationStrategicMergePatchjson, SchemaForRequestBodyApplicationApplyPatchyaml] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json-patch+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJsonPatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationMergePatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationStrategicMergePatchjson

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

# SchemaForRequestBodyApplicationApplyPatchyaml

Patch is provided to give a concrete name and type to the Kubernetes PATCH request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Patch is provided to give a concrete name and type to the Kubernetes PATCH request body. | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional
force | ForceSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ForceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_namespaced_job_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_namespaced_job_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_namespaced_job_status.ApiResponseFor401) | Unauthorized

#### patch_namespaced_job_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### patch_namespaced_job_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### patch_namespaced_job_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_namespaced_cron_job**
<a name="read_namespaced_cron_job"></a>
> V1CronJob read_namespaced_cron_job(namenamespace)



read the specified CronJob

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_cron_job import V1CronJob
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->read_namespaced_cron_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->read_namespaced_cron_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_namespaced_cron_job.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_namespaced_cron_job.ApiResponseFor401) | Unauthorized

#### read_namespaced_cron_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### read_namespaced_cron_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_namespaced_cron_job_status**
<a name="read_namespaced_cron_job_status"></a>
> V1CronJob read_namespaced_cron_job_status(namenamespace)



read status of the specified CronJob

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_cron_job import V1CronJob
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_namespaced_cron_job_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->read_namespaced_cron_job_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_namespaced_cron_job_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->read_namespaced_cron_job_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_namespaced_cron_job_status.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_namespaced_cron_job_status.ApiResponseFor401) | Unauthorized

#### read_namespaced_cron_job_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### read_namespaced_cron_job_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_namespaced_job**
<a name="read_namespaced_job"></a>
> V1Job read_namespaced_job(namenamespace)



read the specified Job

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_job import V1Job
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_namespaced_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->read_namespaced_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_namespaced_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->read_namespaced_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_namespaced_job.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_namespaced_job.ApiResponseFor401) | Unauthorized

#### read_namespaced_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### read_namespaced_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_namespaced_job_status**
<a name="read_namespaced_job_status"></a>
> V1Job read_namespaced_job_status(namenamespace)



read status of the specified Job

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_job import V1Job
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_namespaced_job_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->read_namespaced_job_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_namespaced_job_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->read_namespaced_job_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_namespaced_job_status.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_namespaced_job_status.ApiResponseFor401) | Unauthorized

#### read_namespaced_job_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### read_namespaced_job_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_namespaced_cron_job**
<a name="replace_namespaced_cron_job"></a>
> V1CronJob replace_namespaced_cron_job(namenamespacebody)



replace the specified CronJob

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_cron_job import V1CronJob
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = V1CronJob(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1CronJobSpec(
            concurrency_policy="concurrency_policy_example",
            failed_jobs_history_limit=1,
            job_template=V1JobTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1JobSpec(
                    active_deadline_seconds=1,
                    backoff_limit=1,
                    completion_mode="completion_mode_example",
                    completions=1,
                    manual_selector=True,
                    parallelism=1,
                    pod_failure_policy=V1PodFailurePolicy(
                        rules=[
                            V1PodFailurePolicyRule(
                                action="action_example",
                                on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                                    container_name="container_name_example",
                                    operator="operator_example",
                                    values=[
                                        1
                                    ],
                                ),
                                on_pod_conditions=[
                                    V1PodFailurePolicyOnPodConditionsPattern(
                                        status="status_example",
                                        type="type_example",
                                    )
                                ],
                            )
                        ],
                    ),
                    selector=V1LabelSelector(
                        match_expressions=[
                            V1LabelSelectorRequirement(
                                key="key_example",
                                operator="operator_example",
                                values=[
                                    "values_example"
                                ],
                            )
                        ],
                        match_labels=dict(
                            "key": "key_example",
                        ),
                    ),
                    suspend=True,
                    template=V1PodTemplateSpec(
                        metadata=V1ObjectMeta(),
                        spec=V1PodSpec(
                            active_deadline_seconds=1,
                            affinity=V1Affinity(
                                node_affinity=V1NodeAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1PreferredSchedulingTerm(
                                            preference=V1NodeSelectorTerm(
                                                match_expressions=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example"
                                                        ],
                                                    )
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement()
                                                ],
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                        node_selector_terms=[
                                            V1NodeSelectorTerm()
                                        ],
                                    ),
                                ),
                                pod_affinity=V1PodAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(),
                                                namespace_selector=V1LabelSelector(),
                                                namespaces=[
                                                    "namespaces_example"
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                                pod_anti_affinity=V1PodAntiAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm()
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                            ),
                            automount_service_account_token=True,
                            containers=[
                                V1Container(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
                                    env=[
                                        V1EnvVar(
                                            name="name_example",
                                            value="value_example",
                                            value_from=V1EnvVarSource(
                                                config_map_key_ref=V1ConfigMapKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                field_ref=V1ObjectFieldSelector(
                                                    api_version="api_version_example",
                                                    field_path="field_path_example",
                                                ),
                                                resource_field_ref=V1ResourceFieldSelector(
                                                    container_name="container_name_example",
                                                    divisor="divisor_example",
                                                    resource="resource_example",
                                                ),
                                                secret_key_ref=V1SecretKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                            ),
                                        )
                                    ],
                                    env_from=[
                                        V1EnvFromSource(
                                            config_map_ref=V1ConfigMapEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                            prefix="prefix_example",
                                            secret_ref=V1SecretEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                        )
                                    ],
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example"
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    )
                                                ],
                                                path="path_example",
                                                port=dict(),
                                                scheme="scheme_example",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port=dict(),
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort(
                                            container_port=1,
                                            host_ip="host_ip_example",
                                            host_port=1,
                                            name="name_example",
                                            protocol="protocol_example",
                                        )
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(
                                        limits=dict(
                                            "key": "key_example",
                                        ),
                                        requests=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example"
                                            ],
                                            drop=[
                                                "drop_example"
                                            ],
                                        ),
                                        privileged=True,
                                        proc_mount="proc_mount_example",
                                        read_only_root_filesystem=True,
                                        run_as_group=1,
                                        run_as_non_root=True,
                                        run_as_user=1,
                                        se_linux_options=V1SELinuxOptions(
                                            level="level_example",
                                            role="role_example",
                                            type="type_example",
                                            user="user_example",
                                        ),
                                        seccomp_profile=V1SeccompProfile(
                                            localhost_profile="localhost_profile_example",
                                            type="type_example",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        )
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        )
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            dns_config=V1PodDNSConfig(
                                nameservers=[
                                    "nameservers_example"
                                ],
                                options=[
                                    V1PodDNSConfigOption(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                searches=[
                                    "searches_example"
                                ],
                            ),
                            dns_policy="dns_policy_example",
                            enable_service_links=True,
                            ephemeral_containers=[
                                V1EphemeralContainer(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
,
,
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(),
                                    liveness_probe=V1Probe(),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort()
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(),
                                    security_context=V1SecurityContext(),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    target_container_name="target_container_name_example",
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
,
                                    volume_mounts=[
                                        V1VolumeMount()
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            host_aliases=[
                                V1HostAlias(
                                    hostnames=[
                                        "hostnames_example"
                                    ],
                                    ip="ip_example",
                                )
                            ],
                            host_ipc=True,
                            host_network=True,
                            host_pid=True,
                            host_users=True,
                            hostname="hostname_example",
                            image_pull_secrets=[
                                V1LocalObjectReference(
                                    name="name_example",
                                )
                            ],
                            init_containers=[
                                V1Container()
                            ],
                            node_name="node_name_example",
                            node_selector=dict(
                                "key": "key_example",
                            ),
                            os=V1PodOS(
                                name="name_example",
                            ),
                            overhead=dict(
                                "key": "key_example",
                            ),
                            preemption_policy="preemption_policy_example",
                            priority=1,
                            priority_class_name="priority_class_name_example",
                            readiness_gates=[
                                V1PodReadinessGate(
                                    condition_type="condition_type_example",
                                )
                            ],
                            restart_policy="restart_policy_example",
                            runtime_class_name="runtime_class_name_example",
                            scheduler_name="scheduler_name_example",
                            security_context=V1PodSecurityContext(
                                fs_group=1,
                                fs_group_change_policy="fs_group_change_policy_example",
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(),
                                seccomp_profile=V1SeccompProfile(),
                                supplemental_groups=[
                                    1
                                ],
                                sysctls=[
                                    V1Sysctl(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                windows_options=V1WindowsSecurityContextOptions(),
                            ),
                            service_account="service_account_example",
                            service_account_name="service_account_name_example",
                            set_hostname_as_fqdn=True,
                            share_process_namespace=True,
                            subdomain="subdomain_example",
                            termination_grace_period_seconds=1,
                            tolerations=[
                                V1Toleration(
                                    effect="effect_example",
                                    key="key_example",
                                    operator="operator_example",
                                    toleration_seconds=1,
                                    value="value_example",
                                )
                            ],
                            topology_spread_constraints=[
                                V1TopologySpreadConstraint(
                                    label_selector=V1LabelSelector(),
                                    match_label_keys=[
                                        "match_label_keys_example"
                                    ],
                                    max_skew=1,
                                    min_domains=1,
                                    node_affinity_policy="node_affinity_policy_example",
                                    node_taints_policy="node_taints_policy_example",
                                    topology_key="topology_key_example",
                                    when_unsatisfiable="when_unsatisfiable_example",
                                )
                            ],
                            volumes=[
                                V1Volume(
                                    aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    azure_disk=V1AzureDiskVolumeSource(
                                        caching_mode="caching_mode_example",
                                        disk_name="disk_name_example",
                                        disk_uri="disk_uri_example",
                                        fs_type="fs_type_example",
                                        kind="kind_example",
                                        read_only=True,
                                    ),
                                    azure_file=V1AzureFileVolumeSource(
                                        read_only=True,
                                        secret_name="secret_name_example",
                                        share_name="share_name_example",
                                    ),
                                    cephfs=V1CephFSVolumeSource(
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        path="path_example",
                                        read_only=True,
                                        secret_file="secret_file_example",
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    cinder=V1CinderVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_id="volume_id_example",
                                    ),
                                    config_map=V1ConfigMapVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            )
                                        ],
                                        name="name_example",
                                        optional=True,
                                    ),
                                    csi=V1CSIVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        node_publish_secret_ref=V1LocalObjectReference(),
                                        read_only=True,
                                        volume_attributes=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    downward_api=V1DownwardAPIVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1DownwardAPIVolumeFile(
                                                field_ref=V1ObjectFieldSelector(),
                                                mode=1,
                                                path="path_example",
                                                resource_field_ref=V1ResourceFieldSelector(),
                                            )
                                        ],
                                    ),
                                    empty_dir=V1EmptyDirVolumeSource(
                                        medium="medium_example",
                                        size_limit="size_limit_example",
                                    ),
                                    ephemeral=V1EphemeralVolumeSource(
                                        volume_claim_template=V1PersistentVolumeClaimTemplate(
                                            metadata=V1ObjectMeta(),
                                            spec=V1PersistentVolumeClaimSpec(
                                                access_modes=[
                                                    "access_modes_example"
                                                ],
                                                data_source=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
,
                                                resources=V1ResourceRequirements(),
                                                selector=V1LabelSelector(),
                                                storage_class_name="storage_class_name_example",
                                                volume_mode="volume_mode_example",
                                                volume_name="volume_name_example",
                                            ),
                                        ),
                                    ),
                                    fc=V1FCVolumeSource(
                                        fs_type="fs_type_example",
                                        lun=1,
                                        read_only=True,
                                        target_wwns=[
                                            "target_wwns_example"
                                        ],
                                        wwids=[
                                            "wwids_example"
                                        ],
                                    ),
                                    flex_volume=V1FlexVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        options=dict(
                                            "key": "key_example",
                                        ),
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                    ),
                                    flocker=V1FlockerVolumeSource(
                                        dataset_name="dataset_name_example",
                                        dataset_uuid="dataset_uuid_example",
                                    ),
                                    gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        pd_name="pd_name_example",
                                        read_only=True,
                                    ),
                                    git_repo=V1GitRepoVolumeSource(
                                        directory="directory_example",
                                        repository="repository_example",
                                        revision="revision_example",
                                    ),
                                    glusterfs=V1GlusterfsVolumeSource(
                                        endpoints="endpoints_example",
                                        path="path_example",
                                        read_only=True,
                                    ),
                                    host_path=V1HostPathVolumeSource(
                                        path="path_example",
                                        type="type_example",
                                    ),
                                    iscsi=V1ISCSIVolumeSource(
                                        chap_auth_discovery=True,
                                        chap_auth_session=True,
                                        fs_type="fs_type_example",
                                        initiator_name="initiator_name_example",
                                        iqn="iqn_example",
                                        iscsi_interface="iscsi_interface_example",
                                        lun=1,
                                        portals=[
                                            "portals_example"
                                        ],
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        target_portal="target_portal_example",
                                    ),
                                    name="name_example",
                                    nfs=V1NFSVolumeSource(
                                        path="path_example",
                                        read_only=True,
                                        server="server_example",
                                    ),
                                    persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                        claim_name="claim_name_example",
                                        read_only=True,
                                    ),
                                    photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        pd_id="pd_id_example",
                                    ),
                                    portworx_volume=V1PortworxVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    projected=V1ProjectedVolumeSource(
                                        default_mode=1,
                                        sources=[
                                            V1VolumeProjection(
                                                config_map=V1ConfigMapProjection(
,
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                downward_api=V1DownwardAPIProjection(
                                                    items=[
                                                        V1DownwardAPIVolumeFile()
                                                    ],
                                                ),
                                                secret=V1SecretProjection(
                                                    items=[
                                                        V1KeyToPath()
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                service_account_token=V1ServiceAccountTokenProjection(
                                                    audience="audience_example",
                                                    expiration_seconds=1,
                                                    path="path_example",
                                                ),
                                            )
                                        ],
                                    ),
                                    quobyte=V1QuobyteVolumeSource(
                                        group="group_example",
                                        read_only=True,
                                        registry="registry_example",
                                        tenant="tenant_example",
                                        user="user_example",
                                        volume="volume_example",
                                    ),
                                    rbd=V1RBDVolumeSource(
                                        fs_type="fs_type_example",
                                        image="image_example",
                                        keyring="keyring_example",
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        pool="pool_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    scale_io=V1ScaleIOVolumeSource(
                                        fs_type="fs_type_example",
                                        gateway="gateway_example",
                                        protection_domain="protection_domain_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        ssl_enabled=True,
                                        storage_mode="storage_mode_example",
                                        storage_pool="storage_pool_example",
                                        system="system_example",
                                        volume_name="volume_name_example",
                                    ),
                                    secret=V1SecretVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath()
                                        ],
                                        optional=True,
                                        secret_name="secret_name_example",
                                    ),
                                    storageos=V1StorageOSVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_name="volume_name_example",
                                        volume_namespace="volume_namespace_example",
                                    ),
                                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        storage_policy_id="storage_policy_id_example",
                                        storage_policy_name="storage_policy_name_example",
                                        volume_path="volume_path_example",
                                    ),
                                )
                            ],
                        ),
                    ),
                    ttl_seconds_after_finished=1,
                ),
            ),
            schedule="schedule_example",
            starting_deadline_seconds=1,
            successful_jobs_history_limit=1,
            suspend=True,
            time_zone="time_zone_example",
        ),
        status=V1CronJobStatus(
            active=[
                V1ObjectReference(
                    api_version="api_version_example",
                    field_path="field_path_example",
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    resource_version="resource_version_example",
                    uid="uid_example",
                )
            ],
            last_schedule_time="1970-01-01T00:00:00.00Z",
            last_successful_time="1970-01-01T00:00:00.00Z",
        ),
    )
    try:
        api_response = api_instance.replace_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->replace_namespaced_cron_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1CronJob(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1CronJobSpec(
            concurrency_policy="concurrency_policy_example",
            failed_jobs_history_limit=1,
            job_template=V1JobTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1JobSpec(
                    active_deadline_seconds=1,
                    backoff_limit=1,
                    completion_mode="completion_mode_example",
                    completions=1,
                    manual_selector=True,
                    parallelism=1,
                    pod_failure_policy=V1PodFailurePolicy(
                        rules=[
                            V1PodFailurePolicyRule(
                                action="action_example",
                                on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                                    container_name="container_name_example",
                                    operator="operator_example",
                                    values=[
                                        1
                                    ],
                                ),
                                on_pod_conditions=[
                                    V1PodFailurePolicyOnPodConditionsPattern(
                                        status="status_example",
                                        type="type_example",
                                    )
                                ],
                            )
                        ],
                    ),
                    selector=V1LabelSelector(
                        match_expressions=[
                            V1LabelSelectorRequirement(
                                key="key_example",
                                operator="operator_example",
                                values=[
                                    "values_example"
                                ],
                            )
                        ],
                        match_labels=dict(
                            "key": "key_example",
                        ),
                    ),
                    suspend=True,
                    template=V1PodTemplateSpec(
                        metadata=V1ObjectMeta(),
                        spec=V1PodSpec(
                            active_deadline_seconds=1,
                            affinity=V1Affinity(
                                node_affinity=V1NodeAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1PreferredSchedulingTerm(
                                            preference=V1NodeSelectorTerm(
                                                match_expressions=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example"
                                                        ],
                                                    )
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement()
                                                ],
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                        node_selector_terms=[
                                            V1NodeSelectorTerm()
                                        ],
                                    ),
                                ),
                                pod_affinity=V1PodAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(),
                                                namespace_selector=V1LabelSelector(),
                                                namespaces=[
                                                    "namespaces_example"
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                                pod_anti_affinity=V1PodAntiAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm()
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                            ),
                            automount_service_account_token=True,
                            containers=[
                                V1Container(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
                                    env=[
                                        V1EnvVar(
                                            name="name_example",
                                            value="value_example",
                                            value_from=V1EnvVarSource(
                                                config_map_key_ref=V1ConfigMapKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                field_ref=V1ObjectFieldSelector(
                                                    api_version="api_version_example",
                                                    field_path="field_path_example",
                                                ),
                                                resource_field_ref=V1ResourceFieldSelector(
                                                    container_name="container_name_example",
                                                    divisor="divisor_example",
                                                    resource="resource_example",
                                                ),
                                                secret_key_ref=V1SecretKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                            ),
                                        )
                                    ],
                                    env_from=[
                                        V1EnvFromSource(
                                            config_map_ref=V1ConfigMapEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                            prefix="prefix_example",
                                            secret_ref=V1SecretEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                        )
                                    ],
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example"
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    )
                                                ],
                                                path="path_example",
                                                port=dict(),
                                                scheme="scheme_example",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port=dict(),
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort(
                                            container_port=1,
                                            host_ip="host_ip_example",
                                            host_port=1,
                                            name="name_example",
                                            protocol="protocol_example",
                                        )
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(
                                        limits=dict(
                                            "key": "key_example",
                                        ),
                                        requests=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example"
                                            ],
                                            drop=[
                                                "drop_example"
                                            ],
                                        ),
                                        privileged=True,
                                        proc_mount="proc_mount_example",
                                        read_only_root_filesystem=True,
                                        run_as_group=1,
                                        run_as_non_root=True,
                                        run_as_user=1,
                                        se_linux_options=V1SELinuxOptions(
                                            level="level_example",
                                            role="role_example",
                                            type="type_example",
                                            user="user_example",
                                        ),
                                        seccomp_profile=V1SeccompProfile(
                                            localhost_profile="localhost_profile_example",
                                            type="type_example",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        )
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        )
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            dns_config=V1PodDNSConfig(
                                nameservers=[
                                    "nameservers_example"
                                ],
                                options=[
                                    V1PodDNSConfigOption(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                searches=[
                                    "searches_example"
                                ],
                            ),
                            dns_policy="dns_policy_example",
                            enable_service_links=True,
                            ephemeral_containers=[
                                V1EphemeralContainer(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
,
,
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(),
                                    liveness_probe=V1Probe(),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort()
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(),
                                    security_context=V1SecurityContext(),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    target_container_name="target_container_name_example",
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
,
                                    volume_mounts=[
                                        V1VolumeMount()
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            host_aliases=[
                                V1HostAlias(
                                    hostnames=[
                                        "hostnames_example"
                                    ],
                                    ip="ip_example",
                                )
                            ],
                            host_ipc=True,
                            host_network=True,
                            host_pid=True,
                            host_users=True,
                            hostname="hostname_example",
                            image_pull_secrets=[
                                V1LocalObjectReference(
                                    name="name_example",
                                )
                            ],
                            init_containers=[
                                V1Container()
                            ],
                            node_name="node_name_example",
                            node_selector=dict(
                                "key": "key_example",
                            ),
                            os=V1PodOS(
                                name="name_example",
                            ),
                            overhead=dict(
                                "key": "key_example",
                            ),
                            preemption_policy="preemption_policy_example",
                            priority=1,
                            priority_class_name="priority_class_name_example",
                            readiness_gates=[
                                V1PodReadinessGate(
                                    condition_type="condition_type_example",
                                )
                            ],
                            restart_policy="restart_policy_example",
                            runtime_class_name="runtime_class_name_example",
                            scheduler_name="scheduler_name_example",
                            security_context=V1PodSecurityContext(
                                fs_group=1,
                                fs_group_change_policy="fs_group_change_policy_example",
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(),
                                seccomp_profile=V1SeccompProfile(),
                                supplemental_groups=[
                                    1
                                ],
                                sysctls=[
                                    V1Sysctl(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                windows_options=V1WindowsSecurityContextOptions(),
                            ),
                            service_account="service_account_example",
                            service_account_name="service_account_name_example",
                            set_hostname_as_fqdn=True,
                            share_process_namespace=True,
                            subdomain="subdomain_example",
                            termination_grace_period_seconds=1,
                            tolerations=[
                                V1Toleration(
                                    effect="effect_example",
                                    key="key_example",
                                    operator="operator_example",
                                    toleration_seconds=1,
                                    value="value_example",
                                )
                            ],
                            topology_spread_constraints=[
                                V1TopologySpreadConstraint(
                                    label_selector=V1LabelSelector(),
                                    match_label_keys=[
                                        "match_label_keys_example"
                                    ],
                                    max_skew=1,
                                    min_domains=1,
                                    node_affinity_policy="node_affinity_policy_example",
                                    node_taints_policy="node_taints_policy_example",
                                    topology_key="topology_key_example",
                                    when_unsatisfiable="when_unsatisfiable_example",
                                )
                            ],
                            volumes=[
                                V1Volume(
                                    aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    azure_disk=V1AzureDiskVolumeSource(
                                        caching_mode="caching_mode_example",
                                        disk_name="disk_name_example",
                                        disk_uri="disk_uri_example",
                                        fs_type="fs_type_example",
                                        kind="kind_example",
                                        read_only=True,
                                    ),
                                    azure_file=V1AzureFileVolumeSource(
                                        read_only=True,
                                        secret_name="secret_name_example",
                                        share_name="share_name_example",
                                    ),
                                    cephfs=V1CephFSVolumeSource(
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        path="path_example",
                                        read_only=True,
                                        secret_file="secret_file_example",
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    cinder=V1CinderVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_id="volume_id_example",
                                    ),
                                    config_map=V1ConfigMapVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            )
                                        ],
                                        name="name_example",
                                        optional=True,
                                    ),
                                    csi=V1CSIVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        node_publish_secret_ref=V1LocalObjectReference(),
                                        read_only=True,
                                        volume_attributes=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    downward_api=V1DownwardAPIVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1DownwardAPIVolumeFile(
                                                field_ref=V1ObjectFieldSelector(),
                                                mode=1,
                                                path="path_example",
                                                resource_field_ref=V1ResourceFieldSelector(),
                                            )
                                        ],
                                    ),
                                    empty_dir=V1EmptyDirVolumeSource(
                                        medium="medium_example",
                                        size_limit="size_limit_example",
                                    ),
                                    ephemeral=V1EphemeralVolumeSource(
                                        volume_claim_template=V1PersistentVolumeClaimTemplate(
                                            metadata=V1ObjectMeta(),
                                            spec=V1PersistentVolumeClaimSpec(
                                                access_modes=[
                                                    "access_modes_example"
                                                ],
                                                data_source=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
,
                                                resources=V1ResourceRequirements(),
                                                selector=V1LabelSelector(),
                                                storage_class_name="storage_class_name_example",
                                                volume_mode="volume_mode_example",
                                                volume_name="volume_name_example",
                                            ),
                                        ),
                                    ),
                                    fc=V1FCVolumeSource(
                                        fs_type="fs_type_example",
                                        lun=1,
                                        read_only=True,
                                        target_wwns=[
                                            "target_wwns_example"
                                        ],
                                        wwids=[
                                            "wwids_example"
                                        ],
                                    ),
                                    flex_volume=V1FlexVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        options=dict(
                                            "key": "key_example",
                                        ),
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                    ),
                                    flocker=V1FlockerVolumeSource(
                                        dataset_name="dataset_name_example",
                                        dataset_uuid="dataset_uuid_example",
                                    ),
                                    gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        pd_name="pd_name_example",
                                        read_only=True,
                                    ),
                                    git_repo=V1GitRepoVolumeSource(
                                        directory="directory_example",
                                        repository="repository_example",
                                        revision="revision_example",
                                    ),
                                    glusterfs=V1GlusterfsVolumeSource(
                                        endpoints="endpoints_example",
                                        path="path_example",
                                        read_only=True,
                                    ),
                                    host_path=V1HostPathVolumeSource(
                                        path="path_example",
                                        type="type_example",
                                    ),
                                    iscsi=V1ISCSIVolumeSource(
                                        chap_auth_discovery=True,
                                        chap_auth_session=True,
                                        fs_type="fs_type_example",
                                        initiator_name="initiator_name_example",
                                        iqn="iqn_example",
                                        iscsi_interface="iscsi_interface_example",
                                        lun=1,
                                        portals=[
                                            "portals_example"
                                        ],
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        target_portal="target_portal_example",
                                    ),
                                    name="name_example",
                                    nfs=V1NFSVolumeSource(
                                        path="path_example",
                                        read_only=True,
                                        server="server_example",
                                    ),
                                    persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                        claim_name="claim_name_example",
                                        read_only=True,
                                    ),
                                    photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        pd_id="pd_id_example",
                                    ),
                                    portworx_volume=V1PortworxVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    projected=V1ProjectedVolumeSource(
                                        default_mode=1,
                                        sources=[
                                            V1VolumeProjection(
                                                config_map=V1ConfigMapProjection(
,
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                downward_api=V1DownwardAPIProjection(
                                                    items=[
                                                        V1DownwardAPIVolumeFile()
                                                    ],
                                                ),
                                                secret=V1SecretProjection(
                                                    items=[
                                                        V1KeyToPath()
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                service_account_token=V1ServiceAccountTokenProjection(
                                                    audience="audience_example",
                                                    expiration_seconds=1,
                                                    path="path_example",
                                                ),
                                            )
                                        ],
                                    ),
                                    quobyte=V1QuobyteVolumeSource(
                                        group="group_example",
                                        read_only=True,
                                        registry="registry_example",
                                        tenant="tenant_example",
                                        user="user_example",
                                        volume="volume_example",
                                    ),
                                    rbd=V1RBDVolumeSource(
                                        fs_type="fs_type_example",
                                        image="image_example",
                                        keyring="keyring_example",
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        pool="pool_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    scale_io=V1ScaleIOVolumeSource(
                                        fs_type="fs_type_example",
                                        gateway="gateway_example",
                                        protection_domain="protection_domain_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        ssl_enabled=True,
                                        storage_mode="storage_mode_example",
                                        storage_pool="storage_pool_example",
                                        system="system_example",
                                        volume_name="volume_name_example",
                                    ),
                                    secret=V1SecretVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath()
                                        ],
                                        optional=True,
                                        secret_name="secret_name_example",
                                    ),
                                    storageos=V1StorageOSVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_name="volume_name_example",
                                        volume_namespace="volume_namespace_example",
                                    ),
                                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        storage_policy_id="storage_policy_id_example",
                                        storage_policy_name="storage_policy_name_example",
                                        volume_path="volume_path_example",
                                    ),
                                )
                            ],
                        ),
                    ),
                    ttl_seconds_after_finished=1,
                ),
            ),
            schedule="schedule_example",
            starting_deadline_seconds=1,
            successful_jobs_history_limit=1,
            suspend=True,
            time_zone="time_zone_example",
        ),
        status=V1CronJobStatus(
            active=[
                V1ObjectReference(
                    api_version="api_version_example",
                    field_path="field_path_example",
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    resource_version="resource_version_example",
                    uid="uid_example",
                )
            ],
            last_schedule_time="1970-01-01T00:00:00.00Z",
            last_successful_time="1970-01-01T00:00:00.00Z",
        ),
    )
    try:
        api_response = api_instance.replace_namespaced_cron_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->replace_namespaced_cron_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#replace_namespaced_cron_job.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_namespaced_cron_job.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_namespaced_cron_job.ApiResponseFor401) | Unauthorized

#### replace_namespaced_cron_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### replace_namespaced_cron_job.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### replace_namespaced_cron_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_namespaced_cron_job_status**
<a name="replace_namespaced_cron_job_status"></a>
> V1CronJob replace_namespaced_cron_job_status(namenamespacebody)



replace status of the specified CronJob

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_cron_job import V1CronJob
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = V1CronJob(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1CronJobSpec(
            concurrency_policy="concurrency_policy_example",
            failed_jobs_history_limit=1,
            job_template=V1JobTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1JobSpec(
                    active_deadline_seconds=1,
                    backoff_limit=1,
                    completion_mode="completion_mode_example",
                    completions=1,
                    manual_selector=True,
                    parallelism=1,
                    pod_failure_policy=V1PodFailurePolicy(
                        rules=[
                            V1PodFailurePolicyRule(
                                action="action_example",
                                on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                                    container_name="container_name_example",
                                    operator="operator_example",
                                    values=[
                                        1
                                    ],
                                ),
                                on_pod_conditions=[
                                    V1PodFailurePolicyOnPodConditionsPattern(
                                        status="status_example",
                                        type="type_example",
                                    )
                                ],
                            )
                        ],
                    ),
                    selector=V1LabelSelector(
                        match_expressions=[
                            V1LabelSelectorRequirement(
                                key="key_example",
                                operator="operator_example",
                                values=[
                                    "values_example"
                                ],
                            )
                        ],
                        match_labels=dict(
                            "key": "key_example",
                        ),
                    ),
                    suspend=True,
                    template=V1PodTemplateSpec(
                        metadata=V1ObjectMeta(),
                        spec=V1PodSpec(
                            active_deadline_seconds=1,
                            affinity=V1Affinity(
                                node_affinity=V1NodeAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1PreferredSchedulingTerm(
                                            preference=V1NodeSelectorTerm(
                                                match_expressions=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example"
                                                        ],
                                                    )
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement()
                                                ],
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                        node_selector_terms=[
                                            V1NodeSelectorTerm()
                                        ],
                                    ),
                                ),
                                pod_affinity=V1PodAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(),
                                                namespace_selector=V1LabelSelector(),
                                                namespaces=[
                                                    "namespaces_example"
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                                pod_anti_affinity=V1PodAntiAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm()
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                            ),
                            automount_service_account_token=True,
                            containers=[
                                V1Container(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
                                    env=[
                                        V1EnvVar(
                                            name="name_example",
                                            value="value_example",
                                            value_from=V1EnvVarSource(
                                                config_map_key_ref=V1ConfigMapKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                field_ref=V1ObjectFieldSelector(
                                                    api_version="api_version_example",
                                                    field_path="field_path_example",
                                                ),
                                                resource_field_ref=V1ResourceFieldSelector(
                                                    container_name="container_name_example",
                                                    divisor="divisor_example",
                                                    resource="resource_example",
                                                ),
                                                secret_key_ref=V1SecretKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                            ),
                                        )
                                    ],
                                    env_from=[
                                        V1EnvFromSource(
                                            config_map_ref=V1ConfigMapEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                            prefix="prefix_example",
                                            secret_ref=V1SecretEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                        )
                                    ],
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example"
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    )
                                                ],
                                                path="path_example",
                                                port=dict(),
                                                scheme="scheme_example",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port=dict(),
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort(
                                            container_port=1,
                                            host_ip="host_ip_example",
                                            host_port=1,
                                            name="name_example",
                                            protocol="protocol_example",
                                        )
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(
                                        limits=dict(
                                            "key": "key_example",
                                        ),
                                        requests=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example"
                                            ],
                                            drop=[
                                                "drop_example"
                                            ],
                                        ),
                                        privileged=True,
                                        proc_mount="proc_mount_example",
                                        read_only_root_filesystem=True,
                                        run_as_group=1,
                                        run_as_non_root=True,
                                        run_as_user=1,
                                        se_linux_options=V1SELinuxOptions(
                                            level="level_example",
                                            role="role_example",
                                            type="type_example",
                                            user="user_example",
                                        ),
                                        seccomp_profile=V1SeccompProfile(
                                            localhost_profile="localhost_profile_example",
                                            type="type_example",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        )
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        )
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            dns_config=V1PodDNSConfig(
                                nameservers=[
                                    "nameservers_example"
                                ],
                                options=[
                                    V1PodDNSConfigOption(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                searches=[
                                    "searches_example"
                                ],
                            ),
                            dns_policy="dns_policy_example",
                            enable_service_links=True,
                            ephemeral_containers=[
                                V1EphemeralContainer(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
,
,
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(),
                                    liveness_probe=V1Probe(),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort()
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(),
                                    security_context=V1SecurityContext(),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    target_container_name="target_container_name_example",
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
,
                                    volume_mounts=[
                                        V1VolumeMount()
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            host_aliases=[
                                V1HostAlias(
                                    hostnames=[
                                        "hostnames_example"
                                    ],
                                    ip="ip_example",
                                )
                            ],
                            host_ipc=True,
                            host_network=True,
                            host_pid=True,
                            host_users=True,
                            hostname="hostname_example",
                            image_pull_secrets=[
                                V1LocalObjectReference(
                                    name="name_example",
                                )
                            ],
                            init_containers=[
                                V1Container()
                            ],
                            node_name="node_name_example",
                            node_selector=dict(
                                "key": "key_example",
                            ),
                            os=V1PodOS(
                                name="name_example",
                            ),
                            overhead=dict(
                                "key": "key_example",
                            ),
                            preemption_policy="preemption_policy_example",
                            priority=1,
                            priority_class_name="priority_class_name_example",
                            readiness_gates=[
                                V1PodReadinessGate(
                                    condition_type="condition_type_example",
                                )
                            ],
                            restart_policy="restart_policy_example",
                            runtime_class_name="runtime_class_name_example",
                            scheduler_name="scheduler_name_example",
                            security_context=V1PodSecurityContext(
                                fs_group=1,
                                fs_group_change_policy="fs_group_change_policy_example",
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(),
                                seccomp_profile=V1SeccompProfile(),
                                supplemental_groups=[
                                    1
                                ],
                                sysctls=[
                                    V1Sysctl(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                windows_options=V1WindowsSecurityContextOptions(),
                            ),
                            service_account="service_account_example",
                            service_account_name="service_account_name_example",
                            set_hostname_as_fqdn=True,
                            share_process_namespace=True,
                            subdomain="subdomain_example",
                            termination_grace_period_seconds=1,
                            tolerations=[
                                V1Toleration(
                                    effect="effect_example",
                                    key="key_example",
                                    operator="operator_example",
                                    toleration_seconds=1,
                                    value="value_example",
                                )
                            ],
                            topology_spread_constraints=[
                                V1TopologySpreadConstraint(
                                    label_selector=V1LabelSelector(),
                                    match_label_keys=[
                                        "match_label_keys_example"
                                    ],
                                    max_skew=1,
                                    min_domains=1,
                                    node_affinity_policy="node_affinity_policy_example",
                                    node_taints_policy="node_taints_policy_example",
                                    topology_key="topology_key_example",
                                    when_unsatisfiable="when_unsatisfiable_example",
                                )
                            ],
                            volumes=[
                                V1Volume(
                                    aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    azure_disk=V1AzureDiskVolumeSource(
                                        caching_mode="caching_mode_example",
                                        disk_name="disk_name_example",
                                        disk_uri="disk_uri_example",
                                        fs_type="fs_type_example",
                                        kind="kind_example",
                                        read_only=True,
                                    ),
                                    azure_file=V1AzureFileVolumeSource(
                                        read_only=True,
                                        secret_name="secret_name_example",
                                        share_name="share_name_example",
                                    ),
                                    cephfs=V1CephFSVolumeSource(
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        path="path_example",
                                        read_only=True,
                                        secret_file="secret_file_example",
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    cinder=V1CinderVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_id="volume_id_example",
                                    ),
                                    config_map=V1ConfigMapVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            )
                                        ],
                                        name="name_example",
                                        optional=True,
                                    ),
                                    csi=V1CSIVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        node_publish_secret_ref=V1LocalObjectReference(),
                                        read_only=True,
                                        volume_attributes=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    downward_api=V1DownwardAPIVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1DownwardAPIVolumeFile(
                                                field_ref=V1ObjectFieldSelector(),
                                                mode=1,
                                                path="path_example",
                                                resource_field_ref=V1ResourceFieldSelector(),
                                            )
                                        ],
                                    ),
                                    empty_dir=V1EmptyDirVolumeSource(
                                        medium="medium_example",
                                        size_limit="size_limit_example",
                                    ),
                                    ephemeral=V1EphemeralVolumeSource(
                                        volume_claim_template=V1PersistentVolumeClaimTemplate(
                                            metadata=V1ObjectMeta(),
                                            spec=V1PersistentVolumeClaimSpec(
                                                access_modes=[
                                                    "access_modes_example"
                                                ],
                                                data_source=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
,
                                                resources=V1ResourceRequirements(),
                                                selector=V1LabelSelector(),
                                                storage_class_name="storage_class_name_example",
                                                volume_mode="volume_mode_example",
                                                volume_name="volume_name_example",
                                            ),
                                        ),
                                    ),
                                    fc=V1FCVolumeSource(
                                        fs_type="fs_type_example",
                                        lun=1,
                                        read_only=True,
                                        target_wwns=[
                                            "target_wwns_example"
                                        ],
                                        wwids=[
                                            "wwids_example"
                                        ],
                                    ),
                                    flex_volume=V1FlexVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        options=dict(
                                            "key": "key_example",
                                        ),
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                    ),
                                    flocker=V1FlockerVolumeSource(
                                        dataset_name="dataset_name_example",
                                        dataset_uuid="dataset_uuid_example",
                                    ),
                                    gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        pd_name="pd_name_example",
                                        read_only=True,
                                    ),
                                    git_repo=V1GitRepoVolumeSource(
                                        directory="directory_example",
                                        repository="repository_example",
                                        revision="revision_example",
                                    ),
                                    glusterfs=V1GlusterfsVolumeSource(
                                        endpoints="endpoints_example",
                                        path="path_example",
                                        read_only=True,
                                    ),
                                    host_path=V1HostPathVolumeSource(
                                        path="path_example",
                                        type="type_example",
                                    ),
                                    iscsi=V1ISCSIVolumeSource(
                                        chap_auth_discovery=True,
                                        chap_auth_session=True,
                                        fs_type="fs_type_example",
                                        initiator_name="initiator_name_example",
                                        iqn="iqn_example",
                                        iscsi_interface="iscsi_interface_example",
                                        lun=1,
                                        portals=[
                                            "portals_example"
                                        ],
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        target_portal="target_portal_example",
                                    ),
                                    name="name_example",
                                    nfs=V1NFSVolumeSource(
                                        path="path_example",
                                        read_only=True,
                                        server="server_example",
                                    ),
                                    persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                        claim_name="claim_name_example",
                                        read_only=True,
                                    ),
                                    photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        pd_id="pd_id_example",
                                    ),
                                    portworx_volume=V1PortworxVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    projected=V1ProjectedVolumeSource(
                                        default_mode=1,
                                        sources=[
                                            V1VolumeProjection(
                                                config_map=V1ConfigMapProjection(
,
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                downward_api=V1DownwardAPIProjection(
                                                    items=[
                                                        V1DownwardAPIVolumeFile()
                                                    ],
                                                ),
                                                secret=V1SecretProjection(
                                                    items=[
                                                        V1KeyToPath()
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                service_account_token=V1ServiceAccountTokenProjection(
                                                    audience="audience_example",
                                                    expiration_seconds=1,
                                                    path="path_example",
                                                ),
                                            )
                                        ],
                                    ),
                                    quobyte=V1QuobyteVolumeSource(
                                        group="group_example",
                                        read_only=True,
                                        registry="registry_example",
                                        tenant="tenant_example",
                                        user="user_example",
                                        volume="volume_example",
                                    ),
                                    rbd=V1RBDVolumeSource(
                                        fs_type="fs_type_example",
                                        image="image_example",
                                        keyring="keyring_example",
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        pool="pool_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    scale_io=V1ScaleIOVolumeSource(
                                        fs_type="fs_type_example",
                                        gateway="gateway_example",
                                        protection_domain="protection_domain_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        ssl_enabled=True,
                                        storage_mode="storage_mode_example",
                                        storage_pool="storage_pool_example",
                                        system="system_example",
                                        volume_name="volume_name_example",
                                    ),
                                    secret=V1SecretVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath()
                                        ],
                                        optional=True,
                                        secret_name="secret_name_example",
                                    ),
                                    storageos=V1StorageOSVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_name="volume_name_example",
                                        volume_namespace="volume_namespace_example",
                                    ),
                                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        storage_policy_id="storage_policy_id_example",
                                        storage_policy_name="storage_policy_name_example",
                                        volume_path="volume_path_example",
                                    ),
                                )
                            ],
                        ),
                    ),
                    ttl_seconds_after_finished=1,
                ),
            ),
            schedule="schedule_example",
            starting_deadline_seconds=1,
            successful_jobs_history_limit=1,
            suspend=True,
            time_zone="time_zone_example",
        ),
        status=V1CronJobStatus(
            active=[
                V1ObjectReference(
                    api_version="api_version_example",
                    field_path="field_path_example",
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    resource_version="resource_version_example",
                    uid="uid_example",
                )
            ],
            last_schedule_time="1970-01-01T00:00:00.00Z",
            last_successful_time="1970-01-01T00:00:00.00Z",
        ),
    )
    try:
        api_response = api_instance.replace_namespaced_cron_job_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->replace_namespaced_cron_job_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1CronJob(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1CronJobSpec(
            concurrency_policy="concurrency_policy_example",
            failed_jobs_history_limit=1,
            job_template=V1JobTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1JobSpec(
                    active_deadline_seconds=1,
                    backoff_limit=1,
                    completion_mode="completion_mode_example",
                    completions=1,
                    manual_selector=True,
                    parallelism=1,
                    pod_failure_policy=V1PodFailurePolicy(
                        rules=[
                            V1PodFailurePolicyRule(
                                action="action_example",
                                on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                                    container_name="container_name_example",
                                    operator="operator_example",
                                    values=[
                                        1
                                    ],
                                ),
                                on_pod_conditions=[
                                    V1PodFailurePolicyOnPodConditionsPattern(
                                        status="status_example",
                                        type="type_example",
                                    )
                                ],
                            )
                        ],
                    ),
                    selector=V1LabelSelector(
                        match_expressions=[
                            V1LabelSelectorRequirement(
                                key="key_example",
                                operator="operator_example",
                                values=[
                                    "values_example"
                                ],
                            )
                        ],
                        match_labels=dict(
                            "key": "key_example",
                        ),
                    ),
                    suspend=True,
                    template=V1PodTemplateSpec(
                        metadata=V1ObjectMeta(),
                        spec=V1PodSpec(
                            active_deadline_seconds=1,
                            affinity=V1Affinity(
                                node_affinity=V1NodeAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1PreferredSchedulingTerm(
                                            preference=V1NodeSelectorTerm(
                                                match_expressions=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example"
                                                        ],
                                                    )
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement()
                                                ],
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                        node_selector_terms=[
                                            V1NodeSelectorTerm()
                                        ],
                                    ),
                                ),
                                pod_affinity=V1PodAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(),
                                                namespace_selector=V1LabelSelector(),
                                                namespaces=[
                                                    "namespaces_example"
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        )
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                                pod_anti_affinity=V1PodAntiAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm()
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm()
                                    ],
                                ),
                            ),
                            automount_service_account_token=True,
                            containers=[
                                V1Container(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
                                    env=[
                                        V1EnvVar(
                                            name="name_example",
                                            value="value_example",
                                            value_from=V1EnvVarSource(
                                                config_map_key_ref=V1ConfigMapKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                field_ref=V1ObjectFieldSelector(
                                                    api_version="api_version_example",
                                                    field_path="field_path_example",
                                                ),
                                                resource_field_ref=V1ResourceFieldSelector(
                                                    container_name="container_name_example",
                                                    divisor="divisor_example",
                                                    resource="resource_example",
                                                ),
                                                secret_key_ref=V1SecretKeySelector(
                                                    key="key_example",
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                            ),
                                        )
                                    ],
                                    env_from=[
                                        V1EnvFromSource(
                                            config_map_ref=V1ConfigMapEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                            prefix="prefix_example",
                                            secret_ref=V1SecretEnvSource(
                                                name="name_example",
                                                optional=True,
                                            ),
                                        )
                                    ],
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example"
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    )
                                                ],
                                                path="path_example",
                                                port=dict(),
                                                scheme="scheme_example",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port=dict(),
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort(
                                            container_port=1,
                                            host_ip="host_ip_example",
                                            host_port=1,
                                            name="name_example",
                                            protocol="protocol_example",
                                        )
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(
                                        limits=dict(
                                            "key": "key_example",
                                        ),
                                        requests=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example"
                                            ],
                                            drop=[
                                                "drop_example"
                                            ],
                                        ),
                                        privileged=True,
                                        proc_mount="proc_mount_example",
                                        read_only_root_filesystem=True,
                                        run_as_group=1,
                                        run_as_non_root=True,
                                        run_as_user=1,
                                        se_linux_options=V1SELinuxOptions(
                                            level="level_example",
                                            role="role_example",
                                            type="type_example",
                                            user="user_example",
                                        ),
                                        seccomp_profile=V1SeccompProfile(
                                            localhost_profile="localhost_profile_example",
                                            type="type_example",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        )
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        )
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            dns_config=V1PodDNSConfig(
                                nameservers=[
                                    "nameservers_example"
                                ],
                                options=[
                                    V1PodDNSConfigOption(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                searches=[
                                    "searches_example"
                                ],
                            ),
                            dns_policy="dns_policy_example",
                            enable_service_links=True,
                            ephemeral_containers=[
                                V1EphemeralContainer(
                                    args=[
                                        "args_example"
                                    ],
                                    command=[
                                        "command_example"
                                    ],
,
,
                                    image="image_example",
                                    image_pull_policy="image_pull_policy_example",
                                    lifecycle=V1Lifecycle(),
                                    liveness_probe=V1Probe(),
                                    name="name_example",
                                    ports=[
                                        V1ContainerPort()
                                    ],
                                    readiness_probe=V1Probe(),
                                    resources=V1ResourceRequirements(),
                                    security_context=V1SecurityContext(),
                                    startup_probe=V1Probe(),
                                    stdin=True,
                                    stdin_once=True,
                                    target_container_name="target_container_name_example",
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="termination_message_policy_example",
                                    tty=True,
,
                                    volume_mounts=[
                                        V1VolumeMount()
                                    ],
                                    working_dir="working_dir_example",
                                )
                            ],
                            host_aliases=[
                                V1HostAlias(
                                    hostnames=[
                                        "hostnames_example"
                                    ],
                                    ip="ip_example",
                                )
                            ],
                            host_ipc=True,
                            host_network=True,
                            host_pid=True,
                            host_users=True,
                            hostname="hostname_example",
                            image_pull_secrets=[
                                V1LocalObjectReference(
                                    name="name_example",
                                )
                            ],
                            init_containers=[
                                V1Container()
                            ],
                            node_name="node_name_example",
                            node_selector=dict(
                                "key": "key_example",
                            ),
                            os=V1PodOS(
                                name="name_example",
                            ),
                            overhead=dict(
                                "key": "key_example",
                            ),
                            preemption_policy="preemption_policy_example",
                            priority=1,
                            priority_class_name="priority_class_name_example",
                            readiness_gates=[
                                V1PodReadinessGate(
                                    condition_type="condition_type_example",
                                )
                            ],
                            restart_policy="restart_policy_example",
                            runtime_class_name="runtime_class_name_example",
                            scheduler_name="scheduler_name_example",
                            security_context=V1PodSecurityContext(
                                fs_group=1,
                                fs_group_change_policy="fs_group_change_policy_example",
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(),
                                seccomp_profile=V1SeccompProfile(),
                                supplemental_groups=[
                                    1
                                ],
                                sysctls=[
                                    V1Sysctl(
                                        name="name_example",
                                        value="value_example",
                                    )
                                ],
                                windows_options=V1WindowsSecurityContextOptions(),
                            ),
                            service_account="service_account_example",
                            service_account_name="service_account_name_example",
                            set_hostname_as_fqdn=True,
                            share_process_namespace=True,
                            subdomain="subdomain_example",
                            termination_grace_period_seconds=1,
                            tolerations=[
                                V1Toleration(
                                    effect="effect_example",
                                    key="key_example",
                                    operator="operator_example",
                                    toleration_seconds=1,
                                    value="value_example",
                                )
                            ],
                            topology_spread_constraints=[
                                V1TopologySpreadConstraint(
                                    label_selector=V1LabelSelector(),
                                    match_label_keys=[
                                        "match_label_keys_example"
                                    ],
                                    max_skew=1,
                                    min_domains=1,
                                    node_affinity_policy="node_affinity_policy_example",
                                    node_taints_policy="node_taints_policy_example",
                                    topology_key="topology_key_example",
                                    when_unsatisfiable="when_unsatisfiable_example",
                                )
                            ],
                            volumes=[
                                V1Volume(
                                    aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    azure_disk=V1AzureDiskVolumeSource(
                                        caching_mode="caching_mode_example",
                                        disk_name="disk_name_example",
                                        disk_uri="disk_uri_example",
                                        fs_type="fs_type_example",
                                        kind="kind_example",
                                        read_only=True,
                                    ),
                                    azure_file=V1AzureFileVolumeSource(
                                        read_only=True,
                                        secret_name="secret_name_example",
                                        share_name="share_name_example",
                                    ),
                                    cephfs=V1CephFSVolumeSource(
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        path="path_example",
                                        read_only=True,
                                        secret_file="secret_file_example",
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    cinder=V1CinderVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_id="volume_id_example",
                                    ),
                                    config_map=V1ConfigMapVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            )
                                        ],
                                        name="name_example",
                                        optional=True,
                                    ),
                                    csi=V1CSIVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        node_publish_secret_ref=V1LocalObjectReference(),
                                        read_only=True,
                                        volume_attributes=dict(
                                            "key": "key_example",
                                        ),
                                    ),
                                    downward_api=V1DownwardAPIVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1DownwardAPIVolumeFile(
                                                field_ref=V1ObjectFieldSelector(),
                                                mode=1,
                                                path="path_example",
                                                resource_field_ref=V1ResourceFieldSelector(),
                                            )
                                        ],
                                    ),
                                    empty_dir=V1EmptyDirVolumeSource(
                                        medium="medium_example",
                                        size_limit="size_limit_example",
                                    ),
                                    ephemeral=V1EphemeralVolumeSource(
                                        volume_claim_template=V1PersistentVolumeClaimTemplate(
                                            metadata=V1ObjectMeta(),
                                            spec=V1PersistentVolumeClaimSpec(
                                                access_modes=[
                                                    "access_modes_example"
                                                ],
                                                data_source=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
,
                                                resources=V1ResourceRequirements(),
                                                selector=V1LabelSelector(),
                                                storage_class_name="storage_class_name_example",
                                                volume_mode="volume_mode_example",
                                                volume_name="volume_name_example",
                                            ),
                                        ),
                                    ),
                                    fc=V1FCVolumeSource(
                                        fs_type="fs_type_example",
                                        lun=1,
                                        read_only=True,
                                        target_wwns=[
                                            "target_wwns_example"
                                        ],
                                        wwids=[
                                            "wwids_example"
                                        ],
                                    ),
                                    flex_volume=V1FlexVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        options=dict(
                                            "key": "key_example",
                                        ),
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                    ),
                                    flocker=V1FlockerVolumeSource(
                                        dataset_name="dataset_name_example",
                                        dataset_uuid="dataset_uuid_example",
                                    ),
                                    gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        partition=1,
                                        pd_name="pd_name_example",
                                        read_only=True,
                                    ),
                                    git_repo=V1GitRepoVolumeSource(
                                        directory="directory_example",
                                        repository="repository_example",
                                        revision="revision_example",
                                    ),
                                    glusterfs=V1GlusterfsVolumeSource(
                                        endpoints="endpoints_example",
                                        path="path_example",
                                        read_only=True,
                                    ),
                                    host_path=V1HostPathVolumeSource(
                                        path="path_example",
                                        type="type_example",
                                    ),
                                    iscsi=V1ISCSIVolumeSource(
                                        chap_auth_discovery=True,
                                        chap_auth_session=True,
                                        fs_type="fs_type_example",
                                        initiator_name="initiator_name_example",
                                        iqn="iqn_example",
                                        iscsi_interface="iscsi_interface_example",
                                        lun=1,
                                        portals=[
                                            "portals_example"
                                        ],
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        target_portal="target_portal_example",
                                    ),
                                    name="name_example",
                                    nfs=V1NFSVolumeSource(
                                        path="path_example",
                                        read_only=True,
                                        server="server_example",
                                    ),
                                    persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                        claim_name="claim_name_example",
                                        read_only=True,
                                    ),
                                    photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        pd_id="pd_id_example",
                                    ),
                                    portworx_volume=V1PortworxVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        volume_id="volume_id_example",
                                    ),
                                    projected=V1ProjectedVolumeSource(
                                        default_mode=1,
                                        sources=[
                                            V1VolumeProjection(
                                                config_map=V1ConfigMapProjection(
,
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                downward_api=V1DownwardAPIProjection(
                                                    items=[
                                                        V1DownwardAPIVolumeFile()
                                                    ],
                                                ),
                                                secret=V1SecretProjection(
                                                    items=[
                                                        V1KeyToPath()
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                service_account_token=V1ServiceAccountTokenProjection(
                                                    audience="audience_example",
                                                    expiration_seconds=1,
                                                    path="path_example",
                                                ),
                                            )
                                        ],
                                    ),
                                    quobyte=V1QuobyteVolumeSource(
                                        group="group_example",
                                        read_only=True,
                                        registry="registry_example",
                                        tenant="tenant_example",
                                        user="user_example",
                                        volume="volume_example",
                                    ),
                                    rbd=V1RBDVolumeSource(
                                        fs_type="fs_type_example",
                                        image="image_example",
                                        keyring="keyring_example",
                                        monitors=[
                                            "monitors_example"
                                        ],
                                        pool="pool_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        user="user_example",
                                    ),
                                    scale_io=V1ScaleIOVolumeSource(
                                        fs_type="fs_type_example",
                                        gateway="gateway_example",
                                        protection_domain="protection_domain_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        ssl_enabled=True,
                                        storage_mode="storage_mode_example",
                                        storage_pool="storage_pool_example",
                                        system="system_example",
                                        volume_name="volume_name_example",
                                    ),
                                    secret=V1SecretVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath()
                                        ],
                                        optional=True,
                                        secret_name="secret_name_example",
                                    ),
                                    storageos=V1StorageOSVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(),
                                        volume_name="volume_name_example",
                                        volume_namespace="volume_namespace_example",
                                    ),
                                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        storage_policy_id="storage_policy_id_example",
                                        storage_policy_name="storage_policy_name_example",
                                        volume_path="volume_path_example",
                                    ),
                                )
                            ],
                        ),
                    ),
                    ttl_seconds_after_finished=1,
                ),
            ),
            schedule="schedule_example",
            starting_deadline_seconds=1,
            successful_jobs_history_limit=1,
            suspend=True,
            time_zone="time_zone_example",
        ),
        status=V1CronJobStatus(
            active=[
                V1ObjectReference(
                    api_version="api_version_example",
                    field_path="field_path_example",
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    resource_version="resource_version_example",
                    uid="uid_example",
                )
            ],
            last_schedule_time="1970-01-01T00:00:00.00Z",
            last_successful_time="1970-01-01T00:00:00.00Z",
        ),
    )
    try:
        api_response = api_instance.replace_namespaced_cron_job_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->replace_namespaced_cron_job_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#replace_namespaced_cron_job_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_namespaced_cron_job_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_namespaced_cron_job_status.ApiResponseFor401) | Unauthorized

#### replace_namespaced_cron_job_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### replace_namespaced_cron_job_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CronJob**](../../models/V1CronJob.md) |  | 


#### replace_namespaced_cron_job_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_namespaced_job**
<a name="replace_namespaced_job"></a>
> V1Job replace_namespaced_job(namenamespacebody)



replace the specified Job

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_job import V1Job
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = V1Job(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1JobSpec(
            active_deadline_seconds=1,
            backoff_limit=1,
            completion_mode="completion_mode_example",
            completions=1,
            manual_selector=True,
            parallelism=1,
            pod_failure_policy=V1PodFailurePolicy(
                rules=[
                    V1PodFailurePolicyRule(
                        action="action_example",
                        on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                            container_name="container_name_example",
                            operator="operator_example",
                            values=[
                                1
                            ],
                        ),
                        on_pod_conditions=[
                            V1PodFailurePolicyOnPodConditionsPattern(
                                status="status_example",
                                type="type_example",
                            )
                        ],
                    )
                ],
            ),
            selector=V1LabelSelector(
                match_expressions=[
                    V1LabelSelectorRequirement(
                        key="key_example",
                        operator="operator_example",
                        values=[
                            "values_example"
                        ],
                    )
                ],
                match_labels=dict(
                    "key": "key_example",
                ),
            ),
            suspend=True,
            template=V1PodTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1PodSpec(
                    active_deadline_seconds=1,
                    affinity=V1Affinity(
                        node_affinity=V1NodeAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1PreferredSchedulingTerm(
                                    preference=V1NodeSelectorTerm(
                                        match_expressions=[
                                            V1NodeSelectorRequirement(
                                                key="key_example",
                                                operator="operator_example",
                                                values=[
                                                    "values_example"
                                                ],
                                            )
                                        ],
                                        match_fields=[
                                            V1NodeSelectorRequirement()
                                        ],
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                node_selector_terms=[
                                    V1NodeSelectorTerm()
                                ],
                            ),
                        ),
                        pod_affinity=V1PodAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm(
                                    pod_affinity_term=V1PodAffinityTerm(
                                        label_selector=V1LabelSelector(),
                                        namespace_selector=V1LabelSelector(),
                                        namespaces=[
                                            "namespaces_example"
                                        ],
                                        topology_key="topology_key_example",
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                        pod_anti_affinity=V1PodAntiAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm()
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                    ),
                    automount_service_account_token=True,
                    containers=[
                        V1Container(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
                            env=[
                                V1EnvVar(
                                    name="name_example",
                                    value="value_example",
                                    value_from=V1EnvVarSource(
                                        config_map_key_ref=V1ConfigMapKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                        field_ref=V1ObjectFieldSelector(
                                            api_version="api_version_example",
                                            field_path="field_path_example",
                                        ),
                                        resource_field_ref=V1ResourceFieldSelector(
                                            container_name="container_name_example",
                                            divisor="divisor_example",
                                            resource="resource_example",
                                        ),
                                        secret_key_ref=V1SecretKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                    ),
                                )
                            ],
                            env_from=[
                                V1EnvFromSource(
                                    config_map_ref=V1ConfigMapEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                    prefix="prefix_example",
                                    secret_ref=V1SecretEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                )
                            ],
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(
                                post_start=V1LifecycleHandler(
                                    _exec=V1ExecAction(
                                        command=[
                                            "command_example"
                                        ],
                                    ),
                                    http_get=V1HTTPGetAction(
                                        host="host_example",
                                        http_headers=[
                                            V1HTTPHeader(
                                                name="name_example",
                                                value="value_example",
                                            )
                                        ],
                                        path="path_example",
                                        port=dict(),
                                        scheme="scheme_example",
                                    ),
                                    tcp_socket=V1TCPSocketAction(
                                        host="host_example",
                                        port=dict(),
                                    ),
                                ),
                                pre_stop=V1LifecycleHandler(),
                            ),
                            liveness_probe=V1Probe(
                                _exec=V1ExecAction(),
                                failure_threshold=1,
                                grpc=V1GRPCAction(
                                    port=1,
                                    service="service_example",
                                ),
                                http_get=V1HTTPGetAction(),
                                initial_delay_seconds=1,
                                period_seconds=1,
                                success_threshold=1,
                                tcp_socket=V1TCPSocketAction(),
                                termination_grace_period_seconds=1,
                                timeout_seconds=1,
                            ),
                            name="name_example",
                            ports=[
                                V1ContainerPort(
                                    container_port=1,
                                    host_ip="host_ip_example",
                                    host_port=1,
                                    name="name_example",
                                    protocol="protocol_example",
                                )
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(
                                limits=dict(
                                    "key": "key_example",
                                ),
                                requests=dict(
                                    "key": "key_example",
                                ),
                            ),
                            security_context=V1SecurityContext(
                                allow_privilege_escalation=True,
                                capabilities=V1Capabilities(
                                    add=[
                                        "add_example"
                                    ],
                                    drop=[
                                        "drop_example"
                                    ],
                                ),
                                privileged=True,
                                proc_mount="proc_mount_example",
                                read_only_root_filesystem=True,
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(
                                    level="level_example",
                                    role="role_example",
                                    type="type_example",
                                    user="user_example",
                                ),
                                seccomp_profile=V1SeccompProfile(
                                    localhost_profile="localhost_profile_example",
                                    type="type_example",
                                ),
                                windows_options=V1WindowsSecurityContextOptions(
                                    gmsa_credential_spec="gmsa_credential_spec_example",
                                    gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                    host_process=True,
                                    run_as_user_name="run_as_user_name_example",
                                ),
                            ),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
                            volume_devices=[
                                V1VolumeDevice(
                                    device_path="device_path_example",
                                    name="name_example",
                                )
                            ],
                            volume_mounts=[
                                V1VolumeMount(
                                    mount_path="mount_path_example",
                                    mount_propagation="mount_propagation_example",
                                    name="name_example",
                                    read_only=True,
                                    sub_path="sub_path_example",
                                    sub_path_expr="sub_path_expr_example",
                                )
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    dns_config=V1PodDNSConfig(
                        nameservers=[
                            "nameservers_example"
                        ],
                        options=[
                            V1PodDNSConfigOption(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        searches=[
                            "searches_example"
                        ],
                    ),
                    dns_policy="dns_policy_example",
                    enable_service_links=True,
                    ephemeral_containers=[
                        V1EphemeralContainer(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
,
,
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(),
                            liveness_probe=V1Probe(),
                            name="name_example",
                            ports=[
                                V1ContainerPort()
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(),
                            security_context=V1SecurityContext(),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            target_container_name="target_container_name_example",
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
,
                            volume_mounts=[
                                V1VolumeMount()
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    host_aliases=[
                        V1HostAlias(
                            hostnames=[
                                "hostnames_example"
                            ],
                            ip="ip_example",
                        )
                    ],
                    host_ipc=True,
                    host_network=True,
                    host_pid=True,
                    host_users=True,
                    hostname="hostname_example",
                    image_pull_secrets=[
                        V1LocalObjectReference(
                            name="name_example",
                        )
                    ],
                    init_containers=[
                        V1Container()
                    ],
                    node_name="node_name_example",
                    node_selector=dict(
                        "key": "key_example",
                    ),
                    os=V1PodOS(
                        name="name_example",
                    ),
                    overhead=dict(
                        "key": "key_example",
                    ),
                    preemption_policy="preemption_policy_example",
                    priority=1,
                    priority_class_name="priority_class_name_example",
                    readiness_gates=[
                        V1PodReadinessGate(
                            condition_type="condition_type_example",
                        )
                    ],
                    restart_policy="restart_policy_example",
                    runtime_class_name="runtime_class_name_example",
                    scheduler_name="scheduler_name_example",
                    security_context=V1PodSecurityContext(
                        fs_group=1,
                        fs_group_change_policy="fs_group_change_policy_example",
                        run_as_group=1,
                        run_as_non_root=True,
                        run_as_user=1,
                        se_linux_options=V1SELinuxOptions(),
                        seccomp_profile=V1SeccompProfile(),
                        supplemental_groups=[
                            1
                        ],
                        sysctls=[
                            V1Sysctl(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        windows_options=V1WindowsSecurityContextOptions(),
                    ),
                    service_account="service_account_example",
                    service_account_name="service_account_name_example",
                    set_hostname_as_fqdn=True,
                    share_process_namespace=True,
                    subdomain="subdomain_example",
                    termination_grace_period_seconds=1,
                    tolerations=[
                        V1Toleration(
                            effect="effect_example",
                            key="key_example",
                            operator="operator_example",
                            toleration_seconds=1,
                            value="value_example",
                        )
                    ],
                    topology_spread_constraints=[
                        V1TopologySpreadConstraint(
                            label_selector=V1LabelSelector(),
                            match_label_keys=[
                                "match_label_keys_example"
                            ],
                            max_skew=1,
                            min_domains=1,
                            node_affinity_policy="node_affinity_policy_example",
                            node_taints_policy="node_taints_policy_example",
                            topology_key="topology_key_example",
                            when_unsatisfiable="when_unsatisfiable_example",
                        )
                    ],
                    volumes=[
                        V1Volume(
                            aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            azure_disk=V1AzureDiskVolumeSource(
                                caching_mode="caching_mode_example",
                                disk_name="disk_name_example",
                                disk_uri="disk_uri_example",
                                fs_type="fs_type_example",
                                kind="kind_example",
                                read_only=True,
                            ),
                            azure_file=V1AzureFileVolumeSource(
                                read_only=True,
                                secret_name="secret_name_example",
                                share_name="share_name_example",
                            ),
                            cephfs=V1CephFSVolumeSource(
                                monitors=[
                                    "monitors_example"
                                ],
                                path="path_example",
                                read_only=True,
                                secret_file="secret_file_example",
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            cinder=V1CinderVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_id="volume_id_example",
                            ),
                            config_map=V1ConfigMapVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath(
                                        key="key_example",
                                        mode=1,
                                        path="path_example",
                                    )
                                ],
                                name="name_example",
                                optional=True,
                            ),
                            csi=V1CSIVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                node_publish_secret_ref=V1LocalObjectReference(),
                                read_only=True,
                                volume_attributes=dict(
                                    "key": "key_example",
                                ),
                            ),
                            downward_api=V1DownwardAPIVolumeSource(
                                default_mode=1,
                                items=[
                                    V1DownwardAPIVolumeFile(
                                        field_ref=V1ObjectFieldSelector(),
                                        mode=1,
                                        path="path_example",
                                        resource_field_ref=V1ResourceFieldSelector(),
                                    )
                                ],
                            ),
                            empty_dir=V1EmptyDirVolumeSource(
                                medium="medium_example",
                                size_limit="size_limit_example",
                            ),
                            ephemeral=V1EphemeralVolumeSource(
                                volume_claim_template=V1PersistentVolumeClaimTemplate(
                                    metadata=V1ObjectMeta(),
                                    spec=V1PersistentVolumeClaimSpec(
                                        access_modes=[
                                            "access_modes_example"
                                        ],
                                        data_source=V1TypedLocalObjectReference(
                                            api_group="api_group_example",
                                            kind="kind_example",
                                            name="name_example",
                                        ),
,
                                        resources=V1ResourceRequirements(),
                                        selector=V1LabelSelector(),
                                        storage_class_name="storage_class_name_example",
                                        volume_mode="volume_mode_example",
                                        volume_name="volume_name_example",
                                    ),
                                ),
                            ),
                            fc=V1FCVolumeSource(
                                fs_type="fs_type_example",
                                lun=1,
                                read_only=True,
                                target_wwns=[
                                    "target_wwns_example"
                                ],
                                wwids=[
                                    "wwids_example"
                                ],
                            ),
                            flex_volume=V1FlexVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                options=dict(
                                    "key": "key_example",
                                ),
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                            ),
                            flocker=V1FlockerVolumeSource(
                                dataset_name="dataset_name_example",
                                dataset_uuid="dataset_uuid_example",
                            ),
                            gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                pd_name="pd_name_example",
                                read_only=True,
                            ),
                            git_repo=V1GitRepoVolumeSource(
                                directory="directory_example",
                                repository="repository_example",
                                revision="revision_example",
                            ),
                            glusterfs=V1GlusterfsVolumeSource(
                                endpoints="endpoints_example",
                                path="path_example",
                                read_only=True,
                            ),
                            host_path=V1HostPathVolumeSource(
                                path="path_example",
                                type="type_example",
                            ),
                            iscsi=V1ISCSIVolumeSource(
                                chap_auth_discovery=True,
                                chap_auth_session=True,
                                fs_type="fs_type_example",
                                initiator_name="initiator_name_example",
                                iqn="iqn_example",
                                iscsi_interface="iscsi_interface_example",
                                lun=1,
                                portals=[
                                    "portals_example"
                                ],
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                target_portal="target_portal_example",
                            ),
                            name="name_example",
                            nfs=V1NFSVolumeSource(
                                path="path_example",
                                read_only=True,
                                server="server_example",
                            ),
                            persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                claim_name="claim_name_example",
                                read_only=True,
                            ),
                            photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                pd_id="pd_id_example",
                            ),
                            portworx_volume=V1PortworxVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            projected=V1ProjectedVolumeSource(
                                default_mode=1,
                                sources=[
                                    V1VolumeProjection(
                                        config_map=V1ConfigMapProjection(
,
                                            name="name_example",
                                            optional=True,
                                        ),
                                        downward_api=V1DownwardAPIProjection(
                                            items=[
                                                V1DownwardAPIVolumeFile()
                                            ],
                                        ),
                                        secret=V1SecretProjection(
                                            items=[
                                                V1KeyToPath()
                                            ],
                                            name="name_example",
                                            optional=True,
                                        ),
                                        service_account_token=V1ServiceAccountTokenProjection(
                                            audience="audience_example",
                                            expiration_seconds=1,
                                            path="path_example",
                                        ),
                                    )
                                ],
                            ),
                            quobyte=V1QuobyteVolumeSource(
                                group="group_example",
                                read_only=True,
                                registry="registry_example",
                                tenant="tenant_example",
                                user="user_example",
                                volume="volume_example",
                            ),
                            rbd=V1RBDVolumeSource(
                                fs_type="fs_type_example",
                                image="image_example",
                                keyring="keyring_example",
                                monitors=[
                                    "monitors_example"
                                ],
                                pool="pool_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            scale_io=V1ScaleIOVolumeSource(
                                fs_type="fs_type_example",
                                gateway="gateway_example",
                                protection_domain="protection_domain_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                ssl_enabled=True,
                                storage_mode="storage_mode_example",
                                storage_pool="storage_pool_example",
                                system="system_example",
                                volume_name="volume_name_example",
                            ),
                            secret=V1SecretVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath()
                                ],
                                optional=True,
                                secret_name="secret_name_example",
                            ),
                            storageos=V1StorageOSVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_name="volume_name_example",
                                volume_namespace="volume_namespace_example",
                            ),
                            vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                fs_type="fs_type_example",
                                storage_policy_id="storage_policy_id_example",
                                storage_policy_name="storage_policy_name_example",
                                volume_path="volume_path_example",
                            ),
                        )
                    ],
                ),
            ),
            ttl_seconds_after_finished=1,
        ),
        status=V1JobStatus(
            active=1,
            completed_indexes="completed_indexes_example",
            completion_time="1970-01-01T00:00:00.00Z",
            conditions=[
                V1JobCondition(
                    last_probe_time="1970-01-01T00:00:00.00Z",
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            failed=1,
            ready=1,
            start_time="1970-01-01T00:00:00.00Z",
            succeeded=1,
            uncounted_terminated_pods=V1UncountedTerminatedPods(
                failed=[
                    "failed_example"
                ],
                succeeded=[
                    "succeeded_example"
                ],
            ),
        ),
    )
    try:
        api_response = api_instance.replace_namespaced_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->replace_namespaced_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1Job(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1JobSpec(
            active_deadline_seconds=1,
            backoff_limit=1,
            completion_mode="completion_mode_example",
            completions=1,
            manual_selector=True,
            parallelism=1,
            pod_failure_policy=V1PodFailurePolicy(
                rules=[
                    V1PodFailurePolicyRule(
                        action="action_example",
                        on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                            container_name="container_name_example",
                            operator="operator_example",
                            values=[
                                1
                            ],
                        ),
                        on_pod_conditions=[
                            V1PodFailurePolicyOnPodConditionsPattern(
                                status="status_example",
                                type="type_example",
                            )
                        ],
                    )
                ],
            ),
            selector=V1LabelSelector(
                match_expressions=[
                    V1LabelSelectorRequirement(
                        key="key_example",
                        operator="operator_example",
                        values=[
                            "values_example"
                        ],
                    )
                ],
                match_labels=dict(
                    "key": "key_example",
                ),
            ),
            suspend=True,
            template=V1PodTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1PodSpec(
                    active_deadline_seconds=1,
                    affinity=V1Affinity(
                        node_affinity=V1NodeAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1PreferredSchedulingTerm(
                                    preference=V1NodeSelectorTerm(
                                        match_expressions=[
                                            V1NodeSelectorRequirement(
                                                key="key_example",
                                                operator="operator_example",
                                                values=[
                                                    "values_example"
                                                ],
                                            )
                                        ],
                                        match_fields=[
                                            V1NodeSelectorRequirement()
                                        ],
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                node_selector_terms=[
                                    V1NodeSelectorTerm()
                                ],
                            ),
                        ),
                        pod_affinity=V1PodAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm(
                                    pod_affinity_term=V1PodAffinityTerm(
                                        label_selector=V1LabelSelector(),
                                        namespace_selector=V1LabelSelector(),
                                        namespaces=[
                                            "namespaces_example"
                                        ],
                                        topology_key="topology_key_example",
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                        pod_anti_affinity=V1PodAntiAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm()
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                    ),
                    automount_service_account_token=True,
                    containers=[
                        V1Container(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
                            env=[
                                V1EnvVar(
                                    name="name_example",
                                    value="value_example",
                                    value_from=V1EnvVarSource(
                                        config_map_key_ref=V1ConfigMapKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                        field_ref=V1ObjectFieldSelector(
                                            api_version="api_version_example",
                                            field_path="field_path_example",
                                        ),
                                        resource_field_ref=V1ResourceFieldSelector(
                                            container_name="container_name_example",
                                            divisor="divisor_example",
                                            resource="resource_example",
                                        ),
                                        secret_key_ref=V1SecretKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                    ),
                                )
                            ],
                            env_from=[
                                V1EnvFromSource(
                                    config_map_ref=V1ConfigMapEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                    prefix="prefix_example",
                                    secret_ref=V1SecretEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                )
                            ],
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(
                                post_start=V1LifecycleHandler(
                                    _exec=V1ExecAction(
                                        command=[
                                            "command_example"
                                        ],
                                    ),
                                    http_get=V1HTTPGetAction(
                                        host="host_example",
                                        http_headers=[
                                            V1HTTPHeader(
                                                name="name_example",
                                                value="value_example",
                                            )
                                        ],
                                        path="path_example",
                                        port=dict(),
                                        scheme="scheme_example",
                                    ),
                                    tcp_socket=V1TCPSocketAction(
                                        host="host_example",
                                        port=dict(),
                                    ),
                                ),
                                pre_stop=V1LifecycleHandler(),
                            ),
                            liveness_probe=V1Probe(
                                _exec=V1ExecAction(),
                                failure_threshold=1,
                                grpc=V1GRPCAction(
                                    port=1,
                                    service="service_example",
                                ),
                                http_get=V1HTTPGetAction(),
                                initial_delay_seconds=1,
                                period_seconds=1,
                                success_threshold=1,
                                tcp_socket=V1TCPSocketAction(),
                                termination_grace_period_seconds=1,
                                timeout_seconds=1,
                            ),
                            name="name_example",
                            ports=[
                                V1ContainerPort(
                                    container_port=1,
                                    host_ip="host_ip_example",
                                    host_port=1,
                                    name="name_example",
                                    protocol="protocol_example",
                                )
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(
                                limits=dict(
                                    "key": "key_example",
                                ),
                                requests=dict(
                                    "key": "key_example",
                                ),
                            ),
                            security_context=V1SecurityContext(
                                allow_privilege_escalation=True,
                                capabilities=V1Capabilities(
                                    add=[
                                        "add_example"
                                    ],
                                    drop=[
                                        "drop_example"
                                    ],
                                ),
                                privileged=True,
                                proc_mount="proc_mount_example",
                                read_only_root_filesystem=True,
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(
                                    level="level_example",
                                    role="role_example",
                                    type="type_example",
                                    user="user_example",
                                ),
                                seccomp_profile=V1SeccompProfile(
                                    localhost_profile="localhost_profile_example",
                                    type="type_example",
                                ),
                                windows_options=V1WindowsSecurityContextOptions(
                                    gmsa_credential_spec="gmsa_credential_spec_example",
                                    gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                    host_process=True,
                                    run_as_user_name="run_as_user_name_example",
                                ),
                            ),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
                            volume_devices=[
                                V1VolumeDevice(
                                    device_path="device_path_example",
                                    name="name_example",
                                )
                            ],
                            volume_mounts=[
                                V1VolumeMount(
                                    mount_path="mount_path_example",
                                    mount_propagation="mount_propagation_example",
                                    name="name_example",
                                    read_only=True,
                                    sub_path="sub_path_example",
                                    sub_path_expr="sub_path_expr_example",
                                )
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    dns_config=V1PodDNSConfig(
                        nameservers=[
                            "nameservers_example"
                        ],
                        options=[
                            V1PodDNSConfigOption(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        searches=[
                            "searches_example"
                        ],
                    ),
                    dns_policy="dns_policy_example",
                    enable_service_links=True,
                    ephemeral_containers=[
                        V1EphemeralContainer(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
,
,
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(),
                            liveness_probe=V1Probe(),
                            name="name_example",
                            ports=[
                                V1ContainerPort()
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(),
                            security_context=V1SecurityContext(),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            target_container_name="target_container_name_example",
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
,
                            volume_mounts=[
                                V1VolumeMount()
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    host_aliases=[
                        V1HostAlias(
                            hostnames=[
                                "hostnames_example"
                            ],
                            ip="ip_example",
                        )
                    ],
                    host_ipc=True,
                    host_network=True,
                    host_pid=True,
                    host_users=True,
                    hostname="hostname_example",
                    image_pull_secrets=[
                        V1LocalObjectReference(
                            name="name_example",
                        )
                    ],
                    init_containers=[
                        V1Container()
                    ],
                    node_name="node_name_example",
                    node_selector=dict(
                        "key": "key_example",
                    ),
                    os=V1PodOS(
                        name="name_example",
                    ),
                    overhead=dict(
                        "key": "key_example",
                    ),
                    preemption_policy="preemption_policy_example",
                    priority=1,
                    priority_class_name="priority_class_name_example",
                    readiness_gates=[
                        V1PodReadinessGate(
                            condition_type="condition_type_example",
                        )
                    ],
                    restart_policy="restart_policy_example",
                    runtime_class_name="runtime_class_name_example",
                    scheduler_name="scheduler_name_example",
                    security_context=V1PodSecurityContext(
                        fs_group=1,
                        fs_group_change_policy="fs_group_change_policy_example",
                        run_as_group=1,
                        run_as_non_root=True,
                        run_as_user=1,
                        se_linux_options=V1SELinuxOptions(),
                        seccomp_profile=V1SeccompProfile(),
                        supplemental_groups=[
                            1
                        ],
                        sysctls=[
                            V1Sysctl(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        windows_options=V1WindowsSecurityContextOptions(),
                    ),
                    service_account="service_account_example",
                    service_account_name="service_account_name_example",
                    set_hostname_as_fqdn=True,
                    share_process_namespace=True,
                    subdomain="subdomain_example",
                    termination_grace_period_seconds=1,
                    tolerations=[
                        V1Toleration(
                            effect="effect_example",
                            key="key_example",
                            operator="operator_example",
                            toleration_seconds=1,
                            value="value_example",
                        )
                    ],
                    topology_spread_constraints=[
                        V1TopologySpreadConstraint(
                            label_selector=V1LabelSelector(),
                            match_label_keys=[
                                "match_label_keys_example"
                            ],
                            max_skew=1,
                            min_domains=1,
                            node_affinity_policy="node_affinity_policy_example",
                            node_taints_policy="node_taints_policy_example",
                            topology_key="topology_key_example",
                            when_unsatisfiable="when_unsatisfiable_example",
                        )
                    ],
                    volumes=[
                        V1Volume(
                            aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            azure_disk=V1AzureDiskVolumeSource(
                                caching_mode="caching_mode_example",
                                disk_name="disk_name_example",
                                disk_uri="disk_uri_example",
                                fs_type="fs_type_example",
                                kind="kind_example",
                                read_only=True,
                            ),
                            azure_file=V1AzureFileVolumeSource(
                                read_only=True,
                                secret_name="secret_name_example",
                                share_name="share_name_example",
                            ),
                            cephfs=V1CephFSVolumeSource(
                                monitors=[
                                    "monitors_example"
                                ],
                                path="path_example",
                                read_only=True,
                                secret_file="secret_file_example",
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            cinder=V1CinderVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_id="volume_id_example",
                            ),
                            config_map=V1ConfigMapVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath(
                                        key="key_example",
                                        mode=1,
                                        path="path_example",
                                    )
                                ],
                                name="name_example",
                                optional=True,
                            ),
                            csi=V1CSIVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                node_publish_secret_ref=V1LocalObjectReference(),
                                read_only=True,
                                volume_attributes=dict(
                                    "key": "key_example",
                                ),
                            ),
                            downward_api=V1DownwardAPIVolumeSource(
                                default_mode=1,
                                items=[
                                    V1DownwardAPIVolumeFile(
                                        field_ref=V1ObjectFieldSelector(),
                                        mode=1,
                                        path="path_example",
                                        resource_field_ref=V1ResourceFieldSelector(),
                                    )
                                ],
                            ),
                            empty_dir=V1EmptyDirVolumeSource(
                                medium="medium_example",
                                size_limit="size_limit_example",
                            ),
                            ephemeral=V1EphemeralVolumeSource(
                                volume_claim_template=V1PersistentVolumeClaimTemplate(
                                    metadata=V1ObjectMeta(),
                                    spec=V1PersistentVolumeClaimSpec(
                                        access_modes=[
                                            "access_modes_example"
                                        ],
                                        data_source=V1TypedLocalObjectReference(
                                            api_group="api_group_example",
                                            kind="kind_example",
                                            name="name_example",
                                        ),
,
                                        resources=V1ResourceRequirements(),
                                        selector=V1LabelSelector(),
                                        storage_class_name="storage_class_name_example",
                                        volume_mode="volume_mode_example",
                                        volume_name="volume_name_example",
                                    ),
                                ),
                            ),
                            fc=V1FCVolumeSource(
                                fs_type="fs_type_example",
                                lun=1,
                                read_only=True,
                                target_wwns=[
                                    "target_wwns_example"
                                ],
                                wwids=[
                                    "wwids_example"
                                ],
                            ),
                            flex_volume=V1FlexVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                options=dict(
                                    "key": "key_example",
                                ),
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                            ),
                            flocker=V1FlockerVolumeSource(
                                dataset_name="dataset_name_example",
                                dataset_uuid="dataset_uuid_example",
                            ),
                            gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                pd_name="pd_name_example",
                                read_only=True,
                            ),
                            git_repo=V1GitRepoVolumeSource(
                                directory="directory_example",
                                repository="repository_example",
                                revision="revision_example",
                            ),
                            glusterfs=V1GlusterfsVolumeSource(
                                endpoints="endpoints_example",
                                path="path_example",
                                read_only=True,
                            ),
                            host_path=V1HostPathVolumeSource(
                                path="path_example",
                                type="type_example",
                            ),
                            iscsi=V1ISCSIVolumeSource(
                                chap_auth_discovery=True,
                                chap_auth_session=True,
                                fs_type="fs_type_example",
                                initiator_name="initiator_name_example",
                                iqn="iqn_example",
                                iscsi_interface="iscsi_interface_example",
                                lun=1,
                                portals=[
                                    "portals_example"
                                ],
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                target_portal="target_portal_example",
                            ),
                            name="name_example",
                            nfs=V1NFSVolumeSource(
                                path="path_example",
                                read_only=True,
                                server="server_example",
                            ),
                            persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                claim_name="claim_name_example",
                                read_only=True,
                            ),
                            photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                pd_id="pd_id_example",
                            ),
                            portworx_volume=V1PortworxVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            projected=V1ProjectedVolumeSource(
                                default_mode=1,
                                sources=[
                                    V1VolumeProjection(
                                        config_map=V1ConfigMapProjection(
,
                                            name="name_example",
                                            optional=True,
                                        ),
                                        downward_api=V1DownwardAPIProjection(
                                            items=[
                                                V1DownwardAPIVolumeFile()
                                            ],
                                        ),
                                        secret=V1SecretProjection(
                                            items=[
                                                V1KeyToPath()
                                            ],
                                            name="name_example",
                                            optional=True,
                                        ),
                                        service_account_token=V1ServiceAccountTokenProjection(
                                            audience="audience_example",
                                            expiration_seconds=1,
                                            path="path_example",
                                        ),
                                    )
                                ],
                            ),
                            quobyte=V1QuobyteVolumeSource(
                                group="group_example",
                                read_only=True,
                                registry="registry_example",
                                tenant="tenant_example",
                                user="user_example",
                                volume="volume_example",
                            ),
                            rbd=V1RBDVolumeSource(
                                fs_type="fs_type_example",
                                image="image_example",
                                keyring="keyring_example",
                                monitors=[
                                    "monitors_example"
                                ],
                                pool="pool_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            scale_io=V1ScaleIOVolumeSource(
                                fs_type="fs_type_example",
                                gateway="gateway_example",
                                protection_domain="protection_domain_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                ssl_enabled=True,
                                storage_mode="storage_mode_example",
                                storage_pool="storage_pool_example",
                                system="system_example",
                                volume_name="volume_name_example",
                            ),
                            secret=V1SecretVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath()
                                ],
                                optional=True,
                                secret_name="secret_name_example",
                            ),
                            storageos=V1StorageOSVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_name="volume_name_example",
                                volume_namespace="volume_namespace_example",
                            ),
                            vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                fs_type="fs_type_example",
                                storage_policy_id="storage_policy_id_example",
                                storage_policy_name="storage_policy_name_example",
                                volume_path="volume_path_example",
                            ),
                        )
                    ],
                ),
            ),
            ttl_seconds_after_finished=1,
        ),
        status=V1JobStatus(
            active=1,
            completed_indexes="completed_indexes_example",
            completion_time="1970-01-01T00:00:00.00Z",
            conditions=[
                V1JobCondition(
                    last_probe_time="1970-01-01T00:00:00.00Z",
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            failed=1,
            ready=1,
            start_time="1970-01-01T00:00:00.00Z",
            succeeded=1,
            uncounted_terminated_pods=V1UncountedTerminatedPods(
                failed=[
                    "failed_example"
                ],
                succeeded=[
                    "succeeded_example"
                ],
            ),
        ),
    )
    try:
        api_response = api_instance.replace_namespaced_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->replace_namespaced_job: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#replace_namespaced_job.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_namespaced_job.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_namespaced_job.ApiResponseFor401) | Unauthorized

#### replace_namespaced_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### replace_namespaced_job.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### replace_namespaced_job.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_namespaced_job_status**
<a name="replace_namespaced_job_status"></a>
> V1Job replace_namespaced_job_status(namenamespacebody)



replace status of the specified Job

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import batch_v1_api
from kubernetes.client.model.v1_job import V1Job
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes.client.Configuration(
    host = "http://localhost"
)

# The kubernetes.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batch_v1_api.BatchV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = V1Job(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1JobSpec(
            active_deadline_seconds=1,
            backoff_limit=1,
            completion_mode="completion_mode_example",
            completions=1,
            manual_selector=True,
            parallelism=1,
            pod_failure_policy=V1PodFailurePolicy(
                rules=[
                    V1PodFailurePolicyRule(
                        action="action_example",
                        on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                            container_name="container_name_example",
                            operator="operator_example",
                            values=[
                                1
                            ],
                        ),
                        on_pod_conditions=[
                            V1PodFailurePolicyOnPodConditionsPattern(
                                status="status_example",
                                type="type_example",
                            )
                        ],
                    )
                ],
            ),
            selector=V1LabelSelector(
                match_expressions=[
                    V1LabelSelectorRequirement(
                        key="key_example",
                        operator="operator_example",
                        values=[
                            "values_example"
                        ],
                    )
                ],
                match_labels=dict(
                    "key": "key_example",
                ),
            ),
            suspend=True,
            template=V1PodTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1PodSpec(
                    active_deadline_seconds=1,
                    affinity=V1Affinity(
                        node_affinity=V1NodeAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1PreferredSchedulingTerm(
                                    preference=V1NodeSelectorTerm(
                                        match_expressions=[
                                            V1NodeSelectorRequirement(
                                                key="key_example",
                                                operator="operator_example",
                                                values=[
                                                    "values_example"
                                                ],
                                            )
                                        ],
                                        match_fields=[
                                            V1NodeSelectorRequirement()
                                        ],
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                node_selector_terms=[
                                    V1NodeSelectorTerm()
                                ],
                            ),
                        ),
                        pod_affinity=V1PodAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm(
                                    pod_affinity_term=V1PodAffinityTerm(
                                        label_selector=V1LabelSelector(),
                                        namespace_selector=V1LabelSelector(),
                                        namespaces=[
                                            "namespaces_example"
                                        ],
                                        topology_key="topology_key_example",
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                        pod_anti_affinity=V1PodAntiAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm()
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                    ),
                    automount_service_account_token=True,
                    containers=[
                        V1Container(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
                            env=[
                                V1EnvVar(
                                    name="name_example",
                                    value="value_example",
                                    value_from=V1EnvVarSource(
                                        config_map_key_ref=V1ConfigMapKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                        field_ref=V1ObjectFieldSelector(
                                            api_version="api_version_example",
                                            field_path="field_path_example",
                                        ),
                                        resource_field_ref=V1ResourceFieldSelector(
                                            container_name="container_name_example",
                                            divisor="divisor_example",
                                            resource="resource_example",
                                        ),
                                        secret_key_ref=V1SecretKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                    ),
                                )
                            ],
                            env_from=[
                                V1EnvFromSource(
                                    config_map_ref=V1ConfigMapEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                    prefix="prefix_example",
                                    secret_ref=V1SecretEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                )
                            ],
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(
                                post_start=V1LifecycleHandler(
                                    _exec=V1ExecAction(
                                        command=[
                                            "command_example"
                                        ],
                                    ),
                                    http_get=V1HTTPGetAction(
                                        host="host_example",
                                        http_headers=[
                                            V1HTTPHeader(
                                                name="name_example",
                                                value="value_example",
                                            )
                                        ],
                                        path="path_example",
                                        port=dict(),
                                        scheme="scheme_example",
                                    ),
                                    tcp_socket=V1TCPSocketAction(
                                        host="host_example",
                                        port=dict(),
                                    ),
                                ),
                                pre_stop=V1LifecycleHandler(),
                            ),
                            liveness_probe=V1Probe(
                                _exec=V1ExecAction(),
                                failure_threshold=1,
                                grpc=V1GRPCAction(
                                    port=1,
                                    service="service_example",
                                ),
                                http_get=V1HTTPGetAction(),
                                initial_delay_seconds=1,
                                period_seconds=1,
                                success_threshold=1,
                                tcp_socket=V1TCPSocketAction(),
                                termination_grace_period_seconds=1,
                                timeout_seconds=1,
                            ),
                            name="name_example",
                            ports=[
                                V1ContainerPort(
                                    container_port=1,
                                    host_ip="host_ip_example",
                                    host_port=1,
                                    name="name_example",
                                    protocol="protocol_example",
                                )
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(
                                limits=dict(
                                    "key": "key_example",
                                ),
                                requests=dict(
                                    "key": "key_example",
                                ),
                            ),
                            security_context=V1SecurityContext(
                                allow_privilege_escalation=True,
                                capabilities=V1Capabilities(
                                    add=[
                                        "add_example"
                                    ],
                                    drop=[
                                        "drop_example"
                                    ],
                                ),
                                privileged=True,
                                proc_mount="proc_mount_example",
                                read_only_root_filesystem=True,
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(
                                    level="level_example",
                                    role="role_example",
                                    type="type_example",
                                    user="user_example",
                                ),
                                seccomp_profile=V1SeccompProfile(
                                    localhost_profile="localhost_profile_example",
                                    type="type_example",
                                ),
                                windows_options=V1WindowsSecurityContextOptions(
                                    gmsa_credential_spec="gmsa_credential_spec_example",
                                    gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                    host_process=True,
                                    run_as_user_name="run_as_user_name_example",
                                ),
                            ),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
                            volume_devices=[
                                V1VolumeDevice(
                                    device_path="device_path_example",
                                    name="name_example",
                                )
                            ],
                            volume_mounts=[
                                V1VolumeMount(
                                    mount_path="mount_path_example",
                                    mount_propagation="mount_propagation_example",
                                    name="name_example",
                                    read_only=True,
                                    sub_path="sub_path_example",
                                    sub_path_expr="sub_path_expr_example",
                                )
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    dns_config=V1PodDNSConfig(
                        nameservers=[
                            "nameservers_example"
                        ],
                        options=[
                            V1PodDNSConfigOption(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        searches=[
                            "searches_example"
                        ],
                    ),
                    dns_policy="dns_policy_example",
                    enable_service_links=True,
                    ephemeral_containers=[
                        V1EphemeralContainer(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
,
,
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(),
                            liveness_probe=V1Probe(),
                            name="name_example",
                            ports=[
                                V1ContainerPort()
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(),
                            security_context=V1SecurityContext(),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            target_container_name="target_container_name_example",
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
,
                            volume_mounts=[
                                V1VolumeMount()
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    host_aliases=[
                        V1HostAlias(
                            hostnames=[
                                "hostnames_example"
                            ],
                            ip="ip_example",
                        )
                    ],
                    host_ipc=True,
                    host_network=True,
                    host_pid=True,
                    host_users=True,
                    hostname="hostname_example",
                    image_pull_secrets=[
                        V1LocalObjectReference(
                            name="name_example",
                        )
                    ],
                    init_containers=[
                        V1Container()
                    ],
                    node_name="node_name_example",
                    node_selector=dict(
                        "key": "key_example",
                    ),
                    os=V1PodOS(
                        name="name_example",
                    ),
                    overhead=dict(
                        "key": "key_example",
                    ),
                    preemption_policy="preemption_policy_example",
                    priority=1,
                    priority_class_name="priority_class_name_example",
                    readiness_gates=[
                        V1PodReadinessGate(
                            condition_type="condition_type_example",
                        )
                    ],
                    restart_policy="restart_policy_example",
                    runtime_class_name="runtime_class_name_example",
                    scheduler_name="scheduler_name_example",
                    security_context=V1PodSecurityContext(
                        fs_group=1,
                        fs_group_change_policy="fs_group_change_policy_example",
                        run_as_group=1,
                        run_as_non_root=True,
                        run_as_user=1,
                        se_linux_options=V1SELinuxOptions(),
                        seccomp_profile=V1SeccompProfile(),
                        supplemental_groups=[
                            1
                        ],
                        sysctls=[
                            V1Sysctl(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        windows_options=V1WindowsSecurityContextOptions(),
                    ),
                    service_account="service_account_example",
                    service_account_name="service_account_name_example",
                    set_hostname_as_fqdn=True,
                    share_process_namespace=True,
                    subdomain="subdomain_example",
                    termination_grace_period_seconds=1,
                    tolerations=[
                        V1Toleration(
                            effect="effect_example",
                            key="key_example",
                            operator="operator_example",
                            toleration_seconds=1,
                            value="value_example",
                        )
                    ],
                    topology_spread_constraints=[
                        V1TopologySpreadConstraint(
                            label_selector=V1LabelSelector(),
                            match_label_keys=[
                                "match_label_keys_example"
                            ],
                            max_skew=1,
                            min_domains=1,
                            node_affinity_policy="node_affinity_policy_example",
                            node_taints_policy="node_taints_policy_example",
                            topology_key="topology_key_example",
                            when_unsatisfiable="when_unsatisfiable_example",
                        )
                    ],
                    volumes=[
                        V1Volume(
                            aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            azure_disk=V1AzureDiskVolumeSource(
                                caching_mode="caching_mode_example",
                                disk_name="disk_name_example",
                                disk_uri="disk_uri_example",
                                fs_type="fs_type_example",
                                kind="kind_example",
                                read_only=True,
                            ),
                            azure_file=V1AzureFileVolumeSource(
                                read_only=True,
                                secret_name="secret_name_example",
                                share_name="share_name_example",
                            ),
                            cephfs=V1CephFSVolumeSource(
                                monitors=[
                                    "monitors_example"
                                ],
                                path="path_example",
                                read_only=True,
                                secret_file="secret_file_example",
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            cinder=V1CinderVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_id="volume_id_example",
                            ),
                            config_map=V1ConfigMapVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath(
                                        key="key_example",
                                        mode=1,
                                        path="path_example",
                                    )
                                ],
                                name="name_example",
                                optional=True,
                            ),
                            csi=V1CSIVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                node_publish_secret_ref=V1LocalObjectReference(),
                                read_only=True,
                                volume_attributes=dict(
                                    "key": "key_example",
                                ),
                            ),
                            downward_api=V1DownwardAPIVolumeSource(
                                default_mode=1,
                                items=[
                                    V1DownwardAPIVolumeFile(
                                        field_ref=V1ObjectFieldSelector(),
                                        mode=1,
                                        path="path_example",
                                        resource_field_ref=V1ResourceFieldSelector(),
                                    )
                                ],
                            ),
                            empty_dir=V1EmptyDirVolumeSource(
                                medium="medium_example",
                                size_limit="size_limit_example",
                            ),
                            ephemeral=V1EphemeralVolumeSource(
                                volume_claim_template=V1PersistentVolumeClaimTemplate(
                                    metadata=V1ObjectMeta(),
                                    spec=V1PersistentVolumeClaimSpec(
                                        access_modes=[
                                            "access_modes_example"
                                        ],
                                        data_source=V1TypedLocalObjectReference(
                                            api_group="api_group_example",
                                            kind="kind_example",
                                            name="name_example",
                                        ),
,
                                        resources=V1ResourceRequirements(),
                                        selector=V1LabelSelector(),
                                        storage_class_name="storage_class_name_example",
                                        volume_mode="volume_mode_example",
                                        volume_name="volume_name_example",
                                    ),
                                ),
                            ),
                            fc=V1FCVolumeSource(
                                fs_type="fs_type_example",
                                lun=1,
                                read_only=True,
                                target_wwns=[
                                    "target_wwns_example"
                                ],
                                wwids=[
                                    "wwids_example"
                                ],
                            ),
                            flex_volume=V1FlexVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                options=dict(
                                    "key": "key_example",
                                ),
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                            ),
                            flocker=V1FlockerVolumeSource(
                                dataset_name="dataset_name_example",
                                dataset_uuid="dataset_uuid_example",
                            ),
                            gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                pd_name="pd_name_example",
                                read_only=True,
                            ),
                            git_repo=V1GitRepoVolumeSource(
                                directory="directory_example",
                                repository="repository_example",
                                revision="revision_example",
                            ),
                            glusterfs=V1GlusterfsVolumeSource(
                                endpoints="endpoints_example",
                                path="path_example",
                                read_only=True,
                            ),
                            host_path=V1HostPathVolumeSource(
                                path="path_example",
                                type="type_example",
                            ),
                            iscsi=V1ISCSIVolumeSource(
                                chap_auth_discovery=True,
                                chap_auth_session=True,
                                fs_type="fs_type_example",
                                initiator_name="initiator_name_example",
                                iqn="iqn_example",
                                iscsi_interface="iscsi_interface_example",
                                lun=1,
                                portals=[
                                    "portals_example"
                                ],
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                target_portal="target_portal_example",
                            ),
                            name="name_example",
                            nfs=V1NFSVolumeSource(
                                path="path_example",
                                read_only=True,
                                server="server_example",
                            ),
                            persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                claim_name="claim_name_example",
                                read_only=True,
                            ),
                            photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                pd_id="pd_id_example",
                            ),
                            portworx_volume=V1PortworxVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            projected=V1ProjectedVolumeSource(
                                default_mode=1,
                                sources=[
                                    V1VolumeProjection(
                                        config_map=V1ConfigMapProjection(
,
                                            name="name_example",
                                            optional=True,
                                        ),
                                        downward_api=V1DownwardAPIProjection(
                                            items=[
                                                V1DownwardAPIVolumeFile()
                                            ],
                                        ),
                                        secret=V1SecretProjection(
                                            items=[
                                                V1KeyToPath()
                                            ],
                                            name="name_example",
                                            optional=True,
                                        ),
                                        service_account_token=V1ServiceAccountTokenProjection(
                                            audience="audience_example",
                                            expiration_seconds=1,
                                            path="path_example",
                                        ),
                                    )
                                ],
                            ),
                            quobyte=V1QuobyteVolumeSource(
                                group="group_example",
                                read_only=True,
                                registry="registry_example",
                                tenant="tenant_example",
                                user="user_example",
                                volume="volume_example",
                            ),
                            rbd=V1RBDVolumeSource(
                                fs_type="fs_type_example",
                                image="image_example",
                                keyring="keyring_example",
                                monitors=[
                                    "monitors_example"
                                ],
                                pool="pool_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            scale_io=V1ScaleIOVolumeSource(
                                fs_type="fs_type_example",
                                gateway="gateway_example",
                                protection_domain="protection_domain_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                ssl_enabled=True,
                                storage_mode="storage_mode_example",
                                storage_pool="storage_pool_example",
                                system="system_example",
                                volume_name="volume_name_example",
                            ),
                            secret=V1SecretVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath()
                                ],
                                optional=True,
                                secret_name="secret_name_example",
                            ),
                            storageos=V1StorageOSVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_name="volume_name_example",
                                volume_namespace="volume_namespace_example",
                            ),
                            vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                fs_type="fs_type_example",
                                storage_policy_id="storage_policy_id_example",
                                storage_policy_name="storage_policy_name_example",
                                volume_path="volume_path_example",
                            ),
                        )
                    ],
                ),
            ),
            ttl_seconds_after_finished=1,
        ),
        status=V1JobStatus(
            active=1,
            completed_indexes="completed_indexes_example",
            completion_time="1970-01-01T00:00:00.00Z",
            conditions=[
                V1JobCondition(
                    last_probe_time="1970-01-01T00:00:00.00Z",
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            failed=1,
            ready=1,
            start_time="1970-01-01T00:00:00.00Z",
            succeeded=1,
            uncounted_terminated_pods=V1UncountedTerminatedPods(
                failed=[
                    "failed_example"
                ],
                succeeded=[
                    "succeeded_example"
                ],
            ),
        ),
    )
    try:
        api_response = api_instance.replace_namespaced_job_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->replace_namespaced_job_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1Job(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations=dict(
                "key": "key_example",
            ),
            creation_timestamp="1970-01-01T00:00:00.00Z",
            deletion_grace_period_seconds=1,
            deletion_timestamp="1970-01-01T00:00:00.00Z",
            finalizers=[
                "finalizers_example"
            ],
            generate_name="generate_name_example",
            generation=1,
            labels=dict(
                "key": "key_example",
            ),
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1=dict(),
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time="1970-01-01T00:00:00.00Z",
                )
            ],
            name="name_example",
            namespace="namespace_example",
            owner_references=[
                V1OwnerReference(
                    api_version="api_version_example",
                    block_owner_deletion=True,
                    controller=True,
                    kind="kind_example",
                    name="name_example",
                    uid="uid_example",
                )
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1JobSpec(
            active_deadline_seconds=1,
            backoff_limit=1,
            completion_mode="completion_mode_example",
            completions=1,
            manual_selector=True,
            parallelism=1,
            pod_failure_policy=V1PodFailurePolicy(
                rules=[
                    V1PodFailurePolicyRule(
                        action="action_example",
                        on_exit_codes=V1PodFailurePolicyOnExitCodesRequirement(
                            container_name="container_name_example",
                            operator="operator_example",
                            values=[
                                1
                            ],
                        ),
                        on_pod_conditions=[
                            V1PodFailurePolicyOnPodConditionsPattern(
                                status="status_example",
                                type="type_example",
                            )
                        ],
                    )
                ],
            ),
            selector=V1LabelSelector(
                match_expressions=[
                    V1LabelSelectorRequirement(
                        key="key_example",
                        operator="operator_example",
                        values=[
                            "values_example"
                        ],
                    )
                ],
                match_labels=dict(
                    "key": "key_example",
                ),
            ),
            suspend=True,
            template=V1PodTemplateSpec(
                metadata=V1ObjectMeta(),
                spec=V1PodSpec(
                    active_deadline_seconds=1,
                    affinity=V1Affinity(
                        node_affinity=V1NodeAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1PreferredSchedulingTerm(
                                    preference=V1NodeSelectorTerm(
                                        match_expressions=[
                                            V1NodeSelectorRequirement(
                                                key="key_example",
                                                operator="operator_example",
                                                values=[
                                                    "values_example"
                                                ],
                                            )
                                        ],
                                        match_fields=[
                                            V1NodeSelectorRequirement()
                                        ],
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                node_selector_terms=[
                                    V1NodeSelectorTerm()
                                ],
                            ),
                        ),
                        pod_affinity=V1PodAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm(
                                    pod_affinity_term=V1PodAffinityTerm(
                                        label_selector=V1LabelSelector(),
                                        namespace_selector=V1LabelSelector(),
                                        namespaces=[
                                            "namespaces_example"
                                        ],
                                        topology_key="topology_key_example",
                                    ),
                                    weight=1,
                                )
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                        pod_anti_affinity=V1PodAntiAffinity(
                            preferred_during_scheduling_ignored_during_execution=[
                                V1WeightedPodAffinityTerm()
                            ],
                            required_during_scheduling_ignored_during_execution=[
                                V1PodAffinityTerm()
                            ],
                        ),
                    ),
                    automount_service_account_token=True,
                    containers=[
                        V1Container(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
                            env=[
                                V1EnvVar(
                                    name="name_example",
                                    value="value_example",
                                    value_from=V1EnvVarSource(
                                        config_map_key_ref=V1ConfigMapKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                        field_ref=V1ObjectFieldSelector(
                                            api_version="api_version_example",
                                            field_path="field_path_example",
                                        ),
                                        resource_field_ref=V1ResourceFieldSelector(
                                            container_name="container_name_example",
                                            divisor="divisor_example",
                                            resource="resource_example",
                                        ),
                                        secret_key_ref=V1SecretKeySelector(
                                            key="key_example",
                                            name="name_example",
                                            optional=True,
                                        ),
                                    ),
                                )
                            ],
                            env_from=[
                                V1EnvFromSource(
                                    config_map_ref=V1ConfigMapEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                    prefix="prefix_example",
                                    secret_ref=V1SecretEnvSource(
                                        name="name_example",
                                        optional=True,
                                    ),
                                )
                            ],
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(
                                post_start=V1LifecycleHandler(
                                    _exec=V1ExecAction(
                                        command=[
                                            "command_example"
                                        ],
                                    ),
                                    http_get=V1HTTPGetAction(
                                        host="host_example",
                                        http_headers=[
                                            V1HTTPHeader(
                                                name="name_example",
                                                value="value_example",
                                            )
                                        ],
                                        path="path_example",
                                        port=dict(),
                                        scheme="scheme_example",
                                    ),
                                    tcp_socket=V1TCPSocketAction(
                                        host="host_example",
                                        port=dict(),
                                    ),
                                ),
                                pre_stop=V1LifecycleHandler(),
                            ),
                            liveness_probe=V1Probe(
                                _exec=V1ExecAction(),
                                failure_threshold=1,
                                grpc=V1GRPCAction(
                                    port=1,
                                    service="service_example",
                                ),
                                http_get=V1HTTPGetAction(),
                                initial_delay_seconds=1,
                                period_seconds=1,
                                success_threshold=1,
                                tcp_socket=V1TCPSocketAction(),
                                termination_grace_period_seconds=1,
                                timeout_seconds=1,
                            ),
                            name="name_example",
                            ports=[
                                V1ContainerPort(
                                    container_port=1,
                                    host_ip="host_ip_example",
                                    host_port=1,
                                    name="name_example",
                                    protocol="protocol_example",
                                )
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(
                                limits=dict(
                                    "key": "key_example",
                                ),
                                requests=dict(
                                    "key": "key_example",
                                ),
                            ),
                            security_context=V1SecurityContext(
                                allow_privilege_escalation=True,
                                capabilities=V1Capabilities(
                                    add=[
                                        "add_example"
                                    ],
                                    drop=[
                                        "drop_example"
                                    ],
                                ),
                                privileged=True,
                                proc_mount="proc_mount_example",
                                read_only_root_filesystem=True,
                                run_as_group=1,
                                run_as_non_root=True,
                                run_as_user=1,
                                se_linux_options=V1SELinuxOptions(
                                    level="level_example",
                                    role="role_example",
                                    type="type_example",
                                    user="user_example",
                                ),
                                seccomp_profile=V1SeccompProfile(
                                    localhost_profile="localhost_profile_example",
                                    type="type_example",
                                ),
                                windows_options=V1WindowsSecurityContextOptions(
                                    gmsa_credential_spec="gmsa_credential_spec_example",
                                    gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                    host_process=True,
                                    run_as_user_name="run_as_user_name_example",
                                ),
                            ),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
                            volume_devices=[
                                V1VolumeDevice(
                                    device_path="device_path_example",
                                    name="name_example",
                                )
                            ],
                            volume_mounts=[
                                V1VolumeMount(
                                    mount_path="mount_path_example",
                                    mount_propagation="mount_propagation_example",
                                    name="name_example",
                                    read_only=True,
                                    sub_path="sub_path_example",
                                    sub_path_expr="sub_path_expr_example",
                                )
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    dns_config=V1PodDNSConfig(
                        nameservers=[
                            "nameservers_example"
                        ],
                        options=[
                            V1PodDNSConfigOption(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        searches=[
                            "searches_example"
                        ],
                    ),
                    dns_policy="dns_policy_example",
                    enable_service_links=True,
                    ephemeral_containers=[
                        V1EphemeralContainer(
                            args=[
                                "args_example"
                            ],
                            command=[
                                "command_example"
                            ],
,
,
                            image="image_example",
                            image_pull_policy="image_pull_policy_example",
                            lifecycle=V1Lifecycle(),
                            liveness_probe=V1Probe(),
                            name="name_example",
                            ports=[
                                V1ContainerPort()
                            ],
                            readiness_probe=V1Probe(),
                            resources=V1ResourceRequirements(),
                            security_context=V1SecurityContext(),
                            startup_probe=V1Probe(),
                            stdin=True,
                            stdin_once=True,
                            target_container_name="target_container_name_example",
                            termination_message_path="termination_message_path_example",
                            termination_message_policy="termination_message_policy_example",
                            tty=True,
,
                            volume_mounts=[
                                V1VolumeMount()
                            ],
                            working_dir="working_dir_example",
                        )
                    ],
                    host_aliases=[
                        V1HostAlias(
                            hostnames=[
                                "hostnames_example"
                            ],
                            ip="ip_example",
                        )
                    ],
                    host_ipc=True,
                    host_network=True,
                    host_pid=True,
                    host_users=True,
                    hostname="hostname_example",
                    image_pull_secrets=[
                        V1LocalObjectReference(
                            name="name_example",
                        )
                    ],
                    init_containers=[
                        V1Container()
                    ],
                    node_name="node_name_example",
                    node_selector=dict(
                        "key": "key_example",
                    ),
                    os=V1PodOS(
                        name="name_example",
                    ),
                    overhead=dict(
                        "key": "key_example",
                    ),
                    preemption_policy="preemption_policy_example",
                    priority=1,
                    priority_class_name="priority_class_name_example",
                    readiness_gates=[
                        V1PodReadinessGate(
                            condition_type="condition_type_example",
                        )
                    ],
                    restart_policy="restart_policy_example",
                    runtime_class_name="runtime_class_name_example",
                    scheduler_name="scheduler_name_example",
                    security_context=V1PodSecurityContext(
                        fs_group=1,
                        fs_group_change_policy="fs_group_change_policy_example",
                        run_as_group=1,
                        run_as_non_root=True,
                        run_as_user=1,
                        se_linux_options=V1SELinuxOptions(),
                        seccomp_profile=V1SeccompProfile(),
                        supplemental_groups=[
                            1
                        ],
                        sysctls=[
                            V1Sysctl(
                                name="name_example",
                                value="value_example",
                            )
                        ],
                        windows_options=V1WindowsSecurityContextOptions(),
                    ),
                    service_account="service_account_example",
                    service_account_name="service_account_name_example",
                    set_hostname_as_fqdn=True,
                    share_process_namespace=True,
                    subdomain="subdomain_example",
                    termination_grace_period_seconds=1,
                    tolerations=[
                        V1Toleration(
                            effect="effect_example",
                            key="key_example",
                            operator="operator_example",
                            toleration_seconds=1,
                            value="value_example",
                        )
                    ],
                    topology_spread_constraints=[
                        V1TopologySpreadConstraint(
                            label_selector=V1LabelSelector(),
                            match_label_keys=[
                                "match_label_keys_example"
                            ],
                            max_skew=1,
                            min_domains=1,
                            node_affinity_policy="node_affinity_policy_example",
                            node_taints_policy="node_taints_policy_example",
                            topology_key="topology_key_example",
                            when_unsatisfiable="when_unsatisfiable_example",
                        )
                    ],
                    volumes=[
                        V1Volume(
                            aws_elastic_block_store=V1AWSElasticBlockStoreVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            azure_disk=V1AzureDiskVolumeSource(
                                caching_mode="caching_mode_example",
                                disk_name="disk_name_example",
                                disk_uri="disk_uri_example",
                                fs_type="fs_type_example",
                                kind="kind_example",
                                read_only=True,
                            ),
                            azure_file=V1AzureFileVolumeSource(
                                read_only=True,
                                secret_name="secret_name_example",
                                share_name="share_name_example",
                            ),
                            cephfs=V1CephFSVolumeSource(
                                monitors=[
                                    "monitors_example"
                                ],
                                path="path_example",
                                read_only=True,
                                secret_file="secret_file_example",
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            cinder=V1CinderVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_id="volume_id_example",
                            ),
                            config_map=V1ConfigMapVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath(
                                        key="key_example",
                                        mode=1,
                                        path="path_example",
                                    )
                                ],
                                name="name_example",
                                optional=True,
                            ),
                            csi=V1CSIVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                node_publish_secret_ref=V1LocalObjectReference(),
                                read_only=True,
                                volume_attributes=dict(
                                    "key": "key_example",
                                ),
                            ),
                            downward_api=V1DownwardAPIVolumeSource(
                                default_mode=1,
                                items=[
                                    V1DownwardAPIVolumeFile(
                                        field_ref=V1ObjectFieldSelector(),
                                        mode=1,
                                        path="path_example",
                                        resource_field_ref=V1ResourceFieldSelector(),
                                    )
                                ],
                            ),
                            empty_dir=V1EmptyDirVolumeSource(
                                medium="medium_example",
                                size_limit="size_limit_example",
                            ),
                            ephemeral=V1EphemeralVolumeSource(
                                volume_claim_template=V1PersistentVolumeClaimTemplate(
                                    metadata=V1ObjectMeta(),
                                    spec=V1PersistentVolumeClaimSpec(
                                        access_modes=[
                                            "access_modes_example"
                                        ],
                                        data_source=V1TypedLocalObjectReference(
                                            api_group="api_group_example",
                                            kind="kind_example",
                                            name="name_example",
                                        ),
,
                                        resources=V1ResourceRequirements(),
                                        selector=V1LabelSelector(),
                                        storage_class_name="storage_class_name_example",
                                        volume_mode="volume_mode_example",
                                        volume_name="volume_name_example",
                                    ),
                                ),
                            ),
                            fc=V1FCVolumeSource(
                                fs_type="fs_type_example",
                                lun=1,
                                read_only=True,
                                target_wwns=[
                                    "target_wwns_example"
                                ],
                                wwids=[
                                    "wwids_example"
                                ],
                            ),
                            flex_volume=V1FlexVolumeSource(
                                driver="driver_example",
                                fs_type="fs_type_example",
                                options=dict(
                                    "key": "key_example",
                                ),
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                            ),
                            flocker=V1FlockerVolumeSource(
                                dataset_name="dataset_name_example",
                                dataset_uuid="dataset_uuid_example",
                            ),
                            gce_persistent_disk=V1GCEPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                partition=1,
                                pd_name="pd_name_example",
                                read_only=True,
                            ),
                            git_repo=V1GitRepoVolumeSource(
                                directory="directory_example",
                                repository="repository_example",
                                revision="revision_example",
                            ),
                            glusterfs=V1GlusterfsVolumeSource(
                                endpoints="endpoints_example",
                                path="path_example",
                                read_only=True,
                            ),
                            host_path=V1HostPathVolumeSource(
                                path="path_example",
                                type="type_example",
                            ),
                            iscsi=V1ISCSIVolumeSource(
                                chap_auth_discovery=True,
                                chap_auth_session=True,
                                fs_type="fs_type_example",
                                initiator_name="initiator_name_example",
                                iqn="iqn_example",
                                iscsi_interface="iscsi_interface_example",
                                lun=1,
                                portals=[
                                    "portals_example"
                                ],
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                target_portal="target_portal_example",
                            ),
                            name="name_example",
                            nfs=V1NFSVolumeSource(
                                path="path_example",
                                read_only=True,
                                server="server_example",
                            ),
                            persistent_volume_claim=V1PersistentVolumeClaimVolumeSource(
                                claim_name="claim_name_example",
                                read_only=True,
                            ),
                            photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                                fs_type="fs_type_example",
                                pd_id="pd_id_example",
                            ),
                            portworx_volume=V1PortworxVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                volume_id="volume_id_example",
                            ),
                            projected=V1ProjectedVolumeSource(
                                default_mode=1,
                                sources=[
                                    V1VolumeProjection(
                                        config_map=V1ConfigMapProjection(
,
                                            name="name_example",
                                            optional=True,
                                        ),
                                        downward_api=V1DownwardAPIProjection(
                                            items=[
                                                V1DownwardAPIVolumeFile()
                                            ],
                                        ),
                                        secret=V1SecretProjection(
                                            items=[
                                                V1KeyToPath()
                                            ],
                                            name="name_example",
                                            optional=True,
                                        ),
                                        service_account_token=V1ServiceAccountTokenProjection(
                                            audience="audience_example",
                                            expiration_seconds=1,
                                            path="path_example",
                                        ),
                                    )
                                ],
                            ),
                            quobyte=V1QuobyteVolumeSource(
                                group="group_example",
                                read_only=True,
                                registry="registry_example",
                                tenant="tenant_example",
                                user="user_example",
                                volume="volume_example",
                            ),
                            rbd=V1RBDVolumeSource(
                                fs_type="fs_type_example",
                                image="image_example",
                                keyring="keyring_example",
                                monitors=[
                                    "monitors_example"
                                ],
                                pool="pool_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                user="user_example",
                            ),
                            scale_io=V1ScaleIOVolumeSource(
                                fs_type="fs_type_example",
                                gateway="gateway_example",
                                protection_domain="protection_domain_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                ssl_enabled=True,
                                storage_mode="storage_mode_example",
                                storage_pool="storage_pool_example",
                                system="system_example",
                                volume_name="volume_name_example",
                            ),
                            secret=V1SecretVolumeSource(
                                default_mode=1,
                                items=[
                                    V1KeyToPath()
                                ],
                                optional=True,
                                secret_name="secret_name_example",
                            ),
                            storageos=V1StorageOSVolumeSource(
                                fs_type="fs_type_example",
                                read_only=True,
                                secret_ref=V1LocalObjectReference(),
                                volume_name="volume_name_example",
                                volume_namespace="volume_namespace_example",
                            ),
                            vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                fs_type="fs_type_example",
                                storage_policy_id="storage_policy_id_example",
                                storage_policy_name="storage_policy_name_example",
                                volume_path="volume_path_example",
                            ),
                        )
                    ],
                ),
            ),
            ttl_seconds_after_finished=1,
        ),
        status=V1JobStatus(
            active=1,
            completed_indexes="completed_indexes_example",
            completion_time="1970-01-01T00:00:00.00Z",
            conditions=[
                V1JobCondition(
                    last_probe_time="1970-01-01T00:00:00.00Z",
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            failed=1,
            ready=1,
            start_time="1970-01-01T00:00:00.00Z",
            succeeded=1,
            uncounted_terminated_pods=V1UncountedTerminatedPods(
                failed=[
                    "failed_example"
                ],
                succeeded=[
                    "succeeded_example"
                ],
            ),
        ),
    )
    try:
        api_response = api_instance.replace_namespaced_job_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1Api->replace_namespaced_job_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pretty | PrettySchema | | optional
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional


# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DryRunSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldManagerSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FieldValidationSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
name | NameSchema | | 
namespace | NamespaceSchema | | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NamespaceSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#replace_namespaced_job_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_namespaced_job_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_namespaced_job_status.ApiResponseFor401) | Unauthorized

#### replace_namespaced_job_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### replace_namespaced_job_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1Job**](../../models/V1Job.md) |  | 


#### replace_namespaced_job_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

