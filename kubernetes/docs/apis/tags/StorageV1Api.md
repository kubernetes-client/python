<a name="__pageTop"></a>
# kubernetes.client.apis.tags.storage_v1_api.StorageV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_csi_driver**](#create_csi_driver) | **post** /apis/storage.k8s.io/v1/csidrivers | 
[**create_csi_node**](#create_csi_node) | **post** /apis/storage.k8s.io/v1/csinodes | 
[**create_namespaced_csi_storage_capacity**](#create_namespaced_csi_storage_capacity) | **post** /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities | 
[**create_storage_class**](#create_storage_class) | **post** /apis/storage.k8s.io/v1/storageclasses | 
[**create_volume_attachment**](#create_volume_attachment) | **post** /apis/storage.k8s.io/v1/volumeattachments | 
[**delete_collection_csi_driver**](#delete_collection_csi_driver) | **delete** /apis/storage.k8s.io/v1/csidrivers | 
[**delete_collection_csi_node**](#delete_collection_csi_node) | **delete** /apis/storage.k8s.io/v1/csinodes | 
[**delete_collection_namespaced_csi_storage_capacity**](#delete_collection_namespaced_csi_storage_capacity) | **delete** /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities | 
[**delete_collection_storage_class**](#delete_collection_storage_class) | **delete** /apis/storage.k8s.io/v1/storageclasses | 
[**delete_collection_volume_attachment**](#delete_collection_volume_attachment) | **delete** /apis/storage.k8s.io/v1/volumeattachments | 
[**delete_csi_driver**](#delete_csi_driver) | **delete** /apis/storage.k8s.io/v1/csidrivers/{name} | 
[**delete_csi_node**](#delete_csi_node) | **delete** /apis/storage.k8s.io/v1/csinodes/{name} | 
[**delete_namespaced_csi_storage_capacity**](#delete_namespaced_csi_storage_capacity) | **delete** /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities/{name} | 
[**delete_storage_class**](#delete_storage_class) | **delete** /apis/storage.k8s.io/v1/storageclasses/{name} | 
[**delete_volume_attachment**](#delete_volume_attachment) | **delete** /apis/storage.k8s.io/v1/volumeattachments/{name} | 
[**get_api_resources**](#get_api_resources) | **get** /apis/storage.k8s.io/v1/ | 
[**list_csi_driver**](#list_csi_driver) | **get** /apis/storage.k8s.io/v1/csidrivers | 
[**list_csi_node**](#list_csi_node) | **get** /apis/storage.k8s.io/v1/csinodes | 
[**list_csi_storage_capacity_for_all_namespaces**](#list_csi_storage_capacity_for_all_namespaces) | **get** /apis/storage.k8s.io/v1/csistoragecapacities | 
[**list_namespaced_csi_storage_capacity**](#list_namespaced_csi_storage_capacity) | **get** /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities | 
[**list_storage_class**](#list_storage_class) | **get** /apis/storage.k8s.io/v1/storageclasses | 
[**list_volume_attachment**](#list_volume_attachment) | **get** /apis/storage.k8s.io/v1/volumeattachments | 
[**patch_csi_driver**](#patch_csi_driver) | **patch** /apis/storage.k8s.io/v1/csidrivers/{name} | 
[**patch_csi_node**](#patch_csi_node) | **patch** /apis/storage.k8s.io/v1/csinodes/{name} | 
[**patch_namespaced_csi_storage_capacity**](#patch_namespaced_csi_storage_capacity) | **patch** /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities/{name} | 
[**patch_storage_class**](#patch_storage_class) | **patch** /apis/storage.k8s.io/v1/storageclasses/{name} | 
[**patch_volume_attachment**](#patch_volume_attachment) | **patch** /apis/storage.k8s.io/v1/volumeattachments/{name} | 
[**patch_volume_attachment_status**](#patch_volume_attachment_status) | **patch** /apis/storage.k8s.io/v1/volumeattachments/{name}/status | 
[**read_csi_driver**](#read_csi_driver) | **get** /apis/storage.k8s.io/v1/csidrivers/{name} | 
[**read_csi_node**](#read_csi_node) | **get** /apis/storage.k8s.io/v1/csinodes/{name} | 
[**read_namespaced_csi_storage_capacity**](#read_namespaced_csi_storage_capacity) | **get** /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities/{name} | 
[**read_storage_class**](#read_storage_class) | **get** /apis/storage.k8s.io/v1/storageclasses/{name} | 
[**read_volume_attachment**](#read_volume_attachment) | **get** /apis/storage.k8s.io/v1/volumeattachments/{name} | 
[**read_volume_attachment_status**](#read_volume_attachment_status) | **get** /apis/storage.k8s.io/v1/volumeattachments/{name}/status | 
[**replace_csi_driver**](#replace_csi_driver) | **put** /apis/storage.k8s.io/v1/csidrivers/{name} | 
[**replace_csi_node**](#replace_csi_node) | **put** /apis/storage.k8s.io/v1/csinodes/{name} | 
[**replace_namespaced_csi_storage_capacity**](#replace_namespaced_csi_storage_capacity) | **put** /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities/{name} | 
[**replace_storage_class**](#replace_storage_class) | **put** /apis/storage.k8s.io/v1/storageclasses/{name} | 
[**replace_volume_attachment**](#replace_volume_attachment) | **put** /apis/storage.k8s.io/v1/volumeattachments/{name} | 
[**replace_volume_attachment_status**](#replace_volume_attachment_status) | **put** /apis/storage.k8s.io/v1/volumeattachments/{name}/status | 

# **create_csi_driver**
<a name="create_csi_driver"></a>
> V1CSIDriver create_csi_driver(body)



create a CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = V1CSIDriver(
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
        spec=V1CSIDriverSpec(
            attach_required=True,
            fs_group_policy="fs_group_policy_example",
            pod_info_on_mount=True,
            requires_republish=True,
            se_linux_mount=True,
            storage_capacity=True,
            token_requests=[
                StorageV1TokenRequest(
                    audience="audience_example",
                    expiration_seconds=1,
                )
            ],
            volume_lifecycle_modes=[
                "volume_lifecycle_modes_example"
            ],
        ),
    )
    try:
        api_response = api_instance.create_csi_driver(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_csi_driver: %s\n" % e)

    # example passing only optional values
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1CSIDriver(
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
        spec=V1CSIDriverSpec(
            attach_required=True,
            fs_group_policy="fs_group_policy_example",
            pod_info_on_mount=True,
            requires_republish=True,
            se_linux_mount=True,
            storage_capacity=True,
            token_requests=[
                StorageV1TokenRequest(
                    audience="audience_example",
                    expiration_seconds=1,
                )
            ],
            volume_lifecycle_modes=[
                "volume_lifecycle_modes_example"
            ],
        ),
    )
    try:
        api_response = api_instance.create_csi_driver(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_csi_driver: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_csi_driver.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_csi_driver.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_csi_driver.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_csi_driver.ApiResponseFor401) | Unauthorized

#### create_csi_driver.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


#### create_csi_driver.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


#### create_csi_driver.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


#### create_csi_driver.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_csi_node**
<a name="create_csi_node"></a>
> V1CSINode create_csi_node(body)



create a CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = V1CSINode(
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
        spec=V1CSINodeSpec(
            drivers=[
                V1CSINodeDriver(
                    allocatable=V1VolumeNodeResources(
                        count=1,
                    ),
                    name="name_example",
                    node_id="node_id_example",
                    topology_keys=[
                        "topology_keys_example"
                    ],
                )
            ],
        ),
    )
    try:
        api_response = api_instance.create_csi_node(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_csi_node: %s\n" % e)

    # example passing only optional values
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1CSINode(
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
        spec=V1CSINodeSpec(
            drivers=[
                V1CSINodeDriver(
                    allocatable=V1VolumeNodeResources(
                        count=1,
                    ),
                    name="name_example",
                    node_id="node_id_example",
                    topology_keys=[
                        "topology_keys_example"
                    ],
                )
            ],
        ),
    )
    try:
        api_response = api_instance.create_csi_node(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_csi_node: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_csi_node.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_csi_node.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_csi_node.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_csi_node.ApiResponseFor401) | Unauthorized

#### create_csi_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


#### create_csi_node.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


#### create_csi_node.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


#### create_csi_node.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_namespaced_csi_storage_capacity**
<a name="create_namespaced_csi_storage_capacity"></a>
> V1CSIStorageCapacity create_namespaced_csi_storage_capacity(namespacebody)



create a CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
from kubernetes.client.model.v1_csi_storage_capacity import V1CSIStorageCapacity
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

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = V1CSIStorageCapacity(
        api_version="api_version_example",
        capacity="capacity_example",
        kind="kind_example",
        maximum_volume_size="maximum_volume_size_example",
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
        node_topology=V1LabelSelector(
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
        storage_class_name="storage_class_name_example",
    )
    try:
        api_response = api_instance.create_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_namespaced_csi_storage_capacity: %s\n" % e)

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
    body = V1CSIStorageCapacity(
        api_version="api_version_example",
        capacity="capacity_example",
        kind="kind_example",
        maximum_volume_size="maximum_volume_size_example",
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
        node_topology=V1LabelSelector(
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
        storage_class_name="storage_class_name_example",
    )
    try:
        api_response = api_instance.create_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_namespaced_csi_storage_capacity: %s\n" % e)
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
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


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
200 | [ApiResponseFor200](#create_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_namespaced_csi_storage_capacity.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_namespaced_csi_storage_capacity.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### create_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


#### create_namespaced_csi_storage_capacity.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


#### create_namespaced_csi_storage_capacity.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


#### create_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_storage_class**
<a name="create_storage_class"></a>
> V1StorageClass create_storage_class(body)



create a StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = V1StorageClass(
        allow_volume_expansion=True,
        allowed_topologies=[
            V1TopologySelectorTerm(
                match_label_expressions=[
                    V1TopologySelectorLabelRequirement(
                        key="key_example",
                        values=[
                            "values_example"
                        ],
                    )
                ],
            )
        ],
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
        mount_options=[
            "mount_options_example"
        ],
        parameters=dict(
            "key": "key_example",
        ),
        provisioner="provisioner_example",
        reclaim_policy="reclaim_policy_example",
        volume_binding_mode="volume_binding_mode_example",
    )
    try:
        api_response = api_instance.create_storage_class(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_storage_class: %s\n" % e)

    # example passing only optional values
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1StorageClass(
        allow_volume_expansion=True,
        allowed_topologies=[
            V1TopologySelectorTerm(
                match_label_expressions=[
                    V1TopologySelectorLabelRequirement(
                        key="key_example",
                        values=[
                            "values_example"
                        ],
                    )
                ],
            )
        ],
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
        mount_options=[
            "mount_options_example"
        ],
        parameters=dict(
            "key": "key_example",
        ),
        provisioner="provisioner_example",
        reclaim_policy="reclaim_policy_example",
        volume_binding_mode="volume_binding_mode_example",
    )
    try:
        api_response = api_instance.create_storage_class(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_storage_class: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_storage_class.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_storage_class.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_storage_class.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_storage_class.ApiResponseFor401) | Unauthorized

#### create_storage_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


#### create_storage_class.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


#### create_storage_class.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


#### create_storage_class.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_volume_attachment**
<a name="create_volume_attachment"></a>
> V1VolumeAttachment create_volume_attachment(body)



create a VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = V1VolumeAttachment(
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
        spec=V1VolumeAttachmentSpec(
            attacher="attacher_example",
            node_name="node_name_example",
            source=V1VolumeAttachmentSource(
                inline_volume_spec=V1PersistentVolumeSpec(
                    access_modes=[
                        "access_modes_example"
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
                    capacity=dict(
                        "key": "key_example",
                    ),
                    cephfs=V1CephFSPersistentVolumeSource(
                        monitors=[
                            "monitors_example"
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
                        secret_ref=V1SecretReference(),
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
                        controller_expand_secret_ref=V1SecretReference(),
                        controller_publish_secret_ref=V1SecretReference(),
                        driver="driver_example",
                        fs_type="fs_type_example",
                        node_expand_secret_ref=V1SecretReference(),
                        node_publish_secret_ref=V1SecretReference(),
                        node_stage_secret_ref=V1SecretReference(),
                        read_only=True,
                        volume_attributes=dict(
                            "key": "key_example",
                        ),
                        volume_handle="volume_handle_example",
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
                    flex_volume=V1FlexPersistentVolumeSource(
                        driver="driver_example",
                        fs_type="fs_type_example",
                        options=dict(
                            "key": "key_example",
                        ),
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                            "portals_example"
                        ],
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        target_portal="target_portal_example",
                    ),
                    local=V1LocalVolumeSource(
                        fs_type="fs_type_example",
                        path="path_example",
                    ),
                    mount_options=[
                        "mount_options_example"
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
                                                "values_example"
                                            ],
                                        )
                                    ],
                                    match_fields=[
                                        V1NodeSelectorRequirement()
                                    ],
                                )
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
                            "monitors_example"
                        ],
                        pool="pool_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        user="user_example",
                    ),
                    scale_io=V1ScaleIOPersistentVolumeSource(
                        fs_type="fs_type_example",
                        gateway="gateway_example",
                        protection_domain="protection_domain_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                        secret_ref=V1ObjectReference(),
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
                time="1970-01-01T00:00:00.00Z",
            ),
            attached=True,
            attachment_metadata=dict(
                "key": "key_example",
            ),
            detach_error=V1VolumeError(),
        ),
    )
    try:
        api_response = api_instance.create_volume_attachment(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_volume_attachment: %s\n" % e)

    # example passing only optional values
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1VolumeAttachment(
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
        spec=V1VolumeAttachmentSpec(
            attacher="attacher_example",
            node_name="node_name_example",
            source=V1VolumeAttachmentSource(
                inline_volume_spec=V1PersistentVolumeSpec(
                    access_modes=[
                        "access_modes_example"
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
                    capacity=dict(
                        "key": "key_example",
                    ),
                    cephfs=V1CephFSPersistentVolumeSource(
                        monitors=[
                            "monitors_example"
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
                        secret_ref=V1SecretReference(),
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
                        controller_expand_secret_ref=V1SecretReference(),
                        controller_publish_secret_ref=V1SecretReference(),
                        driver="driver_example",
                        fs_type="fs_type_example",
                        node_expand_secret_ref=V1SecretReference(),
                        node_publish_secret_ref=V1SecretReference(),
                        node_stage_secret_ref=V1SecretReference(),
                        read_only=True,
                        volume_attributes=dict(
                            "key": "key_example",
                        ),
                        volume_handle="volume_handle_example",
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
                    flex_volume=V1FlexPersistentVolumeSource(
                        driver="driver_example",
                        fs_type="fs_type_example",
                        options=dict(
                            "key": "key_example",
                        ),
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                            "portals_example"
                        ],
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        target_portal="target_portal_example",
                    ),
                    local=V1LocalVolumeSource(
                        fs_type="fs_type_example",
                        path="path_example",
                    ),
                    mount_options=[
                        "mount_options_example"
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
                                                "values_example"
                                            ],
                                        )
                                    ],
                                    match_fields=[
                                        V1NodeSelectorRequirement()
                                    ],
                                )
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
                            "monitors_example"
                        ],
                        pool="pool_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        user="user_example",
                    ),
                    scale_io=V1ScaleIOPersistentVolumeSource(
                        fs_type="fs_type_example",
                        gateway="gateway_example",
                        protection_domain="protection_domain_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                        secret_ref=V1ObjectReference(),
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
                time="1970-01-01T00:00:00.00Z",
            ),
            attached=True,
            attachment_metadata=dict(
                "key": "key_example",
            ),
            detach_error=V1VolumeError(),
        ),
    )
    try:
        api_response = api_instance.create_volume_attachment(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->create_volume_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is '*/*' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf', ) | Tells the server the content type(s) that are accepted by the kubernetes.client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest kubernetes.client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBody
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_volume_attachment.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_volume_attachment.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_volume_attachment.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_volume_attachment.ApiResponseFor401) | Unauthorized

#### create_volume_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### create_volume_attachment.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### create_volume_attachment.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### create_volume_attachment.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_collection_csi_driver**
<a name="delete_collection_csi_driver"></a>
> V1Status delete_collection_csi_driver()



delete collection of CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only optional values
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
        api_response = api_instance.delete_collection_csi_driver(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_collection_csi_driver: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_collection_csi_driver.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#delete_collection_csi_driver.ApiResponseFor401) | Unauthorized

#### delete_collection_csi_driver.ApiResponseFor200
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


#### delete_collection_csi_driver.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_collection_csi_node**
<a name="delete_collection_csi_node"></a>
> V1Status delete_collection_csi_node()



delete collection of CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only optional values
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
        api_response = api_instance.delete_collection_csi_node(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_collection_csi_node: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_collection_csi_node.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#delete_collection_csi_node.ApiResponseFor401) | Unauthorized

#### delete_collection_csi_node.ApiResponseFor200
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


#### delete_collection_csi_node.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_collection_namespaced_csi_storage_capacity**
<a name="delete_collection_namespaced_csi_storage_capacity"></a>
> V1Status delete_collection_namespaced_csi_storage_capacity(namespace)



delete collection of CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_collection_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_collection_namespaced_csi_storage_capacity: %s\n" % e)

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
        api_response = api_instance.delete_collection_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_collection_namespaced_csi_storage_capacity: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_collection_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#delete_collection_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### delete_collection_namespaced_csi_storage_capacity.ApiResponseFor200
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


#### delete_collection_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_collection_storage_class**
<a name="delete_collection_storage_class"></a>
> V1Status delete_collection_storage_class()



delete collection of StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only optional values
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
        api_response = api_instance.delete_collection_storage_class(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_collection_storage_class: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_collection_storage_class.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#delete_collection_storage_class.ApiResponseFor401) | Unauthorized

#### delete_collection_storage_class.ApiResponseFor200
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


#### delete_collection_storage_class.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_collection_volume_attachment**
<a name="delete_collection_volume_attachment"></a>
> V1Status delete_collection_volume_attachment()



delete collection of VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only optional values
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
        api_response = api_instance.delete_collection_volume_attachment(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_collection_volume_attachment: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBody, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_collection_volume_attachment.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#delete_collection_volume_attachment.ApiResponseFor401) | Unauthorized

#### delete_collection_volume_attachment.ApiResponseFor200
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


#### delete_collection_volume_attachment.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_csi_driver**
<a name="delete_csi_driver"></a>
> V1CSIDriver delete_csi_driver(name)



delete a CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_csi_driver(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_csi_driver: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
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
        api_response = api_instance.delete_csi_driver(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_csi_driver: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_csi_driver.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#delete_csi_driver.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#delete_csi_driver.ApiResponseFor401) | Unauthorized

#### delete_csi_driver.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


#### delete_csi_driver.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


#### delete_csi_driver.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_csi_node**
<a name="delete_csi_node"></a>
> V1CSINode delete_csi_node(name)



delete a CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_csi_node(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_csi_node: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
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
        api_response = api_instance.delete_csi_node(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_csi_node: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_csi_node.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#delete_csi_node.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#delete_csi_node.ApiResponseFor401) | Unauthorized

#### delete_csi_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


#### delete_csi_node.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


#### delete_csi_node.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_namespaced_csi_storage_capacity**
<a name="delete_namespaced_csi_storage_capacity"></a>
> V1Status delete_namespaced_csi_storage_capacity(namenamespace)



delete a CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_namespaced_csi_storage_capacity: %s\n" % e)

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
        api_response = api_instance.delete_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_namespaced_csi_storage_capacity: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#delete_namespaced_csi_storage_capacity.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#delete_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### delete_namespaced_csi_storage_capacity.ApiResponseFor200
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


#### delete_namespaced_csi_storage_capacity.ApiResponseFor202
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


#### delete_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_storage_class**
<a name="delete_storage_class"></a>
> V1StorageClass delete_storage_class(name)



delete a StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_storage_class(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_storage_class: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
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
        api_response = api_instance.delete_storage_class(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_storage_class: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_storage_class.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#delete_storage_class.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#delete_storage_class.ApiResponseFor401) | Unauthorized

#### delete_storage_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


#### delete_storage_class.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


#### delete_storage_class.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_volume_attachment**
<a name="delete_volume_attachment"></a>
> V1VolumeAttachment delete_volume_attachment(name)



delete a VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_volume_attachment(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_volume_attachment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
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
        api_response = api_instance.delete_volume_attachment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->delete_volume_attachment: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_volume_attachment.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#delete_volume_attachment.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#delete_volume_attachment.ApiResponseFor401) | Unauthorized

#### delete_volume_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### delete_volume_attachment.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### delete_volume_attachment.ApiResponseFor401
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
from kubernetes.client.apis.tags import storage_v1_api
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

# **list_csi_driver**
<a name="list_csi_driver"></a>
> V1CSIDriverList list_csi_driver()



list or watch objects of kind CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only optional values
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
        api_response = api_instance.list_csi_driver(
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->list_csi_driver: %s\n" % e)
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_csi_driver.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_csi_driver.ApiResponseFor401) | Unauthorized

#### list_csi_driver.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriverList**](../../models/V1CSIDriverList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriverList**](../../models/V1CSIDriverList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriverList**](../../models/V1CSIDriverList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriverList**](../../models/V1CSIDriverList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriverList**](../../models/V1CSIDriverList.md) |  | 


#### list_csi_driver.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_csi_node**
<a name="list_csi_node"></a>
> V1CSINodeList list_csi_node()



list or watch objects of kind CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only optional values
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
        api_response = api_instance.list_csi_node(
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->list_csi_node: %s\n" % e)
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_csi_node.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_csi_node.ApiResponseFor401) | Unauthorized

#### list_csi_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINodeList**](../../models/V1CSINodeList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINodeList**](../../models/V1CSINodeList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINodeList**](../../models/V1CSINodeList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINodeList**](../../models/V1CSINodeList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINodeList**](../../models/V1CSINodeList.md) |  | 


#### list_csi_node.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_csi_storage_capacity_for_all_namespaces**
<a name="list_csi_storage_capacity_for_all_namespaces"></a>
> V1CSIStorageCapacityList list_csi_storage_capacity_for_all_namespaces()



list or watch objects of kind CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
from kubernetes.client.model.v1_csi_storage_capacity_list import V1CSIStorageCapacityList
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
        api_response = api_instance.list_csi_storage_capacity_for_all_namespaces(
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->list_csi_storage_capacity_for_all_namespaces: %s\n" % e)
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
200 | [ApiResponseFor200](#list_csi_storage_capacity_for_all_namespaces.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_csi_storage_capacity_for_all_namespaces.ApiResponseFor401) | Unauthorized

#### list_csi_storage_capacity_for_all_namespaces.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacityList**](../../models/V1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacityList**](../../models/V1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacityList**](../../models/V1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacityList**](../../models/V1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacityList**](../../models/V1CSIStorageCapacityList.md) |  | 


#### list_csi_storage_capacity_for_all_namespaces.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_namespaced_csi_storage_capacity**
<a name="list_namespaced_csi_storage_capacity"></a>
> V1CSIStorageCapacityList list_namespaced_csi_storage_capacity(namespace)



list or watch objects of kind CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
from kubernetes.client.model.v1_csi_storage_capacity_list import V1CSIStorageCapacityList
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

    # example passing only required values which don't have defaults set
    path_params = {
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.list_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->list_namespaced_csi_storage_capacity: %s\n" % e)

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
        api_response = api_instance.list_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->list_namespaced_csi_storage_capacity: %s\n" % e)
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
200 | [ApiResponseFor200](#list_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### list_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacityList**](../../models/V1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacityList**](../../models/V1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacityList**](../../models/V1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacityList**](../../models/V1CSIStorageCapacityList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacityList**](../../models/V1CSIStorageCapacityList.md) |  | 


#### list_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_storage_class**
<a name="list_storage_class"></a>
> V1StorageClassList list_storage_class()



list or watch objects of kind StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only optional values
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
        api_response = api_instance.list_storage_class(
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->list_storage_class: %s\n" % e)
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_storage_class.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_storage_class.ApiResponseFor401) | Unauthorized

#### list_storage_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClassList**](../../models/V1StorageClassList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClassList**](../../models/V1StorageClassList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClassList**](../../models/V1StorageClassList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClassList**](../../models/V1StorageClassList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClassList**](../../models/V1StorageClassList.md) |  | 


#### list_storage_class.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_volume_attachment**
<a name="list_volume_attachment"></a>
> V1VolumeAttachmentList list_volume_attachment()



list or watch objects of kind VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only optional values
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
        api_response = api_instance.list_volume_attachment(
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->list_volume_attachment: %s\n" % e)
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_volume_attachment.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_volume_attachment.ApiResponseFor401) | Unauthorized

#### list_volume_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachmentList**](../../models/V1VolumeAttachmentList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachmentList**](../../models/V1VolumeAttachmentList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachmentList**](../../models/V1VolumeAttachmentList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachmentList**](../../models/V1VolumeAttachmentList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachmentList**](../../models/V1VolumeAttachmentList.md) |  | 


#### list_volume_attachment.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_csi_driver**
<a name="patch_csi_driver"></a>
> V1CSIDriver patch_csi_driver(namebody)



partially update the specified CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_csi_driver(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_csi_driver: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
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
        api_response = api_instance.patch_csi_driver(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_csi_driver: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_csi_driver.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_csi_driver.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_csi_driver.ApiResponseFor401) | Unauthorized

#### patch_csi_driver.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


#### patch_csi_driver.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


#### patch_csi_driver.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_csi_node**
<a name="patch_csi_node"></a>
> V1CSINode patch_csi_node(namebody)



partially update the specified CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_csi_node(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_csi_node: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
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
        api_response = api_instance.patch_csi_node(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_csi_node: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_csi_node.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_csi_node.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_csi_node.ApiResponseFor401) | Unauthorized

#### patch_csi_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


#### patch_csi_node.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


#### patch_csi_node.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_namespaced_csi_storage_capacity**
<a name="patch_namespaced_csi_storage_capacity"></a>
> V1CSIStorageCapacity patch_namespaced_csi_storage_capacity(namenamespacebody)



partially update the specified CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
from kubernetes.client.model.v1_csi_storage_capacity import V1CSIStorageCapacity
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_namespaced_csi_storage_capacity: %s\n" % e)

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
        api_response = api_instance.patch_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_namespaced_csi_storage_capacity: %s\n" % e)
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
200 | [ApiResponseFor200](#patch_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_namespaced_csi_storage_capacity.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### patch_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


#### patch_namespaced_csi_storage_capacity.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


#### patch_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_storage_class**
<a name="patch_storage_class"></a>
> V1StorageClass patch_storage_class(namebody)



partially update the specified StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_storage_class(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_storage_class: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
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
        api_response = api_instance.patch_storage_class(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_storage_class: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_storage_class.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_storage_class.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_storage_class.ApiResponseFor401) | Unauthorized

#### patch_storage_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


#### patch_storage_class.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


#### patch_storage_class.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_volume_attachment**
<a name="patch_volume_attachment"></a>
> V1VolumeAttachment patch_volume_attachment(namebody)



partially update the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_volume_attachment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_volume_attachment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
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
        api_response = api_instance.patch_volume_attachment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_volume_attachment: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_volume_attachment.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_volume_attachment.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_volume_attachment.ApiResponseFor401) | Unauthorized

#### patch_volume_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### patch_volume_attachment.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### patch_volume_attachment.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_volume_attachment_status**
<a name="patch_volume_attachment_status"></a>
> V1VolumeAttachment patch_volume_attachment_status(namebody)



partially update status of the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_volume_attachment_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_volume_attachment_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
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
        api_response = api_instance.patch_volume_attachment_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->patch_volume_attachment_status: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_volume_attachment_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_volume_attachment_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_volume_attachment_status.ApiResponseFor401) | Unauthorized

#### patch_volume_attachment_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### patch_volume_attachment_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### patch_volume_attachment_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_csi_driver**
<a name="read_csi_driver"></a>
> V1CSIDriver read_csi_driver(name)



read the specified CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_csi_driver(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_csi_driver: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_csi_driver(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_csi_driver: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_csi_driver.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_csi_driver.ApiResponseFor401) | Unauthorized

#### read_csi_driver.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


#### read_csi_driver.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_csi_node**
<a name="read_csi_node"></a>
> V1CSINode read_csi_node(name)



read the specified CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_csi_node(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_csi_node: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_csi_node(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_csi_node: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_csi_node.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_csi_node.ApiResponseFor401) | Unauthorized

#### read_csi_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


#### read_csi_node.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_namespaced_csi_storage_capacity**
<a name="read_namespaced_csi_storage_capacity"></a>
> V1CSIStorageCapacity read_namespaced_csi_storage_capacity(namenamespace)



read the specified CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
from kubernetes.client.model.v1_csi_storage_capacity import V1CSIStorageCapacity
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_namespaced_csi_storage_capacity: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_namespaced_csi_storage_capacity: %s\n" % e)
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
200 | [ApiResponseFor200](#read_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### read_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


#### read_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_storage_class**
<a name="read_storage_class"></a>
> V1StorageClass read_storage_class(name)



read the specified StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_storage_class(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_storage_class: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_storage_class(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_storage_class: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_storage_class.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_storage_class.ApiResponseFor401) | Unauthorized

#### read_storage_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


#### read_storage_class.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_volume_attachment**
<a name="read_volume_attachment"></a>
> V1VolumeAttachment read_volume_attachment(name)



read the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_volume_attachment(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_volume_attachment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_volume_attachment(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_volume_attachment: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_volume_attachment.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_volume_attachment.ApiResponseFor401) | Unauthorized

#### read_volume_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### read_volume_attachment.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_volume_attachment_status**
<a name="read_volume_attachment_status"></a>
> V1VolumeAttachment read_volume_attachment_status(name)



read status of the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_volume_attachment_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_volume_attachment_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_volume_attachment_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->read_volume_attachment_status: %s\n" % e)
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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#read_volume_attachment_status.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_volume_attachment_status.ApiResponseFor401) | Unauthorized

#### read_volume_attachment_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### read_volume_attachment_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_csi_driver**
<a name="replace_csi_driver"></a>
> V1CSIDriver replace_csi_driver(namebody)



replace the specified CSIDriver

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = V1CSIDriver(
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
        spec=V1CSIDriverSpec(
            attach_required=True,
            fs_group_policy="fs_group_policy_example",
            pod_info_on_mount=True,
            requires_republish=True,
            se_linux_mount=True,
            storage_capacity=True,
            token_requests=[
                StorageV1TokenRequest(
                    audience="audience_example",
                    expiration_seconds=1,
                )
            ],
            volume_lifecycle_modes=[
                "volume_lifecycle_modes_example"
            ],
        ),
    )
    try:
        api_response = api_instance.replace_csi_driver(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_csi_driver: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1CSIDriver(
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
        spec=V1CSIDriverSpec(
            attach_required=True,
            fs_group_policy="fs_group_policy_example",
            pod_info_on_mount=True,
            requires_republish=True,
            se_linux_mount=True,
            storage_capacity=True,
            token_requests=[
                StorageV1TokenRequest(
                    audience="audience_example",
                    expiration_seconds=1,
                )
            ],
            volume_lifecycle_modes=[
                "volume_lifecycle_modes_example"
            ],
        ),
    )
    try:
        api_response = api_instance.replace_csi_driver(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_csi_driver: %s\n" % e)
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
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#replace_csi_driver.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_csi_driver.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_csi_driver.ApiResponseFor401) | Unauthorized

#### replace_csi_driver.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


#### replace_csi_driver.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIDriver**](../../models/V1CSIDriver.md) |  | 


#### replace_csi_driver.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_csi_node**
<a name="replace_csi_node"></a>
> V1CSINode replace_csi_node(namebody)



replace the specified CSINode

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = V1CSINode(
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
        spec=V1CSINodeSpec(
            drivers=[
                V1CSINodeDriver(
                    allocatable=V1VolumeNodeResources(
                        count=1,
                    ),
                    name="name_example",
                    node_id="node_id_example",
                    topology_keys=[
                        "topology_keys_example"
                    ],
                )
            ],
        ),
    )
    try:
        api_response = api_instance.replace_csi_node(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_csi_node: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1CSINode(
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
        spec=V1CSINodeSpec(
            drivers=[
                V1CSINodeDriver(
                    allocatable=V1VolumeNodeResources(
                        count=1,
                    ),
                    name="name_example",
                    node_id="node_id_example",
                    topology_keys=[
                        "topology_keys_example"
                    ],
                )
            ],
        ),
    )
    try:
        api_response = api_instance.replace_csi_node(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_csi_node: %s\n" % e)
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
[**V1CSINode**](../../models/V1CSINode.md) |  | 


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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#replace_csi_node.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_csi_node.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_csi_node.ApiResponseFor401) | Unauthorized

#### replace_csi_node.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


#### replace_csi_node.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSINode**](../../models/V1CSINode.md) |  | 


#### replace_csi_node.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_namespaced_csi_storage_capacity**
<a name="replace_namespaced_csi_storage_capacity"></a>
> V1CSIStorageCapacity replace_namespaced_csi_storage_capacity(namenamespacebody)



replace the specified CSIStorageCapacity

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
from kubernetes.client.model.v1_csi_storage_capacity import V1CSIStorageCapacity
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
        'namespace': "namespace_example",
    }
    query_params = {
    }
    body = V1CSIStorageCapacity(
        api_version="api_version_example",
        capacity="capacity_example",
        kind="kind_example",
        maximum_volume_size="maximum_volume_size_example",
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
        node_topology=V1LabelSelector(
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
        storage_class_name="storage_class_name_example",
    )
    try:
        api_response = api_instance.replace_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_namespaced_csi_storage_capacity: %s\n" % e)

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
    body = V1CSIStorageCapacity(
        api_version="api_version_example",
        capacity="capacity_example",
        kind="kind_example",
        maximum_volume_size="maximum_volume_size_example",
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
        node_topology=V1LabelSelector(
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
        storage_class_name="storage_class_name_example",
    )
    try:
        api_response = api_instance.replace_namespaced_csi_storage_capacity(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_namespaced_csi_storage_capacity: %s\n" % e)
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
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


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
200 | [ApiResponseFor200](#replace_namespaced_csi_storage_capacity.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_namespaced_csi_storage_capacity.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_namespaced_csi_storage_capacity.ApiResponseFor401) | Unauthorized

#### replace_namespaced_csi_storage_capacity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


#### replace_namespaced_csi_storage_capacity.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CSIStorageCapacity**](../../models/V1CSIStorageCapacity.md) |  | 


#### replace_namespaced_csi_storage_capacity.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_storage_class**
<a name="replace_storage_class"></a>
> V1StorageClass replace_storage_class(namebody)



replace the specified StorageClass

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = V1StorageClass(
        allow_volume_expansion=True,
        allowed_topologies=[
            V1TopologySelectorTerm(
                match_label_expressions=[
                    V1TopologySelectorLabelRequirement(
                        key="key_example",
                        values=[
                            "values_example"
                        ],
                    )
                ],
            )
        ],
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
        mount_options=[
            "mount_options_example"
        ],
        parameters=dict(
            "key": "key_example",
        ),
        provisioner="provisioner_example",
        reclaim_policy="reclaim_policy_example",
        volume_binding_mode="volume_binding_mode_example",
    )
    try:
        api_response = api_instance.replace_storage_class(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_storage_class: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1StorageClass(
        allow_volume_expansion=True,
        allowed_topologies=[
            V1TopologySelectorTerm(
                match_label_expressions=[
                    V1TopologySelectorLabelRequirement(
                        key="key_example",
                        values=[
                            "values_example"
                        ],
                    )
                ],
            )
        ],
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
        mount_options=[
            "mount_options_example"
        ],
        parameters=dict(
            "key": "key_example",
        ),
        provisioner="provisioner_example",
        reclaim_policy="reclaim_policy_example",
        volume_binding_mode="volume_binding_mode_example",
    )
    try:
        api_response = api_instance.replace_storage_class(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_storage_class: %s\n" % e)
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
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#replace_storage_class.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_storage_class.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_storage_class.ApiResponseFor401) | Unauthorized

#### replace_storage_class.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


#### replace_storage_class.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1StorageClass**](../../models/V1StorageClass.md) |  | 


#### replace_storage_class.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_volume_attachment**
<a name="replace_volume_attachment"></a>
> V1VolumeAttachment replace_volume_attachment(namebody)



replace the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = V1VolumeAttachment(
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
        spec=V1VolumeAttachmentSpec(
            attacher="attacher_example",
            node_name="node_name_example",
            source=V1VolumeAttachmentSource(
                inline_volume_spec=V1PersistentVolumeSpec(
                    access_modes=[
                        "access_modes_example"
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
                    capacity=dict(
                        "key": "key_example",
                    ),
                    cephfs=V1CephFSPersistentVolumeSource(
                        monitors=[
                            "monitors_example"
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
                        secret_ref=V1SecretReference(),
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
                        controller_expand_secret_ref=V1SecretReference(),
                        controller_publish_secret_ref=V1SecretReference(),
                        driver="driver_example",
                        fs_type="fs_type_example",
                        node_expand_secret_ref=V1SecretReference(),
                        node_publish_secret_ref=V1SecretReference(),
                        node_stage_secret_ref=V1SecretReference(),
                        read_only=True,
                        volume_attributes=dict(
                            "key": "key_example",
                        ),
                        volume_handle="volume_handle_example",
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
                    flex_volume=V1FlexPersistentVolumeSource(
                        driver="driver_example",
                        fs_type="fs_type_example",
                        options=dict(
                            "key": "key_example",
                        ),
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                            "portals_example"
                        ],
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        target_portal="target_portal_example",
                    ),
                    local=V1LocalVolumeSource(
                        fs_type="fs_type_example",
                        path="path_example",
                    ),
                    mount_options=[
                        "mount_options_example"
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
                                                "values_example"
                                            ],
                                        )
                                    ],
                                    match_fields=[
                                        V1NodeSelectorRequirement()
                                    ],
                                )
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
                            "monitors_example"
                        ],
                        pool="pool_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        user="user_example",
                    ),
                    scale_io=V1ScaleIOPersistentVolumeSource(
                        fs_type="fs_type_example",
                        gateway="gateway_example",
                        protection_domain="protection_domain_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                        secret_ref=V1ObjectReference(),
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
                time="1970-01-01T00:00:00.00Z",
            ),
            attached=True,
            attachment_metadata=dict(
                "key": "key_example",
            ),
            detach_error=V1VolumeError(),
        ),
    )
    try:
        api_response = api_instance.replace_volume_attachment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_volume_attachment: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1VolumeAttachment(
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
        spec=V1VolumeAttachmentSpec(
            attacher="attacher_example",
            node_name="node_name_example",
            source=V1VolumeAttachmentSource(
                inline_volume_spec=V1PersistentVolumeSpec(
                    access_modes=[
                        "access_modes_example"
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
                    capacity=dict(
                        "key": "key_example",
                    ),
                    cephfs=V1CephFSPersistentVolumeSource(
                        monitors=[
                            "monitors_example"
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
                        secret_ref=V1SecretReference(),
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
                        controller_expand_secret_ref=V1SecretReference(),
                        controller_publish_secret_ref=V1SecretReference(),
                        driver="driver_example",
                        fs_type="fs_type_example",
                        node_expand_secret_ref=V1SecretReference(),
                        node_publish_secret_ref=V1SecretReference(),
                        node_stage_secret_ref=V1SecretReference(),
                        read_only=True,
                        volume_attributes=dict(
                            "key": "key_example",
                        ),
                        volume_handle="volume_handle_example",
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
                    flex_volume=V1FlexPersistentVolumeSource(
                        driver="driver_example",
                        fs_type="fs_type_example",
                        options=dict(
                            "key": "key_example",
                        ),
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                            "portals_example"
                        ],
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        target_portal="target_portal_example",
                    ),
                    local=V1LocalVolumeSource(
                        fs_type="fs_type_example",
                        path="path_example",
                    ),
                    mount_options=[
                        "mount_options_example"
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
                                                "values_example"
                                            ],
                                        )
                                    ],
                                    match_fields=[
                                        V1NodeSelectorRequirement()
                                    ],
                                )
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
                            "monitors_example"
                        ],
                        pool="pool_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        user="user_example",
                    ),
                    scale_io=V1ScaleIOPersistentVolumeSource(
                        fs_type="fs_type_example",
                        gateway="gateway_example",
                        protection_domain="protection_domain_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                        secret_ref=V1ObjectReference(),
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
                time="1970-01-01T00:00:00.00Z",
            ),
            attached=True,
            attachment_metadata=dict(
                "key": "key_example",
            ),
            detach_error=V1VolumeError(),
        ),
    )
    try:
        api_response = api_instance.replace_volume_attachment(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_volume_attachment: %s\n" % e)
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
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#replace_volume_attachment.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_volume_attachment.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_volume_attachment.ApiResponseFor401) | Unauthorized

#### replace_volume_attachment.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### replace_volume_attachment.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### replace_volume_attachment.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_volume_attachment_status**
<a name="replace_volume_attachment_status"></a>
> V1VolumeAttachment replace_volume_attachment_status(namebody)



replace status of the specified VolumeAttachment

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import storage_v1_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = V1VolumeAttachment(
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
        spec=V1VolumeAttachmentSpec(
            attacher="attacher_example",
            node_name="node_name_example",
            source=V1VolumeAttachmentSource(
                inline_volume_spec=V1PersistentVolumeSpec(
                    access_modes=[
                        "access_modes_example"
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
                    capacity=dict(
                        "key": "key_example",
                    ),
                    cephfs=V1CephFSPersistentVolumeSource(
                        monitors=[
                            "monitors_example"
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
                        secret_ref=V1SecretReference(),
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
                        controller_expand_secret_ref=V1SecretReference(),
                        controller_publish_secret_ref=V1SecretReference(),
                        driver="driver_example",
                        fs_type="fs_type_example",
                        node_expand_secret_ref=V1SecretReference(),
                        node_publish_secret_ref=V1SecretReference(),
                        node_stage_secret_ref=V1SecretReference(),
                        read_only=True,
                        volume_attributes=dict(
                            "key": "key_example",
                        ),
                        volume_handle="volume_handle_example",
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
                    flex_volume=V1FlexPersistentVolumeSource(
                        driver="driver_example",
                        fs_type="fs_type_example",
                        options=dict(
                            "key": "key_example",
                        ),
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                            "portals_example"
                        ],
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        target_portal="target_portal_example",
                    ),
                    local=V1LocalVolumeSource(
                        fs_type="fs_type_example",
                        path="path_example",
                    ),
                    mount_options=[
                        "mount_options_example"
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
                                                "values_example"
                                            ],
                                        )
                                    ],
                                    match_fields=[
                                        V1NodeSelectorRequirement()
                                    ],
                                )
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
                            "monitors_example"
                        ],
                        pool="pool_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        user="user_example",
                    ),
                    scale_io=V1ScaleIOPersistentVolumeSource(
                        fs_type="fs_type_example",
                        gateway="gateway_example",
                        protection_domain="protection_domain_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                        secret_ref=V1ObjectReference(),
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
                time="1970-01-01T00:00:00.00Z",
            ),
            attached=True,
            attachment_metadata=dict(
                "key": "key_example",
            ),
            detach_error=V1VolumeError(),
        ),
    )
    try:
        api_response = api_instance.replace_volume_attachment_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_volume_attachment_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1VolumeAttachment(
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
        spec=V1VolumeAttachmentSpec(
            attacher="attacher_example",
            node_name="node_name_example",
            source=V1VolumeAttachmentSource(
                inline_volume_spec=V1PersistentVolumeSpec(
                    access_modes=[
                        "access_modes_example"
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
                    capacity=dict(
                        "key": "key_example",
                    ),
                    cephfs=V1CephFSPersistentVolumeSource(
                        monitors=[
                            "monitors_example"
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
                        secret_ref=V1SecretReference(),
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
                        controller_expand_secret_ref=V1SecretReference(),
                        controller_publish_secret_ref=V1SecretReference(),
                        driver="driver_example",
                        fs_type="fs_type_example",
                        node_expand_secret_ref=V1SecretReference(),
                        node_publish_secret_ref=V1SecretReference(),
                        node_stage_secret_ref=V1SecretReference(),
                        read_only=True,
                        volume_attributes=dict(
                            "key": "key_example",
                        ),
                        volume_handle="volume_handle_example",
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
                    flex_volume=V1FlexPersistentVolumeSource(
                        driver="driver_example",
                        fs_type="fs_type_example",
                        options=dict(
                            "key": "key_example",
                        ),
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                            "portals_example"
                        ],
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        target_portal="target_portal_example",
                    ),
                    local=V1LocalVolumeSource(
                        fs_type="fs_type_example",
                        path="path_example",
                    ),
                    mount_options=[
                        "mount_options_example"
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
                                                "values_example"
                                            ],
                                        )
                                    ],
                                    match_fields=[
                                        V1NodeSelectorRequirement()
                                    ],
                                )
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
                            "monitors_example"
                        ],
                        pool="pool_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
                        user="user_example",
                    ),
                    scale_io=V1ScaleIOPersistentVolumeSource(
                        fs_type="fs_type_example",
                        gateway="gateway_example",
                        protection_domain="protection_domain_example",
                        read_only=True,
                        secret_ref=V1SecretReference(),
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
                        secret_ref=V1ObjectReference(),
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
                time="1970-01-01T00:00:00.00Z",
            ),
            attached=True,
            attachment_metadata=dict(
                "key": "key_example",
            ),
            detach_error=V1VolumeError(),
        ),
    )
    try:
        api_response = api_instance.replace_volume_attachment_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling StorageV1Api->replace_volume_attachment_status: %s\n" % e)
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
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


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

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#replace_volume_attachment_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_volume_attachment_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_volume_attachment_status.ApiResponseFor401) | Unauthorized

#### replace_volume_attachment_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### replace_volume_attachment_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1VolumeAttachment**](../../models/V1VolumeAttachment.md) |  | 


#### replace_volume_attachment_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

