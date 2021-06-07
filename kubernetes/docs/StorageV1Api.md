# kubernetes.client.StorageV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_csi_driver**](StorageV1Api.md#create_csi_driver) | **POST** /apis/storage.k8s.io/v1/csidrivers | 
[**create_csi_node**](StorageV1Api.md#create_csi_node) | **POST** /apis/storage.k8s.io/v1/csinodes | 
[**create_storage_class**](StorageV1Api.md#create_storage_class) | **POST** /apis/storage.k8s.io/v1/storageclasses | 
[**create_volume_attachment**](StorageV1Api.md#create_volume_attachment) | **POST** /apis/storage.k8s.io/v1/volumeattachments | 
[**delete_collection_csi_driver**](StorageV1Api.md#delete_collection_csi_driver) | **DELETE** /apis/storage.k8s.io/v1/csidrivers | 
[**delete_collection_csi_node**](StorageV1Api.md#delete_collection_csi_node) | **DELETE** /apis/storage.k8s.io/v1/csinodes | 
[**delete_collection_storage_class**](StorageV1Api.md#delete_collection_storage_class) | **DELETE** /apis/storage.k8s.io/v1/storageclasses | 
[**delete_collection_volume_attachment**](StorageV1Api.md#delete_collection_volume_attachment) | **DELETE** /apis/storage.k8s.io/v1/volumeattachments | 
[**delete_csi_driver**](StorageV1Api.md#delete_csi_driver) | **DELETE** /apis/storage.k8s.io/v1/csidrivers/{name} | 
[**delete_csi_node**](StorageV1Api.md#delete_csi_node) | **DELETE** /apis/storage.k8s.io/v1/csinodes/{name} | 
[**delete_storage_class**](StorageV1Api.md#delete_storage_class) | **DELETE** /apis/storage.k8s.io/v1/storageclasses/{name} | 
[**delete_volume_attachment**](StorageV1Api.md#delete_volume_attachment) | **DELETE** /apis/storage.k8s.io/v1/volumeattachments/{name} | 
[**get_api_resources**](StorageV1Api.md#get_api_resources) | **GET** /apis/storage.k8s.io/v1/ | 
[**list_csi_driver**](StorageV1Api.md#list_csi_driver) | **GET** /apis/storage.k8s.io/v1/csidrivers | 
[**list_csi_node**](StorageV1Api.md#list_csi_node) | **GET** /apis/storage.k8s.io/v1/csinodes | 
[**list_storage_class**](StorageV1Api.md#list_storage_class) | **GET** /apis/storage.k8s.io/v1/storageclasses | 
[**list_volume_attachment**](StorageV1Api.md#list_volume_attachment) | **GET** /apis/storage.k8s.io/v1/volumeattachments | 
[**patch_csi_driver**](StorageV1Api.md#patch_csi_driver) | **PATCH** /apis/storage.k8s.io/v1/csidrivers/{name} | 
[**patch_csi_node**](StorageV1Api.md#patch_csi_node) | **PATCH** /apis/storage.k8s.io/v1/csinodes/{name} | 
[**patch_storage_class**](StorageV1Api.md#patch_storage_class) | **PATCH** /apis/storage.k8s.io/v1/storageclasses/{name} | 
[**patch_volume_attachment**](StorageV1Api.md#patch_volume_attachment) | **PATCH** /apis/storage.k8s.io/v1/volumeattachments/{name} | 
[**patch_volume_attachment_status**](StorageV1Api.md#patch_volume_attachment_status) | **PATCH** /apis/storage.k8s.io/v1/volumeattachments/{name}/status | 
[**read_csi_driver**](StorageV1Api.md#read_csi_driver) | **GET** /apis/storage.k8s.io/v1/csidrivers/{name} | 
[**read_csi_node**](StorageV1Api.md#read_csi_node) | **GET** /apis/storage.k8s.io/v1/csinodes/{name} | 
[**read_storage_class**](StorageV1Api.md#read_storage_class) | **GET** /apis/storage.k8s.io/v1/storageclasses/{name} | 
[**read_volume_attachment**](StorageV1Api.md#read_volume_attachment) | **GET** /apis/storage.k8s.io/v1/volumeattachments/{name} | 
[**read_volume_attachment_status**](StorageV1Api.md#read_volume_attachment_status) | **GET** /apis/storage.k8s.io/v1/volumeattachments/{name}/status | 
[**replace_csi_driver**](StorageV1Api.md#replace_csi_driver) | **PUT** /apis/storage.k8s.io/v1/csidrivers/{name} | 
[**replace_csi_node**](StorageV1Api.md#replace_csi_node) | **PUT** /apis/storage.k8s.io/v1/csinodes/{name} | 
[**replace_storage_class**](StorageV1Api.md#replace_storage_class) | **PUT** /apis/storage.k8s.io/v1/storageclasses/{name} | 
[**replace_volume_attachment**](StorageV1Api.md#replace_volume_attachment) | **PUT** /apis/storage.k8s.io/v1/volumeattachments/{name} | 
[**replace_volume_attachment_status**](StorageV1Api.md#replace_volume_attachment_status) | **PUT** /apis/storage.k8s.io/v1/volumeattachments/{name}/status | 


# **create_csi_driver**
> V1CSIDriver create_csi_driver(body)



create a CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_csi_driver import V1CSIDriver
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    body = V1CSIDriver(
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
        spec=V1CSIDriverSpec(
            attach_required=True,
            pod_info_on_mount=True,
            volume_lifecycle_modes=[
                "volume_lifecycle_modes_example",
            ],
        ),
    ) # V1CSIDriver | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_csi_driver(body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_csi_driver: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_csi_driver(body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_csi_driver: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CSIDriver**](V1CSIDriver.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1CSIDriver**](V1CSIDriver.md)

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

# **create_csi_node**
> V1CSINode create_csi_node(body)



create a CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_csi_node import V1CSINode
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    body = V1CSINode(
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
        spec=V1CSINodeSpec(
            drivers=[
                V1CSINodeDriver(
                    allocatable=V1VolumeNodeResources(
                        count=1,
                    ),
                    name="name_example",
                    node_id="node_id_example",
                    topology_keys=[
                        "topology_keys_example",
                    ],
                ),
            ],
        ),
    ) # V1CSINode | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_csi_node(body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_csi_node: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_csi_node(body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_csi_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1CSINode**](V1CSINode.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1CSINode**](V1CSINode.md)

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

# **create_storage_class**
> V1StorageClass create_storage_class(body)



create a StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_storage_class import V1StorageClass
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    body = V1StorageClass(
        allow_volume_expansion=True,
        allowed_topologies=[
            V1TopologySelectorTerm(
                match_label_expressions=[
                    V1TopologySelectorLabelRequirement(
                        key="key_example",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
        ],
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
        mount_options=[
            "mount_options_example",
        ],
        parameters={
            "key": "key_example",
        },
        provisioner="provisioner_example",
        reclaim_policy="reclaim_policy_example",
        volume_binding_mode="volume_binding_mode_example",
    ) # V1StorageClass | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_storage_class(body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_storage_class: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_storage_class(body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_storage_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1StorageClass**](V1StorageClass.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1StorageClass**](V1StorageClass.md)

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

# **create_volume_attachment**
> V1VolumeAttachment create_volume_attachment(body)



create a VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_volume_attachment import V1VolumeAttachment
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    body = V1VolumeAttachment(
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
        spec=V1VolumeAttachmentSpec(
            attacher="attacher_example",
            node_name="node_name_example",
            source=V1VolumeAttachmentSource(
                inline_volume_spec=V1PersistentVolumeSpec(
                    access_modes=[
                        "access_modes_example",
                    ],
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
                    azure_file=V1AzureFilePersistentVolumeSource(
                        read_only=True,
                        secret_name="secret_name_example",
                        secret_namespace="secret_namespace_example",
                        share_name="share_name_example",
                    ),
                    capacity={
                        "key": "key_example",
                    },
                    cephfs=V1CephFSPersistentVolumeSource(
                        monitors=[
                            "monitors_example",
                        ],
                        path="path_example",
                        read_only=True,
                        secret_file="secret_file_example",
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        user="user_example",
                    ),
                    cinder=V1CinderPersistentVolumeSource(
                        fs_type="fs_type_example",
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        volume_id="volume_id_example",
                    ),
                    claim_ref=V1ObjectReference(
                        api_version="api_version_example",
                        field_path="field_path_example",
                        kind="kind_example",
                        name="name_example",
                        namespace="namespace_example",
                        resource_version="resource_version_example",
                        uid="uid_example",
                    ),
                    csi=V1CSIPersistentVolumeSource(
                        controller_expand_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        controller_publish_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        driver="driver_example",
                        fs_type="fs_type_example",
                        node_publish_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        node_stage_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        read_only=True,
                        volume_attributes={
                            "key": "key_example",
                        },
                        volume_handle="volume_handle_example",
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
                    flex_volume=V1FlexPersistentVolumeSource(
                        driver="driver_example",
                        fs_type="fs_type_example",
                        options={
                            "key": "key_example",
                        },
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
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
                    glusterfs=V1GlusterfsPersistentVolumeSource(
                        endpoints="endpoints_example",
                        endpoints_namespace="endpoints_namespace_example",
                        path="path_example",
                        read_only=True,
                    ),
                    host_path=V1HostPathVolumeSource(
                        path="path_example",
                        type="type_example",
                    ),
                    iscsi=V1ISCSIPersistentVolumeSource(
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
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        target_portal="target_portal_example",
                    ),
                    local=V1LocalVolumeSource(
                        fs_type="fs_type_example",
                        path="path_example",
                    ),
                    mount_options=[
                        "mount_options_example",
                    ],
                    nfs=V1NFSVolumeSource(
                        path="path_example",
                        read_only=True,
                        server="server_example",
                    ),
                    node_affinity=V1VolumeNodeAffinity(
                        required=V1NodeSelector(
                            node_selector_terms=[
                                V1NodeSelectorTerm(
                                    match_expressions=[
                                        V1NodeSelectorRequirement(
                                            key="key_example",
                                            operator="operator_example",
                                            values=[
                                                "values_example",
                                            ],
                                        ),
                                    ],
                                    match_fields=[
                                        V1NodeSelectorRequirement(
                                            key="key_example",
                                            operator="operator_example",
                                            values=[
                                                "values_example",
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    persistent_volume_reclaim_policy="persistent_volume_reclaim_policy_example",
                    photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                        fs_type="fs_type_example",
                        pd_id="pd_id_example",
                    ),
                    portworx_volume=V1PortworxVolumeSource(
                        fs_type="fs_type_example",
                        read_only=True,
                        volume_id="volume_id_example",
                    ),
                    quobyte=V1QuobyteVolumeSource(
                        group="group_example",
                        read_only=True,
                        registry="registry_example",
                        tenant="tenant_example",
                        user="user_example",
                        volume="volume_example",
                    ),
                    rbd=V1RBDPersistentVolumeSource(
                        fs_type="fs_type_example",
                        image="image_example",
                        keyring="keyring_example",
                        monitors=[
                            "monitors_example",
                        ],
                        pool="pool_example",
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        user="user_example",
                    ),
                    scale_io=V1ScaleIOPersistentVolumeSource(
                        fs_type="fs_type_example",
                        gateway="gateway_example",
                        protection_domain="protection_domain_example",
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        ssl_enabled=True,
                        storage_mode="storage_mode_example",
                        storage_pool="storage_pool_example",
                        system="system_example",
                        volume_name="volume_name_example",
                    ),
                    storage_class_name="storage_class_name_example",
                    storageos=V1StorageOSPersistentVolumeSource(
                        fs_type="fs_type_example",
                        read_only=True,
                        secret_ref=V1ObjectReference(
                            api_version="api_version_example",
                            field_path="field_path_example",
                            kind="kind_example",
                            name="name_example",
                            namespace="namespace_example",
                            resource_version="resource_version_example",
                            uid="uid_example",
                        ),
                        volume_name="volume_name_example",
                        volume_namespace="volume_namespace_example",
                    ),
                    volume_mode="volume_mode_example",
                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                        fs_type="fs_type_example",
                        storage_policy_id="storage_policy_id_example",
                        storage_policy_name="storage_policy_name_example",
                        volume_path="volume_path_example",
                    ),
                ),
                persistent_volume_name="persistent_volume_name_example",
            ),
        ),
        status=V1VolumeAttachmentStatus(
            attach_error=V1VolumeError(
                message="message_example",
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            attached=True,
            attachment_metadata={
                "key": "key_example",
            },
            detach_error=V1VolumeError(
                message="message_example",
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
    ) # V1VolumeAttachment | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_volume_attachment(body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_volume_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_volume_attachment(body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_volume_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1VolumeAttachment**](V1VolumeAttachment.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1VolumeAttachment**](V1VolumeAttachment.md)

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

# **delete_collection_csi_driver**
> V1Status delete_collection_csi_driver()



delete collection of CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    _continue = "continue_example" # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_selector = "fieldSelector_example" # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    grace_period_seconds = 1 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
    label_selector = "labelSelector_example" # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    limit = 1 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
    propagation_policy = "propagationPolicy_example" # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)
    resource_version = "resourceVersion_example" # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
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
    # and optional values
    try:
        api_response = api_instance.delete_collection_csi_driver(pretty=pretty, _continue=_continue, dry_run=dry_run, field_selector=field_selector, grace_period_seconds=grace_period_seconds, label_selector=label_selector, limit=limit, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, resource_version=resource_version, timeout_seconds=timeout_seconds, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_collection_csi_driver: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional]
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional]
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional]
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

# **delete_collection_csi_node**
> V1Status delete_collection_csi_node()



delete collection of CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    _continue = "continue_example" # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_selector = "fieldSelector_example" # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    grace_period_seconds = 1 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
    label_selector = "labelSelector_example" # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    limit = 1 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
    propagation_policy = "propagationPolicy_example" # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)
    resource_version = "resourceVersion_example" # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
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
    # and optional values
    try:
        api_response = api_instance.delete_collection_csi_node(pretty=pretty, _continue=_continue, dry_run=dry_run, field_selector=field_selector, grace_period_seconds=grace_period_seconds, label_selector=label_selector, limit=limit, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, resource_version=resource_version, timeout_seconds=timeout_seconds, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_collection_csi_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional]
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional]
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional]
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

# **delete_collection_storage_class**
> V1Status delete_collection_storage_class()



delete collection of StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    _continue = "continue_example" # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_selector = "fieldSelector_example" # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    grace_period_seconds = 1 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
    label_selector = "labelSelector_example" # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    limit = 1 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
    propagation_policy = "propagationPolicy_example" # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)
    resource_version = "resourceVersion_example" # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
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
    # and optional values
    try:
        api_response = api_instance.delete_collection_storage_class(pretty=pretty, _continue=_continue, dry_run=dry_run, field_selector=field_selector, grace_period_seconds=grace_period_seconds, label_selector=label_selector, limit=limit, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, resource_version=resource_version, timeout_seconds=timeout_seconds, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_collection_storage_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional]
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional]
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional]
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

# **delete_collection_volume_attachment**
> V1Status delete_collection_volume_attachment()



delete collection of VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    _continue = "continue_example" # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_selector = "fieldSelector_example" # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    grace_period_seconds = 1 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
    label_selector = "labelSelector_example" # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    limit = 1 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
    propagation_policy = "propagationPolicy_example" # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. (optional)
    resource_version = "resourceVersion_example" # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
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
    # and optional values
    try:
        api_response = api_instance.delete_collection_volume_attachment(pretty=pretty, _continue=_continue, dry_run=dry_run, field_selector=field_selector, grace_period_seconds=grace_period_seconds, label_selector=label_selector, limit=limit, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, resource_version=resource_version, timeout_seconds=timeout_seconds, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_collection_volume_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional]
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional]
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional]
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

# **delete_csi_driver**
> V1CSIDriver delete_csi_driver(name)



delete a CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_csi_driver import V1CSIDriver
from kubernetes.client.model.v1_delete_options import V1DeleteOptions
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the CSIDriver
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
        api_response = api_instance.delete_csi_driver(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_csi_driver: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_csi_driver(name, pretty=pretty, dry_run=dry_run, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_csi_driver: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CSIDriver |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional]
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional]
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional]
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | [optional]

### Return type

[**V1CSIDriver**](V1CSIDriver.md)

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

# **delete_csi_node**
> V1CSINode delete_csi_node(name)



delete a CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_delete_options import V1DeleteOptions
from kubernetes.client.model.v1_csi_node import V1CSINode
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the CSINode
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
        api_response = api_instance.delete_csi_node(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_csi_node: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_csi_node(name, pretty=pretty, dry_run=dry_run, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_csi_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CSINode |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional]
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional]
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional]
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | [optional]

### Return type

[**V1CSINode**](V1CSINode.md)

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

# **delete_storage_class**
> V1StorageClass delete_storage_class(name)



delete a StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_storage_class import V1StorageClass
from kubernetes.client.model.v1_delete_options import V1DeleteOptions
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the StorageClass
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
        api_response = api_instance.delete_storage_class(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_storage_class: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_storage_class(name, pretty=pretty, dry_run=dry_run, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_storage_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the StorageClass |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional]
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional]
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional]
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | [optional]

### Return type

[**V1StorageClass**](V1StorageClass.md)

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

# **delete_volume_attachment**
> V1VolumeAttachment delete_volume_attachment(name)



delete a VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_delete_options import V1DeleteOptions
from kubernetes.client.model.v1_volume_attachment import V1VolumeAttachment
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the VolumeAttachment
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
        api_response = api_instance.delete_volume_attachment(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_volume_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_volume_attachment(name, pretty=pretty, dry_run=dry_run, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_volume_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the VolumeAttachment |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional]
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional]
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#39;Orphan&#39; - orphan the dependents; &#39;Background&#39; - allow the garbage collector to delete the dependents in the background; &#39;Foreground&#39; - a cascading policy that deletes all dependents in the foreground. | [optional]
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | [optional]

### Return type

[**V1VolumeAttachment**](V1VolumeAttachment.md)

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
from kubernetes.client.api import storage_v1_api
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
    api_instance = storage_v1_api.StorageV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_api_resources()
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->get_api_resources: %s\n" % e)
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

# **list_csi_driver**
> V1CSIDriverList list_csi_driver()



list or watch objects of kind CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_csi_driver_list import V1CSIDriverList
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    allow_watch_bookmarks = True # bool | allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored. (optional)
    _continue = "continue_example" # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    field_selector = "fieldSelector_example" # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    label_selector = "labelSelector_example" # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    limit = 1 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    resource_version = "resourceVersion_example" # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
    timeout_seconds = 1 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
    watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_csi_driver(pretty=pretty, allow_watch_bookmarks=allow_watch_bookmarks, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->list_csi_driver: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **allow_watch_bookmarks** | **bool**| allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored. | [optional]
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional]
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional]
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional]

### Return type

[**V1CSIDriverList**](V1CSIDriverList.md)

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

# **list_csi_node**
> V1CSINodeList list_csi_node()



list or watch objects of kind CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_csi_node_list import V1CSINodeList
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    allow_watch_bookmarks = True # bool | allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored. (optional)
    _continue = "continue_example" # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    field_selector = "fieldSelector_example" # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    label_selector = "labelSelector_example" # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    limit = 1 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    resource_version = "resourceVersion_example" # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
    timeout_seconds = 1 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
    watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_csi_node(pretty=pretty, allow_watch_bookmarks=allow_watch_bookmarks, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->list_csi_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **allow_watch_bookmarks** | **bool**| allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored. | [optional]
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional]
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional]
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional]

### Return type

[**V1CSINodeList**](V1CSINodeList.md)

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

# **list_storage_class**
> V1StorageClassList list_storage_class()



list or watch objects of kind StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_storage_class_list import V1StorageClassList
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    allow_watch_bookmarks = True # bool | allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored. (optional)
    _continue = "continue_example" # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    field_selector = "fieldSelector_example" # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    label_selector = "labelSelector_example" # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    limit = 1 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    resource_version = "resourceVersion_example" # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
    timeout_seconds = 1 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
    watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_storage_class(pretty=pretty, allow_watch_bookmarks=allow_watch_bookmarks, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->list_storage_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **allow_watch_bookmarks** | **bool**| allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored. | [optional]
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional]
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional]
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional]

### Return type

[**V1StorageClassList**](V1StorageClassList.md)

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

# **list_volume_attachment**
> V1VolumeAttachmentList list_volume_attachment()



list or watch objects of kind VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_volume_attachment_list import V1VolumeAttachmentList
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    allow_watch_bookmarks = True # bool | allowWatchBookmarks requests watch events with type \"BOOKMARK\". Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server's discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored. (optional)
    _continue = "continue_example" # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
    field_selector = "fieldSelector_example" # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
    label_selector = "labelSelector_example" # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
    limit = 1 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
    resource_version = "resourceVersion_example" # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
    timeout_seconds = 1 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
    watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_volume_attachment(pretty=pretty, allow_watch_bookmarks=allow_watch_bookmarks, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->list_volume_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **allow_watch_bookmarks** | **bool**| allowWatchBookmarks requests watch events with type \&quot;BOOKMARK\&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#39;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored. If the feature gate WatchBookmarks is not enabled in apiserver, this field is ignored. | [optional]
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional]
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional]
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional]
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional]
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional]
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional]
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional]

### Return type

[**V1VolumeAttachmentList**](V1VolumeAttachmentList.md)

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

# **patch_csi_driver**
> V1CSIDriver patch_csi_driver(name, body)



partially update the specified CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_csi_driver import V1CSIDriver
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the CSIDriver
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
    force = True # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_csi_driver(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_csi_driver: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_csi_driver(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_csi_driver: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CSIDriver |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional]
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional]

### Return type

[**V1CSIDriver**](V1CSIDriver.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json, application/apply-patch+yaml
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_csi_node**
> V1CSINode patch_csi_node(name, body)



partially update the specified CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_csi_node import V1CSINode
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the CSINode
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
    force = True # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_csi_node(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_csi_node: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_csi_node(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_csi_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CSINode |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional]
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional]

### Return type

[**V1CSINode**](V1CSINode.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json, application/apply-patch+yaml
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_storage_class**
> V1StorageClass patch_storage_class(name, body)



partially update the specified StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_storage_class import V1StorageClass
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the StorageClass
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
    force = True # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_storage_class(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_storage_class: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_storage_class(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_storage_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the StorageClass |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional]
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional]

### Return type

[**V1StorageClass**](V1StorageClass.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json, application/apply-patch+yaml
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_volume_attachment**
> V1VolumeAttachment patch_volume_attachment(name, body)



partially update the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_volume_attachment import V1VolumeAttachment
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the VolumeAttachment
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
    force = True # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_volume_attachment(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_volume_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_volume_attachment(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_volume_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the VolumeAttachment |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional]
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional]

### Return type

[**V1VolumeAttachment**](V1VolumeAttachment.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json, application/apply-patch+yaml
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_volume_attachment_status**
> V1VolumeAttachment patch_volume_attachment_status(name, body)



partially update status of the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_volume_attachment import V1VolumeAttachment
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the VolumeAttachment
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
    force = True # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_volume_attachment_status(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_volume_attachment_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_volume_attachment_status(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_volume_attachment_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the VolumeAttachment |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional]
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional]

### Return type

[**V1VolumeAttachment**](V1VolumeAttachment.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json, application/apply-patch+yaml
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_csi_driver**
> V1CSIDriver read_csi_driver(name)



read the specified CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_csi_driver import V1CSIDriver
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the CSIDriver
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    exact = True # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. Deprecated. Planned for removal in 1.18. (optional)
    export = True # bool | Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.read_csi_driver(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_csi_driver: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.read_csi_driver(name, pretty=pretty, exact=exact, export=export)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_csi_driver: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CSIDriver |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18. | [optional]
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. | [optional]

### Return type

[**V1CSIDriver**](V1CSIDriver.md)

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

# **read_csi_node**
> V1CSINode read_csi_node(name)



read the specified CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_csi_node import V1CSINode
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the CSINode
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    exact = True # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. Deprecated. Planned for removal in 1.18. (optional)
    export = True # bool | Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.read_csi_node(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_csi_node: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.read_csi_node(name, pretty=pretty, exact=exact, export=export)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_csi_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CSINode |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18. | [optional]
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. | [optional]

### Return type

[**V1CSINode**](V1CSINode.md)

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

# **read_storage_class**
> V1StorageClass read_storage_class(name)



read the specified StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_storage_class import V1StorageClass
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the StorageClass
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    exact = True # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. Deprecated. Planned for removal in 1.18. (optional)
    export = True # bool | Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.read_storage_class(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_storage_class: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.read_storage_class(name, pretty=pretty, exact=exact, export=export)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_storage_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the StorageClass |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18. | [optional]
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. | [optional]

### Return type

[**V1StorageClass**](V1StorageClass.md)

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

# **read_volume_attachment**
> V1VolumeAttachment read_volume_attachment(name)



read the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_volume_attachment import V1VolumeAttachment
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the VolumeAttachment
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    exact = True # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. Deprecated. Planned for removal in 1.18. (optional)
    export = True # bool | Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.read_volume_attachment(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_volume_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.read_volume_attachment(name, pretty=pretty, exact=exact, export=export)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_volume_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the VolumeAttachment |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18. | [optional]
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. | [optional]

### Return type

[**V1VolumeAttachment**](V1VolumeAttachment.md)

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

# **read_volume_attachment_status**
> V1VolumeAttachment read_volume_attachment_status(name)



read status of the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_volume_attachment import V1VolumeAttachment
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the VolumeAttachment
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.read_volume_attachment_status(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_volume_attachment_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.read_volume_attachment_status(name, pretty=pretty)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_volume_attachment_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the VolumeAttachment |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]

### Return type

[**V1VolumeAttachment**](V1VolumeAttachment.md)

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

# **replace_csi_driver**
> V1CSIDriver replace_csi_driver(name, body)



replace the specified CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_csi_driver import V1CSIDriver
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the CSIDriver
    body = V1CSIDriver(
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
        spec=V1CSIDriverSpec(
            attach_required=True,
            pod_info_on_mount=True,
            volume_lifecycle_modes=[
                "volume_lifecycle_modes_example",
            ],
        ),
    ) # V1CSIDriver | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_csi_driver(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_csi_driver: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_csi_driver(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_csi_driver: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CSIDriver |
 **body** | [**V1CSIDriver**](V1CSIDriver.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1CSIDriver**](V1CSIDriver.md)

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

# **replace_csi_node**
> V1CSINode replace_csi_node(name, body)



replace the specified CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_csi_node import V1CSINode
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the CSINode
    body = V1CSINode(
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
        spec=V1CSINodeSpec(
            drivers=[
                V1CSINodeDriver(
                    allocatable=V1VolumeNodeResources(
                        count=1,
                    ),
                    name="name_example",
                    node_id="node_id_example",
                    topology_keys=[
                        "topology_keys_example",
                    ],
                ),
            ],
        ),
    ) # V1CSINode | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_csi_node(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_csi_node: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_csi_node(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_csi_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CSINode |
 **body** | [**V1CSINode**](V1CSINode.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1CSINode**](V1CSINode.md)

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

# **replace_storage_class**
> V1StorageClass replace_storage_class(name, body)



replace the specified StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_storage_class import V1StorageClass
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the StorageClass
    body = V1StorageClass(
        allow_volume_expansion=True,
        allowed_topologies=[
            V1TopologySelectorTerm(
                match_label_expressions=[
                    V1TopologySelectorLabelRequirement(
                        key="key_example",
                        values=[
                            "values_example",
                        ],
                    ),
                ],
            ),
        ],
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
        mount_options=[
            "mount_options_example",
        ],
        parameters={
            "key": "key_example",
        },
        provisioner="provisioner_example",
        reclaim_policy="reclaim_policy_example",
        volume_binding_mode="volume_binding_mode_example",
    ) # V1StorageClass | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_storage_class(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_storage_class: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_storage_class(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_storage_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the StorageClass |
 **body** | [**V1StorageClass**](V1StorageClass.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1StorageClass**](V1StorageClass.md)

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

# **replace_volume_attachment**
> V1VolumeAttachment replace_volume_attachment(name, body)



replace the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_volume_attachment import V1VolumeAttachment
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the VolumeAttachment
    body = V1VolumeAttachment(
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
        spec=V1VolumeAttachmentSpec(
            attacher="attacher_example",
            node_name="node_name_example",
            source=V1VolumeAttachmentSource(
                inline_volume_spec=V1PersistentVolumeSpec(
                    access_modes=[
                        "access_modes_example",
                    ],
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
                    azure_file=V1AzureFilePersistentVolumeSource(
                        read_only=True,
                        secret_name="secret_name_example",
                        secret_namespace="secret_namespace_example",
                        share_name="share_name_example",
                    ),
                    capacity={
                        "key": "key_example",
                    },
                    cephfs=V1CephFSPersistentVolumeSource(
                        monitors=[
                            "monitors_example",
                        ],
                        path="path_example",
                        read_only=True,
                        secret_file="secret_file_example",
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        user="user_example",
                    ),
                    cinder=V1CinderPersistentVolumeSource(
                        fs_type="fs_type_example",
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        volume_id="volume_id_example",
                    ),
                    claim_ref=V1ObjectReference(
                        api_version="api_version_example",
                        field_path="field_path_example",
                        kind="kind_example",
                        name="name_example",
                        namespace="namespace_example",
                        resource_version="resource_version_example",
                        uid="uid_example",
                    ),
                    csi=V1CSIPersistentVolumeSource(
                        controller_expand_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        controller_publish_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        driver="driver_example",
                        fs_type="fs_type_example",
                        node_publish_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        node_stage_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        read_only=True,
                        volume_attributes={
                            "key": "key_example",
                        },
                        volume_handle="volume_handle_example",
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
                    flex_volume=V1FlexPersistentVolumeSource(
                        driver="driver_example",
                        fs_type="fs_type_example",
                        options={
                            "key": "key_example",
                        },
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
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
                    glusterfs=V1GlusterfsPersistentVolumeSource(
                        endpoints="endpoints_example",
                        endpoints_namespace="endpoints_namespace_example",
                        path="path_example",
                        read_only=True,
                    ),
                    host_path=V1HostPathVolumeSource(
                        path="path_example",
                        type="type_example",
                    ),
                    iscsi=V1ISCSIPersistentVolumeSource(
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
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        target_portal="target_portal_example",
                    ),
                    local=V1LocalVolumeSource(
                        fs_type="fs_type_example",
                        path="path_example",
                    ),
                    mount_options=[
                        "mount_options_example",
                    ],
                    nfs=V1NFSVolumeSource(
                        path="path_example",
                        read_only=True,
                        server="server_example",
                    ),
                    node_affinity=V1VolumeNodeAffinity(
                        required=V1NodeSelector(
                            node_selector_terms=[
                                V1NodeSelectorTerm(
                                    match_expressions=[
                                        V1NodeSelectorRequirement(
                                            key="key_example",
                                            operator="operator_example",
                                            values=[
                                                "values_example",
                                            ],
                                        ),
                                    ],
                                    match_fields=[
                                        V1NodeSelectorRequirement(
                                            key="key_example",
                                            operator="operator_example",
                                            values=[
                                                "values_example",
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    persistent_volume_reclaim_policy="persistent_volume_reclaim_policy_example",
                    photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                        fs_type="fs_type_example",
                        pd_id="pd_id_example",
                    ),
                    portworx_volume=V1PortworxVolumeSource(
                        fs_type="fs_type_example",
                        read_only=True,
                        volume_id="volume_id_example",
                    ),
                    quobyte=V1QuobyteVolumeSource(
                        group="group_example",
                        read_only=True,
                        registry="registry_example",
                        tenant="tenant_example",
                        user="user_example",
                        volume="volume_example",
                    ),
                    rbd=V1RBDPersistentVolumeSource(
                        fs_type="fs_type_example",
                        image="image_example",
                        keyring="keyring_example",
                        monitors=[
                            "monitors_example",
                        ],
                        pool="pool_example",
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        user="user_example",
                    ),
                    scale_io=V1ScaleIOPersistentVolumeSource(
                        fs_type="fs_type_example",
                        gateway="gateway_example",
                        protection_domain="protection_domain_example",
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        ssl_enabled=True,
                        storage_mode="storage_mode_example",
                        storage_pool="storage_pool_example",
                        system="system_example",
                        volume_name="volume_name_example",
                    ),
                    storage_class_name="storage_class_name_example",
                    storageos=V1StorageOSPersistentVolumeSource(
                        fs_type="fs_type_example",
                        read_only=True,
                        secret_ref=V1ObjectReference(
                            api_version="api_version_example",
                            field_path="field_path_example",
                            kind="kind_example",
                            name="name_example",
                            namespace="namespace_example",
                            resource_version="resource_version_example",
                            uid="uid_example",
                        ),
                        volume_name="volume_name_example",
                        volume_namespace="volume_namespace_example",
                    ),
                    volume_mode="volume_mode_example",
                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                        fs_type="fs_type_example",
                        storage_policy_id="storage_policy_id_example",
                        storage_policy_name="storage_policy_name_example",
                        volume_path="volume_path_example",
                    ),
                ),
                persistent_volume_name="persistent_volume_name_example",
            ),
        ),
        status=V1VolumeAttachmentStatus(
            attach_error=V1VolumeError(
                message="message_example",
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            attached=True,
            attachment_metadata={
                "key": "key_example",
            },
            detach_error=V1VolumeError(
                message="message_example",
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
    ) # V1VolumeAttachment | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_volume_attachment(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_volume_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_volume_attachment(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_volume_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the VolumeAttachment |
 **body** | [**V1VolumeAttachment**](V1VolumeAttachment.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1VolumeAttachment**](V1VolumeAttachment.md)

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

# **replace_volume_attachment_status**
> V1VolumeAttachment replace_volume_attachment_status(name, body)



replace status of the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import storage_v1_api
from kubernetes.client.model.v1_volume_attachment import V1VolumeAttachment
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
    api_instance = storage_v1_api.StorageV1Api(api_client)
    name = "name_example" # str | name of the VolumeAttachment
    body = V1VolumeAttachment(
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
        spec=V1VolumeAttachmentSpec(
            attacher="attacher_example",
            node_name="node_name_example",
            source=V1VolumeAttachmentSource(
                inline_volume_spec=V1PersistentVolumeSpec(
                    access_modes=[
                        "access_modes_example",
                    ],
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
                    azure_file=V1AzureFilePersistentVolumeSource(
                        read_only=True,
                        secret_name="secret_name_example",
                        secret_namespace="secret_namespace_example",
                        share_name="share_name_example",
                    ),
                    capacity={
                        "key": "key_example",
                    },
                    cephfs=V1CephFSPersistentVolumeSource(
                        monitors=[
                            "monitors_example",
                        ],
                        path="path_example",
                        read_only=True,
                        secret_file="secret_file_example",
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        user="user_example",
                    ),
                    cinder=V1CinderPersistentVolumeSource(
                        fs_type="fs_type_example",
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        volume_id="volume_id_example",
                    ),
                    claim_ref=V1ObjectReference(
                        api_version="api_version_example",
                        field_path="field_path_example",
                        kind="kind_example",
                        name="name_example",
                        namespace="namespace_example",
                        resource_version="resource_version_example",
                        uid="uid_example",
                    ),
                    csi=V1CSIPersistentVolumeSource(
                        controller_expand_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        controller_publish_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        driver="driver_example",
                        fs_type="fs_type_example",
                        node_publish_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        node_stage_secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        read_only=True,
                        volume_attributes={
                            "key": "key_example",
                        },
                        volume_handle="volume_handle_example",
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
                    flex_volume=V1FlexPersistentVolumeSource(
                        driver="driver_example",
                        fs_type="fs_type_example",
                        options={
                            "key": "key_example",
                        },
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
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
                    glusterfs=V1GlusterfsPersistentVolumeSource(
                        endpoints="endpoints_example",
                        endpoints_namespace="endpoints_namespace_example",
                        path="path_example",
                        read_only=True,
                    ),
                    host_path=V1HostPathVolumeSource(
                        path="path_example",
                        type="type_example",
                    ),
                    iscsi=V1ISCSIPersistentVolumeSource(
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
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        target_portal="target_portal_example",
                    ),
                    local=V1LocalVolumeSource(
                        fs_type="fs_type_example",
                        path="path_example",
                    ),
                    mount_options=[
                        "mount_options_example",
                    ],
                    nfs=V1NFSVolumeSource(
                        path="path_example",
                        read_only=True,
                        server="server_example",
                    ),
                    node_affinity=V1VolumeNodeAffinity(
                        required=V1NodeSelector(
                            node_selector_terms=[
                                V1NodeSelectorTerm(
                                    match_expressions=[
                                        V1NodeSelectorRequirement(
                                            key="key_example",
                                            operator="operator_example",
                                            values=[
                                                "values_example",
                                            ],
                                        ),
                                    ],
                                    match_fields=[
                                        V1NodeSelectorRequirement(
                                            key="key_example",
                                            operator="operator_example",
                                            values=[
                                                "values_example",
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    persistent_volume_reclaim_policy="persistent_volume_reclaim_policy_example",
                    photon_persistent_disk=V1PhotonPersistentDiskVolumeSource(
                        fs_type="fs_type_example",
                        pd_id="pd_id_example",
                    ),
                    portworx_volume=V1PortworxVolumeSource(
                        fs_type="fs_type_example",
                        read_only=True,
                        volume_id="volume_id_example",
                    ),
                    quobyte=V1QuobyteVolumeSource(
                        group="group_example",
                        read_only=True,
                        registry="registry_example",
                        tenant="tenant_example",
                        user="user_example",
                        volume="volume_example",
                    ),
                    rbd=V1RBDPersistentVolumeSource(
                        fs_type="fs_type_example",
                        image="image_example",
                        keyring="keyring_example",
                        monitors=[
                            "monitors_example",
                        ],
                        pool="pool_example",
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        user="user_example",
                    ),
                    scale_io=V1ScaleIOPersistentVolumeSource(
                        fs_type="fs_type_example",
                        gateway="gateway_example",
                        protection_domain="protection_domain_example",
                        read_only=True,
                        secret_ref=V1SecretReference(
                            name="name_example",
                            namespace="namespace_example",
                        ),
                        ssl_enabled=True,
                        storage_mode="storage_mode_example",
                        storage_pool="storage_pool_example",
                        system="system_example",
                        volume_name="volume_name_example",
                    ),
                    storage_class_name="storage_class_name_example",
                    storageos=V1StorageOSPersistentVolumeSource(
                        fs_type="fs_type_example",
                        read_only=True,
                        secret_ref=V1ObjectReference(
                            api_version="api_version_example",
                            field_path="field_path_example",
                            kind="kind_example",
                            name="name_example",
                            namespace="namespace_example",
                            resource_version="resource_version_example",
                            uid="uid_example",
                        ),
                        volume_name="volume_name_example",
                        volume_namespace="volume_namespace_example",
                    ),
                    volume_mode="volume_mode_example",
                    vsphere_volume=V1VsphereVirtualDiskVolumeSource(
                        fs_type="fs_type_example",
                        storage_policy_id="storage_policy_id_example",
                        storage_policy_name="storage_policy_name_example",
                        volume_path="volume_path_example",
                    ),
                ),
                persistent_volume_name="persistent_volume_name_example",
            ),
        ),
        status=V1VolumeAttachmentStatus(
            attach_error=V1VolumeError(
                message="message_example",
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            attached=True,
            attachment_metadata={
                "key": "key_example",
            },
            detach_error=V1VolumeError(
                message="message_example",
                time=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ),
    ) # V1VolumeAttachment | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_volume_attachment_status(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_volume_attachment_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_volume_attachment_status(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_volume_attachment_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the VolumeAttachment |
 **body** | [**V1VolumeAttachment**](V1VolumeAttachment.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1VolumeAttachment**](V1VolumeAttachment.md)

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

