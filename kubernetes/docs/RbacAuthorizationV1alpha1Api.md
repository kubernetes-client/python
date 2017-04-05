# kubernetes.client.RbacAuthorizationV1alpha1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_role**](RbacAuthorizationV1alpha1Api.md#create_cluster_role) | **POST** /apis/rbac.authorization.k8s.io/v1alpha1/clusterroles | 
[**create_cluster_role_binding**](RbacAuthorizationV1alpha1Api.md#create_cluster_role_binding) | **POST** /apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings | 
[**create_namespaced_role**](RbacAuthorizationV1alpha1Api.md#create_namespaced_role) | **POST** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles | 
[**create_namespaced_role_binding**](RbacAuthorizationV1alpha1Api.md#create_namespaced_role_binding) | **POST** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings | 
[**delete_cluster_role**](RbacAuthorizationV1alpha1Api.md#delete_cluster_role) | **DELETE** /apis/rbac.authorization.k8s.io/v1alpha1/clusterroles/{name} | 
[**delete_cluster_role_binding**](RbacAuthorizationV1alpha1Api.md#delete_cluster_role_binding) | **DELETE** /apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings/{name} | 
[**delete_collection_cluster_role**](RbacAuthorizationV1alpha1Api.md#delete_collection_cluster_role) | **DELETE** /apis/rbac.authorization.k8s.io/v1alpha1/clusterroles | 
[**delete_collection_cluster_role_binding**](RbacAuthorizationV1alpha1Api.md#delete_collection_cluster_role_binding) | **DELETE** /apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings | 
[**delete_collection_namespaced_role**](RbacAuthorizationV1alpha1Api.md#delete_collection_namespaced_role) | **DELETE** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles | 
[**delete_collection_namespaced_role_binding**](RbacAuthorizationV1alpha1Api.md#delete_collection_namespaced_role_binding) | **DELETE** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings | 
[**delete_namespaced_role**](RbacAuthorizationV1alpha1Api.md#delete_namespaced_role) | **DELETE** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles/{name} | 
[**delete_namespaced_role_binding**](RbacAuthorizationV1alpha1Api.md#delete_namespaced_role_binding) | **DELETE** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings/{name} | 
[**get_api_resources**](RbacAuthorizationV1alpha1Api.md#get_api_resources) | **GET** /apis/rbac.authorization.k8s.io/v1alpha1/ | 
[**list_cluster_role**](RbacAuthorizationV1alpha1Api.md#list_cluster_role) | **GET** /apis/rbac.authorization.k8s.io/v1alpha1/clusterroles | 
[**list_cluster_role_binding**](RbacAuthorizationV1alpha1Api.md#list_cluster_role_binding) | **GET** /apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings | 
[**list_namespaced_role**](RbacAuthorizationV1alpha1Api.md#list_namespaced_role) | **GET** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles | 
[**list_namespaced_role_binding**](RbacAuthorizationV1alpha1Api.md#list_namespaced_role_binding) | **GET** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings | 
[**list_role_binding_for_all_namespaces**](RbacAuthorizationV1alpha1Api.md#list_role_binding_for_all_namespaces) | **GET** /apis/rbac.authorization.k8s.io/v1alpha1/rolebindings | 
[**list_role_for_all_namespaces**](RbacAuthorizationV1alpha1Api.md#list_role_for_all_namespaces) | **GET** /apis/rbac.authorization.k8s.io/v1alpha1/roles | 
[**patch_cluster_role**](RbacAuthorizationV1alpha1Api.md#patch_cluster_role) | **PATCH** /apis/rbac.authorization.k8s.io/v1alpha1/clusterroles/{name} | 
[**patch_cluster_role_binding**](RbacAuthorizationV1alpha1Api.md#patch_cluster_role_binding) | **PATCH** /apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings/{name} | 
[**patch_namespaced_role**](RbacAuthorizationV1alpha1Api.md#patch_namespaced_role) | **PATCH** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles/{name} | 
[**patch_namespaced_role_binding**](RbacAuthorizationV1alpha1Api.md#patch_namespaced_role_binding) | **PATCH** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings/{name} | 
[**read_cluster_role**](RbacAuthorizationV1alpha1Api.md#read_cluster_role) | **GET** /apis/rbac.authorization.k8s.io/v1alpha1/clusterroles/{name} | 
[**read_cluster_role_binding**](RbacAuthorizationV1alpha1Api.md#read_cluster_role_binding) | **GET** /apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings/{name} | 
[**read_namespaced_role**](RbacAuthorizationV1alpha1Api.md#read_namespaced_role) | **GET** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles/{name} | 
[**read_namespaced_role_binding**](RbacAuthorizationV1alpha1Api.md#read_namespaced_role_binding) | **GET** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings/{name} | 
[**replace_cluster_role**](RbacAuthorizationV1alpha1Api.md#replace_cluster_role) | **PUT** /apis/rbac.authorization.k8s.io/v1alpha1/clusterroles/{name} | 
[**replace_cluster_role_binding**](RbacAuthorizationV1alpha1Api.md#replace_cluster_role_binding) | **PUT** /apis/rbac.authorization.k8s.io/v1alpha1/clusterrolebindings/{name} | 
[**replace_namespaced_role**](RbacAuthorizationV1alpha1Api.md#replace_namespaced_role) | **PUT** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/roles/{name} | 
[**replace_namespaced_role_binding**](RbacAuthorizationV1alpha1Api.md#replace_namespaced_role_binding) | **PUT** /apis/rbac.authorization.k8s.io/v1alpha1/namespaces/{namespace}/rolebindings/{name} | 


# **create_cluster_role**
> V1alpha1ClusterRole create_cluster_role(body, pretty=pretty)



create a ClusterRole

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
body = kubernetes.client.V1alpha1ClusterRole() # V1alpha1ClusterRole | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_cluster_role(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->create_cluster_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1ClusterRole**](V1alpha1ClusterRole.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1ClusterRole**](V1alpha1ClusterRole.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_role_binding**
> V1alpha1ClusterRoleBinding create_cluster_role_binding(body, pretty=pretty)



create a ClusterRoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
body = kubernetes.client.V1alpha1ClusterRoleBinding() # V1alpha1ClusterRoleBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_cluster_role_binding(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->create_cluster_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1ClusterRoleBinding**](V1alpha1ClusterRoleBinding.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1ClusterRoleBinding**](V1alpha1ClusterRoleBinding.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_role**
> V1alpha1Role create_namespaced_role(namespace, body, pretty=pretty)



create a Role

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1alpha1Role() # V1alpha1Role | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_role(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->create_namespaced_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1alpha1Role**](V1alpha1Role.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1Role**](V1alpha1Role.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_role_binding**
> V1alpha1RoleBinding create_namespaced_role_binding(namespace, body, pretty=pretty)



create a RoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1alpha1RoleBinding() # V1alpha1RoleBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_role_binding(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->create_namespaced_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1alpha1RoleBinding**](V1alpha1RoleBinding.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1RoleBinding**](V1alpha1RoleBinding.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_role**
> V1Status delete_cluster_role(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a ClusterRole

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the ClusterRole
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_cluster_role(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->delete_cluster_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterRole | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 

### Return type

[**V1Status**](V1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_role_binding**
> V1Status delete_cluster_role_binding(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a ClusterRoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the ClusterRoleBinding
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_cluster_role_binding(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->delete_cluster_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterRoleBinding | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 

### Return type

[**V1Status**](V1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_cluster_role**
> V1Status delete_collection_cluster_role(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of ClusterRole

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_cluster_role(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->delete_collection_cluster_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1Status**](V1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_cluster_role_binding**
> V1Status delete_collection_cluster_role_binding(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of ClusterRoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_cluster_role_binding(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->delete_collection_cluster_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1Status**](V1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_role**
> V1Status delete_collection_namespaced_role(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of Role

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_role(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->delete_collection_namespaced_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1Status**](V1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_role_binding**
> V1Status delete_collection_namespaced_role_binding(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of RoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_role_binding(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->delete_collection_namespaced_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1Status**](V1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_role**
> V1Status delete_namespaced_role(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a Role

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the Role
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_namespaced_role(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->delete_namespaced_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Role | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 

### Return type

[**V1Status**](V1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_role_binding**
> V1Status delete_namespaced_role_binding(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a RoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the RoleBinding
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_namespaced_role_binding(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->delete_namespaced_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the RoleBinding | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 

### Return type

[**V1Status**](V1Status.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources**
> V1APIResourceList get_api_resources()



get available resources

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()

try: 
    api_response = api_instance.get_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->get_api_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1APIResourceList**](V1APIResourceList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_role**
> V1alpha1ClusterRoleList list_cluster_role(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ClusterRole

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_cluster_role(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->list_cluster_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1ClusterRoleList**](V1alpha1ClusterRoleList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_role_binding**
> V1alpha1ClusterRoleBindingList list_cluster_role_binding(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ClusterRoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_cluster_role_binding(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->list_cluster_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1ClusterRoleBindingList**](V1alpha1ClusterRoleBindingList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_role**
> V1alpha1RoleList list_namespaced_role(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Role

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_role(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->list_namespaced_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1RoleList**](V1alpha1RoleList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_role_binding**
> V1alpha1RoleBindingList list_namespaced_role_binding(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind RoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_role_binding(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->list_namespaced_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1RoleBindingList**](V1alpha1RoleBindingList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_binding_for_all_namespaces**
> V1alpha1RoleBindingList list_role_binding_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind RoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_role_binding_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->list_role_binding_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1RoleBindingList**](V1alpha1RoleBindingList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_for_all_namespaces**
> V1alpha1RoleList list_role_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Role

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_role_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->list_role_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1alpha1RoleList**](V1alpha1RoleList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cluster_role**
> V1alpha1ClusterRole patch_cluster_role(name, body, pretty=pretty)



partially update the specified ClusterRole

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the ClusterRole
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_cluster_role(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->patch_cluster_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterRole | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1ClusterRole**](V1alpha1ClusterRole.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cluster_role_binding**
> V1alpha1ClusterRoleBinding patch_cluster_role_binding(name, body, pretty=pretty)



partially update the specified ClusterRoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the ClusterRoleBinding
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_cluster_role_binding(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->patch_cluster_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterRoleBinding | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1ClusterRoleBinding**](V1alpha1ClusterRoleBinding.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_role**
> V1alpha1Role patch_namespaced_role(name, namespace, body, pretty=pretty)



partially update the specified Role

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the Role
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_role(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->patch_namespaced_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Role | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1Role**](V1alpha1Role.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_role_binding**
> V1alpha1RoleBinding patch_namespaced_role_binding(name, namespace, body, pretty=pretty)



partially update the specified RoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the RoleBinding
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_role_binding(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->patch_namespaced_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the RoleBinding | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1RoleBinding**](V1alpha1RoleBinding.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_role**
> V1alpha1ClusterRole read_cluster_role(name, pretty=pretty)



read the specified ClusterRole

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the ClusterRole
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_cluster_role(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->read_cluster_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterRole | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1ClusterRole**](V1alpha1ClusterRole.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_cluster_role_binding**
> V1alpha1ClusterRoleBinding read_cluster_role_binding(name, pretty=pretty)



read the specified ClusterRoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the ClusterRoleBinding
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_cluster_role_binding(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->read_cluster_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterRoleBinding | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1ClusterRoleBinding**](V1alpha1ClusterRoleBinding.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_role**
> V1alpha1Role read_namespaced_role(name, namespace, pretty=pretty)



read the specified Role

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the Role
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_role(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->read_namespaced_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Role | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1Role**](V1alpha1Role.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_role_binding**
> V1alpha1RoleBinding read_namespaced_role_binding(name, namespace, pretty=pretty)



read the specified RoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the RoleBinding
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_role_binding(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->read_namespaced_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the RoleBinding | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1RoleBinding**](V1alpha1RoleBinding.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_cluster_role**
> V1alpha1ClusterRole replace_cluster_role(name, body, pretty=pretty)



replace the specified ClusterRole

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the ClusterRole
body = kubernetes.client.V1alpha1ClusterRole() # V1alpha1ClusterRole | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_cluster_role(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->replace_cluster_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterRole | 
 **body** | [**V1alpha1ClusterRole**](V1alpha1ClusterRole.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1ClusterRole**](V1alpha1ClusterRole.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_cluster_role_binding**
> V1alpha1ClusterRoleBinding replace_cluster_role_binding(name, body, pretty=pretty)



replace the specified ClusterRoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the ClusterRoleBinding
body = kubernetes.client.V1alpha1ClusterRoleBinding() # V1alpha1ClusterRoleBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_cluster_role_binding(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->replace_cluster_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterRoleBinding | 
 **body** | [**V1alpha1ClusterRoleBinding**](V1alpha1ClusterRoleBinding.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1ClusterRoleBinding**](V1alpha1ClusterRoleBinding.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_role**
> V1alpha1Role replace_namespaced_role(name, namespace, body, pretty=pretty)



replace the specified Role

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the Role
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1alpha1Role() # V1alpha1Role | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_role(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->replace_namespaced_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Role | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1alpha1Role**](V1alpha1Role.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1Role**](V1alpha1Role.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_role_binding**
> V1alpha1RoleBinding replace_namespaced_role_binding(name, namespace, body, pretty=pretty)



replace the specified RoleBinding

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
kubernetes.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kubernetes.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.RbacAuthorizationV1alpha1Api()
name = 'name_example' # str | name of the RoleBinding
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1alpha1RoleBinding() # V1alpha1RoleBinding | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_role_binding(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationV1alpha1Api->replace_namespaced_role_binding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the RoleBinding | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1alpha1RoleBinding**](V1alpha1RoleBinding.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1alpha1RoleBinding**](V1alpha1RoleBinding.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

