# k8sclient.BatchV2alpha1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_cron_job**](BatchV2alpha1Api.md#create_namespaced_cron_job) | **POST** /apis/batch/v2alpha1/namespaces/{namespace}/cronjobs | 
[**create_namespaced_job**](BatchV2alpha1Api.md#create_namespaced_job) | **POST** /apis/batch/v2alpha1/namespaces/{namespace}/jobs | 
[**create_namespaced_scheduled_job**](BatchV2alpha1Api.md#create_namespaced_scheduled_job) | **POST** /apis/batch/v2alpha1/namespaces/{namespace}/scheduledjobs | 
[**delete_collection_namespaced_cron_job**](BatchV2alpha1Api.md#delete_collection_namespaced_cron_job) | **DELETE** /apis/batch/v2alpha1/namespaces/{namespace}/cronjobs | 
[**delete_collection_namespaced_job**](BatchV2alpha1Api.md#delete_collection_namespaced_job) | **DELETE** /apis/batch/v2alpha1/namespaces/{namespace}/jobs | 
[**delete_collection_namespaced_scheduled_job**](BatchV2alpha1Api.md#delete_collection_namespaced_scheduled_job) | **DELETE** /apis/batch/v2alpha1/namespaces/{namespace}/scheduledjobs | 
[**delete_namespaced_cron_job**](BatchV2alpha1Api.md#delete_namespaced_cron_job) | **DELETE** /apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name} | 
[**delete_namespaced_job**](BatchV2alpha1Api.md#delete_namespaced_job) | **DELETE** /apis/batch/v2alpha1/namespaces/{namespace}/jobs/{name} | 
[**delete_namespaced_scheduled_job**](BatchV2alpha1Api.md#delete_namespaced_scheduled_job) | **DELETE** /apis/batch/v2alpha1/namespaces/{namespace}/scheduledjobs/{name} | 
[**get_api_resources**](BatchV2alpha1Api.md#get_api_resources) | **GET** /apis/batch/v2alpha1/ | 
[**list_cron_job_for_all_namespaces**](BatchV2alpha1Api.md#list_cron_job_for_all_namespaces) | **GET** /apis/batch/v2alpha1/cronjobs | 
[**list_job_for_all_namespaces**](BatchV2alpha1Api.md#list_job_for_all_namespaces) | **GET** /apis/batch/v2alpha1/jobs | 
[**list_namespaced_cron_job**](BatchV2alpha1Api.md#list_namespaced_cron_job) | **GET** /apis/batch/v2alpha1/namespaces/{namespace}/cronjobs | 
[**list_namespaced_job**](BatchV2alpha1Api.md#list_namespaced_job) | **GET** /apis/batch/v2alpha1/namespaces/{namespace}/jobs | 
[**list_namespaced_scheduled_job**](BatchV2alpha1Api.md#list_namespaced_scheduled_job) | **GET** /apis/batch/v2alpha1/namespaces/{namespace}/scheduledjobs | 
[**list_scheduled_job_for_all_namespaces**](BatchV2alpha1Api.md#list_scheduled_job_for_all_namespaces) | **GET** /apis/batch/v2alpha1/scheduledjobs | 
[**patch_namespaced_cron_job**](BatchV2alpha1Api.md#patch_namespaced_cron_job) | **PATCH** /apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name} | 
[**patch_namespaced_cron_job_status**](BatchV2alpha1Api.md#patch_namespaced_cron_job_status) | **PATCH** /apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}/status | 
[**patch_namespaced_job**](BatchV2alpha1Api.md#patch_namespaced_job) | **PATCH** /apis/batch/v2alpha1/namespaces/{namespace}/jobs/{name} | 
[**patch_namespaced_job_status**](BatchV2alpha1Api.md#patch_namespaced_job_status) | **PATCH** /apis/batch/v2alpha1/namespaces/{namespace}/jobs/{name}/status | 
[**patch_namespaced_scheduled_job**](BatchV2alpha1Api.md#patch_namespaced_scheduled_job) | **PATCH** /apis/batch/v2alpha1/namespaces/{namespace}/scheduledjobs/{name} | 
[**patch_namespaced_scheduled_job_status**](BatchV2alpha1Api.md#patch_namespaced_scheduled_job_status) | **PATCH** /apis/batch/v2alpha1/namespaces/{namespace}/scheduledjobs/{name}/status | 
[**read_namespaced_cron_job**](BatchV2alpha1Api.md#read_namespaced_cron_job) | **GET** /apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name} | 
[**read_namespaced_cron_job_status**](BatchV2alpha1Api.md#read_namespaced_cron_job_status) | **GET** /apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}/status | 
[**read_namespaced_job**](BatchV2alpha1Api.md#read_namespaced_job) | **GET** /apis/batch/v2alpha1/namespaces/{namespace}/jobs/{name} | 
[**read_namespaced_job_status**](BatchV2alpha1Api.md#read_namespaced_job_status) | **GET** /apis/batch/v2alpha1/namespaces/{namespace}/jobs/{name}/status | 
[**read_namespaced_scheduled_job**](BatchV2alpha1Api.md#read_namespaced_scheduled_job) | **GET** /apis/batch/v2alpha1/namespaces/{namespace}/scheduledjobs/{name} | 
[**read_namespaced_scheduled_job_status**](BatchV2alpha1Api.md#read_namespaced_scheduled_job_status) | **GET** /apis/batch/v2alpha1/namespaces/{namespace}/scheduledjobs/{name}/status | 
[**replace_namespaced_cron_job**](BatchV2alpha1Api.md#replace_namespaced_cron_job) | **PUT** /apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name} | 
[**replace_namespaced_cron_job_status**](BatchV2alpha1Api.md#replace_namespaced_cron_job_status) | **PUT** /apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}/status | 
[**replace_namespaced_job**](BatchV2alpha1Api.md#replace_namespaced_job) | **PUT** /apis/batch/v2alpha1/namespaces/{namespace}/jobs/{name} | 
[**replace_namespaced_job_status**](BatchV2alpha1Api.md#replace_namespaced_job_status) | **PUT** /apis/batch/v2alpha1/namespaces/{namespace}/jobs/{name}/status | 
[**replace_namespaced_scheduled_job**](BatchV2alpha1Api.md#replace_namespaced_scheduled_job) | **PUT** /apis/batch/v2alpha1/namespaces/{namespace}/scheduledjobs/{name} | 
[**replace_namespaced_scheduled_job_status**](BatchV2alpha1Api.md#replace_namespaced_scheduled_job_status) | **PUT** /apis/batch/v2alpha1/namespaces/{namespace}/scheduledjobs/{name}/status | 
[**watch_cron_job_list_for_all_namespaces**](BatchV2alpha1Api.md#watch_cron_job_list_for_all_namespaces) | **GET** /apis/batch/v2alpha1/watch/cronjobs | 
[**watch_job_list_for_all_namespaces**](BatchV2alpha1Api.md#watch_job_list_for_all_namespaces) | **GET** /apis/batch/v2alpha1/watch/jobs | 
[**watch_namespaced_cron_job**](BatchV2alpha1Api.md#watch_namespaced_cron_job) | **GET** /apis/batch/v2alpha1/watch/namespaces/{namespace}/cronjobs/{name} | 
[**watch_namespaced_cron_job_list**](BatchV2alpha1Api.md#watch_namespaced_cron_job_list) | **GET** /apis/batch/v2alpha1/watch/namespaces/{namespace}/cronjobs | 
[**watch_namespaced_job**](BatchV2alpha1Api.md#watch_namespaced_job) | **GET** /apis/batch/v2alpha1/watch/namespaces/{namespace}/jobs/{name} | 
[**watch_namespaced_job_list**](BatchV2alpha1Api.md#watch_namespaced_job_list) | **GET** /apis/batch/v2alpha1/watch/namespaces/{namespace}/jobs | 
[**watch_namespaced_scheduled_job**](BatchV2alpha1Api.md#watch_namespaced_scheduled_job) | **GET** /apis/batch/v2alpha1/watch/namespaces/{namespace}/scheduledjobs/{name} | 
[**watch_namespaced_scheduled_job_list**](BatchV2alpha1Api.md#watch_namespaced_scheduled_job_list) | **GET** /apis/batch/v2alpha1/watch/namespaces/{namespace}/scheduledjobs | 
[**watch_scheduled_job_list_for_all_namespaces**](BatchV2alpha1Api.md#watch_scheduled_job_list_for_all_namespaces) | **GET** /apis/batch/v2alpha1/watch/scheduledjobs | 


# **create_namespaced_cron_job**
> V2alpha1CronJob create_namespaced_cron_job(namespace, body, pretty=pretty)



create a CronJob

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V2alpha1CronJob() # V2alpha1CronJob | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_cron_job(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->create_namespaced_cron_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V2alpha1CronJob**](V2alpha1CronJob.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_job**
> V2alpha1Job create_namespaced_job(namespace, body, pretty=pretty)



create a Job

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V2alpha1Job() # V2alpha1Job | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_job(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->create_namespaced_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V2alpha1Job**](V2alpha1Job.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1Job**](V2alpha1Job.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_scheduled_job**
> V2alpha1CronJob create_namespaced_scheduled_job(namespace, body, pretty=pretty)



create a ScheduledJob

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V2alpha1CronJob() # V2alpha1CronJob | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_scheduled_job(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->create_namespaced_scheduled_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V2alpha1CronJob**](V2alpha1CronJob.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_cron_job**
> UnversionedStatus delete_collection_namespaced_cron_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of CronJob

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_cron_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->delete_collection_namespaced_cron_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_job**
> UnversionedStatus delete_collection_namespaced_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of Job

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->delete_collection_namespaced_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_scheduled_job**
> UnversionedStatus delete_collection_namespaced_scheduled_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of ScheduledJob

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_scheduled_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->delete_collection_namespaced_scheduled_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_cron_job**
> UnversionedStatus delete_namespaced_cron_job(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete a CronJob

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
name = 'name_example' # str | name of the CronJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_namespaced_cron_job(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->delete_namespaced_cron_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_job**
> UnversionedStatus delete_namespaced_job(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete a Job

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
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_namespaced_job(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->delete_namespaced_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_scheduled_job**
> UnversionedStatus delete_namespaced_scheduled_job(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete a ScheduledJob

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
name = 'name_example' # str | name of the ScheduledJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_namespaced_scheduled_job(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->delete_namespaced_scheduled_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ScheduledJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources**
> UnversionedAPIResourceList get_api_resources()



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
    api_response = api_instance.get_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->get_api_resources: %s\n" % e)
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

# **list_cron_job_for_all_namespaces**
> V2alpha1CronJobList list_cron_job_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind CronJob

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
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_cron_job_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->list_cron_job_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V2alpha1CronJobList**](V2alpha1CronJobList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_job_for_all_namespaces**
> V2alpha1JobList list_job_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Job

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
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_job_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->list_job_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V2alpha1JobList**](V2alpha1JobList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_cron_job**
> V2alpha1CronJobList list_namespaced_cron_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind CronJob

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_cron_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->list_namespaced_cron_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V2alpha1CronJobList**](V2alpha1CronJobList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_job**
> V2alpha1JobList list_namespaced_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Job

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->list_namespaced_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V2alpha1JobList**](V2alpha1JobList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_scheduled_job**
> V2alpha1CronJobList list_namespaced_scheduled_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ScheduledJob

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_scheduled_job(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->list_namespaced_scheduled_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V2alpha1CronJobList**](V2alpha1CronJobList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scheduled_job_for_all_namespaces**
> V2alpha1CronJobList list_scheduled_job_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ScheduledJob

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
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_scheduled_job_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->list_scheduled_job_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V2alpha1CronJobList**](V2alpha1CronJobList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_cron_job**
> V2alpha1CronJob patch_namespaced_cron_job(name, namespace, body, pretty=pretty)



partially update the specified CronJob

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
name = 'name_example' # str | name of the CronJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_cron_job(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->patch_namespaced_cron_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_cron_job_status**
> V2alpha1CronJob patch_namespaced_cron_job_status(name, namespace, body, pretty=pretty)



partially update status of the specified CronJob

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
name = 'name_example' # str | name of the CronJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_cron_job_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->patch_namespaced_cron_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_job**
> V2alpha1Job patch_namespaced_job(name, namespace, body, pretty=pretty)



partially update the specified Job

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
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_job(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->patch_namespaced_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1Job**](V2alpha1Job.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_job_status**
> V2alpha1Job patch_namespaced_job_status(name, namespace, body, pretty=pretty)



partially update status of the specified Job

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
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_job_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->patch_namespaced_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1Job**](V2alpha1Job.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_scheduled_job**
> V2alpha1CronJob patch_namespaced_scheduled_job(name, namespace, body, pretty=pretty)



partially update the specified ScheduledJob

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
name = 'name_example' # str | name of the ScheduledJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_scheduled_job(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->patch_namespaced_scheduled_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ScheduledJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_scheduled_job_status**
> V2alpha1CronJob patch_namespaced_scheduled_job_status(name, namespace, body, pretty=pretty)



partially update status of the specified ScheduledJob

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
name = 'name_example' # str | name of the ScheduledJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_scheduled_job_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->patch_namespaced_scheduled_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ScheduledJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_cron_job**
> V2alpha1CronJob read_namespaced_cron_job(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified CronJob

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
name = 'name_example' # str | name of the CronJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_cron_job(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->read_namespaced_cron_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_cron_job_status**
> V2alpha1CronJob read_namespaced_cron_job_status(name, namespace, pretty=pretty)



read status of the specified CronJob

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
name = 'name_example' # str | name of the CronJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_cron_job_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->read_namespaced_cron_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_job**
> V2alpha1Job read_namespaced_job(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified Job

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
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_job(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->read_namespaced_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V2alpha1Job**](V2alpha1Job.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_job_status**
> V2alpha1Job read_namespaced_job_status(name, namespace, pretty=pretty)



read status of the specified Job

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
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_job_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->read_namespaced_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1Job**](V2alpha1Job.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_scheduled_job**
> V2alpha1CronJob read_namespaced_scheduled_job(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified ScheduledJob

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
name = 'name_example' # str | name of the ScheduledJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_scheduled_job(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->read_namespaced_scheduled_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ScheduledJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_scheduled_job_status**
> V2alpha1CronJob read_namespaced_scheduled_job_status(name, namespace, pretty=pretty)



read status of the specified ScheduledJob

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
name = 'name_example' # str | name of the ScheduledJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_scheduled_job_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->read_namespaced_scheduled_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ScheduledJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_cron_job**
> V2alpha1CronJob replace_namespaced_cron_job(name, namespace, body, pretty=pretty)



replace the specified CronJob

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
name = 'name_example' # str | name of the CronJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V2alpha1CronJob() # V2alpha1CronJob | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_cron_job(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->replace_namespaced_cron_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V2alpha1CronJob**](V2alpha1CronJob.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_cron_job_status**
> V2alpha1CronJob replace_namespaced_cron_job_status(name, namespace, body, pretty=pretty)



replace status of the specified CronJob

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
name = 'name_example' # str | name of the CronJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V2alpha1CronJob() # V2alpha1CronJob | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_cron_job_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->replace_namespaced_cron_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V2alpha1CronJob**](V2alpha1CronJob.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_job**
> V2alpha1Job replace_namespaced_job(name, namespace, body, pretty=pretty)



replace the specified Job

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
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V2alpha1Job() # V2alpha1Job | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_job(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->replace_namespaced_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V2alpha1Job**](V2alpha1Job.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1Job**](V2alpha1Job.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_job_status**
> V2alpha1Job replace_namespaced_job_status(name, namespace, body, pretty=pretty)



replace status of the specified Job

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
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V2alpha1Job() # V2alpha1Job | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_job_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->replace_namespaced_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V2alpha1Job**](V2alpha1Job.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1Job**](V2alpha1Job.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_scheduled_job**
> V2alpha1CronJob replace_namespaced_scheduled_job(name, namespace, body, pretty=pretty)



replace the specified ScheduledJob

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
name = 'name_example' # str | name of the ScheduledJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V2alpha1CronJob() # V2alpha1CronJob | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_scheduled_job(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->replace_namespaced_scheduled_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ScheduledJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V2alpha1CronJob**](V2alpha1CronJob.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_scheduled_job_status**
> V2alpha1CronJob replace_namespaced_scheduled_job_status(name, namespace, body, pretty=pretty)



replace status of the specified ScheduledJob

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
name = 'name_example' # str | name of the ScheduledJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = k8sclient.V2alpha1CronJob() # V2alpha1CronJob | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_scheduled_job_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->replace_namespaced_scheduled_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ScheduledJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V2alpha1CronJob**](V2alpha1CronJob.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V2alpha1CronJob**](V2alpha1CronJob.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_cron_job_list_for_all_namespaces**
> VersionedEvent watch_cron_job_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of CronJob

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
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_cron_job_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->watch_cron_job_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_job_list_for_all_namespaces**
> VersionedEvent watch_job_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of Job

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
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_job_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->watch_job_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_cron_job**
> VersionedEvent watch_namespaced_cron_job(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind CronJob

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
name = 'name_example' # str | name of the CronJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_cron_job(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->watch_namespaced_cron_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the CronJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_cron_job_list**
> VersionedEvent watch_namespaced_cron_job_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of CronJob

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_cron_job_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->watch_namespaced_cron_job_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_job**
> VersionedEvent watch_namespaced_job(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind Job

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
name = 'name_example' # str | name of the Job
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_job(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->watch_namespaced_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Job | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_job_list**
> VersionedEvent watch_namespaced_job_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of Job

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_job_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->watch_namespaced_job_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_scheduled_job**
> VersionedEvent watch_namespaced_scheduled_job(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch changes to an object of kind ScheduledJob

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
name = 'name_example' # str | name of the ScheduledJob
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_scheduled_job(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->watch_namespaced_scheduled_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ScheduledJob | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_namespaced_scheduled_job_list**
> VersionedEvent watch_namespaced_scheduled_job_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of ScheduledJob

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
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_namespaced_scheduled_job_list(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->watch_namespaced_scheduled_job_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch_scheduled_job_list_for_all_namespaces**
> VersionedEvent watch_scheduled_job_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



watch individual changes to a list of ScheduledJob

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
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.watch_scheduled_job_list_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BatchV2alpha1Api->watch_scheduled_job_list_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**VersionedEvent**](VersionedEvent.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

