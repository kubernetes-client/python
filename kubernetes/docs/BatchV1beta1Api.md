# kubernetes.client.BatchV1beta1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_cron_job**](BatchV1beta1Api.md#create_namespaced_cron_job) | **POST** /apis/batch/v1beta1/namespaces/{namespace}/cronjobs | 
[**delete_collection_namespaced_cron_job**](BatchV1beta1Api.md#delete_collection_namespaced_cron_job) | **DELETE** /apis/batch/v1beta1/namespaces/{namespace}/cronjobs | 
[**delete_namespaced_cron_job**](BatchV1beta1Api.md#delete_namespaced_cron_job) | **DELETE** /apis/batch/v1beta1/namespaces/{namespace}/cronjobs/{name} | 
[**get_api_resources**](BatchV1beta1Api.md#get_api_resources) | **GET** /apis/batch/v1beta1/ | 
[**list_cron_job_for_all_namespaces**](BatchV1beta1Api.md#list_cron_job_for_all_namespaces) | **GET** /apis/batch/v1beta1/cronjobs | 
[**list_namespaced_cron_job**](BatchV1beta1Api.md#list_namespaced_cron_job) | **GET** /apis/batch/v1beta1/namespaces/{namespace}/cronjobs | 
[**patch_namespaced_cron_job**](BatchV1beta1Api.md#patch_namespaced_cron_job) | **PATCH** /apis/batch/v1beta1/namespaces/{namespace}/cronjobs/{name} | 
[**patch_namespaced_cron_job_status**](BatchV1beta1Api.md#patch_namespaced_cron_job_status) | **PATCH** /apis/batch/v1beta1/namespaces/{namespace}/cronjobs/{name}/status | 
[**read_namespaced_cron_job**](BatchV1beta1Api.md#read_namespaced_cron_job) | **GET** /apis/batch/v1beta1/namespaces/{namespace}/cronjobs/{name} | 
[**read_namespaced_cron_job_status**](BatchV1beta1Api.md#read_namespaced_cron_job_status) | **GET** /apis/batch/v1beta1/namespaces/{namespace}/cronjobs/{name}/status | 
[**replace_namespaced_cron_job**](BatchV1beta1Api.md#replace_namespaced_cron_job) | **PUT** /apis/batch/v1beta1/namespaces/{namespace}/cronjobs/{name} | 
[**replace_namespaced_cron_job_status**](BatchV1beta1Api.md#replace_namespaced_cron_job_status) | **PUT** /apis/batch/v1beta1/namespaces/{namespace}/cronjobs/{name}/status | 


# **create_namespaced_cron_job**
> V1beta1CronJob create_namespaced_cron_job(namespace, body)



create a CronJob

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
from kubernetes.client.model.v1beta1_cron_job import V1beta1CronJob
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)
    namespace = "namespace_example" # str | object name and auth scope, such as for teams and projects
    body = V1beta1CronJob(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations={
                "key": "key_example",
            },
            cluster_name="cluster_name_example",
            creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
            deletion_grace_period_seconds=1,
            deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
            finalizers=[
                "finalizers_example",
            ],
            generate_name="generate_name_example",
            generation=1,
            labels={
                "key": "key_example",
            },
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1={},
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
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
                ),
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1beta1CronJobSpec(
            concurrency_policy="concurrency_policy_example",
            failed_jobs_history_limit=1,
            job_template=V1beta1JobTemplateSpec(
                metadata=V1ObjectMeta(
                    annotations={
                        "key": "key_example",
                    },
                    cluster_name="cluster_name_example",
                    creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    deletion_grace_period_seconds=1,
                    deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    finalizers=[
                        "finalizers_example",
                    ],
                    generate_name="generate_name_example",
                    generation=1,
                    labels={
                        "key": "key_example",
                    },
                    managed_fields=[
                        V1ManagedFieldsEntry(
                            api_version="api_version_example",
                            fields_type="fields_type_example",
                            fields_v1={},
                            manager="manager_example",
                            operation="operation_example",
                            subresource="subresource_example",
                            time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
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
                        ),
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
                    selector=V1LabelSelector(
                        match_expressions=[
                            V1LabelSelectorRequirement(
                                key="key_example",
                                operator="operator_example",
                                values=[
                                    "values_example",
                                ],
                            ),
                        ],
                        match_labels={
                            "key": "key_example",
                        },
                    ),
                    suspend=True,
                    template=V1PodTemplateSpec(
                        metadata=V1ObjectMeta(
                            annotations={
                                "key": "key_example",
                            },
                            cluster_name="cluster_name_example",
                            creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            deletion_grace_period_seconds=1,
                            deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            finalizers=[
                                "finalizers_example",
                            ],
                            generate_name="generate_name_example",
                            generation=1,
                            labels={
                                "key": "key_example",
                            },
                            managed_fields=[
                                V1ManagedFieldsEntry(
                                    api_version="api_version_example",
                                    fields_type="fields_type_example",
                                    fields_v1={},
                                    manager="manager_example",
                                    operation="operation_example",
                                    subresource="subresource_example",
                                    time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                ),
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
                                ),
                            ],
                            resource_version="resource_version_example",
                            self_link="self_link_example",
                            uid="uid_example",
                        ),
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
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            weight=1,
                                        ),
                                    ],
                                    required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                        node_selector_terms=[
                                            V1NodeSelectorTerm(
                                                match_expressions=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                                pod_affinity=V1PodAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespace_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespaces=[
                                                    "namespaces_example",
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        ),
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm(
                                            label_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespace_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespaces=[
                                                "namespaces_example",
                                            ],
                                            topology_key="topology_key_example",
                                        ),
                                    ],
                                ),
                                pod_anti_affinity=V1PodAntiAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespace_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespaces=[
                                                    "namespaces_example",
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        ),
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm(
                                            label_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespace_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespaces=[
                                                "namespaces_example",
                                            ],
                                            topology_key="topology_key_example",
                                        ),
                                    ],
                                ),
                            ),
                            automount_service_account_token=True,
                            containers=[
                                V1Container(
                                    args=[
                                        "args_example",
                                    ],
                                    command=[
                                        "command_example",
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
                                        ),
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
                                        ),
                                    ],
                                    image="image_example",
                                    image_pull_policy="Always",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
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
                                            protocol="SCTP",
                                        ),
                                    ],
                                    readiness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    resources=V1ResourceRequirements(
                                        limits={
                                            "key": "key_example",
                                        },
                                        requests={
                                            "key": "key_example",
                                        },
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example",
                                            ],
                                            drop=[
                                                "drop_example",
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
                                            type="Localhost",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="FallbackToLogsOnError",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        ),
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        ),
                                    ],
                                    working_dir="working_dir_example",
                                ),
                            ],
                            dns_config=V1PodDNSConfig(
                                nameservers=[
                                    "nameservers_example",
                                ],
                                options=[
                                    V1PodDNSConfigOption(
                                        name="name_example",
                                        value="value_example",
                                    ),
                                ],
                                searches=[
                                    "searches_example",
                                ],
                            ),
                            dns_policy="ClusterFirst",
                            enable_service_links=True,
                            ephemeral_containers=[
                                V1EphemeralContainer(
                                    args=[
                                        "args_example",
                                    ],
                                    command=[
                                        "command_example",
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
                                        ),
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
                                        ),
                                    ],
                                    image="image_example",
                                    image_pull_policy="Always",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
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
                                            protocol="SCTP",
                                        ),
                                    ],
                                    readiness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    resources=V1ResourceRequirements(
                                        limits={
                                            "key": "key_example",
                                        },
                                        requests={
                                            "key": "key_example",
                                        },
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example",
                                            ],
                                            drop=[
                                                "drop_example",
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
                                            type="Localhost",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    stdin=True,
                                    stdin_once=True,
                                    target_container_name="target_container_name_example",
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="FallbackToLogsOnError",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        ),
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        ),
                                    ],
                                    working_dir="working_dir_example",
                                ),
                            ],
                            host_aliases=[
                                V1HostAlias(
                                    hostnames=[
                                        "hostnames_example",
                                    ],
                                    ip="ip_example",
                                ),
                            ],
                            host_ipc=True,
                            host_network=True,
                            host_pid=True,
                            hostname="hostname_example",
                            image_pull_secrets=[
                                V1LocalObjectReference(
                                    name="name_example",
                                ),
                            ],
                            init_containers=[
                                V1Container(
                                    args=[
                                        "args_example",
                                    ],
                                    command=[
                                        "command_example",
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
                                        ),
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
                                        ),
                                    ],
                                    image="image_example",
                                    image_pull_policy="Always",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
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
                                            protocol="SCTP",
                                        ),
                                    ],
                                    readiness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    resources=V1ResourceRequirements(
                                        limits={
                                            "key": "key_example",
                                        },
                                        requests={
                                            "key": "key_example",
                                        },
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example",
                                            ],
                                            drop=[
                                                "drop_example",
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
                                            type="Localhost",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="FallbackToLogsOnError",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        ),
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        ),
                                    ],
                                    working_dir="working_dir_example",
                                ),
                            ],
                            node_name="node_name_example",
                            node_selector={
                                "key": "key_example",
                            },
                            os=V1PodOS(
                                name="name_example",
                            ),
                            overhead={
                                "key": "key_example",
                            },
                            preemption_policy="preemption_policy_example",
                            priority=1,
                            priority_class_name="priority_class_name_example",
                            readiness_gates=[
                                V1PodReadinessGate(
                                    condition_type="ContainersReady",
                                ),
                            ],
                            restart_policy="Always",
                            runtime_class_name="runtime_class_name_example",
                            scheduler_name="scheduler_name_example",
                            security_context=V1PodSecurityContext(
                                fs_group=1,
                                fs_group_change_policy="fs_group_change_policy_example",
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
                                    type="Localhost",
                                ),
                                supplemental_groups=[
                                    1,
                                ],
                                sysctls=[
                                    V1Sysctl(
                                        name="name_example",
                                        value="value_example",
                                    ),
                                ],
                                windows_options=V1WindowsSecurityContextOptions(
                                    gmsa_credential_spec="gmsa_credential_spec_example",
                                    gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                    host_process=True,
                                    run_as_user_name="run_as_user_name_example",
                                ),
                            ),
                            service_account="service_account_example",
                            service_account_name="service_account_name_example",
                            set_hostname_as_fqdn=True,
                            share_process_namespace=True,
                            subdomain="subdomain_example",
                            termination_grace_period_seconds=1,
                            tolerations=[
                                V1Toleration(
                                    effect="NoExecute",
                                    key="key_example",
                                    operator="Equal",
                                    toleration_seconds=1,
                                    value="value_example",
                                ),
                            ],
                            topology_spread_constraints=[
                                V1TopologySpreadConstraint(
                                    label_selector=V1LabelSelector(
                                        match_expressions=[
                                            V1LabelSelectorRequirement(
                                                key="key_example",
                                                operator="operator_example",
                                                values=[
                                                    "values_example",
                                                ],
                                            ),
                                        ],
                                        match_labels={
                                            "key": "key_example",
                                        },
                                    ),
                                    max_skew=1,
                                    topology_key="topology_key_example",
                                    when_unsatisfiable="DoNotSchedule",
                                ),
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
                                            "monitors_example",
                                        ],
                                        path="path_example",
                                        read_only=True,
                                        secret_file="secret_file_example",
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        user="user_example",
                                    ),
                                    cinder=V1CinderVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        volume_id="volume_id_example",
                                    ),
                                    config_map=V1ConfigMapVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            ),
                                        ],
                                        name="name_example",
                                        optional=True,
                                    ),
                                    csi=V1CSIVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        node_publish_secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        read_only=True,
                                        volume_attributes={
                                            "key": "key_example",
                                        },
                                    ),
                                    downward_api=V1DownwardAPIVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1DownwardAPIVolumeFile(
                                                field_ref=V1ObjectFieldSelector(
                                                    api_version="api_version_example",
                                                    field_path="field_path_example",
                                                ),
                                                mode=1,
                                                path="path_example",
                                                resource_field_ref=V1ResourceFieldSelector(
                                                    container_name="container_name_example",
                                                    divisor="divisor_example",
                                                    resource="resource_example",
                                                ),
                                            ),
                                        ],
                                    ),
                                    empty_dir=V1EmptyDirVolumeSource(
                                        medium="medium_example",
                                        size_limit="size_limit_example",
                                    ),
                                    ephemeral=V1EphemeralVolumeSource(
                                        volume_claim_template=V1PersistentVolumeClaimTemplate(
                                            metadata=V1ObjectMeta(
                                                annotations={
                                                    "key": "key_example",
                                                },
                                                cluster_name="cluster_name_example",
                                                creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                                deletion_grace_period_seconds=1,
                                                deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                                finalizers=[
                                                    "finalizers_example",
                                                ],
                                                generate_name="generate_name_example",
                                                generation=1,
                                                labels={
                                                    "key": "key_example",
                                                },
                                                managed_fields=[
                                                    V1ManagedFieldsEntry(
                                                        api_version="api_version_example",
                                                        fields_type="fields_type_example",
                                                        fields_v1={},
                                                        manager="manager_example",
                                                        operation="operation_example",
                                                        subresource="subresource_example",
                                                        time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                                    ),
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
                                                    ),
                                                ],
                                                resource_version="resource_version_example",
                                                self_link="self_link_example",
                                                uid="uid_example",
                                            ),
                                            spec=V1PersistentVolumeClaimSpec(
                                                access_modes=[
                                                    "access_modes_example",
                                                ],
                                                data_source=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
                                                data_source_ref=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
                                                resources=V1ResourceRequirements(
                                                    limits={
                                                        "key": "key_example",
                                                    },
                                                    requests={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
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
                                            "target_wwns_example",
                                        ],
                                        wwids=[
                                            "wwids_example",
                                        ],
                                    ),
                                    flex_volume=V1FlexVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        options={
                                            "key": "key_example",
                                        },
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
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
                                            "portals_example",
                                        ],
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
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
                                                    items=[
                                                        V1KeyToPath(
                                                            key="key_example",
                                                            mode=1,
                                                            path="path_example",
                                                        ),
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                downward_api=V1DownwardAPIProjection(
                                                    items=[
                                                        V1DownwardAPIVolumeFile(
                                                            field_ref=V1ObjectFieldSelector(
                                                                api_version="api_version_example",
                                                                field_path="field_path_example",
                                                            ),
                                                            mode=1,
                                                            path="path_example",
                                                            resource_field_ref=V1ResourceFieldSelector(
                                                                container_name="container_name_example",
                                                                divisor="divisor_example",
                                                                resource="resource_example",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                secret=V1SecretProjection(
                                                    items=[
                                                        V1KeyToPath(
                                                            key="key_example",
                                                            mode=1,
                                                            path="path_example",
                                                        ),
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                service_account_token=V1ServiceAccountTokenProjection(
                                                    audience="audience_example",
                                                    expiration_seconds=1,
                                                    path="path_example",
                                                ),
                                            ),
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
                                            "monitors_example",
                                        ],
                                        pool="pool_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        user="user_example",
                                    ),
                                    scale_io=V1ScaleIOVolumeSource(
                                        fs_type="fs_type_example",
                                        gateway="gateway_example",
                                        protection_domain="protection_domain_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        ssl_enabled=True,
                                        storage_mode="storage_mode_example",
                                        storage_pool="storage_pool_example",
                                        system="system_example",
                                        volume_name="volume_name_example",
                                    ),
                                    secret=V1SecretVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            ),
                                        ],
                                        optional=True,
                                        secret_name="secret_name_example",
                                    ),
                                    storageos=V1StorageOSVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        volume_name="volume_name_example",
                                        volume_namespace="volume_namespace_example",
                                    ),
                                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        storage_policy_id="storage_policy_id_example",
                                        storage_policy_name="storage_policy_name_example",
                                        volume_path="volume_path_example",
                                    ),
                                ),
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
        ),
        status=V1beta1CronJobStatus(
            active=[
                V1ObjectReference(
                    api_version="api_version_example",
                    field_path="field_path_example",
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    resource_version="resource_version_example",
                    uid="uid_example",
                ),
            ],
            last_schedule_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_successful_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # V1beta1CronJob | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
    field_validation = "fieldValidation_example" # str | fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the `ServerSideFieldValidation` feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_namespaced_cron_job(namespace, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->create_namespaced_cron_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_namespaced_cron_job(namespace, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, field_validation=field_validation)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->create_namespaced_cron_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects |
 **body** | [**V1beta1CronJob**](V1beta1CronJob.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]
 **field_validation** | **str**| fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the &#x60;ServerSideFieldValidation&#x60; feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. | [optional]

### Return type

[**V1beta1CronJob**](V1beta1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_cron_job**
> V1Status delete_collection_namespaced_cron_job(namespace)



delete collection of CronJob

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)
    namespace = "namespace_example" # str | object name and auth scope, such as for teams and projects
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    _continue = "continue_example" # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_selector = "fieldSelector_example" # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    grace_period_seconds = 1 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
    label_selector = "labelSelector_example" # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    limit = 1 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
    propagation_policy = "propagationPolicy_example" # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)
    resource_version = "resourceVersion_example" # str | resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset (optional)
    resource_version_match = "resourceVersionMatch_example" # str | resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset (optional)
    timeout_seconds = 1 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
    body = V1DeleteOptions(
        api_version="api_version_example",
        dry_run=[
            "dry_run_example",
        ],
        grace_period_seconds=1,
        kind="kind_example",
        orphan_dependents=True,
        preconditions=V1Preconditions(
            resource_version="resource_version_example",
            uid="uid_example",
        ),
        propagation_policy="propagation_policy_example",
    ) # V1DeleteOptions |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_collection_namespaced_cron_job(namespace)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->delete_collection_namespaced_cron_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_collection_namespaced_cron_job(namespace, pretty=pretty, _continue=_continue, dry_run=dry_run, field_selector=field_selector, grace_period_seconds=grace_period_seconds, label_selector=label_selector, limit=limit, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, resource_version=resource_version, resource_version_match=resource_version_match, timeout_seconds=timeout_seconds, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->delete_collection_namespaced_cron_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional]
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional]
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional]
 **resource_version** | **str**| resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset | [optional]
 **resource_version_match** | **str**| resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset | [optional]
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional]
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | [optional]

### Return type

[**V1Status**](V1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_cron_job**
> V1Status delete_namespaced_cron_job(name, namespace)



delete a CronJob

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)
    name = "name_example" # str | name of the CronJob
    namespace = "namespace_example" # str | object name and auth scope, such as for teams and projects
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    grace_period_seconds = 1 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
    orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
    propagation_policy = "propagationPolicy_example" # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)
    body = V1DeleteOptions(
        api_version="api_version_example",
        dry_run=[
            "dry_run_example",
        ],
        grace_period_seconds=1,
        kind="kind_example",
        orphan_dependents=True,
        preconditions=V1Preconditions(
            resource_version="resource_version_example",
            uid="uid_example",
        ),
        propagation_policy="propagation_policy_example",
    ) # V1DeleteOptions |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_namespaced_cron_job(name, namespace)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->delete_namespaced_cron_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_namespaced_cron_job(name, namespace, pretty=pretty, dry_run=dry_run, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->delete_namespaced_cron_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob |
 **namespace** | **str**| object name and auth scope, such as for teams and projects |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional]
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional]
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional]
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | [optional]

### Return type

[**V1Status**](V1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources**
> V1APIResourceList get_api_resources()



get available resources

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_api_resources()
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->get_api_resources: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**V1APIResourceList**](V1APIResourceList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cron_job_for_all_namespaces**
> V1beta1CronJobList list_cron_job_for_all_namespaces()



list or watch objects of kind CronJob

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
from kubernetes.client.model.v1beta1_cron_job_list import V1beta1CronJobList
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)
    allow_watch_bookmarks = True # bool | allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. (optional)
    _continue = "continue_example" # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    field_selector = "fieldSelector_example" # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    label_selector = "labelSelector_example" # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    limit = 1 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    resource_version = "resourceVersion_example" # str | resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset (optional)
    resource_version_match = "resourceVersionMatch_example" # str | resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset (optional)
    timeout_seconds = 1 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
    watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_cron_job_for_all_namespaces(allow_watch_bookmarks=allow_watch_bookmarks, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, pretty=pretty, resource_version=resource_version, resource_version_match=resource_version_match, timeout_seconds=timeout_seconds, watch=watch)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->list_cron_job_for_all_namespaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_watch_bookmarks** | **bool**| allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. | [optional]
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional]
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **resource_version** | **str**| resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset | [optional]
 **resource_version_match** | **str**| resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset | [optional]
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional]
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional]

### Return type

[**V1beta1CronJobList**](V1beta1CronJobList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_cron_job**
> V1beta1CronJobList list_namespaced_cron_job(namespace)



list or watch objects of kind CronJob

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
from kubernetes.client.model.v1beta1_cron_job_list import V1beta1CronJobList
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)
    namespace = "namespace_example" # str | object name and auth scope, such as for teams and projects
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    allow_watch_bookmarks = True # bool | allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. (optional)
    _continue = "continue_example" # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    field_selector = "fieldSelector_example" # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    label_selector = "labelSelector_example" # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    limit = 1 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    resource_version = "resourceVersion_example" # str | resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset (optional)
    resource_version_match = "resourceVersionMatch_example" # str | resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset (optional)
    timeout_seconds = 1 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
    watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_namespaced_cron_job(namespace)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->list_namespaced_cron_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_namespaced_cron_job(namespace, pretty=pretty, allow_watch_bookmarks=allow_watch_bookmarks, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, resource_version_match=resource_version_match, timeout_seconds=timeout_seconds, watch=watch)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->list_namespaced_cron_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **allow_watch_bookmarks** | **bool**| allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. | [optional]
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional]
 **resource_version** | **str**| resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset | [optional]
 **resource_version_match** | **str**| resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.  Defaults to unset | [optional]
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional]
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional]

### Return type

[**V1beta1CronJobList**](V1beta1CronJobList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_cron_job**
> V1beta1CronJob patch_namespaced_cron_job(name, namespace, body)



partially update the specified CronJob

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
from kubernetes.client.model.v1beta1_cron_job import V1beta1CronJob
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)
    name = "name_example" # str | name of the CronJob
    namespace = "namespace_example" # str | object name and auth scope, such as for teams and projects
    body = {} # bool, date, datetime, dict, float, int, list, str, none_type | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
    field_validation = "fieldValidation_example" # str | fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the `ServerSideFieldValidation` feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. (optional)
    force = True # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_namespaced_cron_job(name, namespace, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->patch_namespaced_cron_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_namespaced_cron_job(name, namespace, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, field_validation=field_validation, force=force)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->patch_namespaced_cron_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob |
 **namespace** | **str**| object name and auth scope, such as for teams and projects |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional]
 **field_validation** | **str**| fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the &#x60;ServerSideFieldValidation&#x60; feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. | [optional]
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional]

### Return type

[**V1beta1CronJob**](V1beta1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json, application/apply-patch+yaml
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_cron_job_status**
> V1beta1CronJob patch_namespaced_cron_job_status(name, namespace, body)



partially update status of the specified CronJob

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
from kubernetes.client.model.v1beta1_cron_job import V1beta1CronJob
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)
    name = "name_example" # str | name of the CronJob
    namespace = "namespace_example" # str | object name and auth scope, such as for teams and projects
    body = {} # bool, date, datetime, dict, float, int, list, str, none_type | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
    field_validation = "fieldValidation_example" # str | fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the `ServerSideFieldValidation` feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. (optional)
    force = True # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_namespaced_cron_job_status(name, namespace, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->patch_namespaced_cron_job_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_namespaced_cron_job_status(name, namespace, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, field_validation=field_validation, force=force)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->patch_namespaced_cron_job_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob |
 **namespace** | **str**| object name and auth scope, such as for teams and projects |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional]
 **field_validation** | **str**| fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the &#x60;ServerSideFieldValidation&#x60; feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. | [optional]
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional]

### Return type

[**V1beta1CronJob**](V1beta1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json, application/apply-patch+yaml
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_cron_job**
> V1beta1CronJob read_namespaced_cron_job(name, namespace)



read the specified CronJob

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
from kubernetes.client.model.v1beta1_cron_job import V1beta1CronJob
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)
    name = "name_example" # str | name of the CronJob
    namespace = "namespace_example" # str | object name and auth scope, such as for teams and projects
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.read_namespaced_cron_job(name, namespace)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->read_namespaced_cron_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.read_namespaced_cron_job(name, namespace, pretty=pretty)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->read_namespaced_cron_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob |
 **namespace** | **str**| object name and auth scope, such as for teams and projects |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]

### Return type

[**V1beta1CronJob**](V1beta1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_cron_job_status**
> V1beta1CronJob read_namespaced_cron_job_status(name, namespace)



read status of the specified CronJob

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
from kubernetes.client.model.v1beta1_cron_job import V1beta1CronJob
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)
    name = "name_example" # str | name of the CronJob
    namespace = "namespace_example" # str | object name and auth scope, such as for teams and projects
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.read_namespaced_cron_job_status(name, namespace)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->read_namespaced_cron_job_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.read_namespaced_cron_job_status(name, namespace, pretty=pretty)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->read_namespaced_cron_job_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob |
 **namespace** | **str**| object name and auth scope, such as for teams and projects |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]

### Return type

[**V1beta1CronJob**](V1beta1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_cron_job**
> V1beta1CronJob replace_namespaced_cron_job(name, namespace, body)



replace the specified CronJob

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
from kubernetes.client.model.v1beta1_cron_job import V1beta1CronJob
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)
    name = "name_example" # str | name of the CronJob
    namespace = "namespace_example" # str | object name and auth scope, such as for teams and projects
    body = V1beta1CronJob(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations={
                "key": "key_example",
            },
            cluster_name="cluster_name_example",
            creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
            deletion_grace_period_seconds=1,
            deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
            finalizers=[
                "finalizers_example",
            ],
            generate_name="generate_name_example",
            generation=1,
            labels={
                "key": "key_example",
            },
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1={},
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
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
                ),
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1beta1CronJobSpec(
            concurrency_policy="concurrency_policy_example",
            failed_jobs_history_limit=1,
            job_template=V1beta1JobTemplateSpec(
                metadata=V1ObjectMeta(
                    annotations={
                        "key": "key_example",
                    },
                    cluster_name="cluster_name_example",
                    creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    deletion_grace_period_seconds=1,
                    deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    finalizers=[
                        "finalizers_example",
                    ],
                    generate_name="generate_name_example",
                    generation=1,
                    labels={
                        "key": "key_example",
                    },
                    managed_fields=[
                        V1ManagedFieldsEntry(
                            api_version="api_version_example",
                            fields_type="fields_type_example",
                            fields_v1={},
                            manager="manager_example",
                            operation="operation_example",
                            subresource="subresource_example",
                            time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
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
                        ),
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
                    selector=V1LabelSelector(
                        match_expressions=[
                            V1LabelSelectorRequirement(
                                key="key_example",
                                operator="operator_example",
                                values=[
                                    "values_example",
                                ],
                            ),
                        ],
                        match_labels={
                            "key": "key_example",
                        },
                    ),
                    suspend=True,
                    template=V1PodTemplateSpec(
                        metadata=V1ObjectMeta(
                            annotations={
                                "key": "key_example",
                            },
                            cluster_name="cluster_name_example",
                            creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            deletion_grace_period_seconds=1,
                            deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            finalizers=[
                                "finalizers_example",
                            ],
                            generate_name="generate_name_example",
                            generation=1,
                            labels={
                                "key": "key_example",
                            },
                            managed_fields=[
                                V1ManagedFieldsEntry(
                                    api_version="api_version_example",
                                    fields_type="fields_type_example",
                                    fields_v1={},
                                    manager="manager_example",
                                    operation="operation_example",
                                    subresource="subresource_example",
                                    time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                ),
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
                                ),
                            ],
                            resource_version="resource_version_example",
                            self_link="self_link_example",
                            uid="uid_example",
                        ),
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
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            weight=1,
                                        ),
                                    ],
                                    required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                        node_selector_terms=[
                                            V1NodeSelectorTerm(
                                                match_expressions=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                                pod_affinity=V1PodAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespace_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespaces=[
                                                    "namespaces_example",
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        ),
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm(
                                            label_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespace_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespaces=[
                                                "namespaces_example",
                                            ],
                                            topology_key="topology_key_example",
                                        ),
                                    ],
                                ),
                                pod_anti_affinity=V1PodAntiAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespace_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespaces=[
                                                    "namespaces_example",
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        ),
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm(
                                            label_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespace_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespaces=[
                                                "namespaces_example",
                                            ],
                                            topology_key="topology_key_example",
                                        ),
                                    ],
                                ),
                            ),
                            automount_service_account_token=True,
                            containers=[
                                V1Container(
                                    args=[
                                        "args_example",
                                    ],
                                    command=[
                                        "command_example",
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
                                        ),
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
                                        ),
                                    ],
                                    image="image_example",
                                    image_pull_policy="Always",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
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
                                            protocol="SCTP",
                                        ),
                                    ],
                                    readiness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    resources=V1ResourceRequirements(
                                        limits={
                                            "key": "key_example",
                                        },
                                        requests={
                                            "key": "key_example",
                                        },
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example",
                                            ],
                                            drop=[
                                                "drop_example",
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
                                            type="Localhost",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="FallbackToLogsOnError",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        ),
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        ),
                                    ],
                                    working_dir="working_dir_example",
                                ),
                            ],
                            dns_config=V1PodDNSConfig(
                                nameservers=[
                                    "nameservers_example",
                                ],
                                options=[
                                    V1PodDNSConfigOption(
                                        name="name_example",
                                        value="value_example",
                                    ),
                                ],
                                searches=[
                                    "searches_example",
                                ],
                            ),
                            dns_policy="ClusterFirst",
                            enable_service_links=True,
                            ephemeral_containers=[
                                V1EphemeralContainer(
                                    args=[
                                        "args_example",
                                    ],
                                    command=[
                                        "command_example",
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
                                        ),
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
                                        ),
                                    ],
                                    image="image_example",
                                    image_pull_policy="Always",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
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
                                            protocol="SCTP",
                                        ),
                                    ],
                                    readiness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    resources=V1ResourceRequirements(
                                        limits={
                                            "key": "key_example",
                                        },
                                        requests={
                                            "key": "key_example",
                                        },
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example",
                                            ],
                                            drop=[
                                                "drop_example",
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
                                            type="Localhost",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    stdin=True,
                                    stdin_once=True,
                                    target_container_name="target_container_name_example",
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="FallbackToLogsOnError",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        ),
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        ),
                                    ],
                                    working_dir="working_dir_example",
                                ),
                            ],
                            host_aliases=[
                                V1HostAlias(
                                    hostnames=[
                                        "hostnames_example",
                                    ],
                                    ip="ip_example",
                                ),
                            ],
                            host_ipc=True,
                            host_network=True,
                            host_pid=True,
                            hostname="hostname_example",
                            image_pull_secrets=[
                                V1LocalObjectReference(
                                    name="name_example",
                                ),
                            ],
                            init_containers=[
                                V1Container(
                                    args=[
                                        "args_example",
                                    ],
                                    command=[
                                        "command_example",
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
                                        ),
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
                                        ),
                                    ],
                                    image="image_example",
                                    image_pull_policy="Always",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
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
                                            protocol="SCTP",
                                        ),
                                    ],
                                    readiness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    resources=V1ResourceRequirements(
                                        limits={
                                            "key": "key_example",
                                        },
                                        requests={
                                            "key": "key_example",
                                        },
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example",
                                            ],
                                            drop=[
                                                "drop_example",
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
                                            type="Localhost",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="FallbackToLogsOnError",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        ),
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        ),
                                    ],
                                    working_dir="working_dir_example",
                                ),
                            ],
                            node_name="node_name_example",
                            node_selector={
                                "key": "key_example",
                            },
                            os=V1PodOS(
                                name="name_example",
                            ),
                            overhead={
                                "key": "key_example",
                            },
                            preemption_policy="preemption_policy_example",
                            priority=1,
                            priority_class_name="priority_class_name_example",
                            readiness_gates=[
                                V1PodReadinessGate(
                                    condition_type="ContainersReady",
                                ),
                            ],
                            restart_policy="Always",
                            runtime_class_name="runtime_class_name_example",
                            scheduler_name="scheduler_name_example",
                            security_context=V1PodSecurityContext(
                                fs_group=1,
                                fs_group_change_policy="fs_group_change_policy_example",
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
                                    type="Localhost",
                                ),
                                supplemental_groups=[
                                    1,
                                ],
                                sysctls=[
                                    V1Sysctl(
                                        name="name_example",
                                        value="value_example",
                                    ),
                                ],
                                windows_options=V1WindowsSecurityContextOptions(
                                    gmsa_credential_spec="gmsa_credential_spec_example",
                                    gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                    host_process=True,
                                    run_as_user_name="run_as_user_name_example",
                                ),
                            ),
                            service_account="service_account_example",
                            service_account_name="service_account_name_example",
                            set_hostname_as_fqdn=True,
                            share_process_namespace=True,
                            subdomain="subdomain_example",
                            termination_grace_period_seconds=1,
                            tolerations=[
                                V1Toleration(
                                    effect="NoExecute",
                                    key="key_example",
                                    operator="Equal",
                                    toleration_seconds=1,
                                    value="value_example",
                                ),
                            ],
                            topology_spread_constraints=[
                                V1TopologySpreadConstraint(
                                    label_selector=V1LabelSelector(
                                        match_expressions=[
                                            V1LabelSelectorRequirement(
                                                key="key_example",
                                                operator="operator_example",
                                                values=[
                                                    "values_example",
                                                ],
                                            ),
                                        ],
                                        match_labels={
                                            "key": "key_example",
                                        },
                                    ),
                                    max_skew=1,
                                    topology_key="topology_key_example",
                                    when_unsatisfiable="DoNotSchedule",
                                ),
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
                                            "monitors_example",
                                        ],
                                        path="path_example",
                                        read_only=True,
                                        secret_file="secret_file_example",
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        user="user_example",
                                    ),
                                    cinder=V1CinderVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        volume_id="volume_id_example",
                                    ),
                                    config_map=V1ConfigMapVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            ),
                                        ],
                                        name="name_example",
                                        optional=True,
                                    ),
                                    csi=V1CSIVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        node_publish_secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        read_only=True,
                                        volume_attributes={
                                            "key": "key_example",
                                        },
                                    ),
                                    downward_api=V1DownwardAPIVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1DownwardAPIVolumeFile(
                                                field_ref=V1ObjectFieldSelector(
                                                    api_version="api_version_example",
                                                    field_path="field_path_example",
                                                ),
                                                mode=1,
                                                path="path_example",
                                                resource_field_ref=V1ResourceFieldSelector(
                                                    container_name="container_name_example",
                                                    divisor="divisor_example",
                                                    resource="resource_example",
                                                ),
                                            ),
                                        ],
                                    ),
                                    empty_dir=V1EmptyDirVolumeSource(
                                        medium="medium_example",
                                        size_limit="size_limit_example",
                                    ),
                                    ephemeral=V1EphemeralVolumeSource(
                                        volume_claim_template=V1PersistentVolumeClaimTemplate(
                                            metadata=V1ObjectMeta(
                                                annotations={
                                                    "key": "key_example",
                                                },
                                                cluster_name="cluster_name_example",
                                                creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                                deletion_grace_period_seconds=1,
                                                deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                                finalizers=[
                                                    "finalizers_example",
                                                ],
                                                generate_name="generate_name_example",
                                                generation=1,
                                                labels={
                                                    "key": "key_example",
                                                },
                                                managed_fields=[
                                                    V1ManagedFieldsEntry(
                                                        api_version="api_version_example",
                                                        fields_type="fields_type_example",
                                                        fields_v1={},
                                                        manager="manager_example",
                                                        operation="operation_example",
                                                        subresource="subresource_example",
                                                        time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                                    ),
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
                                                    ),
                                                ],
                                                resource_version="resource_version_example",
                                                self_link="self_link_example",
                                                uid="uid_example",
                                            ),
                                            spec=V1PersistentVolumeClaimSpec(
                                                access_modes=[
                                                    "access_modes_example",
                                                ],
                                                data_source=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
                                                data_source_ref=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
                                                resources=V1ResourceRequirements(
                                                    limits={
                                                        "key": "key_example",
                                                    },
                                                    requests={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
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
                                            "target_wwns_example",
                                        ],
                                        wwids=[
                                            "wwids_example",
                                        ],
                                    ),
                                    flex_volume=V1FlexVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        options={
                                            "key": "key_example",
                                        },
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
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
                                            "portals_example",
                                        ],
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
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
                                                    items=[
                                                        V1KeyToPath(
                                                            key="key_example",
                                                            mode=1,
                                                            path="path_example",
                                                        ),
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                downward_api=V1DownwardAPIProjection(
                                                    items=[
                                                        V1DownwardAPIVolumeFile(
                                                            field_ref=V1ObjectFieldSelector(
                                                                api_version="api_version_example",
                                                                field_path="field_path_example",
                                                            ),
                                                            mode=1,
                                                            path="path_example",
                                                            resource_field_ref=V1ResourceFieldSelector(
                                                                container_name="container_name_example",
                                                                divisor="divisor_example",
                                                                resource="resource_example",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                secret=V1SecretProjection(
                                                    items=[
                                                        V1KeyToPath(
                                                            key="key_example",
                                                            mode=1,
                                                            path="path_example",
                                                        ),
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                service_account_token=V1ServiceAccountTokenProjection(
                                                    audience="audience_example",
                                                    expiration_seconds=1,
                                                    path="path_example",
                                                ),
                                            ),
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
                                            "monitors_example",
                                        ],
                                        pool="pool_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        user="user_example",
                                    ),
                                    scale_io=V1ScaleIOVolumeSource(
                                        fs_type="fs_type_example",
                                        gateway="gateway_example",
                                        protection_domain="protection_domain_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        ssl_enabled=True,
                                        storage_mode="storage_mode_example",
                                        storage_pool="storage_pool_example",
                                        system="system_example",
                                        volume_name="volume_name_example",
                                    ),
                                    secret=V1SecretVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            ),
                                        ],
                                        optional=True,
                                        secret_name="secret_name_example",
                                    ),
                                    storageos=V1StorageOSVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        volume_name="volume_name_example",
                                        volume_namespace="volume_namespace_example",
                                    ),
                                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        storage_policy_id="storage_policy_id_example",
                                        storage_policy_name="storage_policy_name_example",
                                        volume_path="volume_path_example",
                                    ),
                                ),
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
        ),
        status=V1beta1CronJobStatus(
            active=[
                V1ObjectReference(
                    api_version="api_version_example",
                    field_path="field_path_example",
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    resource_version="resource_version_example",
                    uid="uid_example",
                ),
            ],
            last_schedule_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_successful_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # V1beta1CronJob | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
    field_validation = "fieldValidation_example" # str | fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the `ServerSideFieldValidation` feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_namespaced_cron_job(name, namespace, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->replace_namespaced_cron_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_namespaced_cron_job(name, namespace, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, field_validation=field_validation)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->replace_namespaced_cron_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob |
 **namespace** | **str**| object name and auth scope, such as for teams and projects |
 **body** | [**V1beta1CronJob**](V1beta1CronJob.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]
 **field_validation** | **str**| fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the &#x60;ServerSideFieldValidation&#x60; feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. | [optional]

### Return type

[**V1beta1CronJob**](V1beta1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_cron_job_status**
> V1beta1CronJob replace_namespaced_cron_job_status(name, namespace, body)



replace status of the specified CronJob

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import batch_v1beta1_api
from kubernetes.client.model.v1beta1_cron_job import V1beta1CronJob
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
    api_instance = batch_v1beta1_api.BatchV1beta1Api(api_client)
    name = "name_example" # str | name of the CronJob
    namespace = "namespace_example" # str | object name and auth scope, such as for teams and projects
    body = V1beta1CronJob(
        api_version="api_version_example",
        kind="kind_example",
        metadata=V1ObjectMeta(
            annotations={
                "key": "key_example",
            },
            cluster_name="cluster_name_example",
            creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
            deletion_grace_period_seconds=1,
            deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
            finalizers=[
                "finalizers_example",
            ],
            generate_name="generate_name_example",
            generation=1,
            labels={
                "key": "key_example",
            },
            managed_fields=[
                V1ManagedFieldsEntry(
                    api_version="api_version_example",
                    fields_type="fields_type_example",
                    fields_v1={},
                    manager="manager_example",
                    operation="operation_example",
                    subresource="subresource_example",
                    time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
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
                ),
            ],
            resource_version="resource_version_example",
            self_link="self_link_example",
            uid="uid_example",
        ),
        spec=V1beta1CronJobSpec(
            concurrency_policy="concurrency_policy_example",
            failed_jobs_history_limit=1,
            job_template=V1beta1JobTemplateSpec(
                metadata=V1ObjectMeta(
                    annotations={
                        "key": "key_example",
                    },
                    cluster_name="cluster_name_example",
                    creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    deletion_grace_period_seconds=1,
                    deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    finalizers=[
                        "finalizers_example",
                    ],
                    generate_name="generate_name_example",
                    generation=1,
                    labels={
                        "key": "key_example",
                    },
                    managed_fields=[
                        V1ManagedFieldsEntry(
                            api_version="api_version_example",
                            fields_type="fields_type_example",
                            fields_v1={},
                            manager="manager_example",
                            operation="operation_example",
                            subresource="subresource_example",
                            time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        ),
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
                        ),
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
                    selector=V1LabelSelector(
                        match_expressions=[
                            V1LabelSelectorRequirement(
                                key="key_example",
                                operator="operator_example",
                                values=[
                                    "values_example",
                                ],
                            ),
                        ],
                        match_labels={
                            "key": "key_example",
                        },
                    ),
                    suspend=True,
                    template=V1PodTemplateSpec(
                        metadata=V1ObjectMeta(
                            annotations={
                                "key": "key_example",
                            },
                            cluster_name="cluster_name_example",
                            creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            deletion_grace_period_seconds=1,
                            deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                            finalizers=[
                                "finalizers_example",
                            ],
                            generate_name="generate_name_example",
                            generation=1,
                            labels={
                                "key": "key_example",
                            },
                            managed_fields=[
                                V1ManagedFieldsEntry(
                                    api_version="api_version_example",
                                    fields_type="fields_type_example",
                                    fields_v1={},
                                    manager="manager_example",
                                    operation="operation_example",
                                    subresource="subresource_example",
                                    time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                ),
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
                                ),
                            ],
                            resource_version="resource_version_example",
                            self_link="self_link_example",
                            uid="uid_example",
                        ),
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
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                            ),
                                            weight=1,
                                        ),
                                    ],
                                    required_during_scheduling_ignored_during_execution=V1NodeSelector(
                                        node_selector_terms=[
                                            V1NodeSelectorTerm(
                                                match_expressions=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_fields=[
                                                    V1NodeSelectorRequirement(
                                                        key="key_example",
                                                        operator="DoesNotExist",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                                pod_affinity=V1PodAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespace_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespaces=[
                                                    "namespaces_example",
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        ),
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm(
                                            label_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespace_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespaces=[
                                                "namespaces_example",
                                            ],
                                            topology_key="topology_key_example",
                                        ),
                                    ],
                                ),
                                pod_anti_affinity=V1PodAntiAffinity(
                                    preferred_during_scheduling_ignored_during_execution=[
                                        V1WeightedPodAffinityTerm(
                                            pod_affinity_term=V1PodAffinityTerm(
                                                label_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespace_selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                namespaces=[
                                                    "namespaces_example",
                                                ],
                                                topology_key="topology_key_example",
                                            ),
                                            weight=1,
                                        ),
                                    ],
                                    required_during_scheduling_ignored_during_execution=[
                                        V1PodAffinityTerm(
                                            label_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespace_selector=V1LabelSelector(
                                                match_expressions=[
                                                    V1LabelSelectorRequirement(
                                                        key="key_example",
                                                        operator="operator_example",
                                                        values=[
                                                            "values_example",
                                                        ],
                                                    ),
                                                ],
                                                match_labels={
                                                    "key": "key_example",
                                                },
                                            ),
                                            namespaces=[
                                                "namespaces_example",
                                            ],
                                            topology_key="topology_key_example",
                                        ),
                                    ],
                                ),
                            ),
                            automount_service_account_token=True,
                            containers=[
                                V1Container(
                                    args=[
                                        "args_example",
                                    ],
                                    command=[
                                        "command_example",
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
                                        ),
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
                                        ),
                                    ],
                                    image="image_example",
                                    image_pull_policy="Always",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
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
                                            protocol="SCTP",
                                        ),
                                    ],
                                    readiness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    resources=V1ResourceRequirements(
                                        limits={
                                            "key": "key_example",
                                        },
                                        requests={
                                            "key": "key_example",
                                        },
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example",
                                            ],
                                            drop=[
                                                "drop_example",
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
                                            type="Localhost",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="FallbackToLogsOnError",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        ),
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        ),
                                    ],
                                    working_dir="working_dir_example",
                                ),
                            ],
                            dns_config=V1PodDNSConfig(
                                nameservers=[
                                    "nameservers_example",
                                ],
                                options=[
                                    V1PodDNSConfigOption(
                                        name="name_example",
                                        value="value_example",
                                    ),
                                ],
                                searches=[
                                    "searches_example",
                                ],
                            ),
                            dns_policy="ClusterFirst",
                            enable_service_links=True,
                            ephemeral_containers=[
                                V1EphemeralContainer(
                                    args=[
                                        "args_example",
                                    ],
                                    command=[
                                        "command_example",
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
                                        ),
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
                                        ),
                                    ],
                                    image="image_example",
                                    image_pull_policy="Always",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
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
                                            protocol="SCTP",
                                        ),
                                    ],
                                    readiness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    resources=V1ResourceRequirements(
                                        limits={
                                            "key": "key_example",
                                        },
                                        requests={
                                            "key": "key_example",
                                        },
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example",
                                            ],
                                            drop=[
                                                "drop_example",
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
                                            type="Localhost",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    stdin=True,
                                    stdin_once=True,
                                    target_container_name="target_container_name_example",
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="FallbackToLogsOnError",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        ),
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        ),
                                    ],
                                    working_dir="working_dir_example",
                                ),
                            ],
                            host_aliases=[
                                V1HostAlias(
                                    hostnames=[
                                        "hostnames_example",
                                    ],
                                    ip="ip_example",
                                ),
                            ],
                            host_ipc=True,
                            host_network=True,
                            host_pid=True,
                            hostname="hostname_example",
                            image_pull_secrets=[
                                V1LocalObjectReference(
                                    name="name_example",
                                ),
                            ],
                            init_containers=[
                                V1Container(
                                    args=[
                                        "args_example",
                                    ],
                                    command=[
                                        "command_example",
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
                                        ),
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
                                        ),
                                    ],
                                    image="image_example",
                                    image_pull_policy="Always",
                                    lifecycle=V1Lifecycle(
                                        post_start=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                        pre_stop=V1LifecycleHandler(
                                            _exec=V1ExecAction(
                                                command=[
                                                    "command_example",
                                                ],
                                            ),
                                            http_get=V1HTTPGetAction(
                                                host="host_example",
                                                http_headers=[
                                                    V1HTTPHeader(
                                                        name="name_example",
                                                        value="value_example",
                                                    ),
                                                ],
                                                path="path_example",
                                                port={},
                                                scheme="HTTP",
                                            ),
                                            tcp_socket=V1TCPSocketAction(
                                                host="host_example",
                                                port={},
                                            ),
                                        ),
                                    ),
                                    liveness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
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
                                            protocol="SCTP",
                                        ),
                                    ],
                                    readiness_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    resources=V1ResourceRequirements(
                                        limits={
                                            "key": "key_example",
                                        },
                                        requests={
                                            "key": "key_example",
                                        },
                                    ),
                                    security_context=V1SecurityContext(
                                        allow_privilege_escalation=True,
                                        capabilities=V1Capabilities(
                                            add=[
                                                "add_example",
                                            ],
                                            drop=[
                                                "drop_example",
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
                                            type="Localhost",
                                        ),
                                        windows_options=V1WindowsSecurityContextOptions(
                                            gmsa_credential_spec="gmsa_credential_spec_example",
                                            gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                            host_process=True,
                                            run_as_user_name="run_as_user_name_example",
                                        ),
                                    ),
                                    startup_probe=V1Probe(
                                        _exec=V1ExecAction(
                                            command=[
                                                "command_example",
                                            ],
                                        ),
                                        failure_threshold=1,
                                        grpc=V1GRPCAction(
                                            port=1,
                                            service="service_example",
                                        ),
                                        http_get=V1HTTPGetAction(
                                            host="host_example",
                                            http_headers=[
                                                V1HTTPHeader(
                                                    name="name_example",
                                                    value="value_example",
                                                ),
                                            ],
                                            path="path_example",
                                            port={},
                                            scheme="HTTP",
                                        ),
                                        initial_delay_seconds=1,
                                        period_seconds=1,
                                        success_threshold=1,
                                        tcp_socket=V1TCPSocketAction(
                                            host="host_example",
                                            port={},
                                        ),
                                        termination_grace_period_seconds=1,
                                        timeout_seconds=1,
                                    ),
                                    stdin=True,
                                    stdin_once=True,
                                    termination_message_path="termination_message_path_example",
                                    termination_message_policy="FallbackToLogsOnError",
                                    tty=True,
                                    volume_devices=[
                                        V1VolumeDevice(
                                            device_path="device_path_example",
                                            name="name_example",
                                        ),
                                    ],
                                    volume_mounts=[
                                        V1VolumeMount(
                                            mount_path="mount_path_example",
                                            mount_propagation="mount_propagation_example",
                                            name="name_example",
                                            read_only=True,
                                            sub_path="sub_path_example",
                                            sub_path_expr="sub_path_expr_example",
                                        ),
                                    ],
                                    working_dir="working_dir_example",
                                ),
                            ],
                            node_name="node_name_example",
                            node_selector={
                                "key": "key_example",
                            },
                            os=V1PodOS(
                                name="name_example",
                            ),
                            overhead={
                                "key": "key_example",
                            },
                            preemption_policy="preemption_policy_example",
                            priority=1,
                            priority_class_name="priority_class_name_example",
                            readiness_gates=[
                                V1PodReadinessGate(
                                    condition_type="ContainersReady",
                                ),
                            ],
                            restart_policy="Always",
                            runtime_class_name="runtime_class_name_example",
                            scheduler_name="scheduler_name_example",
                            security_context=V1PodSecurityContext(
                                fs_group=1,
                                fs_group_change_policy="fs_group_change_policy_example",
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
                                    type="Localhost",
                                ),
                                supplemental_groups=[
                                    1,
                                ],
                                sysctls=[
                                    V1Sysctl(
                                        name="name_example",
                                        value="value_example",
                                    ),
                                ],
                                windows_options=V1WindowsSecurityContextOptions(
                                    gmsa_credential_spec="gmsa_credential_spec_example",
                                    gmsa_credential_spec_name="gmsa_credential_spec_name_example",
                                    host_process=True,
                                    run_as_user_name="run_as_user_name_example",
                                ),
                            ),
                            service_account="service_account_example",
                            service_account_name="service_account_name_example",
                            set_hostname_as_fqdn=True,
                            share_process_namespace=True,
                            subdomain="subdomain_example",
                            termination_grace_period_seconds=1,
                            tolerations=[
                                V1Toleration(
                                    effect="NoExecute",
                                    key="key_example",
                                    operator="Equal",
                                    toleration_seconds=1,
                                    value="value_example",
                                ),
                            ],
                            topology_spread_constraints=[
                                V1TopologySpreadConstraint(
                                    label_selector=V1LabelSelector(
                                        match_expressions=[
                                            V1LabelSelectorRequirement(
                                                key="key_example",
                                                operator="operator_example",
                                                values=[
                                                    "values_example",
                                                ],
                                            ),
                                        ],
                                        match_labels={
                                            "key": "key_example",
                                        },
                                    ),
                                    max_skew=1,
                                    topology_key="topology_key_example",
                                    when_unsatisfiable="DoNotSchedule",
                                ),
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
                                            "monitors_example",
                                        ],
                                        path="path_example",
                                        read_only=True,
                                        secret_file="secret_file_example",
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        user="user_example",
                                    ),
                                    cinder=V1CinderVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        volume_id="volume_id_example",
                                    ),
                                    config_map=V1ConfigMapVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            ),
                                        ],
                                        name="name_example",
                                        optional=True,
                                    ),
                                    csi=V1CSIVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        node_publish_secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        read_only=True,
                                        volume_attributes={
                                            "key": "key_example",
                                        },
                                    ),
                                    downward_api=V1DownwardAPIVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1DownwardAPIVolumeFile(
                                                field_ref=V1ObjectFieldSelector(
                                                    api_version="api_version_example",
                                                    field_path="field_path_example",
                                                ),
                                                mode=1,
                                                path="path_example",
                                                resource_field_ref=V1ResourceFieldSelector(
                                                    container_name="container_name_example",
                                                    divisor="divisor_example",
                                                    resource="resource_example",
                                                ),
                                            ),
                                        ],
                                    ),
                                    empty_dir=V1EmptyDirVolumeSource(
                                        medium="medium_example",
                                        size_limit="size_limit_example",
                                    ),
                                    ephemeral=V1EphemeralVolumeSource(
                                        volume_claim_template=V1PersistentVolumeClaimTemplate(
                                            metadata=V1ObjectMeta(
                                                annotations={
                                                    "key": "key_example",
                                                },
                                                cluster_name="cluster_name_example",
                                                creation_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                                deletion_grace_period_seconds=1,
                                                deletion_timestamp=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                                finalizers=[
                                                    "finalizers_example",
                                                ],
                                                generate_name="generate_name_example",
                                                generation=1,
                                                labels={
                                                    "key": "key_example",
                                                },
                                                managed_fields=[
                                                    V1ManagedFieldsEntry(
                                                        api_version="api_version_example",
                                                        fields_type="fields_type_example",
                                                        fields_v1={},
                                                        manager="manager_example",
                                                        operation="operation_example",
                                                        subresource="subresource_example",
                                                        time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                                                    ),
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
                                                    ),
                                                ],
                                                resource_version="resource_version_example",
                                                self_link="self_link_example",
                                                uid="uid_example",
                                            ),
                                            spec=V1PersistentVolumeClaimSpec(
                                                access_modes=[
                                                    "access_modes_example",
                                                ],
                                                data_source=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
                                                data_source_ref=V1TypedLocalObjectReference(
                                                    api_group="api_group_example",
                                                    kind="kind_example",
                                                    name="name_example",
                                                ),
                                                resources=V1ResourceRequirements(
                                                    limits={
                                                        "key": "key_example",
                                                    },
                                                    requests={
                                                        "key": "key_example",
                                                    },
                                                ),
                                                selector=V1LabelSelector(
                                                    match_expressions=[
                                                        V1LabelSelectorRequirement(
                                                            key="key_example",
                                                            operator="operator_example",
                                                            values=[
                                                                "values_example",
                                                            ],
                                                        ),
                                                    ],
                                                    match_labels={
                                                        "key": "key_example",
                                                    },
                                                ),
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
                                            "target_wwns_example",
                                        ],
                                        wwids=[
                                            "wwids_example",
                                        ],
                                    ),
                                    flex_volume=V1FlexVolumeSource(
                                        driver="driver_example",
                                        fs_type="fs_type_example",
                                        options={
                                            "key": "key_example",
                                        },
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
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
                                            "portals_example",
                                        ],
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
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
                                                    items=[
                                                        V1KeyToPath(
                                                            key="key_example",
                                                            mode=1,
                                                            path="path_example",
                                                        ),
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                downward_api=V1DownwardAPIProjection(
                                                    items=[
                                                        V1DownwardAPIVolumeFile(
                                                            field_ref=V1ObjectFieldSelector(
                                                                api_version="api_version_example",
                                                                field_path="field_path_example",
                                                            ),
                                                            mode=1,
                                                            path="path_example",
                                                            resource_field_ref=V1ResourceFieldSelector(
                                                                container_name="container_name_example",
                                                                divisor="divisor_example",
                                                                resource="resource_example",
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                                secret=V1SecretProjection(
                                                    items=[
                                                        V1KeyToPath(
                                                            key="key_example",
                                                            mode=1,
                                                            path="path_example",
                                                        ),
                                                    ],
                                                    name="name_example",
                                                    optional=True,
                                                ),
                                                service_account_token=V1ServiceAccountTokenProjection(
                                                    audience="audience_example",
                                                    expiration_seconds=1,
                                                    path="path_example",
                                                ),
                                            ),
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
                                            "monitors_example",
                                        ],
                                        pool="pool_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        user="user_example",
                                    ),
                                    scale_io=V1ScaleIOVolumeSource(
                                        fs_type="fs_type_example",
                                        gateway="gateway_example",
                                        protection_domain="protection_domain_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        ssl_enabled=True,
                                        storage_mode="storage_mode_example",
                                        storage_pool="storage_pool_example",
                                        system="system_example",
                                        volume_name="volume_name_example",
                                    ),
                                    secret=V1SecretVolumeSource(
                                        default_mode=1,
                                        items=[
                                            V1KeyToPath(
                                                key="key_example",
                                                mode=1,
                                                path="path_example",
                                            ),
                                        ],
                                        optional=True,
                                        secret_name="secret_name_example",
                                    ),
                                    storageos=V1StorageOSVolumeSource(
                                        fs_type="fs_type_example",
                                        read_only=True,
                                        secret_ref=V1LocalObjectReference(
                                            name="name_example",
                                        ),
                                        volume_name="volume_name_example",
                                        volume_namespace="volume_namespace_example",
                                    ),
                                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                                        fs_type="fs_type_example",
                                        storage_policy_id="storage_policy_id_example",
                                        storage_policy_name="storage_policy_name_example",
                                        volume_path="volume_path_example",
                                    ),
                                ),
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
        ),
        status=V1beta1CronJobStatus(
            active=[
                V1ObjectReference(
                    api_version="api_version_example",
                    field_path="field_path_example",
                    kind="kind_example",
                    name="name_example",
                    namespace="namespace_example",
                    resource_version="resource_version_example",
                    uid="uid_example",
                ),
            ],
            last_schedule_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            last_successful_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # V1beta1CronJob | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
    field_validation = "fieldValidation_example" # str | fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the `ServerSideFieldValidation` feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_namespaced_cron_job_status(name, namespace, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->replace_namespaced_cron_job_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_namespaced_cron_job_status(name, namespace, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, field_validation=field_validation)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling BatchV1beta1Api->replace_namespaced_cron_job_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob |
 **namespace** | **str**| object name and auth scope, such as for teams and projects |
 **body** | [**V1beta1CronJob**](V1beta1CronJob.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]
 **field_validation** | **str**| fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the &#x60;ServerSideFieldValidation&#x60; feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. | [optional]

### Return type

[**V1beta1CronJob**](V1beta1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | Created |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

