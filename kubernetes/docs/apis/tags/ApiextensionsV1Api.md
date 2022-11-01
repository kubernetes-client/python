<a name="__pageTop"></a>
# kubernetes.client.apis.tags.apiextensions_v1_api.ApiextensionsV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_resource_definition**](#create_custom_resource_definition) | **post** /apis/apiextensions.k8s.io/v1/customresourcedefinitions | 
[**delete_collection_custom_resource_definition**](#delete_collection_custom_resource_definition) | **delete** /apis/apiextensions.k8s.io/v1/customresourcedefinitions | 
[**delete_custom_resource_definition**](#delete_custom_resource_definition) | **delete** /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name} | 
[**get_api_resources**](#get_api_resources) | **get** /apis/apiextensions.k8s.io/v1/ | 
[**list_custom_resource_definition**](#list_custom_resource_definition) | **get** /apis/apiextensions.k8s.io/v1/customresourcedefinitions | 
[**patch_custom_resource_definition**](#patch_custom_resource_definition) | **patch** /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name} | 
[**patch_custom_resource_definition_status**](#patch_custom_resource_definition_status) | **patch** /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}/status | 
[**read_custom_resource_definition**](#read_custom_resource_definition) | **get** /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name} | 
[**read_custom_resource_definition_status**](#read_custom_resource_definition_status) | **get** /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}/status | 
[**replace_custom_resource_definition**](#replace_custom_resource_definition) | **put** /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name} | 
[**replace_custom_resource_definition_status**](#replace_custom_resource_definition_status) | **put** /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}/status | 

# **create_custom_resource_definition**
<a name="create_custom_resource_definition"></a>
> V1CustomResourceDefinition create_custom_resource_definition(body)



create a CustomResourceDefinition

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import apiextensions_v1_api
from kubernetes.client.model.v1_custom_resource_definition import V1CustomResourceDefinition
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
    api_instance = apiextensions_v1_api.ApiextensionsV1Api(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = V1CustomResourceDefinition(
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
        spec=V1CustomResourceDefinitionSpec(
            conversion=V1CustomResourceConversion(
                strategy="strategy_example",
                webhook=V1WebhookConversion(
                    kubernetes.client_config=ApiextensionsV1WebhookClientConfig(
                        ca_bundle='YQ==',
                        service=ApiextensionsV1ServiceReference(
                            name="name_example",
                            namespace="namespace_example",
                            path="path_example",
                            port=1,
                        ),
                        url="url_example",
                    ),
                    conversion_review_versions=[
                        "conversion_review_versions_example"
                    ],
                ),
            ),
            group="group_example",
            names=V1CustomResourceDefinitionNames(
                categories=[
                    "categories_example"
                ],
                kind="kind_example",
                list_kind="list_kind_example",
                plural="plural_example",
                short_names=[
                    "short_names_example"
                ],
                singular="singular_example",
            ),
            preserve_unknown_fields=True,
            scope="scope_example",
            versions=[
                V1CustomResourceDefinitionVersion(
                    additional_printer_columns=[
                        V1CustomResourceColumnDefinition(
                            description="description_example",
                            format="format_example",
                            json_path="json_path_example",
                            name="name_example",
                            priority=1,
                            type="type_example",
                        )
                    ],
                    deprecated=True,
                    deprecation_warning="deprecation_warning_example",
                    name="name_example",
                    schema=V1CustomResourceValidation(
                        open_apiv3_schema=V1JSONSchemaProps(
                            ref="ref_example",
                            schema="schema_example",
                            additional_items=dict(),
                            additional_properties=dict(),
                            all_of=[
                                V1JSONSchemaProps()
                            ],
,
                            default=dict(),
                            definitions=dict(
                                "key": V1JSONSchemaProps(),
                            ),
                            dependencies=dict(
                                "key": dict(),
                            ),
                            description="description_example",
                            enum=[
                                dict()
                            ],
                            example=dict(),
                            exclusive_maximum=True,
                            exclusive_minimum=True,
                            external_docs=V1ExternalDocumentation(
                                description="description_example",
                                url="url_example",
                            ),
                            format="format_example",
                            id="id_example",
                            items=dict(),
                            max_items=1,
                            max_length=1,
                            max_properties=1,
                            maximum=3.14,
                            min_items=1,
                            min_length=1,
                            min_properties=1,
                            minimum=3.14,
                            multiple_of=3.14,
                            _not=V1JSONSchemaProps(),
                            nullable=True,
,
                            pattern="pattern_example",
                            pattern_properties=dict(),
                            properties=dict(),
                            required=[
                                "required_example"
                            ],
                            title="title_example",
                            type="type_example",
                            unique_items=True,
                            x_kubernetes_embedded_resource=True,
                            x_kubernetes_int_or_string=True,
                            x_kubernetes_list_map_keys=[
                                "x_kubernetes_list_map_keys_example"
                            ],
                            x_kubernetes_list_type="x_kubernetes_list_type_example",
                            x_kubernetes_map_type="x_kubernetes_map_type_example",
                            x_kubernetes_preserve_unknown_fields=True,
                            x_kubernetes_validations=[
                                V1ValidationRule(
                                    message="message_example",
                                    rule="rule_example",
                                )
                            ],
                        ),
                    ),
                    served=True,
                    storage=True,
                    subresources=V1CustomResourceSubresources(
                        scale=V1CustomResourceSubresourceScale(
                            label_selector_path="label_selector_path_example",
                            spec_replicas_path="spec_replicas_path_example",
                            status_replicas_path="status_replicas_path_example",
                        ),
                        status=dict(),
                    ),
                )
            ],
        ),
        status=V1CustomResourceDefinitionStatus(
            accepted_names=V1CustomResourceDefinitionNames(),
            conditions=[
                V1CustomResourceDefinitionCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            stored_versions=[
                "stored_versions_example"
            ],
        ),
    )
    try:
        api_response = api_instance.create_custom_resource_definition(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->create_custom_resource_definition: %s\n" % e)

    # example passing only optional values
    query_params = {
        'pretty': "pretty_example",
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
    }
    body = V1CustomResourceDefinition(
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
        spec=V1CustomResourceDefinitionSpec(
            conversion=V1CustomResourceConversion(
                strategy="strategy_example",
                webhook=V1WebhookConversion(
                    kubernetes.client_config=ApiextensionsV1WebhookClientConfig(
                        ca_bundle='YQ==',
                        service=ApiextensionsV1ServiceReference(
                            name="name_example",
                            namespace="namespace_example",
                            path="path_example",
                            port=1,
                        ),
                        url="url_example",
                    ),
                    conversion_review_versions=[
                        "conversion_review_versions_example"
                    ],
                ),
            ),
            group="group_example",
            names=V1CustomResourceDefinitionNames(
                categories=[
                    "categories_example"
                ],
                kind="kind_example",
                list_kind="list_kind_example",
                plural="plural_example",
                short_names=[
                    "short_names_example"
                ],
                singular="singular_example",
            ),
            preserve_unknown_fields=True,
            scope="scope_example",
            versions=[
                V1CustomResourceDefinitionVersion(
                    additional_printer_columns=[
                        V1CustomResourceColumnDefinition(
                            description="description_example",
                            format="format_example",
                            json_path="json_path_example",
                            name="name_example",
                            priority=1,
                            type="type_example",
                        )
                    ],
                    deprecated=True,
                    deprecation_warning="deprecation_warning_example",
                    name="name_example",
                    schema=V1CustomResourceValidation(
                        open_apiv3_schema=V1JSONSchemaProps(
                            ref="ref_example",
                            schema="schema_example",
                            additional_items=dict(),
                            additional_properties=dict(),
                            all_of=[
                                V1JSONSchemaProps()
                            ],
,
                            default=dict(),
                            definitions=dict(
                                "key": V1JSONSchemaProps(),
                            ),
                            dependencies=dict(
                                "key": dict(),
                            ),
                            description="description_example",
                            enum=[
                                dict()
                            ],
                            example=dict(),
                            exclusive_maximum=True,
                            exclusive_minimum=True,
                            external_docs=V1ExternalDocumentation(
                                description="description_example",
                                url="url_example",
                            ),
                            format="format_example",
                            id="id_example",
                            items=dict(),
                            max_items=1,
                            max_length=1,
                            max_properties=1,
                            maximum=3.14,
                            min_items=1,
                            min_length=1,
                            min_properties=1,
                            minimum=3.14,
                            multiple_of=3.14,
                            _not=V1JSONSchemaProps(),
                            nullable=True,
,
                            pattern="pattern_example",
                            pattern_properties=dict(),
                            properties=dict(),
                            required=[
                                "required_example"
                            ],
                            title="title_example",
                            type="type_example",
                            unique_items=True,
                            x_kubernetes_embedded_resource=True,
                            x_kubernetes_int_or_string=True,
                            x_kubernetes_list_map_keys=[
                                "x_kubernetes_list_map_keys_example"
                            ],
                            x_kubernetes_list_type="x_kubernetes_list_type_example",
                            x_kubernetes_map_type="x_kubernetes_map_type_example",
                            x_kubernetes_preserve_unknown_fields=True,
                            x_kubernetes_validations=[
                                V1ValidationRule(
                                    message="message_example",
                                    rule="rule_example",
                                )
                            ],
                        ),
                    ),
                    served=True,
                    storage=True,
                    subresources=V1CustomResourceSubresources(
                        scale=V1CustomResourceSubresourceScale(
                            label_selector_path="label_selector_path_example",
                            spec_replicas_path="spec_replicas_path_example",
                            status_replicas_path="status_replicas_path_example",
                        ),
                        status=dict(),
                    ),
                )
            ],
        ),
        status=V1CustomResourceDefinitionStatus(
            accepted_names=V1CustomResourceDefinitionNames(),
            conditions=[
                V1CustomResourceDefinitionCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            stored_versions=[
                "stored_versions_example"
            ],
        ),
    )
    try:
        api_response = api_instance.create_custom_resource_definition(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->create_custom_resource_definition: %s\n" % e)
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
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


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
200 | [ApiResponseFor200](#create_custom_resource_definition.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_custom_resource_definition.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_custom_resource_definition.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_custom_resource_definition.ApiResponseFor401) | Unauthorized

#### create_custom_resource_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### create_custom_resource_definition.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### create_custom_resource_definition.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### create_custom_resource_definition.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_collection_custom_resource_definition**
<a name="delete_collection_custom_resource_definition"></a>
> V1Status delete_collection_custom_resource_definition()



delete collection of CustomResourceDefinition

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import apiextensions_v1_api
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
    api_instance = apiextensions_v1_api.ApiextensionsV1Api(api_client)

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
        api_response = api_instance.delete_collection_custom_resource_definition(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->delete_collection_custom_resource_definition: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_collection_custom_resource_definition.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#delete_collection_custom_resource_definition.ApiResponseFor401) | Unauthorized

#### delete_collection_custom_resource_definition.ApiResponseFor200
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


#### delete_collection_custom_resource_definition.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_custom_resource_definition**
<a name="delete_custom_resource_definition"></a>
> V1Status delete_custom_resource_definition(name)



delete a CustomResourceDefinition

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import apiextensions_v1_api
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
    api_instance = apiextensions_v1_api.ApiextensionsV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_custom_resource_definition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->delete_custom_resource_definition: %s\n" % e)

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
        api_response = api_instance.delete_custom_resource_definition(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->delete_custom_resource_definition: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_custom_resource_definition.ApiResponseFor200) | OK
202 | [ApiResponseFor202](#delete_custom_resource_definition.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#delete_custom_resource_definition.ApiResponseFor401) | Unauthorized

#### delete_custom_resource_definition.ApiResponseFor200
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


#### delete_custom_resource_definition.ApiResponseFor202
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


#### delete_custom_resource_definition.ApiResponseFor401
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
from kubernetes.client.apis.tags import apiextensions_v1_api
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
    api_instance = apiextensions_v1_api.ApiextensionsV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_api_resources()
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->get_api_resources: %s\n" % e)
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

# **list_custom_resource_definition**
<a name="list_custom_resource_definition"></a>
> V1CustomResourceDefinitionList list_custom_resource_definition()



list or watch objects of kind CustomResourceDefinition

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import apiextensions_v1_api
from kubernetes.client.model.v1_custom_resource_definition_list import V1CustomResourceDefinitionList
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
    api_instance = apiextensions_v1_api.ApiextensionsV1Api(api_client)

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
        api_response = api_instance.list_custom_resource_definition(
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->list_custom_resource_definition: %s\n" % e)
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
200 | [ApiResponseFor200](#list_custom_resource_definition.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_custom_resource_definition.ApiResponseFor401) | Unauthorized

#### list_custom_resource_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, SchemaFor200ResponseBodyApplicationJsonstreamwatch, SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinitionList**](../../models/V1CustomResourceDefinitionList.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinitionList**](../../models/V1CustomResourceDefinitionList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinitionList**](../../models/V1CustomResourceDefinitionList.md) |  | 


# SchemaFor200ResponseBodyApplicationJsonstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinitionList**](../../models/V1CustomResourceDefinitionList.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobufstreamwatch
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinitionList**](../../models/V1CustomResourceDefinitionList.md) |  | 


#### list_custom_resource_definition.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_custom_resource_definition**
<a name="patch_custom_resource_definition"></a>
> V1CustomResourceDefinition patch_custom_resource_definition(namebody)



partially update the specified CustomResourceDefinition

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import apiextensions_v1_api
from kubernetes.client.model.v1_custom_resource_definition import V1CustomResourceDefinition
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
    api_instance = apiextensions_v1_api.ApiextensionsV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_custom_resource_definition(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->patch_custom_resource_definition: %s\n" % e)

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
        api_response = api_instance.patch_custom_resource_definition(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->patch_custom_resource_definition: %s\n" % e)
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
200 | [ApiResponseFor200](#patch_custom_resource_definition.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_custom_resource_definition.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_custom_resource_definition.ApiResponseFor401) | Unauthorized

#### patch_custom_resource_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### patch_custom_resource_definition.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### patch_custom_resource_definition.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_custom_resource_definition_status**
<a name="patch_custom_resource_definition_status"></a>
> V1CustomResourceDefinition patch_custom_resource_definition_status(namebody)



partially update status of the specified CustomResourceDefinition

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import apiextensions_v1_api
from kubernetes.client.model.v1_custom_resource_definition import V1CustomResourceDefinition
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
    api_instance = apiextensions_v1_api.ApiextensionsV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = dict()
    try:
        api_response = api_instance.patch_custom_resource_definition_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->patch_custom_resource_definition_status: %s\n" % e)

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
        api_response = api_instance.patch_custom_resource_definition_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->patch_custom_resource_definition_status: %s\n" % e)
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
200 | [ApiResponseFor200](#patch_custom_resource_definition_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#patch_custom_resource_definition_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#patch_custom_resource_definition_status.ApiResponseFor401) | Unauthorized

#### patch_custom_resource_definition_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### patch_custom_resource_definition_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### patch_custom_resource_definition_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_custom_resource_definition**
<a name="read_custom_resource_definition"></a>
> V1CustomResourceDefinition read_custom_resource_definition(name)



read the specified CustomResourceDefinition

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import apiextensions_v1_api
from kubernetes.client.model.v1_custom_resource_definition import V1CustomResourceDefinition
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
    api_instance = apiextensions_v1_api.ApiextensionsV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_custom_resource_definition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->read_custom_resource_definition: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_custom_resource_definition(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->read_custom_resource_definition: %s\n" % e)
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
200 | [ApiResponseFor200](#read_custom_resource_definition.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_custom_resource_definition.ApiResponseFor401) | Unauthorized

#### read_custom_resource_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### read_custom_resource_definition.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **read_custom_resource_definition_status**
<a name="read_custom_resource_definition_status"></a>
> V1CustomResourceDefinition read_custom_resource_definition_status(name)



read status of the specified CustomResourceDefinition

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import apiextensions_v1_api
from kubernetes.client.model.v1_custom_resource_definition import V1CustomResourceDefinition
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
    api_instance = apiextensions_v1_api.ApiextensionsV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.read_custom_resource_definition_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->read_custom_resource_definition_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'name': "name_example",
    }
    query_params = {
        'pretty': "pretty_example",
    }
    try:
        api_response = api_instance.read_custom_resource_definition_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->read_custom_resource_definition_status: %s\n" % e)
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
200 | [ApiResponseFor200](#read_custom_resource_definition_status.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#read_custom_resource_definition_status.ApiResponseFor401) | Unauthorized

#### read_custom_resource_definition_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### read_custom_resource_definition_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_custom_resource_definition**
<a name="replace_custom_resource_definition"></a>
> V1CustomResourceDefinition replace_custom_resource_definition(namebody)



replace the specified CustomResourceDefinition

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import apiextensions_v1_api
from kubernetes.client.model.v1_custom_resource_definition import V1CustomResourceDefinition
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
    api_instance = apiextensions_v1_api.ApiextensionsV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = V1CustomResourceDefinition(
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
        spec=V1CustomResourceDefinitionSpec(
            conversion=V1CustomResourceConversion(
                strategy="strategy_example",
                webhook=V1WebhookConversion(
                    kubernetes.client_config=ApiextensionsV1WebhookClientConfig(
                        ca_bundle='YQ==',
                        service=ApiextensionsV1ServiceReference(
                            name="name_example",
                            namespace="namespace_example",
                            path="path_example",
                            port=1,
                        ),
                        url="url_example",
                    ),
                    conversion_review_versions=[
                        "conversion_review_versions_example"
                    ],
                ),
            ),
            group="group_example",
            names=V1CustomResourceDefinitionNames(
                categories=[
                    "categories_example"
                ],
                kind="kind_example",
                list_kind="list_kind_example",
                plural="plural_example",
                short_names=[
                    "short_names_example"
                ],
                singular="singular_example",
            ),
            preserve_unknown_fields=True,
            scope="scope_example",
            versions=[
                V1CustomResourceDefinitionVersion(
                    additional_printer_columns=[
                        V1CustomResourceColumnDefinition(
                            description="description_example",
                            format="format_example",
                            json_path="json_path_example",
                            name="name_example",
                            priority=1,
                            type="type_example",
                        )
                    ],
                    deprecated=True,
                    deprecation_warning="deprecation_warning_example",
                    name="name_example",
                    schema=V1CustomResourceValidation(
                        open_apiv3_schema=V1JSONSchemaProps(
                            ref="ref_example",
                            schema="schema_example",
                            additional_items=dict(),
                            additional_properties=dict(),
                            all_of=[
                                V1JSONSchemaProps()
                            ],
,
                            default=dict(),
                            definitions=dict(
                                "key": V1JSONSchemaProps(),
                            ),
                            dependencies=dict(
                                "key": dict(),
                            ),
                            description="description_example",
                            enum=[
                                dict()
                            ],
                            example=dict(),
                            exclusive_maximum=True,
                            exclusive_minimum=True,
                            external_docs=V1ExternalDocumentation(
                                description="description_example",
                                url="url_example",
                            ),
                            format="format_example",
                            id="id_example",
                            items=dict(),
                            max_items=1,
                            max_length=1,
                            max_properties=1,
                            maximum=3.14,
                            min_items=1,
                            min_length=1,
                            min_properties=1,
                            minimum=3.14,
                            multiple_of=3.14,
                            _not=V1JSONSchemaProps(),
                            nullable=True,
,
                            pattern="pattern_example",
                            pattern_properties=dict(),
                            properties=dict(),
                            required=[
                                "required_example"
                            ],
                            title="title_example",
                            type="type_example",
                            unique_items=True,
                            x_kubernetes_embedded_resource=True,
                            x_kubernetes_int_or_string=True,
                            x_kubernetes_list_map_keys=[
                                "x_kubernetes_list_map_keys_example"
                            ],
                            x_kubernetes_list_type="x_kubernetes_list_type_example",
                            x_kubernetes_map_type="x_kubernetes_map_type_example",
                            x_kubernetes_preserve_unknown_fields=True,
                            x_kubernetes_validations=[
                                V1ValidationRule(
                                    message="message_example",
                                    rule="rule_example",
                                )
                            ],
                        ),
                    ),
                    served=True,
                    storage=True,
                    subresources=V1CustomResourceSubresources(
                        scale=V1CustomResourceSubresourceScale(
                            label_selector_path="label_selector_path_example",
                            spec_replicas_path="spec_replicas_path_example",
                            status_replicas_path="status_replicas_path_example",
                        ),
                        status=dict(),
                    ),
                )
            ],
        ),
        status=V1CustomResourceDefinitionStatus(
            accepted_names=V1CustomResourceDefinitionNames(),
            conditions=[
                V1CustomResourceDefinitionCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            stored_versions=[
                "stored_versions_example"
            ],
        ),
    )
    try:
        api_response = api_instance.replace_custom_resource_definition(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->replace_custom_resource_definition: %s\n" % e)

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
    body = V1CustomResourceDefinition(
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
        spec=V1CustomResourceDefinitionSpec(
            conversion=V1CustomResourceConversion(
                strategy="strategy_example",
                webhook=V1WebhookConversion(
                    kubernetes.client_config=ApiextensionsV1WebhookClientConfig(
                        ca_bundle='YQ==',
                        service=ApiextensionsV1ServiceReference(
                            name="name_example",
                            namespace="namespace_example",
                            path="path_example",
                            port=1,
                        ),
                        url="url_example",
                    ),
                    conversion_review_versions=[
                        "conversion_review_versions_example"
                    ],
                ),
            ),
            group="group_example",
            names=V1CustomResourceDefinitionNames(
                categories=[
                    "categories_example"
                ],
                kind="kind_example",
                list_kind="list_kind_example",
                plural="plural_example",
                short_names=[
                    "short_names_example"
                ],
                singular="singular_example",
            ),
            preserve_unknown_fields=True,
            scope="scope_example",
            versions=[
                V1CustomResourceDefinitionVersion(
                    additional_printer_columns=[
                        V1CustomResourceColumnDefinition(
                            description="description_example",
                            format="format_example",
                            json_path="json_path_example",
                            name="name_example",
                            priority=1,
                            type="type_example",
                        )
                    ],
                    deprecated=True,
                    deprecation_warning="deprecation_warning_example",
                    name="name_example",
                    schema=V1CustomResourceValidation(
                        open_apiv3_schema=V1JSONSchemaProps(
                            ref="ref_example",
                            schema="schema_example",
                            additional_items=dict(),
                            additional_properties=dict(),
                            all_of=[
                                V1JSONSchemaProps()
                            ],
,
                            default=dict(),
                            definitions=dict(
                                "key": V1JSONSchemaProps(),
                            ),
                            dependencies=dict(
                                "key": dict(),
                            ),
                            description="description_example",
                            enum=[
                                dict()
                            ],
                            example=dict(),
                            exclusive_maximum=True,
                            exclusive_minimum=True,
                            external_docs=V1ExternalDocumentation(
                                description="description_example",
                                url="url_example",
                            ),
                            format="format_example",
                            id="id_example",
                            items=dict(),
                            max_items=1,
                            max_length=1,
                            max_properties=1,
                            maximum=3.14,
                            min_items=1,
                            min_length=1,
                            min_properties=1,
                            minimum=3.14,
                            multiple_of=3.14,
                            _not=V1JSONSchemaProps(),
                            nullable=True,
,
                            pattern="pattern_example",
                            pattern_properties=dict(),
                            properties=dict(),
                            required=[
                                "required_example"
                            ],
                            title="title_example",
                            type="type_example",
                            unique_items=True,
                            x_kubernetes_embedded_resource=True,
                            x_kubernetes_int_or_string=True,
                            x_kubernetes_list_map_keys=[
                                "x_kubernetes_list_map_keys_example"
                            ],
                            x_kubernetes_list_type="x_kubernetes_list_type_example",
                            x_kubernetes_map_type="x_kubernetes_map_type_example",
                            x_kubernetes_preserve_unknown_fields=True,
                            x_kubernetes_validations=[
                                V1ValidationRule(
                                    message="message_example",
                                    rule="rule_example",
                                )
                            ],
                        ),
                    ),
                    served=True,
                    storage=True,
                    subresources=V1CustomResourceSubresources(
                        scale=V1CustomResourceSubresourceScale(
                            label_selector_path="label_selector_path_example",
                            spec_replicas_path="spec_replicas_path_example",
                            status_replicas_path="status_replicas_path_example",
                        ),
                        status=dict(),
                    ),
                )
            ],
        ),
        status=V1CustomResourceDefinitionStatus(
            accepted_names=V1CustomResourceDefinitionNames(),
            conditions=[
                V1CustomResourceDefinitionCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            stored_versions=[
                "stored_versions_example"
            ],
        ),
    )
    try:
        api_response = api_instance.replace_custom_resource_definition(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->replace_custom_resource_definition: %s\n" % e)
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
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


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
200 | [ApiResponseFor200](#replace_custom_resource_definition.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_custom_resource_definition.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_custom_resource_definition.ApiResponseFor401) | Unauthorized

#### replace_custom_resource_definition.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### replace_custom_resource_definition.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### replace_custom_resource_definition.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **replace_custom_resource_definition_status**
<a name="replace_custom_resource_definition_status"></a>
> V1CustomResourceDefinition replace_custom_resource_definition_status(namebody)



replace status of the specified CustomResourceDefinition

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import apiextensions_v1_api
from kubernetes.client.model.v1_custom_resource_definition import V1CustomResourceDefinition
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
    api_instance = apiextensions_v1_api.ApiextensionsV1Api(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'name': "name_example",
    }
    query_params = {
    }
    body = V1CustomResourceDefinition(
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
        spec=V1CustomResourceDefinitionSpec(
            conversion=V1CustomResourceConversion(
                strategy="strategy_example",
                webhook=V1WebhookConversion(
                    kubernetes.client_config=ApiextensionsV1WebhookClientConfig(
                        ca_bundle='YQ==',
                        service=ApiextensionsV1ServiceReference(
                            name="name_example",
                            namespace="namespace_example",
                            path="path_example",
                            port=1,
                        ),
                        url="url_example",
                    ),
                    conversion_review_versions=[
                        "conversion_review_versions_example"
                    ],
                ),
            ),
            group="group_example",
            names=V1CustomResourceDefinitionNames(
                categories=[
                    "categories_example"
                ],
                kind="kind_example",
                list_kind="list_kind_example",
                plural="plural_example",
                short_names=[
                    "short_names_example"
                ],
                singular="singular_example",
            ),
            preserve_unknown_fields=True,
            scope="scope_example",
            versions=[
                V1CustomResourceDefinitionVersion(
                    additional_printer_columns=[
                        V1CustomResourceColumnDefinition(
                            description="description_example",
                            format="format_example",
                            json_path="json_path_example",
                            name="name_example",
                            priority=1,
                            type="type_example",
                        )
                    ],
                    deprecated=True,
                    deprecation_warning="deprecation_warning_example",
                    name="name_example",
                    schema=V1CustomResourceValidation(
                        open_apiv3_schema=V1JSONSchemaProps(
                            ref="ref_example",
                            schema="schema_example",
                            additional_items=dict(),
                            additional_properties=dict(),
                            all_of=[
                                V1JSONSchemaProps()
                            ],
,
                            default=dict(),
                            definitions=dict(
                                "key": V1JSONSchemaProps(),
                            ),
                            dependencies=dict(
                                "key": dict(),
                            ),
                            description="description_example",
                            enum=[
                                dict()
                            ],
                            example=dict(),
                            exclusive_maximum=True,
                            exclusive_minimum=True,
                            external_docs=V1ExternalDocumentation(
                                description="description_example",
                                url="url_example",
                            ),
                            format="format_example",
                            id="id_example",
                            items=dict(),
                            max_items=1,
                            max_length=1,
                            max_properties=1,
                            maximum=3.14,
                            min_items=1,
                            min_length=1,
                            min_properties=1,
                            minimum=3.14,
                            multiple_of=3.14,
                            _not=V1JSONSchemaProps(),
                            nullable=True,
,
                            pattern="pattern_example",
                            pattern_properties=dict(),
                            properties=dict(),
                            required=[
                                "required_example"
                            ],
                            title="title_example",
                            type="type_example",
                            unique_items=True,
                            x_kubernetes_embedded_resource=True,
                            x_kubernetes_int_or_string=True,
                            x_kubernetes_list_map_keys=[
                                "x_kubernetes_list_map_keys_example"
                            ],
                            x_kubernetes_list_type="x_kubernetes_list_type_example",
                            x_kubernetes_map_type="x_kubernetes_map_type_example",
                            x_kubernetes_preserve_unknown_fields=True,
                            x_kubernetes_validations=[
                                V1ValidationRule(
                                    message="message_example",
                                    rule="rule_example",
                                )
                            ],
                        ),
                    ),
                    served=True,
                    storage=True,
                    subresources=V1CustomResourceSubresources(
                        scale=V1CustomResourceSubresourceScale(
                            label_selector_path="label_selector_path_example",
                            spec_replicas_path="spec_replicas_path_example",
                            status_replicas_path="status_replicas_path_example",
                        ),
                        status=dict(),
                    ),
                )
            ],
        ),
        status=V1CustomResourceDefinitionStatus(
            accepted_names=V1CustomResourceDefinitionNames(),
            conditions=[
                V1CustomResourceDefinitionCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            stored_versions=[
                "stored_versions_example"
            ],
        ),
    )
    try:
        api_response = api_instance.replace_custom_resource_definition_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->replace_custom_resource_definition_status: %s\n" % e)

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
    body = V1CustomResourceDefinition(
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
        spec=V1CustomResourceDefinitionSpec(
            conversion=V1CustomResourceConversion(
                strategy="strategy_example",
                webhook=V1WebhookConversion(
                    kubernetes.client_config=ApiextensionsV1WebhookClientConfig(
                        ca_bundle='YQ==',
                        service=ApiextensionsV1ServiceReference(
                            name="name_example",
                            namespace="namespace_example",
                            path="path_example",
                            port=1,
                        ),
                        url="url_example",
                    ),
                    conversion_review_versions=[
                        "conversion_review_versions_example"
                    ],
                ),
            ),
            group="group_example",
            names=V1CustomResourceDefinitionNames(
                categories=[
                    "categories_example"
                ],
                kind="kind_example",
                list_kind="list_kind_example",
                plural="plural_example",
                short_names=[
                    "short_names_example"
                ],
                singular="singular_example",
            ),
            preserve_unknown_fields=True,
            scope="scope_example",
            versions=[
                V1CustomResourceDefinitionVersion(
                    additional_printer_columns=[
                        V1CustomResourceColumnDefinition(
                            description="description_example",
                            format="format_example",
                            json_path="json_path_example",
                            name="name_example",
                            priority=1,
                            type="type_example",
                        )
                    ],
                    deprecated=True,
                    deprecation_warning="deprecation_warning_example",
                    name="name_example",
                    schema=V1CustomResourceValidation(
                        open_apiv3_schema=V1JSONSchemaProps(
                            ref="ref_example",
                            schema="schema_example",
                            additional_items=dict(),
                            additional_properties=dict(),
                            all_of=[
                                V1JSONSchemaProps()
                            ],
,
                            default=dict(),
                            definitions=dict(
                                "key": V1JSONSchemaProps(),
                            ),
                            dependencies=dict(
                                "key": dict(),
                            ),
                            description="description_example",
                            enum=[
                                dict()
                            ],
                            example=dict(),
                            exclusive_maximum=True,
                            exclusive_minimum=True,
                            external_docs=V1ExternalDocumentation(
                                description="description_example",
                                url="url_example",
                            ),
                            format="format_example",
                            id="id_example",
                            items=dict(),
                            max_items=1,
                            max_length=1,
                            max_properties=1,
                            maximum=3.14,
                            min_items=1,
                            min_length=1,
                            min_properties=1,
                            minimum=3.14,
                            multiple_of=3.14,
                            _not=V1JSONSchemaProps(),
                            nullable=True,
,
                            pattern="pattern_example",
                            pattern_properties=dict(),
                            properties=dict(),
                            required=[
                                "required_example"
                            ],
                            title="title_example",
                            type="type_example",
                            unique_items=True,
                            x_kubernetes_embedded_resource=True,
                            x_kubernetes_int_or_string=True,
                            x_kubernetes_list_map_keys=[
                                "x_kubernetes_list_map_keys_example"
                            ],
                            x_kubernetes_list_type="x_kubernetes_list_type_example",
                            x_kubernetes_map_type="x_kubernetes_map_type_example",
                            x_kubernetes_preserve_unknown_fields=True,
                            x_kubernetes_validations=[
                                V1ValidationRule(
                                    message="message_example",
                                    rule="rule_example",
                                )
                            ],
                        ),
                    ),
                    served=True,
                    storage=True,
                    subresources=V1CustomResourceSubresources(
                        scale=V1CustomResourceSubresourceScale(
                            label_selector_path="label_selector_path_example",
                            spec_replicas_path="spec_replicas_path_example",
                            status_replicas_path="status_replicas_path_example",
                        ),
                        status=dict(),
                    ),
                )
            ],
        ),
        status=V1CustomResourceDefinitionStatus(
            accepted_names=V1CustomResourceDefinitionNames(),
            conditions=[
                V1CustomResourceDefinitionCondition(
                    last_transition_time="1970-01-01T00:00:00.00Z",
                    message="message_example",
                    reason="reason_example",
                    status="status_example",
                    type="type_example",
                )
            ],
            stored_versions=[
                "stored_versions_example"
            ],
        ),
    )
    try:
        api_response = api_instance.replace_custom_resource_definition_status(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling ApiextensionsV1Api->replace_custom_resource_definition_status: %s\n" % e)
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
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


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
200 | [ApiResponseFor200](#replace_custom_resource_definition_status.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#replace_custom_resource_definition_status.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#replace_custom_resource_definition_status.ApiResponseFor401) | Unauthorized

#### replace_custom_resource_definition_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### replace_custom_resource_definition_status.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1CustomResourceDefinition**](../../models/V1CustomResourceDefinition.md) |  | 


#### replace_custom_resource_definition_status.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[] |  |
headers | Unset | headers were not defined |

### Authorization

[BearerToken](../../../README.md#BearerToken)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

