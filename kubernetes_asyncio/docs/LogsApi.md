# kubernetes_asyncio.client.LogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_file_handler**](LogsApi.md#log_file_handler) | **GET** /logs/{logpath} | 
[**log_file_list_handler**](LogsApi.md#log_file_list_handler) | **GET** /logs/ | 


# **log_file_handler**
> log_file_handler(logpath)



### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import kubernetes_asyncio.client
from kubernetes_asyncio.client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes_asyncio.client.Configuration(
    host = "http://localhost"
)

# The kubernetes_asyncio.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API kubernetes_asyncio.client
with kubernetes_asyncio.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_asyncio.client.LogsApi(api_client)
    logpath = 'logpath_example' # str | path to the log

    try:
        api_instance.log_file_handler(logpath)
    except ApiException as e:
        print("Exception when calling LogsApi->log_file_handler: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logpath** | **str**| path to the log | 

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_file_list_handler**
> log_file_list_handler()



### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import kubernetes_asyncio.client
from kubernetes_asyncio.client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = kubernetes_asyncio.client.Configuration(
    host = "http://localhost"
)

# The kubernetes_asyncio.client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerToken
configuration.api_key['BearerToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerToken'] = 'Bearer'

# Enter a context with an instance of the API kubernetes_asyncio.client
with kubernetes_asyncio.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes_asyncio.client.LogsApi(api_client)
    
    try:
        api_instance.log_file_list_handler()
    except ApiException as e:
        print("Exception when calling LogsApi->log_file_list_handler: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

