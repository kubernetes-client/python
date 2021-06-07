# kubernetes.client.AuthorizationV1beta1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_local_subject_access_review**](AuthorizationV1beta1Api.md#create_namespaced_local_subject_access_review) | **POST** /apis/authorization.k8s.io/v1beta1/namespaces/{namespace}/localsubjectaccessreviews | 
[**create_self_subject_access_review**](AuthorizationV1beta1Api.md#create_self_subject_access_review) | **POST** /apis/authorization.k8s.io/v1beta1/selfsubjectaccessreviews | 
[**create_self_subject_rules_review**](AuthorizationV1beta1Api.md#create_self_subject_rules_review) | **POST** /apis/authorization.k8s.io/v1beta1/selfsubjectrulesreviews | 
[**create_subject_access_review**](AuthorizationV1beta1Api.md#create_subject_access_review) | **POST** /apis/authorization.k8s.io/v1beta1/subjectaccessreviews | 
[**get_api_resources**](AuthorizationV1beta1Api.md#get_api_resources) | **GET** /apis/authorization.k8s.io/v1beta1/ | 


# **create_namespaced_local_subject_access_review**
> V1beta1LocalSubjectAccessReview create_namespaced_local_subject_access_review(namespace, body)



create a LocalSubjectAccessReview

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import authorization_v1beta1_api
from kubernetes.client.model.v1beta1_local_subject_access_review import V1beta1LocalSubjectAccessReview
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
    api_instance = authorization_v1beta1_api.AuthorizationV1beta1Api(api_client)
    namespace = "namespace_example" # str | object name and auth scope, such as for teams and projects
    body = V1beta1LocalSubjectAccessReview(
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
        spec=V1beta1SubjectAccessReviewSpec(
            extra={
                "key": [
                    "key_example",
                ],
            },
            group=[
                "group_example",
            ],
            non_resource_attributes=V1beta1NonResourceAttributes(
                path="path_example",
                verb="verb_example",
            ),
            resource_attributes=V1beta1ResourceAttributes(
                group="group_example",
                name="name_example",
                namespace="namespace_example",
                resource="resource_example",
                subresource="subresource_example",
                verb="verb_example",
                version="version_example",
            ),
            uid="uid_example",
            user="user_example",
        ),
        status=V1beta1SubjectAccessReviewStatus(
            allowed=True,
            denied=True,
            evaluation_error="evaluation_error_example",
            reason="reason_example",
        ),
    ) # V1beta1LocalSubjectAccessReview | 
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_namespaced_local_subject_access_review(namespace, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthorizationV1beta1Api->create_namespaced_local_subject_access_review: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_namespaced_local_subject_access_review(namespace, body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthorizationV1beta1Api->create_namespaced_local_subject_access_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects |
 **body** | [**V1beta1LocalSubjectAccessReview**](V1beta1LocalSubjectAccessReview.md)|  |
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]

### Return type

[**V1beta1LocalSubjectAccessReview**](V1beta1LocalSubjectAccessReview.md)

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

# **create_self_subject_access_review**
> V1beta1SelfSubjectAccessReview create_self_subject_access_review(body)



create a SelfSubjectAccessReview

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import authorization_v1beta1_api
from kubernetes.client.model.v1beta1_self_subject_access_review import V1beta1SelfSubjectAccessReview
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
    api_instance = authorization_v1beta1_api.AuthorizationV1beta1Api(api_client)
    body = V1beta1SelfSubjectAccessReview(
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
        spec=V1beta1SelfSubjectAccessReviewSpec(
            non_resource_attributes=V1beta1NonResourceAttributes(
                path="path_example",
                verb="verb_example",
            ),
            resource_attributes=V1beta1ResourceAttributes(
                group="group_example",
                name="name_example",
                namespace="namespace_example",
                resource="resource_example",
                subresource="subresource_example",
                verb="verb_example",
                version="version_example",
            ),
        ),
        status=V1beta1SubjectAccessReviewStatus(
            allowed=True,
            denied=True,
            evaluation_error="evaluation_error_example",
            reason="reason_example",
        ),
    ) # V1beta1SelfSubjectAccessReview | 
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_self_subject_access_review(body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthorizationV1beta1Api->create_self_subject_access_review: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_self_subject_access_review(body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthorizationV1beta1Api->create_self_subject_access_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1SelfSubjectAccessReview**](V1beta1SelfSubjectAccessReview.md)|  |
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]

### Return type

[**V1beta1SelfSubjectAccessReview**](V1beta1SelfSubjectAccessReview.md)

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

# **create_self_subject_rules_review**
> V1beta1SelfSubjectRulesReview create_self_subject_rules_review(body)



create a SelfSubjectRulesReview

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import authorization_v1beta1_api
from kubernetes.client.model.v1beta1_self_subject_rules_review import V1beta1SelfSubjectRulesReview
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
    api_instance = authorization_v1beta1_api.AuthorizationV1beta1Api(api_client)
    body = V1beta1SelfSubjectRulesReview(
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
        spec=V1beta1SelfSubjectRulesReviewSpec(
            namespace="namespace_example",
        ),
        status=V1beta1SubjectRulesReviewStatus(
            evaluation_error="evaluation_error_example",
            incomplete=True,
            non_resource_rules=[
                V1beta1NonResourceRule(
                    non_resource_urls=[
                        "non_resource_urls_example",
                    ],
                    verbs=[
                        "verbs_example",
                    ],
                ),
            ],
            resource_rules=[
                V1beta1ResourceRule(
                    api_groups=[
                        "api_groups_example",
                    ],
                    resource_names=[
                        "resource_names_example",
                    ],
                    resources=[
                        "resources_example",
                    ],
                    verbs=[
                        "verbs_example",
                    ],
                ),
            ],
        ),
    ) # V1beta1SelfSubjectRulesReview | 
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_self_subject_rules_review(body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthorizationV1beta1Api->create_self_subject_rules_review: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_self_subject_rules_review(body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthorizationV1beta1Api->create_self_subject_rules_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1SelfSubjectRulesReview**](V1beta1SelfSubjectRulesReview.md)|  |
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]

### Return type

[**V1beta1SelfSubjectRulesReview**](V1beta1SelfSubjectRulesReview.md)

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

# **create_subject_access_review**
> V1beta1SubjectAccessReview create_subject_access_review(body)



create a SubjectAccessReview

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import authorization_v1beta1_api
from kubernetes.client.model.v1beta1_subject_access_review import V1beta1SubjectAccessReview
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
    api_instance = authorization_v1beta1_api.AuthorizationV1beta1Api(api_client)
    body = V1beta1SubjectAccessReview(
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
        spec=V1beta1SubjectAccessReviewSpec(
            extra={
                "key": [
                    "key_example",
                ],
            },
            group=[
                "group_example",
            ],
            non_resource_attributes=V1beta1NonResourceAttributes(
                path="path_example",
                verb="verb_example",
            ),
            resource_attributes=V1beta1ResourceAttributes(
                group="group_example",
                name="name_example",
                namespace="namespace_example",
                resource="resource_example",
                subresource="subresource_example",
                verb="verb_example",
                version="version_example",
            ),
            uid="uid_example",
            user="user_example",
        ),
        status=V1beta1SubjectAccessReviewStatus(
            allowed=True,
            denied=True,
            evaluation_error="evaluation_error_example",
            reason="reason_example",
        ),
    ) # V1beta1SubjectAccessReview | 
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_subject_access_review(body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthorizationV1beta1Api->create_subject_access_review: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_subject_access_review(body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthorizationV1beta1Api->create_subject_access_review: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1SubjectAccessReview**](V1beta1SubjectAccessReview.md)|  |
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]

### Return type

[**V1beta1SubjectAccessReview**](V1beta1SubjectAccessReview.md)

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
from kubernetes.client.api import authorization_v1beta1_api
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
    api_instance = authorization_v1beta1_api.AuthorizationV1beta1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_api_resources()
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling AuthorizationV1beta1Api->get_api_resources: %s\n" % e)
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

