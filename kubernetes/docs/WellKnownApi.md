# kubernetes.client.WellKnownApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_account_issuer_open_id_configuration**](WellKnownApi.md#get_service_account_issuer_open_id_configuration) | **GET** /.well-known/openid-configuration/ | 


# **get_service_account_issuer_open_id_configuration**
> str get_service_account_issuer_open_id_configuration()



get service account issuer OpenID configuration, also known as the 'OIDC discovery doc'

### Example

* Api Key Authentication (BearerToken):
```python
from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint
configuration = kubernetes.client.Configuration()
# Configure API key authorization: BearerToken
configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"

# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes.client.WellKnownApi(api_client)
    
    try:
        api_response = api_instance.get_service_account_issuer_open_id_configuration()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WellKnownApi->get_service_account_issuer_open_id_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

