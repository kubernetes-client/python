<a name="__pageTop"></a>
# kubernetes.client.apis.tags.authentication_v1_api.AuthenticationV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_review**](#create_token_review) | **post** /apis/authentication.k8s.io/v1/tokenreviews | 
[**get_api_resources**](#get_api_resources) | **get** /apis/authentication.k8s.io/v1/ | 

# **create_token_review**
<a name="create_token_review"></a>
> V1TokenReview create_token_review(body)



create a TokenReview

### Example

* Api Key Authentication (BearerToken):
```python
import kubernetes.client
from kubernetes.client.apis.tags import authentication_v1_api
from kubernetes.client.model.v1_token_review import V1TokenReview
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
    api_instance = authentication_v1_api.AuthenticationV1Api(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = V1TokenReview(
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
        spec=V1TokenReviewSpec(
            audiences=[
                "audiences_example"
            ],
            token="token_example",
        ),
        status=V1TokenReviewStatus(
            audiences=[
                "audiences_example"
            ],
            authenticated=True,
            error="error_example",
            user=V1UserInfo(
                extra=dict(
                    "key": [
                        "key_example"
                    ],
                ),
                groups=[
                    "groups_example"
                ],
                uid="uid_example",
                username="username_example",
            ),
        ),
    )
    try:
        api_response = api_instance.create_token_review(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthenticationV1Api->create_token_review: %s\n" % e)

    # example passing only optional values
    query_params = {
        'dryRun': "dryRun_example",
        'fieldManager': "fieldManager_example",
        'fieldValidation': "fieldValidation_example",
        'pretty': "pretty_example",
    }
    body = V1TokenReview(
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
        spec=V1TokenReviewSpec(
            audiences=[
                "audiences_example"
            ],
            token="token_example",
        ),
        status=V1TokenReviewStatus(
            audiences=[
                "audiences_example"
            ],
            authenticated=True,
            error="error_example",
            user=V1UserInfo(
                extra=dict(
                    "key": [
                        "key_example"
                    ],
                ),
                groups=[
                    "groups_example"
                ],
                uid="uid_example",
                username="username_example",
            ),
        ),
    )
    try:
        api_response = api_instance.create_token_review(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthenticationV1Api->create_token_review: %s\n" % e)
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
[**V1TokenReview**](../../models/V1TokenReview.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dryRun | DryRunSchema | | optional
fieldManager | FieldManagerSchema | | optional
fieldValidation | FieldValidationSchema | | optional
pretty | PrettySchema | | optional


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

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_token_review.ApiResponseFor200) | OK
201 | [ApiResponseFor201](#create_token_review.ApiResponseFor201) | Created
202 | [ApiResponseFor202](#create_token_review.ApiResponseFor202) | Accepted
401 | [ApiResponseFor401](#create_token_review.ApiResponseFor401) | Unauthorized

#### create_token_review.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, SchemaFor200ResponseBodyApplicationYaml, SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1TokenReview**](../../models/V1TokenReview.md) |  | 


# SchemaFor200ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1TokenReview**](../../models/V1TokenReview.md) |  | 


# SchemaFor200ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1TokenReview**](../../models/V1TokenReview.md) |  | 


#### create_token_review.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, SchemaFor201ResponseBodyApplicationYaml, SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1TokenReview**](../../models/V1TokenReview.md) |  | 


# SchemaFor201ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1TokenReview**](../../models/V1TokenReview.md) |  | 


# SchemaFor201ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1TokenReview**](../../models/V1TokenReview.md) |  | 


#### create_token_review.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, SchemaFor202ResponseBodyApplicationYaml, SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**V1TokenReview**](../../models/V1TokenReview.md) |  | 


# SchemaFor202ResponseBodyApplicationYaml
Type | Description  | Notes
------------- | ------------- | -------------
[**V1TokenReview**](../../models/V1TokenReview.md) |  | 


# SchemaFor202ResponseBodyApplicationVndKubernetesProtobuf
Type | Description  | Notes
------------- | ------------- | -------------
[**V1TokenReview**](../../models/V1TokenReview.md) |  | 


#### create_token_review.ApiResponseFor401
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
from kubernetes.client.apis.tags import authentication_v1_api
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
    api_instance = authentication_v1_api.AuthenticationV1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_api_resources()
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthenticationV1Api->get_api_resources: %s\n" % e)
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

