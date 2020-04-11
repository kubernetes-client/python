# kubernetes.client.CustomObjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_custom_object**](CustomObjectsApi.md#create_cluster_custom_object) | **POST** /apis/{group}/{version}/{plural} | 
[**create_namespaced_custom_object**](CustomObjectsApi.md#create_namespaced_custom_object) | **POST** /apis/{group}/{version}/namespaces/{namespace}/{plural} | 
[**delete_cluster_custom_object**](CustomObjectsApi.md#delete_cluster_custom_object) | **DELETE** /apis/{group}/{version}/{plural} | 
[**delete_cluster_custom_object_0**](CustomObjectsApi.md#delete_cluster_custom_object_0) | **DELETE** /apis/{group}/{version}/{plural}/{name} | 
[**delete_namespaced_custom_object**](CustomObjectsApi.md#delete_namespaced_custom_object) | **DELETE** /apis/{group}/{version}/namespaces/{namespace}/{plural} | 
[**delete_namespaced_custom_object_0**](CustomObjectsApi.md#delete_namespaced_custom_object_0) | **DELETE** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name} | 
[**get_cluster_custom_object**](CustomObjectsApi.md#get_cluster_custom_object) | **GET** /apis/{group}/{version}/{plural}/{name} | 
[**get_cluster_custom_object_scale**](CustomObjectsApi.md#get_cluster_custom_object_scale) | **GET** /apis/{group}/{version}/{plural}/{name}/scale | 
[**get_cluster_custom_object_status**](CustomObjectsApi.md#get_cluster_custom_object_status) | **GET** /apis/{group}/{version}/{plural}/{name}/status | 
[**get_namespaced_custom_object**](CustomObjectsApi.md#get_namespaced_custom_object) | **GET** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name} | 
[**get_namespaced_custom_object_scale**](CustomObjectsApi.md#get_namespaced_custom_object_scale) | **GET** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name}/scale | 
[**get_namespaced_custom_object_status**](CustomObjectsApi.md#get_namespaced_custom_object_status) | **GET** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name}/status | 
[**list_cluster_custom_object**](CustomObjectsApi.md#list_cluster_custom_object) | **GET** /apis/{group}/{version}/{plural} | 
[**list_namespaced_custom_object**](CustomObjectsApi.md#list_namespaced_custom_object) | **GET** /apis/{group}/{version}/namespaces/{namespace}/{plural} | 
[**patch_cluster_custom_object**](CustomObjectsApi.md#patch_cluster_custom_object) | **PATCH** /apis/{group}/{version}/{plural}/{name} | 
[**patch_cluster_custom_object_scale**](CustomObjectsApi.md#patch_cluster_custom_object_scale) | **PATCH** /apis/{group}/{version}/{plural}/{name}/scale | 
[**patch_cluster_custom_object_status**](CustomObjectsApi.md#patch_cluster_custom_object_status) | **PATCH** /apis/{group}/{version}/{plural}/{name}/status | 
[**patch_namespaced_custom_object**](CustomObjectsApi.md#patch_namespaced_custom_object) | **PATCH** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name} | 
[**patch_namespaced_custom_object_scale**](CustomObjectsApi.md#patch_namespaced_custom_object_scale) | **PATCH** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name}/scale | 
[**patch_namespaced_custom_object_status**](CustomObjectsApi.md#patch_namespaced_custom_object_status) | **PATCH** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name}/status | 
[**replace_cluster_custom_object**](CustomObjectsApi.md#replace_cluster_custom_object) | **PUT** /apis/{group}/{version}/{plural}/{name} | 
[**replace_cluster_custom_object_scale**](CustomObjectsApi.md#replace_cluster_custom_object_scale) | **PUT** /apis/{group}/{version}/{plural}/{name}/scale | 
[**replace_cluster_custom_object_status**](CustomObjectsApi.md#replace_cluster_custom_object_status) | **PUT** /apis/{group}/{version}/{plural}/{name}/status | 
[**replace_namespaced_custom_object**](CustomObjectsApi.md#replace_namespaced_custom_object) | **PUT** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name} | 
[**replace_namespaced_custom_object_scale**](CustomObjectsApi.md#replace_namespaced_custom_object_scale) | **PUT** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name}/scale | 
[**replace_namespaced_custom_object_status**](CustomObjectsApi.md#replace_namespaced_custom_object_status) | **PUT** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name}/status | 


# **create_cluster_custom_object**
> object create_cluster_custom_object(group, version, plural, body, pretty=pretty)



Creates a cluster scoped Custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | The custom resource's group name
version = 'version_example' # str | The custom resource's version
plural = 'plural_example' # str | The custom resource's plural name. For TPRs this would be lowercase plural kind.
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | The JSON schema of the Resource to create.
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.create_cluster_custom_object(group, version, plural, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->create_cluster_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| The custom resource&#39;s group name | 
 **version** | **str**| The custom resource&#39;s version | 
 **plural** | **str**| The custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The JSON schema of the Resource to create. | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_custom_object**
> object create_namespaced_custom_object(group, version, namespace, plural, body, pretty=pretty)



Creates a namespace scoped Custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | The custom resource's group name
version = 'version_example' # str | The custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | The custom resource's plural name. For TPRs this would be lowercase plural kind.
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | The JSON schema of the Resource to create.
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try:
    api_response = api_instance.create_namespaced_custom_object(group, version, namespace, plural, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->create_namespaced_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| The custom resource&#39;s group name | 
 **version** | **str**| The custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| The custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The JSON schema of the Resource to create. | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_custom_object**
> object delete_cluster_custom_object(group, version, plural, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)



Deletes the specified cluster scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | The custom resource's group name
version = 'version_example' # str | The custom resource's version
plural = 'plural_example' # str | The custom resource's plural name. For TPRs this would be lowercase plural kind.
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

try:
    api_response = api_instance.delete_cluster_custom_object(group, version, plural, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->delete_cluster_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| The custom resource&#39;s group name | 
 **version** | **str**| The custom resource&#39;s version | 
 **plural** | **str**| The custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_custom_object_0**
> object delete_cluster_custom_object_0(group, version, plural, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)



Deletes the specified cluster scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom object's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

try:
    api_response = api_instance.delete_cluster_custom_object_0(group, version, plural, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->delete_cluster_custom_object_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **plural** | **str**| the custom object&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_custom_object**
> object delete_namespaced_custom_object(group, version, namespace, plural, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)



Deletes the specified namespace scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | The custom resource's group name
version = 'version_example' # str | The custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | The custom resource's plural name. For TPRs this would be lowercase plural kind.
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

try:
    api_response = api_instance.delete_namespaced_custom_object(group, version, namespace, plural, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->delete_namespaced_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| The custom resource&#39;s group name | 
 **version** | **str**| The custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| The custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_custom_object_0**
> object delete_namespaced_custom_object_0(group, version, namespace, plural, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)



Deletes the specified namespace scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = True # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions |  (optional)

try:
    api_response = api_instance.delete_namespaced_custom_object_0(group, version, namespace, plural, name, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->delete_namespaced_custom_object_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_custom_object**
> object get_cluster_custom_object(group, version, plural, name)



Returns a cluster scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom object's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name

try:
    api_response = api_instance.get_cluster_custom_object(group, version, plural, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->get_cluster_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **plural** | **str**| the custom object&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_custom_object_scale**
> object get_cluster_custom_object_scale(group, version, plural, name)



read scale of the specified custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name

try:
    api_response = api_instance.get_cluster_custom_object_scale(group, version, plural, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->get_cluster_custom_object_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_custom_object_status**
> object get_cluster_custom_object_status(group, version, plural, name)



read status of the specified cluster scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name

try:
    api_response = api_instance.get_cluster_custom_object_status(group, version, plural, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->get_cluster_custom_object_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_custom_object**
> object get_namespaced_custom_object(group, version, namespace, plural, name)



Returns a namespace scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name

try:
    api_response = api_instance.get_namespaced_custom_object(group, version, namespace, plural, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->get_namespaced_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_custom_object_scale**
> object get_namespaced_custom_object_scale(group, version, namespace, plural, name)



read scale of the specified namespace scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name

try:
    api_response = api_instance.get_namespaced_custom_object_scale(group, version, namespace, plural, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->get_namespaced_custom_object_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_custom_object_status**
> object get_namespaced_custom_object_status(group, version, namespace, plural, name)



read status of the specified namespace scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name

try:
    api_response = api_instance.get_namespaced_custom_object_status(group, version, namespace, plural, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->get_namespaced_custom_object_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_custom_object**
> object list_cluster_custom_object(group, version, plural, pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch cluster scoped custom objects

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | The custom resource's group name
version = 'version_example' # str | The custom resource's version
plural = 'plural_example' # str | The custom resource's plural name. For TPRs this would be lowercase plural kind.
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. (optional)

try:
    api_response = api_instance.list_cluster_custom_object(group, version, plural, pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->list_cluster_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| The custom resource&#39;s group name | 
 **version** | **str**| The custom resource&#39;s version | 
 **plural** | **str**| The custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_custom_object**
> object list_namespaced_custom_object(group, version, namespace, plural, pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch namespace scoped custom objects

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | The custom resource's group name
version = 'version_example' # str | The custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | The custom resource's plural name. For TPRs this would be lowercase plural kind.
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
_continue = '_continue_example' # str | The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
limit = 56 # int | limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. (optional)
watch = True # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. (optional)

try:
    api_response = api_instance.list_namespaced_custom_object(group, version, namespace, plural, pretty=pretty, _continue=_continue, field_selector=field_selector, label_selector=label_selector, limit=limit, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->list_namespaced_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| The custom resource&#39;s group name | 
 **version** | **str**| The custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| The custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **_continue** | **str**| The continue option should be set when retrieving more results from the server. Since this value is server defined, kubernetes.clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the kubernetes.client needs a consistent list, it must restart their list without the continue field. Otherwise, the kubernetes.client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \&quot;next key\&quot;.  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **limit** | **int**| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and kubernetes.clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, kubernetes.clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a kubernetes.client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cluster_custom_object**
> object patch_cluster_custom_object(group, version, plural, name, body)



patch the specified cluster scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom object's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | The JSON schema of the Resource to patch.

try:
    api_response = api_instance.patch_cluster_custom_object(group, version, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->patch_cluster_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **plural** | **str**| the custom object&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The JSON schema of the Resource to patch. | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cluster_custom_object_scale**
> object patch_cluster_custom_object_scale(group, version, plural, name, body)



partially update scale of the specified cluster scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    api_response = api_instance.patch_cluster_custom_object_scale(group, version, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->patch_cluster_custom_object_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_cluster_custom_object_status**
> object patch_cluster_custom_object_status(group, version, plural, name, body)



partially update status of the specified cluster scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    api_response = api_instance.patch_cluster_custom_object_status(group, version, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->patch_cluster_custom_object_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_custom_object**
> object patch_namespaced_custom_object(group, version, namespace, plural, name, body)



patch the specified namespace scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | The JSON schema of the Resource to patch.

try:
    api_response = api_instance.patch_namespaced_custom_object(group, version, namespace, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->patch_namespaced_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The JSON schema of the Resource to patch. | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_custom_object_scale**
> object patch_namespaced_custom_object_scale(group, version, namespace, plural, name, body)



partially update scale of the specified namespace scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    api_response = api_instance.patch_namespaced_custom_object_scale(group, version, namespace, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->patch_namespaced_custom_object_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_custom_object_status**
> object patch_namespaced_custom_object_status(group, version, namespace, plural, name, body)



partially update status of the specified namespace scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    api_response = api_instance.patch_namespaced_custom_object_status(group, version, namespace, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->patch_namespaced_custom_object_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_cluster_custom_object**
> object replace_cluster_custom_object(group, version, plural, name, body)



replace the specified cluster scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom object's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | The JSON schema of the Resource to replace.

try:
    api_response = api_instance.replace_cluster_custom_object(group, version, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->replace_cluster_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **plural** | **str**| the custom object&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The JSON schema of the Resource to replace. | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_cluster_custom_object_scale**
> object replace_cluster_custom_object_scale(group, version, plural, name, body)



replace scale of the specified cluster scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    api_response = api_instance.replace_cluster_custom_object_scale(group, version, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->replace_cluster_custom_object_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_cluster_custom_object_status**
> object replace_cluster_custom_object_status(group, version, plural, name, body)



replace status of the cluster scoped specified custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    api_response = api_instance.replace_cluster_custom_object_status(group, version, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->replace_cluster_custom_object_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_custom_object**
> object replace_namespaced_custom_object(group, version, namespace, plural, name, body)



replace the specified namespace scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | The JSON schema of the Resource to replace.

try:
    api_response = api_instance.replace_namespaced_custom_object(group, version, namespace, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->replace_namespaced_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The JSON schema of the Resource to replace. | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_custom_object_scale**
> object replace_namespaced_custom_object_scale(group, version, namespace, plural, name, body)



replace scale of the specified namespace scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    api_response = api_instance.replace_namespaced_custom_object_scale(group, version, namespace, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->replace_namespaced_custom_object_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_custom_object_status**
> object replace_namespaced_custom_object_status(group, version, namespace, plural, name, body)



replace status of the specified namespace scoped custom object

### Example

* Api Key Authentication (BearerToken): 
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
configuration = kubernetes.client.Configuration()
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubernetes.client.CustomObjectsApi(kubernetes.client.ApiClient(configuration))
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | 

try:
    api_response = api_instance.replace_namespaced_custom_object_status(group, version, namespace, plural, name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->replace_namespaced_custom_object_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

