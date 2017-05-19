# kubernetes.client.ThirdPartyResourcesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_third_party_resource**](ThirdPartyResourcesApi.md#create_third_party_resource) | **POST** /apis/{fqdn}/v1/namespaces/{namespace}/{resource} | Create a Resource
[**delete_third_party_resource**](ThirdPartyResourcesApi.md#delete_third_party_resource) | **DELETE** /apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name} | Deletes a specific Resource
[**get_third_party_resource**](ThirdPartyResourcesApi.md#get_third_party_resource) | **GET** /apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name} | Gets a specific Resource
[**list_third_party_resource**](ThirdPartyResourcesApi.md#list_third_party_resource) | **GET** /apis/{fqdn}/v1/{resource} | Gets Resources
[**update_third_party_resource**](ThirdPartyResourcesApi.md#update_third_party_resource) | **PUT** /apis/{fqdn}/v1/namespaces/{namespace}/{resource}/{name} | Update a Resource


# **create_third_party_resource**
> object create_third_party_resource(namespace, fqdn, resource, body)

Create a Resource

Creates a third party resource of the type specified

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubernetes.client.ThirdPartyResourcesApi()
namespace = 'namespace_example' # str | The Resource's namespace
fqdn = 'fqdn_example' # str | The Third party Resource fqdn
resource = 'resource_example' # str | The Resource type
body = NULL # object | The JSON schema of the Resource to create.

try: 
    # Create a Resource
    api_response = api_instance.create_third_party_resource(namespace, fqdn, resource, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdPartyResourcesApi->create_third_party_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Resource&#39;s namespace | 
 **fqdn** | **str**| The Third party Resource fqdn | 
 **resource** | **str**| The Resource type | 
 **body** | **object**| The JSON schema of the Resource to create. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_third_party_resource**
> object delete_third_party_resource(body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)

Deletes a specific Resource

Deletes the specified Resource in the specified namespace

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubernetes.client.ThirdPartyResourcesApi()
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    # Deletes a specific Resource
    api_response = api_instance.delete_third_party_resource(body, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdPartyResourcesApi->delete_third_party_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. Either this field or PropagationPolicy may be set, but not both. | [optional] 
 **propagation_policy** | **str**| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_third_party_resource**
> object get_third_party_resource(namespace, name, fqdn, resource)

Gets a specific Resource

Returns a specific Resource in a namespace

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubernetes.client.ThirdPartyResourcesApi()
namespace = 'namespace_example' # str | The Resource's namespace
name = 'name_example' # str | The Resource's name
fqdn = 'fqdn_example' # str | The Third party Resource fqdn
resource = 'resource_example' # str | The Resource type

try: 
    # Gets a specific Resource
    api_response = api_instance.get_third_party_resource(namespace, name, fqdn, resource)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdPartyResourcesApi->get_third_party_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Resource&#39;s namespace | 
 **name** | **str**| The Resource&#39;s name | 
 **fqdn** | **str**| The Third party Resource fqdn | 
 **resource** | **str**| The Resource type | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_third_party_resource**
> object list_third_party_resource(fqdn, resource, watch=watch)

Gets Resources

Returns a list of Resources

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubernetes.client.ThirdPartyResourcesApi()
fqdn = 'fqdn_example' # str | The Third party Resource fqdn
resource = 'resource_example' # str | The Resource type
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    # Gets Resources
    api_response = api_instance.list_third_party_resource(fqdn, resource, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdPartyResourcesApi->list_third_party_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**| The Third party Resource fqdn | 
 **resource** | **str**| The Resource type | 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_third_party_resource**
> object update_third_party_resource(namespace, fqdn, resource, body)

Update a Resource

Update the specified third party resource of the type specified

### Example 
```python
from __future__ import print_statement
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kubernetes.client.ThirdPartyResourcesApi()
namespace = 'namespace_example' # str | The Resource's namespace
fqdn = 'fqdn_example' # str | The Third party Resource fqdn
resource = 'resource_example' # str | The Resource type
body = NULL # object | The JSON schema of the Resource to create.

try: 
    # Update a Resource
    api_response = api_instance.update_third_party_resource(namespace, fqdn, resource, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThirdPartyResourcesApi->update_third_party_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| The Resource&#39;s namespace | 
 **fqdn** | **str**| The Third party Resource fqdn | 
 **resource** | **str**| The Resource type | 
 **body** | **object**| The JSON schema of the Resource to create. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

