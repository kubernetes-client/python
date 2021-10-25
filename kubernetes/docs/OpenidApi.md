# kubernetes.client.OpenidApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_account_issuer_open_id_keyset**](OpenidApi.md#get_service_account_issuer_open_id_keyset) | **GET** /openid/v1/jwks/ | 


# **get_service_account_issuer_open_id_keyset**
> str get_service_account_issuer_open_id_keyset()



get service account issuer OpenID JSON Web Key Set (contains public token verification keys)

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
    api_instance = kubernetes.client.OpenidApi(api_client)
    
    try:
        api_response = api_instance.get_service_account_issuer_open_id_keyset()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OpenidApi->get_service_account_issuer_open_id_keyset: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/jwk-set+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

