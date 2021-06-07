# kubernetes.client.CertificatesV1beta1Api

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificate_signing_request**](CertificatesV1beta1Api.md#create_certificate_signing_request) | **POST** /apis/certificates.k8s.io/v1beta1/certificatesigningrequests | 
[**delete_certificate_signing_request**](CertificatesV1beta1Api.md#delete_certificate_signing_request) | **DELETE** /apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name} | 
[**delete_collection_certificate_signing_request**](CertificatesV1beta1Api.md#delete_collection_certificate_signing_request) | **DELETE** /apis/certificates.k8s.io/v1beta1/certificatesigningrequests | 
[**get_api_resources**](CertificatesV1beta1Api.md#get_api_resources) | **GET** /apis/certificates.k8s.io/v1beta1/ | 
[**list_certificate_signing_request**](CertificatesV1beta1Api.md#list_certificate_signing_request) | **GET** /apis/certificates.k8s.io/v1beta1/certificatesigningrequests | 
[**patch_certificate_signing_request**](CertificatesV1beta1Api.md#patch_certificate_signing_request) | **PATCH** /apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name} | 
[**patch_certificate_signing_request_status**](CertificatesV1beta1Api.md#patch_certificate_signing_request_status) | **PATCH** /apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}/status | 
[**read_certificate_signing_request**](CertificatesV1beta1Api.md#read_certificate_signing_request) | **GET** /apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name} | 
[**read_certificate_signing_request_status**](CertificatesV1beta1Api.md#read_certificate_signing_request_status) | **GET** /apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}/status | 
[**replace_certificate_signing_request**](CertificatesV1beta1Api.md#replace_certificate_signing_request) | **PUT** /apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name} | 
[**replace_certificate_signing_request_approval**](CertificatesV1beta1Api.md#replace_certificate_signing_request_approval) | **PUT** /apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}/approval | 
[**replace_certificate_signing_request_status**](CertificatesV1beta1Api.md#replace_certificate_signing_request_status) | **PUT** /apis/certificates.k8s.io/v1beta1/certificatesigningrequests/{name}/status | 


# **create_certificate_signing_request**
> V1beta1CertificateSigningRequest create_certificate_signing_request(body)



create a CertificateSigningRequest

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
from kubernetes.client.model.v1beta1_certificate_signing_request import V1beta1CertificateSigningRequest
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)
    body = V1beta1CertificateSigningRequest(
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
        spec=V1beta1CertificateSigningRequestSpec(
            extra={
                "key": [
                    "key_example",
                ],
            },
            groups=[
                "groups_example",
            ],
            request='YQ==',
            signer_name="signer_name_example",
            uid="uid_example",
            usages=[
                "usages_example",
            ],
            username="username_example",
        ),
        status=V1beta1CertificateSigningRequestStatus(
            certificate='YQ==',
            conditions=[
                V1beta1CertificateSigningRequestCondition(
                    last_update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    reason="reason_example",
                    type="type_example",
                ),
            ],
        ),
    ) # V1beta1CertificateSigningRequest | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_certificate_signing_request(body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->create_certificate_signing_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_certificate_signing_request(body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->create_certificate_signing_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)

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

# **delete_certificate_signing_request**
> V1Status delete_certificate_signing_request(name)



delete a CertificateSigningRequest

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)
    name = "name_example" # str | name of the CertificateSigningRequest
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
        api_response = api_instance.delete_certificate_signing_request(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->delete_certificate_signing_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.delete_certificate_signing_request(name, pretty=pretty, dry_run=dry_run, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->delete_certificate_signing_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CertificateSigningRequest |
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

# **delete_collection_certificate_signing_request**
> V1Status delete_collection_certificate_signing_request()



delete collection of CertificateSigningRequest

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)
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
        api_response = api_instance.delete_collection_certificate_signing_request(pretty=pretty, _continue=_continue, dry_run=dry_run, field_selector=field_selector, grace_period_seconds=grace_period_seconds, label_selector=label_selector, limit=limit, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, resource_version=resource_version, timeout_seconds=timeout_seconds, body=body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->delete_collection_certificate_signing_request: %s\n" % e)
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

# **get_api_resources**
> V1APIResourceList get_api_resources()



get available resources

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.get_api_resources()
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->get_api_resources: %s\n" % e)
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

# **list_certificate_signing_request**
> V1beta1CertificateSigningRequestList list_certificate_signing_request()



list or watch objects of kind CertificateSigningRequest

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
from kubernetes.client.model.v1beta1_certificate_signing_request_list import V1beta1CertificateSigningRequestList
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)
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
        api_response = api_instance.list_certificate_signing_request(pretty=pretty, allow_watch_bookmarks=allow_watch_bookmarks, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->list_certificate_signing_request: %s\n" % e)
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

[**V1beta1CertificateSigningRequestList**](V1beta1CertificateSigningRequestList.md)

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

# **patch_certificate_signing_request**
> V1beta1CertificateSigningRequest patch_certificate_signing_request(name, body)



partially update the specified CertificateSigningRequest

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
from kubernetes.client.model.v1beta1_certificate_signing_request import V1beta1CertificateSigningRequest
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)
    name = "name_example" # str | name of the CertificateSigningRequest
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
    force = True # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_certificate_signing_request(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->patch_certificate_signing_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_certificate_signing_request(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->patch_certificate_signing_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CertificateSigningRequest |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional]
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional]

### Return type

[**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)

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

# **patch_certificate_signing_request_status**
> V1beta1CertificateSigningRequest patch_certificate_signing_request_status(name, body)



partially update status of the specified CertificateSigningRequest

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
from kubernetes.client.model.v1beta1_certificate_signing_request import V1beta1CertificateSigningRequest
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)
    name = "name_example" # str | name of the CertificateSigningRequest
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). (optional)
    force = True # bool | Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.patch_certificate_signing_request_status(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->patch_certificate_signing_request_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.patch_certificate_signing_request_status(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager, force=force)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->patch_certificate_signing_request_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CertificateSigningRequest |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch). | [optional]
 **force** | **bool**| Force is going to \&quot;force\&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests. | [optional]

### Return type

[**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)

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

# **read_certificate_signing_request**
> V1beta1CertificateSigningRequest read_certificate_signing_request(name)



read the specified CertificateSigningRequest

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
from kubernetes.client.model.v1beta1_certificate_signing_request import V1beta1CertificateSigningRequest
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)
    name = "name_example" # str | name of the CertificateSigningRequest
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    exact = True # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. Deprecated. Planned for removal in 1.18. (optional)
    export = True # bool | Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.read_certificate_signing_request(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->read_certificate_signing_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.read_certificate_signing_request(name, pretty=pretty, exact=exact, export=export)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->read_certificate_signing_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CertificateSigningRequest |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. Deprecated. Planned for removal in 1.18. | [optional]
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. Deprecated. Planned for removal in 1.18. | [optional]

### Return type

[**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)

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

# **read_certificate_signing_request_status**
> V1beta1CertificateSigningRequest read_certificate_signing_request_status(name)



read status of the specified CertificateSigningRequest

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
from kubernetes.client.model.v1beta1_certificate_signing_request import V1beta1CertificateSigningRequest
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)
    name = "name_example" # str | name of the CertificateSigningRequest
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.read_certificate_signing_request_status(name)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->read_certificate_signing_request_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.read_certificate_signing_request_status(name, pretty=pretty)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->read_certificate_signing_request_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CertificateSigningRequest |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]

### Return type

[**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)

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

# **replace_certificate_signing_request**
> V1beta1CertificateSigningRequest replace_certificate_signing_request(name, body)



replace the specified CertificateSigningRequest

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
from kubernetes.client.model.v1beta1_certificate_signing_request import V1beta1CertificateSigningRequest
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)
    name = "name_example" # str | name of the CertificateSigningRequest
    body = V1beta1CertificateSigningRequest(
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
        spec=V1beta1CertificateSigningRequestSpec(
            extra={
                "key": [
                    "key_example",
                ],
            },
            groups=[
                "groups_example",
            ],
            request='YQ==',
            signer_name="signer_name_example",
            uid="uid_example",
            usages=[
                "usages_example",
            ],
            username="username_example",
        ),
        status=V1beta1CertificateSigningRequestStatus(
            certificate='YQ==',
            conditions=[
                V1beta1CertificateSigningRequestCondition(
                    last_update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    reason="reason_example",
                    type="type_example",
                ),
            ],
        ),
    ) # V1beta1CertificateSigningRequest | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_certificate_signing_request(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->replace_certificate_signing_request: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_certificate_signing_request(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->replace_certificate_signing_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CertificateSigningRequest |
 **body** | [**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)

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

# **replace_certificate_signing_request_approval**
> V1beta1CertificateSigningRequest replace_certificate_signing_request_approval(name, body)



replace approval of the specified CertificateSigningRequest

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
from kubernetes.client.model.v1beta1_certificate_signing_request import V1beta1CertificateSigningRequest
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)
    name = "name_example" # str | name of the CertificateSigningRequest
    body = V1beta1CertificateSigningRequest(
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
        spec=V1beta1CertificateSigningRequestSpec(
            extra={
                "key": [
                    "key_example",
                ],
            },
            groups=[
                "groups_example",
            ],
            request='YQ==',
            signer_name="signer_name_example",
            uid="uid_example",
            usages=[
                "usages_example",
            ],
            username="username_example",
        ),
        status=V1beta1CertificateSigningRequestStatus(
            certificate='YQ==',
            conditions=[
                V1beta1CertificateSigningRequestCondition(
                    last_update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    reason="reason_example",
                    type="type_example",
                ),
            ],
        ),
    ) # V1beta1CertificateSigningRequest | 
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_certificate_signing_request_approval(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->replace_certificate_signing_request_approval: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_certificate_signing_request_approval(name, body, dry_run=dry_run, field_manager=field_manager, pretty=pretty)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->replace_certificate_signing_request_approval: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CertificateSigningRequest |
 **body** | [**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)|  |
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]

### Return type

[**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)

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

# **replace_certificate_signing_request_status**
> V1beta1CertificateSigningRequest replace_certificate_signing_request_status(name, body)



replace status of the specified CertificateSigningRequest

### Example

* Api Key Authentication (BearerToken):
```python
import time
import kubernetes.client
from kubernetes.client.api import certificates_v1beta1_api
from kubernetes.client.model.v1beta1_certificate_signing_request import V1beta1CertificateSigningRequest
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
    api_instance = certificates_v1beta1_api.CertificatesV1beta1Api(api_client)
    name = "name_example" # str | name of the CertificateSigningRequest
    body = V1beta1CertificateSigningRequest(
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
        spec=V1beta1CertificateSigningRequestSpec(
            extra={
                "key": [
                    "key_example",
                ],
            },
            groups=[
                "groups_example",
            ],
            request='YQ==',
            signer_name="signer_name_example",
            uid="uid_example",
            usages=[
                "usages_example",
            ],
            username="username_example",
        ),
        status=V1beta1CertificateSigningRequestStatus(
            certificate='YQ==',
            conditions=[
                V1beta1CertificateSigningRequestCondition(
                    last_update_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    message="message_example",
                    reason="reason_example",
                    type="type_example",
                ),
            ],
        ),
    ) # V1beta1CertificateSigningRequest | 
    pretty = "pretty_example" # str | If 'true', then the output is pretty printed. (optional)
    dry_run = "dryRun_example" # str | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed (optional)
    field_manager = "fieldManager_example" # str | fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.replace_certificate_signing_request_status(name, body)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->replace_certificate_signing_request_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.replace_certificate_signing_request_status(name, body, pretty=pretty, dry_run=dry_run, field_manager=field_manager)
        pprint(api_response)
    except kubernetes.client.ApiException as e:
        print("Exception when calling CertificatesV1beta1Api->replace_certificate_signing_request_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CertificateSigningRequest |
 **body** | [**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)|  |
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional]
 **dry_run** | **str**| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed | [optional]
 **field_manager** | **str**| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. | [optional]

### Return type

[**V1beta1CertificateSigningRequest**](V1beta1CertificateSigningRequest.md)

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

