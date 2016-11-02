# k8sclient.BatchV2alpha1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_batch_v2alpha1_api_resources**](BatchV2alpha1Api.md#get_batch_v2alpha1_api_resources) | **GET** /apis/batch/v2alpha1/ | 


# **get_batch_v2alpha1_api_resources**
> UnversionedAPIResourceList get_batch_v2alpha1_api_resources()



get available resources

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
api_instance = k8sclient.BatchV2alpha1Api()

try: 
    api_response = api_instance.get_batch_v2alpha1_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->get_batch_v2alpha1_api_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnversionedAPIResourceList**](UnversionedAPIResourceList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

