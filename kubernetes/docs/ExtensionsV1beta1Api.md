# kubernetes.client.ExtensionsV1beta1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_daemon_set**](ExtensionsV1beta1Api.md#create_namespaced_daemon_set) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets | 
[**create_namespaced_deployment**](ExtensionsV1beta1Api.md#create_namespaced_deployment) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/deployments | 
[**create_namespaced_deployment_rollback_rollback**](ExtensionsV1beta1Api.md#create_namespaced_deployment_rollback_rollback) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/rollback | 
[**create_namespaced_ingress**](ExtensionsV1beta1Api.md#create_namespaced_ingress) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses | 
[**create_namespaced_network_policy**](ExtensionsV1beta1Api.md#create_namespaced_network_policy) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies | 
[**create_namespaced_replica_set**](ExtensionsV1beta1Api.md#create_namespaced_replica_set) | **POST** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets | 
[**create_pod_security_policy**](ExtensionsV1beta1Api.md#create_pod_security_policy) | **POST** /apis/extensions/v1beta1/podsecuritypolicies | 
[**create_third_party_resource**](ExtensionsV1beta1Api.md#create_third_party_resource) | **POST** /apis/extensions/v1beta1/thirdpartyresources | 
[**delete_collection_namespaced_daemon_set**](ExtensionsV1beta1Api.md#delete_collection_namespaced_daemon_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets | 
[**delete_collection_namespaced_deployment**](ExtensionsV1beta1Api.md#delete_collection_namespaced_deployment) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/deployments | 
[**delete_collection_namespaced_ingress**](ExtensionsV1beta1Api.md#delete_collection_namespaced_ingress) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses | 
[**delete_collection_namespaced_network_policy**](ExtensionsV1beta1Api.md#delete_collection_namespaced_network_policy) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies | 
[**delete_collection_namespaced_replica_set**](ExtensionsV1beta1Api.md#delete_collection_namespaced_replica_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets | 
[**delete_collection_pod_security_policy**](ExtensionsV1beta1Api.md#delete_collection_pod_security_policy) | **DELETE** /apis/extensions/v1beta1/podsecuritypolicies | 
[**delete_collection_third_party_resource**](ExtensionsV1beta1Api.md#delete_collection_third_party_resource) | **DELETE** /apis/extensions/v1beta1/thirdpartyresources | 
[**delete_namespaced_daemon_set**](ExtensionsV1beta1Api.md#delete_namespaced_daemon_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | 
[**delete_namespaced_deployment**](ExtensionsV1beta1Api.md#delete_namespaced_deployment) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | 
[**delete_namespaced_ingress**](ExtensionsV1beta1Api.md#delete_namespaced_ingress) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | 
[**delete_namespaced_network_policy**](ExtensionsV1beta1Api.md#delete_namespaced_network_policy) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | 
[**delete_namespaced_replica_set**](ExtensionsV1beta1Api.md#delete_namespaced_replica_set) | **DELETE** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | 
[**delete_pod_security_policy**](ExtensionsV1beta1Api.md#delete_pod_security_policy) | **DELETE** /apis/extensions/v1beta1/podsecuritypolicies/{name} | 
[**delete_third_party_resource**](ExtensionsV1beta1Api.md#delete_third_party_resource) | **DELETE** /apis/extensions/v1beta1/thirdpartyresources/{name} | 
[**get_api_resources**](ExtensionsV1beta1Api.md#get_api_resources) | **GET** /apis/extensions/v1beta1/ | 
[**list_daemon_set_for_all_namespaces**](ExtensionsV1beta1Api.md#list_daemon_set_for_all_namespaces) | **GET** /apis/extensions/v1beta1/daemonsets | 
[**list_deployment_for_all_namespaces**](ExtensionsV1beta1Api.md#list_deployment_for_all_namespaces) | **GET** /apis/extensions/v1beta1/deployments | 
[**list_ingress_for_all_namespaces**](ExtensionsV1beta1Api.md#list_ingress_for_all_namespaces) | **GET** /apis/extensions/v1beta1/ingresses | 
[**list_namespaced_daemon_set**](ExtensionsV1beta1Api.md#list_namespaced_daemon_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets | 
[**list_namespaced_deployment**](ExtensionsV1beta1Api.md#list_namespaced_deployment) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments | 
[**list_namespaced_ingress**](ExtensionsV1beta1Api.md#list_namespaced_ingress) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses | 
[**list_namespaced_network_policy**](ExtensionsV1beta1Api.md#list_namespaced_network_policy) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies | 
[**list_namespaced_replica_set**](ExtensionsV1beta1Api.md#list_namespaced_replica_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets | 
[**list_network_policy_for_all_namespaces**](ExtensionsV1beta1Api.md#list_network_policy_for_all_namespaces) | **GET** /apis/extensions/v1beta1/networkpolicies | 
[**list_pod_security_policy**](ExtensionsV1beta1Api.md#list_pod_security_policy) | **GET** /apis/extensions/v1beta1/podsecuritypolicies | 
[**list_replica_set_for_all_namespaces**](ExtensionsV1beta1Api.md#list_replica_set_for_all_namespaces) | **GET** /apis/extensions/v1beta1/replicasets | 
[**list_third_party_resource**](ExtensionsV1beta1Api.md#list_third_party_resource) | **GET** /apis/extensions/v1beta1/thirdpartyresources | 
[**patch_namespaced_daemon_set**](ExtensionsV1beta1Api.md#patch_namespaced_daemon_set) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | 
[**patch_namespaced_daemon_set_status**](ExtensionsV1beta1Api.md#patch_namespaced_daemon_set_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name}/status | 
[**patch_namespaced_deployment**](ExtensionsV1beta1Api.md#patch_namespaced_deployment) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | 
[**patch_namespaced_deployment_status**](ExtensionsV1beta1Api.md#patch_namespaced_deployment_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/status | 
[**patch_namespaced_deployments_scale**](ExtensionsV1beta1Api.md#patch_namespaced_deployments_scale) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/scale | 
[**patch_namespaced_ingress**](ExtensionsV1beta1Api.md#patch_namespaced_ingress) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | 
[**patch_namespaced_ingress_status**](ExtensionsV1beta1Api.md#patch_namespaced_ingress_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name}/status | 
[**patch_namespaced_network_policy**](ExtensionsV1beta1Api.md#patch_namespaced_network_policy) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | 
[**patch_namespaced_replica_set**](ExtensionsV1beta1Api.md#patch_namespaced_replica_set) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | 
[**patch_namespaced_replica_set_status**](ExtensionsV1beta1Api.md#patch_namespaced_replica_set_status) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/status | 
[**patch_namespaced_replicasets_scale**](ExtensionsV1beta1Api.md#patch_namespaced_replicasets_scale) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/scale | 
[**patch_namespaced_replicationcontrollers_scale**](ExtensionsV1beta1Api.md#patch_namespaced_replicationcontrollers_scale) | **PATCH** /apis/extensions/v1beta1/namespaces/{namespace}/replicationcontrollers/{name}/scale | 
[**patch_pod_security_policy**](ExtensionsV1beta1Api.md#patch_pod_security_policy) | **PATCH** /apis/extensions/v1beta1/podsecuritypolicies/{name} | 
[**patch_third_party_resource**](ExtensionsV1beta1Api.md#patch_third_party_resource) | **PATCH** /apis/extensions/v1beta1/thirdpartyresources/{name} | 
[**read_namespaced_daemon_set**](ExtensionsV1beta1Api.md#read_namespaced_daemon_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | 
[**read_namespaced_daemon_set_status**](ExtensionsV1beta1Api.md#read_namespaced_daemon_set_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name}/status | 
[**read_namespaced_deployment**](ExtensionsV1beta1Api.md#read_namespaced_deployment) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | 
[**read_namespaced_deployment_status**](ExtensionsV1beta1Api.md#read_namespaced_deployment_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/status | 
[**read_namespaced_deployments_scale**](ExtensionsV1beta1Api.md#read_namespaced_deployments_scale) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/scale | 
[**read_namespaced_ingress**](ExtensionsV1beta1Api.md#read_namespaced_ingress) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | 
[**read_namespaced_ingress_status**](ExtensionsV1beta1Api.md#read_namespaced_ingress_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name}/status | 
[**read_namespaced_network_policy**](ExtensionsV1beta1Api.md#read_namespaced_network_policy) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | 
[**read_namespaced_replica_set**](ExtensionsV1beta1Api.md#read_namespaced_replica_set) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | 
[**read_namespaced_replica_set_status**](ExtensionsV1beta1Api.md#read_namespaced_replica_set_status) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/status | 
[**read_namespaced_replicasets_scale**](ExtensionsV1beta1Api.md#read_namespaced_replicasets_scale) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/scale | 
[**read_namespaced_replicationcontrollers_scale**](ExtensionsV1beta1Api.md#read_namespaced_replicationcontrollers_scale) | **GET** /apis/extensions/v1beta1/namespaces/{namespace}/replicationcontrollers/{name}/scale | 
[**read_pod_security_policy**](ExtensionsV1beta1Api.md#read_pod_security_policy) | **GET** /apis/extensions/v1beta1/podsecuritypolicies/{name} | 
[**read_third_party_resource**](ExtensionsV1beta1Api.md#read_third_party_resource) | **GET** /apis/extensions/v1beta1/thirdpartyresources/{name} | 
[**replace_namespaced_daemon_set**](ExtensionsV1beta1Api.md#replace_namespaced_daemon_set) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name} | 
[**replace_namespaced_daemon_set_status**](ExtensionsV1beta1Api.md#replace_namespaced_daemon_set_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/daemonsets/{name}/status | 
[**replace_namespaced_deployment**](ExtensionsV1beta1Api.md#replace_namespaced_deployment) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name} | 
[**replace_namespaced_deployment_status**](ExtensionsV1beta1Api.md#replace_namespaced_deployment_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/status | 
[**replace_namespaced_deployments_scale**](ExtensionsV1beta1Api.md#replace_namespaced_deployments_scale) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/deployments/{name}/scale | 
[**replace_namespaced_ingress**](ExtensionsV1beta1Api.md#replace_namespaced_ingress) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name} | 
[**replace_namespaced_ingress_status**](ExtensionsV1beta1Api.md#replace_namespaced_ingress_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/ingresses/{name}/status | 
[**replace_namespaced_network_policy**](ExtensionsV1beta1Api.md#replace_namespaced_network_policy) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/networkpolicies/{name} | 
[**replace_namespaced_replica_set**](ExtensionsV1beta1Api.md#replace_namespaced_replica_set) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name} | 
[**replace_namespaced_replica_set_status**](ExtensionsV1beta1Api.md#replace_namespaced_replica_set_status) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/status | 
[**replace_namespaced_replicasets_scale**](ExtensionsV1beta1Api.md#replace_namespaced_replicasets_scale) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicasets/{name}/scale | 
[**replace_namespaced_replicationcontrollers_scale**](ExtensionsV1beta1Api.md#replace_namespaced_replicationcontrollers_scale) | **PUT** /apis/extensions/v1beta1/namespaces/{namespace}/replicationcontrollers/{name}/scale | 
[**replace_pod_security_policy**](ExtensionsV1beta1Api.md#replace_pod_security_policy) | **PUT** /apis/extensions/v1beta1/podsecuritypolicies/{name} | 
[**replace_third_party_resource**](ExtensionsV1beta1Api.md#replace_third_party_resource) | **PUT** /apis/extensions/v1beta1/thirdpartyresources/{name} | 


# **create_namespaced_daemon_set**
> V1beta1DaemonSet create_namespaced_daemon_set(namespace, body, pretty=pretty)



create a DaemonSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1beta1DaemonSet() # V1beta1DaemonSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_daemon_set(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->create_namespaced_daemon_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1DaemonSet**](V1beta1DaemonSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_deployment**
> ExtensionsV1beta1Deployment create_namespaced_deployment(namespace, body, pretty=pretty)



create a Deployment

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.ExtensionsV1beta1Deployment() # ExtensionsV1beta1Deployment | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_deployment(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->create_namespaced_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**ExtensionsV1beta1Deployment**](ExtensionsV1beta1Deployment.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Deployment**](ExtensionsV1beta1Deployment.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_deployment_rollback_rollback**
> ExtensionsV1beta1DeploymentRollback create_namespaced_deployment_rollback_rollback(name, namespace, body, pretty=pretty)



create rollback of a DeploymentRollback

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the DeploymentRollback
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.ExtensionsV1beta1DeploymentRollback() # ExtensionsV1beta1DeploymentRollback | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_deployment_rollback_rollback(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->create_namespaced_deployment_rollback_rollback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DeploymentRollback | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**ExtensionsV1beta1DeploymentRollback**](ExtensionsV1beta1DeploymentRollback.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1DeploymentRollback**](ExtensionsV1beta1DeploymentRollback.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_ingress**
> V1beta1Ingress create_namespaced_ingress(namespace, body, pretty=pretty)



create an Ingress

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1beta1Ingress() # V1beta1Ingress | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_ingress(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->create_namespaced_ingress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Ingress**](V1beta1Ingress.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_network_policy**
> V1beta1NetworkPolicy create_namespaced_network_policy(namespace, body, pretty=pretty)



create a NetworkPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1beta1NetworkPolicy() # V1beta1NetworkPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_network_policy(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->create_namespaced_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_replica_set**
> V1beta1ReplicaSet create_namespaced_replica_set(namespace, body, pretty=pretty)



create a ReplicaSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1beta1ReplicaSet() # V1beta1ReplicaSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_replica_set(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->create_namespaced_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pod_security_policy**
> V1beta1PodSecurityPolicy create_pod_security_policy(body, pretty=pretty)



create a PodSecurityPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
body = kubernetes.client.V1beta1PodSecurityPolicy() # V1beta1PodSecurityPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_pod_security_policy(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->create_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1PodSecurityPolicy**](V1beta1PodSecurityPolicy.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1PodSecurityPolicy**](V1beta1PodSecurityPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_third_party_resource**
> V1beta1ThirdPartyResource create_third_party_resource(body, pretty=pretty)



create a ThirdPartyResource

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
body = kubernetes.client.V1beta1ThirdPartyResource() # V1beta1ThirdPartyResource | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_third_party_resource(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->create_third_party_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection_namespaced_daemon_set**
> V1Status delete_collection_namespaced_daemon_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of DaemonSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_daemon_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_collection_namespaced_daemon_set: %s\n" % e)
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

# **delete_collection_namespaced_deployment**
> V1Status delete_collection_namespaced_deployment(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of Deployment

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_deployment(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_collection_namespaced_deployment: %s\n" % e)
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

# **delete_collection_namespaced_ingress**
> V1Status delete_collection_namespaced_ingress(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of Ingress

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_ingress(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_collection_namespaced_ingress: %s\n" % e)
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

# **delete_collection_namespaced_network_policy**
> V1Status delete_collection_namespaced_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of NetworkPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_collection_namespaced_network_policy: %s\n" % e)
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

# **delete_collection_namespaced_replica_set**
> V1Status delete_collection_namespaced_replica_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of ReplicaSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_namespaced_replica_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_collection_namespaced_replica_set: %s\n" % e)
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

# **delete_collection_pod_security_policy**
> V1Status delete_collection_pod_security_policy(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of PodSecurityPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_pod_security_policy(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_collection_pod_security_policy: %s\n" % e)
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

# **delete_collection_third_party_resource**
> V1Status delete_collection_third_party_resource(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of ThirdPartyResource

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_collection_third_party_resource(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_collection_third_party_resource: %s\n" % e)
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

# **delete_namespaced_daemon_set**
> V1Status delete_namespaced_daemon_set(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a DaemonSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_namespaced_daemon_set(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_namespaced_daemon_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
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

# **delete_namespaced_deployment**
> V1Status delete_namespaced_deployment(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a Deployment

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_namespaced_deployment(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_namespaced_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
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

# **delete_namespaced_ingress**
> V1Status delete_namespaced_ingress(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete an Ingress

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_namespaced_ingress(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_namespaced_ingress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
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

# **delete_namespaced_network_policy**
> V1Status delete_namespaced_network_policy(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a NetworkPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the NetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_namespaced_network_policy(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_namespaced_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetworkPolicy | 
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

# **delete_namespaced_replica_set**
> V1Status delete_namespaced_replica_set(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a ReplicaSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_namespaced_replica_set(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_namespaced_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
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

# **delete_pod_security_policy**
> V1Status delete_pod_security_policy(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a PodSecurityPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the PodSecurityPolicy
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_pod_security_policy(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodSecurityPolicy | 
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

# **delete_third_party_resource**
> V1Status delete_third_party_resource(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)



delete a ThirdPartyResource

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the ThirdPartyResource
body = kubernetes.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. Either this field or PropagationPolicy may be set, but not both. (optional)
propagation_policy = 'propagation_policy_example' # str | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. (optional)

try: 
    api_response = api_instance.delete_third_party_resource(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents, propagation_policy=propagation_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->delete_third_party_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ThirdPartyResource | 
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
api_instance = kubernetes.client.ExtensionsV1beta1Api()

try: 
    api_response = api_instance.get_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->get_api_resources: %s\n" % e)
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

# **list_daemon_set_for_all_namespaces**
> V1beta1DaemonSetList list_daemon_set_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind DaemonSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_daemon_set_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_daemon_set_for_all_namespaces: %s\n" % e)
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

[**V1beta1DaemonSetList**](V1beta1DaemonSetList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployment_for_all_namespaces**
> ExtensionsV1beta1DeploymentList list_deployment_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Deployment

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_deployment_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_deployment_for_all_namespaces: %s\n" % e)
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

[**ExtensionsV1beta1DeploymentList**](ExtensionsV1beta1DeploymentList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ingress_for_all_namespaces**
> V1beta1IngressList list_ingress_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Ingress

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_ingress_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_ingress_for_all_namespaces: %s\n" % e)
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

[**V1beta1IngressList**](V1beta1IngressList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_daemon_set**
> V1beta1DaemonSetList list_namespaced_daemon_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind DaemonSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_daemon_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_namespaced_daemon_set: %s\n" % e)
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

[**V1beta1DaemonSetList**](V1beta1DaemonSetList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_deployment**
> ExtensionsV1beta1DeploymentList list_namespaced_deployment(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Deployment

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_deployment(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_namespaced_deployment: %s\n" % e)
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

[**ExtensionsV1beta1DeploymentList**](ExtensionsV1beta1DeploymentList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_ingress**
> V1beta1IngressList list_namespaced_ingress(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Ingress

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_ingress(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_namespaced_ingress: %s\n" % e)
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

[**V1beta1IngressList**](V1beta1IngressList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_network_policy**
> V1beta1NetworkPolicyList list_namespaced_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind NetworkPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_namespaced_network_policy: %s\n" % e)
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

[**V1beta1NetworkPolicyList**](V1beta1NetworkPolicyList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_namespaced_replica_set**
> V1beta1ReplicaSetList list_namespaced_replica_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ReplicaSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_namespaced_replica_set(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_namespaced_replica_set: %s\n" % e)
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

[**V1beta1ReplicaSetList**](V1beta1ReplicaSetList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_policy_for_all_namespaces**
> V1beta1NetworkPolicyList list_network_policy_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind NetworkPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_network_policy_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_network_policy_for_all_namespaces: %s\n" % e)
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

[**V1beta1NetworkPolicyList**](V1beta1NetworkPolicyList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pod_security_policy**
> V1beta1PodSecurityPolicyList list_pod_security_policy(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind PodSecurityPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_pod_security_policy(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_pod_security_policy: %s\n" % e)
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

[**V1beta1PodSecurityPolicyList**](V1beta1PodSecurityPolicyList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_replica_set_for_all_namespaces**
> V1beta1ReplicaSetList list_replica_set_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ReplicaSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_replica_set_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_replica_set_for_all_namespaces: %s\n" % e)
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

[**V1beta1ReplicaSetList**](V1beta1ReplicaSetList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_third_party_resource**
> V1beta1ThirdPartyResourceList list_third_party_resource(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ThirdPartyResource

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_third_party_resource(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->list_third_party_resource: %s\n" % e)
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

[**V1beta1ThirdPartyResourceList**](V1beta1ThirdPartyResourceList.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_daemon_set**
> V1beta1DaemonSet patch_namespaced_daemon_set(name, namespace, body, pretty=pretty)



partially update the specified DaemonSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_daemon_set(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_daemon_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_daemon_set_status**
> V1beta1DaemonSet patch_namespaced_daemon_set_status(name, namespace, body, pretty=pretty)



partially update status of the specified DaemonSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_daemon_set_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_daemon_set_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_deployment**
> ExtensionsV1beta1Deployment patch_namespaced_deployment(name, namespace, body, pretty=pretty)



partially update the specified Deployment

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_deployment(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Deployment**](ExtensionsV1beta1Deployment.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_deployment_status**
> ExtensionsV1beta1Deployment patch_namespaced_deployment_status(name, namespace, body, pretty=pretty)



partially update status of the specified Deployment

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_deployment_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_deployment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Deployment**](ExtensionsV1beta1Deployment.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_deployments_scale**
> ExtensionsV1beta1Scale patch_namespaced_deployments_scale(name, namespace, body, pretty=pretty)



partially update scale of the specified Scale

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_deployments_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_deployments_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_ingress**
> V1beta1Ingress patch_namespaced_ingress(name, namespace, body, pretty=pretty)



partially update the specified Ingress

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_ingress(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_ingress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_ingress_status**
> V1beta1Ingress patch_namespaced_ingress_status(name, namespace, body, pretty=pretty)



partially update status of the specified Ingress

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_ingress_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_ingress_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_network_policy**
> V1beta1NetworkPolicy patch_namespaced_network_policy(name, namespace, body, pretty=pretty)



partially update the specified NetworkPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the NetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_network_policy(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetworkPolicy | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_replica_set**
> V1beta1ReplicaSet patch_namespaced_replica_set(name, namespace, body, pretty=pretty)



partially update the specified ReplicaSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_replica_set(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_replica_set_status**
> V1beta1ReplicaSet patch_namespaced_replica_set_status(name, namespace, body, pretty=pretty)



partially update status of the specified ReplicaSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_replica_set_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_replica_set_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_replicasets_scale**
> ExtensionsV1beta1Scale patch_namespaced_replicasets_scale(name, namespace, body, pretty=pretty)



partially update scale of the specified Scale

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_replicasets_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_replicasets_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_namespaced_replicationcontrollers_scale**
> ExtensionsV1beta1Scale patch_namespaced_replicationcontrollers_scale(name, namespace, body, pretty=pretty)



partially update scale of the specified Scale

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_namespaced_replicationcontrollers_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_namespaced_replicationcontrollers_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_pod_security_policy**
> V1beta1PodSecurityPolicy patch_pod_security_policy(name, body, pretty=pretty)



partially update the specified PodSecurityPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the PodSecurityPolicy
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_pod_security_policy(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodSecurityPolicy | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1PodSecurityPolicy**](V1beta1PodSecurityPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_third_party_resource**
> V1beta1ThirdPartyResource patch_third_party_resource(name, body, pretty=pretty)



partially update the specified ThirdPartyResource

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the ThirdPartyResource
body = kubernetes.client.V1Patch() # V1Patch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_third_party_resource(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->patch_third_party_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ThirdPartyResource | 
 **body** | [**V1Patch**](V1Patch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_daemon_set**
> V1beta1DaemonSet read_namespaced_daemon_set(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified DaemonSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_daemon_set(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_daemon_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_daemon_set_status**
> V1beta1DaemonSet read_namespaced_daemon_set_status(name, namespace, pretty=pretty)



read status of the specified DaemonSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_daemon_set_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_daemon_set_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_deployment**
> ExtensionsV1beta1Deployment read_namespaced_deployment(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified Deployment

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_deployment(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**ExtensionsV1beta1Deployment**](ExtensionsV1beta1Deployment.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_deployment_status**
> ExtensionsV1beta1Deployment read_namespaced_deployment_status(name, namespace, pretty=pretty)



read status of the specified Deployment

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_deployment_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_deployment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Deployment**](ExtensionsV1beta1Deployment.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_deployments_scale**
> ExtensionsV1beta1Scale read_namespaced_deployments_scale(name, namespace, pretty=pretty)



read scale of the specified Scale

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_deployments_scale(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_deployments_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_ingress**
> V1beta1Ingress read_namespaced_ingress(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified Ingress

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_ingress(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_ingress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_ingress_status**
> V1beta1Ingress read_namespaced_ingress_status(name, namespace, pretty=pretty)



read status of the specified Ingress

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_ingress_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_ingress_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_network_policy**
> V1beta1NetworkPolicy read_namespaced_network_policy(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified NetworkPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the NetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_network_policy(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetworkPolicy | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_replica_set**
> V1beta1ReplicaSet read_namespaced_replica_set(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified ReplicaSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_namespaced_replica_set(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_replica_set_status**
> V1beta1ReplicaSet read_namespaced_replica_set_status(name, namespace, pretty=pretty)



read status of the specified ReplicaSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_replica_set_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_replica_set_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_replicasets_scale**
> ExtensionsV1beta1Scale read_namespaced_replicasets_scale(name, namespace, pretty=pretty)



read scale of the specified Scale

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_replicasets_scale(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_replicasets_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_namespaced_replicationcontrollers_scale**
> ExtensionsV1beta1Scale read_namespaced_replicationcontrollers_scale(name, namespace, pretty=pretty)



read scale of the specified Scale

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_namespaced_replicationcontrollers_scale(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_namespaced_replicationcontrollers_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_pod_security_policy**
> V1beta1PodSecurityPolicy read_pod_security_policy(name, pretty=pretty, exact=exact, export=export)



read the specified PodSecurityPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the PodSecurityPolicy
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_pod_security_policy(name, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodSecurityPolicy | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1PodSecurityPolicy**](V1beta1PodSecurityPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_third_party_resource**
> V1beta1ThirdPartyResource read_third_party_resource(name, pretty=pretty, exact=exact, export=export)



read the specified ThirdPartyResource

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the ThirdPartyResource
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace'. (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_third_party_resource(name, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->read_third_party_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ThirdPartyResource | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39;. | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_daemon_set**
> V1beta1DaemonSet replace_namespaced_daemon_set(name, namespace, body, pretty=pretty)



replace the specified DaemonSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1beta1DaemonSet() # V1beta1DaemonSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_daemon_set(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_daemon_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1DaemonSet**](V1beta1DaemonSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_daemon_set_status**
> V1beta1DaemonSet replace_namespaced_daemon_set_status(name, namespace, body, pretty=pretty)



replace status of the specified DaemonSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the DaemonSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1beta1DaemonSet() # V1beta1DaemonSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_daemon_set_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_daemon_set_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DaemonSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1DaemonSet**](V1beta1DaemonSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1DaemonSet**](V1beta1DaemonSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_deployment**
> ExtensionsV1beta1Deployment replace_namespaced_deployment(name, namespace, body, pretty=pretty)



replace the specified Deployment

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.ExtensionsV1beta1Deployment() # ExtensionsV1beta1Deployment | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_deployment(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**ExtensionsV1beta1Deployment**](ExtensionsV1beta1Deployment.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Deployment**](ExtensionsV1beta1Deployment.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_deployment_status**
> ExtensionsV1beta1Deployment replace_namespaced_deployment_status(name, namespace, body, pretty=pretty)



replace status of the specified Deployment

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Deployment
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.ExtensionsV1beta1Deployment() # ExtensionsV1beta1Deployment | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_deployment_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_deployment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Deployment | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**ExtensionsV1beta1Deployment**](ExtensionsV1beta1Deployment.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Deployment**](ExtensionsV1beta1Deployment.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_deployments_scale**
> ExtensionsV1beta1Scale replace_namespaced_deployments_scale(name, namespace, body, pretty=pretty)



replace scale of the specified Scale

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.ExtensionsV1beta1Scale() # ExtensionsV1beta1Scale | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_deployments_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_deployments_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_ingress**
> V1beta1Ingress replace_namespaced_ingress(name, namespace, body, pretty=pretty)



replace the specified Ingress

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1beta1Ingress() # V1beta1Ingress | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_ingress(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_ingress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Ingress**](V1beta1Ingress.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_ingress_status**
> V1beta1Ingress replace_namespaced_ingress_status(name, namespace, body, pretty=pretty)



replace status of the specified Ingress

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Ingress
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1beta1Ingress() # V1beta1Ingress | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_ingress_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_ingress_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Ingress | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Ingress**](V1beta1Ingress.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Ingress**](V1beta1Ingress.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_network_policy**
> V1beta1NetworkPolicy replace_namespaced_network_policy(name, namespace, body, pretty=pretty)



replace the specified NetworkPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the NetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1beta1NetworkPolicy() # V1beta1NetworkPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_network_policy(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetworkPolicy | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1NetworkPolicy**](V1beta1NetworkPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replica_set**
> V1beta1ReplicaSet replace_namespaced_replica_set(name, namespace, body, pretty=pretty)



replace the specified ReplicaSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1beta1ReplicaSet() # V1beta1ReplicaSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_replica_set(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_replica_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replica_set_status**
> V1beta1ReplicaSet replace_namespaced_replica_set_status(name, namespace, body, pretty=pretty)



replace status of the specified ReplicaSet

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the ReplicaSet
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.V1beta1ReplicaSet() # V1beta1ReplicaSet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_replica_set_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_replica_set_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ReplicaSet | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ReplicaSet**](V1beta1ReplicaSet.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replicasets_scale**
> ExtensionsV1beta1Scale replace_namespaced_replicasets_scale(name, namespace, body, pretty=pretty)



replace scale of the specified Scale

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.ExtensionsV1beta1Scale() # ExtensionsV1beta1Scale | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_replicasets_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_replicasets_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_namespaced_replicationcontrollers_scale**
> ExtensionsV1beta1Scale replace_namespaced_replicationcontrollers_scale(name, namespace, body, pretty=pretty)



replace scale of the specified Scale

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = kubernetes.client.ExtensionsV1beta1Scale() # ExtensionsV1beta1Scale | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_namespaced_replicationcontrollers_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_namespaced_replicationcontrollers_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**ExtensionsV1beta1Scale**](ExtensionsV1beta1Scale.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_pod_security_policy**
> V1beta1PodSecurityPolicy replace_pod_security_policy(name, body, pretty=pretty)



replace the specified PodSecurityPolicy

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the PodSecurityPolicy
body = kubernetes.client.V1beta1PodSecurityPolicy() # V1beta1PodSecurityPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_pod_security_policy(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_pod_security_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the PodSecurityPolicy | 
 **body** | [**V1beta1PodSecurityPolicy**](V1beta1PodSecurityPolicy.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1PodSecurityPolicy**](V1beta1PodSecurityPolicy.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_third_party_resource**
> V1beta1ThirdPartyResource replace_third_party_resource(name, body, pretty=pretty)



replace the specified ThirdPartyResource

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
api_instance = kubernetes.client.ExtensionsV1beta1Api()
name = 'name_example' # str | name of the ThirdPartyResource
body = kubernetes.client.V1beta1ThirdPartyResource() # V1beta1ThirdPartyResource | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_third_party_resource(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsV1beta1Api->replace_third_party_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ThirdPartyResource | 
 **body** | [**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1ThirdPartyResource**](V1beta1ThirdPartyResource.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

