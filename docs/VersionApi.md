# k8sclient.VersionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_code**](VersionApi.md#get_code) | **GET** /version/ | 


# **get_code**
> VersionInfo get_code()



get the code version

### Example 
```python
from __future__ import print_statement
import time
import k8sclient
from k8sclient.rest import ApiException
from pprint import pprint

# Configure API key authorization: BearerToken
k8sclient.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# k8sclient.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = k8sclient.VersionApi()

try: 
    api_response = api_instance.get_code()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->get_code: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

