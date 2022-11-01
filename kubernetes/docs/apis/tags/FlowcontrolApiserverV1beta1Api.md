<a name="__pageTop"></a>
# kubernetes.client.apis.tags.flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_flow_schema**](#create_flow_schema) | **post** /apis/flowcontrol.apiserver.k8s.io/v1beta1/flowschemas | 
[**create_priority_level_configuration**](#create_priority_level_configuration) | **post** /apis/flowcontrol.apiserver.k8s.io/v1beta1/prioritylevelconfigurations | 
[**delete_collection_flow_schema**](#delete_collection_flow_schema) | **delete** /apis/flowcontrol.apiserver.k8s.io/v1beta1/flowschemas | 
[**delete_collection_priority_level_configuration**](#delete_collection_priority_level_configuration) | **delete** /apis/flowcontrol.apiserver.k8s.io/v1beta1/prioritylevelconfigurations | 
[**delete_flow_schema**](#delete_flow_schema) | **delete** /apis/flowcontrol.apiserver.k8s.io/v1beta1/flowschemas/{name} | 
[**delete_priority_level_configuration**](#delete_priority_level_configuration) | **delete** /apis/flowcontrol.apiserver.k8s.io/v1beta1/prioritylevelconfigurations/{name} | 
[**get_api_resources**](#get_api_resources) | **get** /apis/flowcontrol.apiserver.k8s.io/v1beta1/ | 
[**list_flow_schema**](#list_flow_schema) | **get** /apis/flowcontrol.apiserver.k8s.io/v1beta1/flowschemas | 
[**list_priority_level_configuration**](#list_priority_level_configuration) | **get** /apis/flowcontrol.apiserver.k8s.io/v1beta1/prioritylevelconfigurations | 
[**patch_flow_schema**](#patch_flow_schema) | **patch** /apis/flowcontrol.apiserver.k8s.io/v1beta1/flowschemas/{name} | 
[**patch_flow_schema_status**](#patch_flow_schema_status) | **patch** /apis/flowcontrol.apiserver.k8s.io/v1beta1/flowschemas/{name}/status | 
[**patch_priority_level_configuration**](#patch_priority_level_configuration) | **patch** /apis/flowcontrol.apiserver.k8s.io/v1beta1/prioritylevelconfigurations/{name} | 
[**patch_priority_level_configuration_status**](#patch_priority_level_configuration_status) | **patch** /apis/flowcontrol.apiserver.k8s.io/v1beta1/prioritylevelconfigurations/{name}/status | 
[**read_flow_schema**](#read_flow_schema) | **get** /apis/flowcontrol.apiserver.k8s.io/v1beta1/flowschemas/{name} | 
[**read_flow_schema_status**](#read_flow_schema_status) | **get** /apis/flowcontrol.apiserver.k8s.io/v1beta1/flowschemas/{name}/status | 
[**read_priority_level_configuration**](#read_priority_level_configuration) | **get** /apis/flowcontrol.apiserver.k8s.io/v1beta1/prioritylevelconfigurations/{name} | 
[**read_priority_level_configuration_status**](#read_priority_level_configuration_status) | **get** /apis/flowcontrol.apiserver.k8s.io/v1beta1/prioritylevelconfigurations/{name}/status | 
[**replace_flow_schema**](#replace_flow_schema) | **put** /apis/flowcontrol.apiserver.k8s.io/v1beta1/flowschemas/{name} | 
[**replace_flow_schema_status**](#replace_flow_schema_status) | **put** /apis/flowcontrol.apiserver.k8s.io/v1beta1/flowschemas/{name}/status | 
[**replace_priority_level_configuration**](#replace_priority_level_configuration) | **put** /apis/flowcontrol.apiserver.k8s.io/v1beta1/prioritylevelconfigurations/{name} | 
[**replace_priority_level_configuration_status**](#replace_priority_level_configuration_status) | **put** /apis/flowcontrol.apiserver.k8s.io/v1beta1/prioritylevelconfigurations/{name}/status | 

# **create_flow_schema**
<a name="create_flow_schema"></a>
> V1beta1FlowSchema create_flow_schema(body)



create a FlowSchema

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_flow_schema import V1beta1FlowSchema
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = V1beta1FlowSchema(
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
        spec=V1beta1FlowSchemaSpec(
            distinguisher_method=V1beta1FlowDistinguisherMethod(
                type="type_example",
            ),
            matching_precedence=1,
            priority_level_configuration=V1beta1PriorityLevelConfigurationReference(
                name="name_example",
            ),
            rules=[
                V1beta1PolicyRulesWithSubjects(
                    non_resource_rules=[
                        V1beta1NonResourcePolicyRule(
                            non_resource_urls=[
                                "non_resource_urls_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    resource_rules=[
                        V1beta1ResourcePolicyRule(
                            api_groups=[
                                "api_groups_example"
                            ],
                            cluster_scope=True,
                            namespaces=[
                                "namespaces_example"
                            ],
                            resources=[
                                "resources_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    subjects=[
                        V1beta1Subject(
                            group=V1beta1GroupSubject(
                                name="name_example",
                            ),
                            kind="kind_example",
                            service_account=V1beta1ServiceAccountSubject(
                                name="name_example",
                                namespace="namespace_example",
                            ),
                            user=V1beta1UserSubject(
                                name="name_example",
                            ),
                        )
                    ],
                )
            ],
        ),
        status=V1beta1FlowSchemaStatus(
            conditions=[
                V1beta1FlowSchemaCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.create_flow_schema(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->create_flow_schema: %s\n" % e)

    # example passing only optional values
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1beta1FlowSchema(
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
        spec=V1beta1FlowSchemaSpec(
            distinguisher_method=V1beta1FlowDistinguisherMethod(
                type="type_example",
            ),
            matching_precedence=1,
            priority_level_configuration=V1beta1PriorityLevelConfigurationReference(
                name="name_example",
            ),
            rules=[
                V1beta1PolicyRulesWithSubjects(
                    non_resource_rules=[
                        V1beta1NonResourcePolicyRule(
                            non_resource_urls=[
                                "non_resource_urls_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    resource_rules=[
                        V1beta1ResourcePolicyRule(
                            api_groups=[
                                "api_groups_example"
                            ],
                            cluster_scope=True,
                            namespaces=[
                                "namespaces_example"
                            ],
                            resources=[
                                "resources_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    subjects=[
                        V1beta1Subject(
                            group=V1beta1GroupSubject(
                                name="name_example",
                            ),
                            kind="kind_example",
                            service_account=V1beta1ServiceAccountSubject(
                                name="name_example",
                                namespace="namespace_example",
                            ),
                            user=V1beta1UserSubject(
                                name="name_example",
                            ),
                        )
                    ],
                )
            ],
        ),
        status=V1beta1FlowSchemaStatus(
            conditions=[
                V1beta1FlowSchemaCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.create_flow_schema(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->create_flow_schema: %s\n" % e)
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
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


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
200 | [ApiResponseFor200](#create_flow_schema.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_flow_schema.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_flow_schema.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_flow_schema.ApiResponseFor401) | Unauthorized

#### create_flow_schema.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### create_flow_schema.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### create_flow_schema.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### create_flow_schema.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_priority_level_configuration**
<a name="create_priority_level_configuration"></a>
> V1beta1PriorityLevelConfiguration create_priority_level_configuration(body)



create a PriorityLevelConfiguration

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_priority_level_configuration import V1beta1PriorityLevelConfiguration
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = V1beta1PriorityLevelConfiguration(
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
        spec=V1beta1PriorityLevelConfigurationSpec(
            limited=V1beta1LimitedPriorityLevelConfiguration(
                assured_concurrency_shares=1,
                limit_response=V1beta1LimitResponse(
                    queuing=V1beta1QueuingConfiguration(
                        hand_size=1,
                        queue_length_limit=1,
                        queues=1,
                    ),
                    type="type_example",
                ),
            ),
            type="type_example",
        ),
        status=V1beta1PriorityLevelConfigurationStatus(
            conditions=[
                V1beta1PriorityLevelConfigurationCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.create_priority_level_configuration(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->create_priority_level_configuration: %s\n" % e)

    # example passing only optional values
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1beta1PriorityLevelConfiguration(
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
        spec=V1beta1PriorityLevelConfigurationSpec(
            limited=V1beta1LimitedPriorityLevelConfiguration(
                assured_concurrency_shares=1,
                limit_response=V1beta1LimitResponse(
                    queuing=V1beta1QueuingConfiguration(
                        hand_size=1,
                        queue_length_limit=1,
                        queues=1,
                    ),
                    type="type_example",
                ),
            ),
            type="type_example",
        ),
        status=V1beta1PriorityLevelConfigurationStatus(
            conditions=[
                V1beta1PriorityLevelConfigurationCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.create_priority_level_configuration(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->create_priority_level_configuration: %s\n" % e)
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
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


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
200 | [ApiResponseFor200](#create_priority_level_configuration.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_priority_level_configuration.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_priority_level_configuration.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_priority_level_configuration.ApiResponseFor401) | Unauthorized

#### create_priority_level_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### create_priority_level_configuration.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### create_priority_level_configuration.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### create_priority_level_configuration.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_collection_flow_schema**
<a name="delete_collection_flow_schema"></a>
> V1Status delete_collection_flow_schema()



delete collection of FlowSchema

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

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
        api_response = api_instance.delete_collection_flow_schema(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->delete_collection_flow_schema: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_collection_flow_schema.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#delete_collection_flow_schema.ApiResponseFor401) | Unauthorized

#### delete_collection_flow_schema.ApiResponseFor200
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


#### delete_collection_flow_schema.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_collection_priority_level_configuration**
<a name="delete_collection_priority_level_configuration"></a>
> V1Status delete_collection_priority_level_configuration()



delete collection of PriorityLevelConfiguration

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

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
        api_response = api_instance.delete_collection_priority_level_configuration(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->delete_collection_priority_level_configuration: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_collection_priority_level_configuration.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#delete_collection_priority_level_configuration.ApiResponseFor401) | Unauthorized

#### delete_collection_priority_level_configuration.ApiResponseFor200
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


#### delete_collection_priority_level_configuration.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_flow_schema**
<a name="delete_flow_schema"></a>
> V1Status delete_flow_schema(name)



delete a FlowSchema

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_flow_schema(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->delete_flow_schema: %s\n" % e)

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
        api_response = api_instance.delete_flow_schema(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->delete_flow_schema: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_flow_schema.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#delete_flow_schema.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#delete_flow_schema.ApiResponseFor401) | Unauthorized

#### delete_flow_schema.ApiResponseFor200
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


#### delete_flow_schema.ApiResponseFor202
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


#### delete_flow_schema.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_priority_level_configuration**
<a name="delete_priority_level_configuration"></a>
> V1Status delete_priority_level_configuration(name)



delete a PriorityLevelConfiguration

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_priority_level_configuration(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->delete_priority_level_configuration: %s\n" % e)

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
        api_response = api_instance.delete_priority_level_configuration(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->delete_priority_level_configuration: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_priority_level_configuration.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#delete_priority_level_configuration.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#delete_priority_level_configuration.ApiResponseFor401) | Unauthorized

#### delete_priority_level_configuration.ApiResponseFor200
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


#### delete_priority_level_configuration.ApiResponseFor202
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


#### delete_priority_level_configuration.ApiResponseFor401
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
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_api_resources()
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->get_api_resources: %s\n" % e)
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

# **list_flow_schema**
<a name="list_flow_schema"></a>
> V1beta1FlowSchemaList list_flow_schema()



list or watch objects of kind FlowSchema

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_flow_schema_list import V1beta1FlowSchemaList
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

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
        api_response = api_instance.list_flow_schema(
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->list_flow_schema: %s\n" % e)
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
200 | [ApiResponseFor200](#list_flow_schema.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_flow_schema.ApiResponseFor401) | Unauthorized

#### list_flow_schema.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchemaList**](../../models/V1beta1FlowSchemaList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchemaList**](../../models/V1beta1FlowSchemaList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchemaList**](../../models/V1beta1FlowSchemaList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchemaList**](../../models/V1beta1FlowSchemaList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchemaList**](../../models/V1beta1FlowSchemaList.md) |  | 


#### list_flow_schema.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_priority_level_configuration**
<a name="list_priority_level_configuration"></a>
> V1beta1PriorityLevelConfigurationList list_priority_level_configuration()



list or watch objects of kind PriorityLevelConfiguration

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_priority_level_configuration_list import V1beta1PriorityLevelConfigurationList
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

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
        api_response = api_instance.list_priority_level_configuration(
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->list_priority_level_configuration: %s\n" % e)
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
200 | [ApiResponseFor200](#list_priority_level_configuration.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_priority_level_configuration.ApiResponseFor401) | Unauthorized

#### list_priority_level_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfigurationList**](../../models/V1beta1PriorityLevelConfigurationList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfigurationList**](../../models/V1beta1PriorityLevelConfigurationList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfigurationList**](../../models/V1beta1PriorityLevelConfigurationList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfigurationList**](../../models/V1beta1PriorityLevelConfigurationList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfigurationList**](../../models/V1beta1PriorityLevelConfigurationList.md) |  | 


#### list_priority_level_configuration.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_flow_schema**
<a name="patch_flow_schema"></a>
> V1beta1FlowSchema patch_flow_schema(namebody)



partially update the specified FlowSchema

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_flow_schema import V1beta1FlowSchema
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_flow_schema(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->patch_flow_schema: %s\n" % e)

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
        api_response = api_instance.patch_flow_schema(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->patch_flow_schema: %s\n" % e)
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
200 | [ApiResponseFor200](#patch_flow_schema.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_flow_schema.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_flow_schema.ApiResponseFor401) | Unauthorized

#### patch_flow_schema.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### patch_flow_schema.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### patch_flow_schema.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_flow_schema_status**
<a name="patch_flow_schema_status"></a>
> V1beta1FlowSchema patch_flow_schema_status(namebody)



partially update status of the specified FlowSchema

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_flow_schema import V1beta1FlowSchema
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_flow_schema_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->patch_flow_schema_status: %s\n" % e)

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
        api_response = api_instance.patch_flow_schema_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->patch_flow_schema_status: %s\n" % e)
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
200 | [ApiResponseFor200](#patch_flow_schema_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_flow_schema_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_flow_schema_status.ApiResponseFor401) | Unauthorized

#### patch_flow_schema_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### patch_flow_schema_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### patch_flow_schema_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_priority_level_configuration**
<a name="patch_priority_level_configuration"></a>
> V1beta1PriorityLevelConfiguration patch_priority_level_configuration(namebody)



partially update the specified PriorityLevelConfiguration

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_priority_level_configuration import V1beta1PriorityLevelConfiguration
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_priority_level_configuration(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->patch_priority_level_configuration: %s\n" % e)

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
        api_response = api_instance.patch_priority_level_configuration(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->patch_priority_level_configuration: %s\n" % e)
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
200 | [ApiResponseFor200](#patch_priority_level_configuration.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_priority_level_configuration.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_priority_level_configuration.ApiResponseFor401) | Unauthorized

#### patch_priority_level_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### patch_priority_level_configuration.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### patch_priority_level_configuration.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_priority_level_configuration_status**
<a name="patch_priority_level_configuration_status"></a>
> V1beta1PriorityLevelConfiguration patch_priority_level_configuration_status(namebody)



partially update status of the specified PriorityLevelConfiguration

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_priority_level_configuration import V1beta1PriorityLevelConfiguration
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_priority_level_configuration_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->patch_priority_level_configuration_status: %s\n" % e)

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
        api_response = api_instance.patch_priority_level_configuration_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->patch_priority_level_configuration_status: %s\n" % e)
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
200 | [ApiResponseFor200](#patch_priority_level_configuration_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_priority_level_configuration_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_priority_level_configuration_status.ApiResponseFor401) | Unauthorized

#### patch_priority_level_configuration_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### patch_priority_level_configuration_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### patch_priority_level_configuration_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_flow_schema**
<a name="read_flow_schema"></a>
> V1beta1FlowSchema read_flow_schema(name)



read the specified FlowSchema

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_flow_schema import V1beta1FlowSchema
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_flow_schema(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->read_flow_schema: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_flow_schema(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->read_flow_schema: %s\n" % e)
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
200 | [ApiResponseFor200](#read_flow_schema.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_flow_schema.ApiResponseFor401) | Unauthorized

#### read_flow_schema.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### read_flow_schema.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_flow_schema_status**
<a name="read_flow_schema_status"></a>
> V1beta1FlowSchema read_flow_schema_status(name)



read status of the specified FlowSchema

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_flow_schema import V1beta1FlowSchema
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_flow_schema_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->read_flow_schema_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_flow_schema_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->read_flow_schema_status: %s\n" % e)
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
200 | [ApiResponseFor200](#read_flow_schema_status.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_flow_schema_status.ApiResponseFor401) | Unauthorized

#### read_flow_schema_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### read_flow_schema_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_priority_level_configuration**
<a name="read_priority_level_configuration"></a>
> V1beta1PriorityLevelConfiguration read_priority_level_configuration(name)



read the specified PriorityLevelConfiguration

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_priority_level_configuration import V1beta1PriorityLevelConfiguration
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_priority_level_configuration(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->read_priority_level_configuration: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_priority_level_configuration(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->read_priority_level_configuration: %s\n" % e)
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
200 | [ApiResponseFor200](#read_priority_level_configuration.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_priority_level_configuration.ApiResponseFor401) | Unauthorized

#### read_priority_level_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### read_priority_level_configuration.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_priority_level_configuration_status**
<a name="read_priority_level_configuration_status"></a>
> V1beta1PriorityLevelConfiguration read_priority_level_configuration_status(name)



read status of the specified PriorityLevelConfiguration

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_priority_level_configuration import V1beta1PriorityLevelConfiguration
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_priority_level_configuration_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->read_priority_level_configuration_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_priority_level_configuration_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->read_priority_level_configuration_status: %s\n" % e)
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
200 | [ApiResponseFor200](#read_priority_level_configuration_status.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_priority_level_configuration_status.ApiResponseFor401) | Unauthorized

#### read_priority_level_configuration_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### read_priority_level_configuration_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_flow_schema**
<a name="replace_flow_schema"></a>
> V1beta1FlowSchema replace_flow_schema(namebody)



replace the specified FlowSchema

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_flow_schema import V1beta1FlowSchema
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = V1beta1FlowSchema(
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
        spec=V1beta1FlowSchemaSpec(
            distinguisher_method=V1beta1FlowDistinguisherMethod(
                type="type_example",
            ),
            matching_precedence=1,
            priority_level_configuration=V1beta1PriorityLevelConfigurationReference(
                name="name_example",
            ),
            rules=[
                V1beta1PolicyRulesWithSubjects(
                    non_resource_rules=[
                        V1beta1NonResourcePolicyRule(
                            non_resource_urls=[
                                "non_resource_urls_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    resource_rules=[
                        V1beta1ResourcePolicyRule(
                            api_groups=[
                                "api_groups_example"
                            ],
                            cluster_scope=True,
                            namespaces=[
                                "namespaces_example"
                            ],
                            resources=[
                                "resources_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    subjects=[
                        V1beta1Subject(
                            group=V1beta1GroupSubject(
                                name="name_example",
                            ),
                            kind="kind_example",
                            service_account=V1beta1ServiceAccountSubject(
                                name="name_example",
                                namespace="namespace_example",
                            ),
                            user=V1beta1UserSubject(
                                name="name_example",
                            ),
                        )
                    ],
                )
            ],
        ),
        status=V1beta1FlowSchemaStatus(
            conditions=[
                V1beta1FlowSchemaCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.replace_flow_schema(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->replace_flow_schema: %s\n" % e)

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
    body = V1beta1FlowSchema(
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
        spec=V1beta1FlowSchemaSpec(
            distinguisher_method=V1beta1FlowDistinguisherMethod(
                type="type_example",
            ),
            matching_precedence=1,
            priority_level_configuration=V1beta1PriorityLevelConfigurationReference(
                name="name_example",
            ),
            rules=[
                V1beta1PolicyRulesWithSubjects(
                    non_resource_rules=[
                        V1beta1NonResourcePolicyRule(
                            non_resource_urls=[
                                "non_resource_urls_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    resource_rules=[
                        V1beta1ResourcePolicyRule(
                            api_groups=[
                                "api_groups_example"
                            ],
                            cluster_scope=True,
                            namespaces=[
                                "namespaces_example"
                            ],
                            resources=[
                                "resources_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    subjects=[
                        V1beta1Subject(
                            group=V1beta1GroupSubject(
                                name="name_example",
                            ),
                            kind="kind_example",
                            service_account=V1beta1ServiceAccountSubject(
                                name="name_example",
                                namespace="namespace_example",
                            ),
                            user=V1beta1UserSubject(
                                name="name_example",
                            ),
                        )
                    ],
                )
            ],
        ),
        status=V1beta1FlowSchemaStatus(
            conditions=[
                V1beta1FlowSchemaCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.replace_flow_schema(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->replace_flow_schema: %s\n" % e)
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
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


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
200 | [ApiResponseFor200](#replace_flow_schema.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_flow_schema.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_flow_schema.ApiResponseFor401) | Unauthorized

#### replace_flow_schema.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### replace_flow_schema.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### replace_flow_schema.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_flow_schema_status**
<a name="replace_flow_schema_status"></a>
> V1beta1FlowSchema replace_flow_schema_status(namebody)



replace status of the specified FlowSchema

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_flow_schema import V1beta1FlowSchema
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = V1beta1FlowSchema(
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
        spec=V1beta1FlowSchemaSpec(
            distinguisher_method=V1beta1FlowDistinguisherMethod(
                type="type_example",
            ),
            matching_precedence=1,
            priority_level_configuration=V1beta1PriorityLevelConfigurationReference(
                name="name_example",
            ),
            rules=[
                V1beta1PolicyRulesWithSubjects(
                    non_resource_rules=[
                        V1beta1NonResourcePolicyRule(
                            non_resource_urls=[
                                "non_resource_urls_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    resource_rules=[
                        V1beta1ResourcePolicyRule(
                            api_groups=[
                                "api_groups_example"
                            ],
                            cluster_scope=True,
                            namespaces=[
                                "namespaces_example"
                            ],
                            resources=[
                                "resources_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    subjects=[
                        V1beta1Subject(
                            group=V1beta1GroupSubject(
                                name="name_example",
                            ),
                            kind="kind_example",
                            service_account=V1beta1ServiceAccountSubject(
                                name="name_example",
                                namespace="namespace_example",
                            ),
                            user=V1beta1UserSubject(
                                name="name_example",
                            ),
                        )
                    ],
                )
            ],
        ),
        status=V1beta1FlowSchemaStatus(
            conditions=[
                V1beta1FlowSchemaCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.replace_flow_schema_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->replace_flow_schema_status: %s\n" % e)

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
    body = V1beta1FlowSchema(
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
        spec=V1beta1FlowSchemaSpec(
            distinguisher_method=V1beta1FlowDistinguisherMethod(
                type="type_example",
            ),
            matching_precedence=1,
            priority_level_configuration=V1beta1PriorityLevelConfigurationReference(
                name="name_example",
            ),
            rules=[
                V1beta1PolicyRulesWithSubjects(
                    non_resource_rules=[
                        V1beta1NonResourcePolicyRule(
                            non_resource_urls=[
                                "non_resource_urls_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    resource_rules=[
                        V1beta1ResourcePolicyRule(
                            api_groups=[
                                "api_groups_example"
                            ],
                            cluster_scope=True,
                            namespaces=[
                                "namespaces_example"
                            ],
                            resources=[
                                "resources_example"
                            ],
                            verbs=[
                                "verbs_example"
                            ],
                        )
                    ],
                    subjects=[
                        V1beta1Subject(
                            group=V1beta1GroupSubject(
                                name="name_example",
                            ),
                            kind="kind_example",
                            service_account=V1beta1ServiceAccountSubject(
                                name="name_example",
                                namespace="namespace_example",
                            ),
                            user=V1beta1UserSubject(
                                name="name_example",
                            ),
                        )
                    ],
                )
            ],
        ),
        status=V1beta1FlowSchemaStatus(
            conditions=[
                V1beta1FlowSchemaCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.replace_flow_schema_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->replace_flow_schema_status: %s\n" % e)
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
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


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
200 | [ApiResponseFor200](#replace_flow_schema_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_flow_schema_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_flow_schema_status.ApiResponseFor401) | Unauthorized

#### replace_flow_schema_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### replace_flow_schema_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1FlowSchema**](../../models/V1beta1FlowSchema.md) |  | 


#### replace_flow_schema_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_priority_level_configuration**
<a name="replace_priority_level_configuration"></a>
> V1beta1PriorityLevelConfiguration replace_priority_level_configuration(namebody)



replace the specified PriorityLevelConfiguration

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_priority_level_configuration import V1beta1PriorityLevelConfiguration
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = V1beta1PriorityLevelConfiguration(
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
        spec=V1beta1PriorityLevelConfigurationSpec(
            limited=V1beta1LimitedPriorityLevelConfiguration(
                assured_concurrency_shares=1,
                limit_response=V1beta1LimitResponse(
                    queuing=V1beta1QueuingConfiguration(
                        hand_size=1,
                        queue_length_limit=1,
                        queues=1,
                    ),
                    type="type_example",
                ),
            ),
            type="type_example",
        ),
        status=V1beta1PriorityLevelConfigurationStatus(
            conditions=[
                V1beta1PriorityLevelConfigurationCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.replace_priority_level_configuration(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->replace_priority_level_configuration: %s\n" % e)

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
    body = V1beta1PriorityLevelConfiguration(
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
        spec=V1beta1PriorityLevelConfigurationSpec(
            limited=V1beta1LimitedPriorityLevelConfiguration(
                assured_concurrency_shares=1,
                limit_response=V1beta1LimitResponse(
                    queuing=V1beta1QueuingConfiguration(
                        hand_size=1,
                        queue_length_limit=1,
                        queues=1,
                    ),
                    type="type_example",
                ),
            ),
            type="type_example",
        ),
        status=V1beta1PriorityLevelConfigurationStatus(
            conditions=[
                V1beta1PriorityLevelConfigurationCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.replace_priority_level_configuration(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->replace_priority_level_configuration: %s\n" % e)
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
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


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
200 | [ApiResponseFor200](#replace_priority_level_configuration.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_priority_level_configuration.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_priority_level_configuration.ApiResponseFor401) | Unauthorized

#### replace_priority_level_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### replace_priority_level_configuration.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### replace_priority_level_configuration.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_priority_level_configuration_status**
<a name="replace_priority_level_configuration_status"></a>
> V1beta1PriorityLevelConfiguration replace_priority_level_configuration_status(namebody)



replace status of the specified PriorityLevelConfiguration

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import flowcontrol_apiserver_v1beta1_api
from kubernetes.client.model.v1beta1_priority_level_configuration import V1beta1PriorityLevelConfiguration
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
    api_instance = flowcontrol_apiserver_v1beta1_api.FlowcontrolApiserverV1beta1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = V1beta1PriorityLevelConfiguration(
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
        spec=V1beta1PriorityLevelConfigurationSpec(
            limited=V1beta1LimitedPriorityLevelConfiguration(
                assured_concurrency_shares=1,
                limit_response=V1beta1LimitResponse(
                    queuing=V1beta1QueuingConfiguration(
                        hand_size=1,
                        queue_length_limit=1,
                        queues=1,
                    ),
                    type="type_example",
                ),
            ),
            type="type_example",
        ),
        status=V1beta1PriorityLevelConfigurationStatus(
            conditions=[
                V1beta1PriorityLevelConfigurationCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.replace_priority_level_configuration_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->replace_priority_level_configuration_status: %s\n" % e)

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
    body = V1beta1PriorityLevelConfiguration(
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
        spec=V1beta1PriorityLevelConfigurationSpec(
            limited=V1beta1LimitedPriorityLevelConfiguration(
                assured_concurrency_shares=1,
                limit_response=V1beta1LimitResponse(
                    queuing=V1beta1QueuingConfiguration(
                        hand_size=1,
                        queue_length_limit=1,
                        queues=1,
                    ),
                    type="type_example",
                ),
            ),
            type="type_example",
        ),
        status=V1beta1PriorityLevelConfigurationStatus(
            conditions=[
                V1beta1PriorityLevelConfigurationCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
        ),
    )
    try:
        api_response = api_instance.replace_priority_level_configuration_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling FlowcontrolApiserverV1beta1Api->replace_priority_level_configuration_status: %s\n" % e)
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
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


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
200 | [ApiResponseFor200](#replace_priority_level_configuration_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_priority_level_configuration_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_priority_level_configuration_status.ApiResponseFor401) | Unauthorized

#### replace_priority_level_configuration_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### replace_priority_level_configuration_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1beta1PriorityLevelConfiguration**](../../models/V1beta1PriorityLevelConfiguration.md) |  | 


#### replace_priority_level_configuration_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

