# kubernetes.client.CustomObjectsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_custom_object**](CustomObjectsApi.md#create_cluster_custom_object) | **POST** /apis/{group}/{version}/{plural} | 
[**create_namespaced_custom_object**](CustomObjectsApi.md#create_namespaced_custom_object) | **POST** /apis/{group}/{version}/namespaces/{namespace}/{plural} | 
[**delete_cluster_custom_object**](CustomObjectsApi.md#delete_cluster_custom_object) | **DELETE** /apis/{group}/{version}/{plural}/{name} | 
[**delete_namespaced_custom_object**](CustomObjectsApi.md#delete_namespaced_custom_object) | **DELETE** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name} | 
[**get_cluster_custom_object**](CustomObjectsApi.md#get_cluster_custom_object) | **GET** /apis/{group}/{version}/{plural}/{name} | 
[**get_namespaced_custom_object**](CustomObjectsApi.md#get_namespaced_custom_object) | **GET** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name} | 
[**list_cluster_custom_object**](CustomObjectsApi.md#list_cluster_custom_object) | **GET** /apis/{group}/{version}/{plural} | 
[**list_namespaced_custom_object**](CustomObjectsApi.md#list_namespaced_custom_object) | **GET** /apis/{group}/{version}/namespaces/{namespace}/{plural} | 
[**replace_cluster_custom_object**](CustomObjectsApi.md#replace_cluster_custom_object) | **PUT** /apis/{group}/{version}/{plural}/{name} | 
[**replace_namespaced_custom_object**](CustomObjectsApi.md#replace_namespaced_custom_object) | **PUT** /apis/{group}/{version}/namespaces/{namespace}/{plural}/{name} | 


# **create_cluster_custom_object**
> object create_cluster_custom_object(group, version, plural, body, pretty=pretty)



Creates a cluster scoped Custom object

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
api_instance = kubernetes.client.CustomObjectsApi()
group = 'group_example' # str | The custom resource's group name
version = 'version_example' # str | The custom resource's version
plural = 'plural_example' # str | The custom resource's plural name. For TPRs this would be lowercase plural kind.
body = NULL # object | The JSON schema of the Resource to create.
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
 **body** | **object**| The JSON schema of the Resource to create. | 
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
api_instance = kubernetes.client.CustomObjectsApi()
group = 'group_example' # str | The custom resource's group name
version = 'version_example' # str | The custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | The custom resource's plural name. For TPRs this would be lowercase plural kind.
body = NULL # object | The JSON schema of the Resource to create.
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
 **body** | **object**| The JSON schema of the Resource to create. | 
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
> object delete_cluster_custom_object(group, version, plural, name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Deletes the specified cluster scoped custom object

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
api_instance = kubernetes.client.CustomObjectsApi()
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom object's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_cluster_custom_object(group, version, plural, name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->delete_cluster_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **plural** | **str**| the custom object&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_custom_object**
> object delete_namespaced_custom_object(group, version, namespace, plural, name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



Deletes the specified namespace scoped custom object

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
api_instance = kubernetes.client.CustomObjectsApi()
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_namespaced_custom_object(group, version, namespace, plural, name, body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomObjectsApi->delete_namespaced_custom_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**| the custom resource&#39;s group | 
 **version** | **str**| the custom resource&#39;s version | 
 **namespace** | **str**| The custom resource&#39;s namespace | 
 **plural** | **str**| the custom resource&#39;s plural name. For TPRs this would be lowercase plural kind. | 
 **name** | **str**| the custom object&#39;s name | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_custom_object**
> object get_cluster_custom_object(group, version, plural, name)



Returns a cluster scoped custom object

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
api_instance = kubernetes.client.CustomObjectsApi()
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

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_custom_object**
> object get_namespaced_custom_object(group, version, namespace, plural, name)



Returns a namespace scoped custom object

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
api_instance = kubernetes.client.CustomObjectsApi()
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

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_custom_object**
> object list_cluster_custom_object(group, version, plural, pretty=pretty, label_selector=label_selector, resource_version=resource_version, watch=watch)



list or watch cluster scoped custom objects

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
api_instance = kubernetes.client.CustomObjectsApi()
group = 'group_example' # str | The custom resource's group name
version = 'version_example' # str | The custom resource's version
plural = 'plural_example' # str | The custom resource's plural name. For TPRs this would be lowercase plural kind.
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. (optional)

try: 
    api_response = api_instance.list_cluster_custom_object(group, version, plural, pretty=pretty, label_selector=label_selector, resource_version=resource_version, watch=watch)
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
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_custom_object**
> object list_namespaced_custom_object(group, version, namespace, plural, pretty=pretty, label_selector=label_selector, resource_version=resource_version, watch=watch)



list or watch namespace scoped custom objects

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
api_instance = kubernetes.client.CustomObjectsApi()
group = 'group_example' # str | The custom resource's group name
version = 'version_example' # str | The custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | The custom resource's plural name. For TPRs this would be lowercase plural kind.
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. (optional)

try: 
    api_response = api_instance.list_namespaced_custom_object(group, version, namespace, plural, pretty=pretty, label_selector=label_selector, resource_version=resource_version, watch=watch)
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
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. | [optional] 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/json;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_cluster_custom_object**
> object replace_cluster_custom_object(group, version, plural, name, body)



replace the specified cluster scoped custom object

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
api_instance = kubernetes.client.CustomObjectsApi()
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
plural = 'plural_example' # str | the custom object's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = NULL # object | The JSON schema of the Resource to replace.

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
 **body** | **object**| The JSON schema of the Resource to replace. | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_custom_object**
> object replace_namespaced_custom_object(group, version, namespace, plural, name, body)



replace the specified namespace scoped custom object

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
api_instance = kubernetes.client.CustomObjectsApi()
group = 'group_example' # str | the custom resource's group
version = 'version_example' # str | the custom resource's version
namespace = 'namespace_example' # str | The custom resource's namespace
plural = 'plural_example' # str | the custom resource's plural name. For TPRs this would be lowercase plural kind.
name = 'name_example' # str | the custom object's name
body = NULL # object | The JSON schema of the Resource to replace.

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
 **body** | **object**| The JSON schema of the Resource to replace. | 

### Return type

**object**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

