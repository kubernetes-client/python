# kubernetes.client.AuthenticationV1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_review**](AuthenticationV1Api.md#create_token_review) | **POST** /apis/authentication.k8s.io/v1/tokenreviews | 
[**get_api_resources**](AuthenticationV1Api.md#get_api_resources) | **GET** /apis/authentication.k8s.io/v1/ | 


# **create_token_review**
> V1TokenReview create_token_review(body)



create a TokenReview

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import authentication_v1_api
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
    body = V1TokenReview(
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
        spec=V1TokenReviewSpec(
            audiences=[
                "audiences_example",
            ],
            token="token_example",
        ),
        status=V1TokenReviewStatus(
            audiences=[
                "audiences_example",
            ],
            authenticated=True,
            error="error_example",
            user=V1UserInfo(
                extra={
                    "key": [
                        "key_example",
                    ],
                },
                groups=[
                    "groups_example",
                ],
                uid="uid_example",
                username="username_example",
            ),
        ),
    ) # V1TokenReview | 
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
    field_validation = "fieldValidation_example" # str | fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the `ServerSideFieldValidation` feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. (optional)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_token_review(body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthenticationV1Api->create_token_review: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_token_review(body, dry_run=dry_run, field_manager=field_manager, field_validation=field_validation, pretty=pretty)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthenticationV1Api->create_token_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1TokenReview**](V1TokenReview.md)|  |
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]
 **field_validation** | **str**| fieldValidation determines how the server should respond to unknown/duplicate fields in the object in the request. Introduced as alpha in 1.23, older servers or servers with the &#x60;ServerSideFieldValidation&#x60; feature disabled will discard valid values specified in  this param and not perform any server side field validation. Valid values are: - Ignore: ignores unknown/duplicate fields. - Warn: responds with a warning for each unknown/duplicate field, but successfully serves the request. - Strict: fails the request on unknown/duplicate fields. | [optional]
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]

### Return type

[**V1TokenReview**](V1TokenReview.md)

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

# **get_api_resources**
> V1APIResourceList get_api_resources()



get available resources

### Example

* Api Key Authentication (BearerToken):

```python
import time
import kubernetes.client
from kubernetes.client.api import authentication_v1_api
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

