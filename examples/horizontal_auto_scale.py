# Copyright 2021 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Script has functions helping:
GET, UPDATE and DELETE for kind :HorizontalPodAutoscaler.
The below class has common functions for HPA referenced
from core_v1_api.py with few tweaks.
"""

from kubernetes import client, config
from kubernetes.client.exceptions import (
    ApiTypeError,
    ApiValueError
)


import six
import os


class KubeExample():
    """
        Helper class with functions allowing CREATE|GET|PATCH|DELETE operations for HorizontalPodAutoscaler # noqa: E501
    """
    def __init__(self, kube_config_file=None):
        """
        Function initializing class with specific config file or it will be picked from
        :param str kube_config_file : kube config file. If None assuming environment var KUBECONFIG is set. # noqa: E501
        """
        self.kube_config_file = kube_config_file
        if kube_config_file:
            config.load_kube_config(kube_config_file)
        else:
            if os.environ.get('KUBECONFIG'):
                config.load_kube_config()
            else:
                print("ERROR: Please set environment variable `KUBECONFIG`")
                quit()

        self.api_client = client.CoreV1Api().api_client

    def create_namespaced_hpa(self, namespace, body, **kwargs):
        """create_namespaced_hpa
        This method makes a synchronous POST HTTP request by default.
        To make an asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_namespaced_hpa(name, namespace, body, async_req=True)  # noqa: E501
        >>> result = thread.get()
        :param async_req bool: execute request asynchronously
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param object body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
        :param str field_manager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
        :param bool force: Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is False.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ***
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        return self.hpa_namespaced_with_http_info('', namespace, body, _request_type='POST', _ignore_params=[], **kwargs)  # noqa: E501

    def get_namespaced_hpa(self, name, namespace, **kwargs):  # noqa: E501
        """get_namespaced_hpa # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespaced_hpa(name, namespace,  async_req=True)
        >>> result = thread.get()
        :param async_req bool: execute request asynchronously
        :param str name: name of the hpa (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
        :param str field_manager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
        :param bool force: Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is False.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ***
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.hpa_namespaced_with_http_info(name=name, namespace=namespace, body=None, _request_type='GET', _ignore_params=['body'], **kwargs)  # noqa: E501

    def patch_namespaced_hpa(self, name, namespace, body, **kwargs):  # noqa: E501
        """patch_namespaced_hpa # noqa: E501

        partially update the specified hpa  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_namespaced_hpa(name, namespace, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str name: name of the hpa (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param object body: (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
        :param str field_manager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
        :param bool force: Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is False.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ***
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        return self.hpa_namespaced_with_http_info(name, namespace, body, _request_type='PATCH', _ignore_params=[], **kwargs)  # noqa: E501

    def delete_namespaced_hpa(self, name, namespace, **kwargs):
        """delete_namespaced_hpa # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_namespaced_hpa(name, namespace,  async_req=True)
        >>> result = thread.get()
        :param async_req bool: execute request asynchronously
        :param str name: name of the hpa (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
        :param str field_manager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
        :param bool force: Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is False.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ***
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.hpa_namespaced_with_http_info(name=name, namespace=namespace, body=None, _request_type='DELETE', _ignore_params=['body'], **kwargs)  # noqa: E501

    def hpa_namespaced_with_http_info(self, name, namespace, body, **kwargs):  # noqa: E501
        """hpa_namespaced_with_http_info  # noqa: E501
        This is a generic method we are using for all requests: CREATE|GET|PATCH|DELETE.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hpa_namespaced_with_http_info(name, namespace, body, request_type='CREATE|GET|PATCH|DELETE',async_req=True)
        >>> result = thread.get()
        :param async_req bool: execute request asynchronously
        :param str name: name of the hpa (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param object body: (required for CREATE|PATCH)
        :param str pretty: If 'true', then the output is pretty printed.
        :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
        :param str field_manager: fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
        :param bool force: Force is going to \"force\" Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is False.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeout
        :param _ignore_params : defaults to []
        :param _request_type: defaults to GET.
        :return: **
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()
        all_params = [
            'name',
            'namespace',
            'body',
            'pretty',
            'dry_run',
            'field_manager',
            'force'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_type',
                '_ignore_params'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method hpa_namespaced_with_http_info" % key
                )
            local_var_params[key] = val

        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                       local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `hpa_namespaced_with_http_info`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                       local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `hpa_namespaced_with_http_info`")  # noqa: E501

        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and 'body' not in local_var_params['_ignore_params'] and ('body' not in local_var_params or  # noqa: E501
                                                                                                            local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `hpa_namespaced_with_http_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'name' in local_var_params:
            path_params['name'] = local_var_params['name']  # noqa: E501
        if 'namespace' in local_var_params:
            path_params['namespace'] = local_var_params['namespace']  # noqa: E501

        query_params = []
        if 'pretty' in local_var_params and local_var_params['pretty'] is not None:  # noqa: E501
            query_params.append(('pretty', local_var_params['pretty']))  # noqa: E501
        if 'dry_run' in local_var_params and local_var_params['dry_run'] is not None:  # noqa: E501
            query_params.append(('dryRun', local_var_params['dry_run']))  # noqa: E501
        if 'field_manager' in local_var_params and local_var_params['field_manager'] is not None:  # noqa: E501
            query_params.append(('fieldManager', local_var_params['field_manager']))  # noqa: E501
        if 'force' in local_var_params and local_var_params['force'] is not None:  # noqa: E501
            query_params.append(('force', local_var_params['force']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/yaml', 'application/vnd.kubernetes.protobuf'])  # noqa: E501

        content_list = ['application/json-patch+json', 'application/merge-patch+json', 'application/strategic-merge-patch+json', 'application/apply-patch+yaml']  # noqa: E501

        if local_var_params['_request_type'] != 'PATCH':
            content_list = content_list + ['application/json', 'application/yaml']  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(content_list)  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501

        return self.api_client.call_api(
            '/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}', local_var_params['_request_type'],  # noqa: E501
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            # response_type='V1Pod',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req', False),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', False),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)


def main():
    kubeEx = KubeExample()
    namespace = "default"
    hpa = "test-hpa"
    """
    Create HPA example
    """
    body_dict = {"apiVersion": "autoscaling/v1",
                 "kind": "HorizontalPodAutoscaler",
                 "metadata": {
                     "name": hpa,
                     "namespace": namespace
                             },
                 "spec": {
                   "scaleTargetRef": {
                       "apiVersion": "apps/v1",
                       "kind": "Deployment",
                       "name": hpa
                                     },
                   "minReplicas": 1,
                   "maxReplicas": 1,
                   "targetCPUUtilizationPercentage": 80
                         }
                 }

    resp_post = None
    try:
        resp_post = kubeEx.create_namespaced_hpa(namespace, body_dict)  # noqa: E501
    except Exception as e:
        resp_post = e

    print("Create HPA Status:", resp_post.status)

    """
     Patching max and min replicas in Horizontal pod autoscaler.
    """
    resp_patch = None
    try:
        resp_patch = kubeEx.patch_namespaced_hpa(hpa, namespace, {"spec": {"maxReplicas": 3, "minReplicas": 3}})  # noqa: E501
    except Exception as e:
        resp_patch = e

    print("Patch HPA Status:", resp_patch.status)

    """
      Getting details of Horizontal pod autoscaler.
    """
    resp_get = kubeEx.get_namespaced_hpa(hpa, namespace)
    print("GET HPA Status:", resp_get.status)
    print(resp_get.read().decode())

    """Delete of Horizontal pod autoscaler.
    """
    resp_del = kubeEx.delete_namespaced_hpa(hpa, namespace)
    print("DELETE HPA Status:", resp_del.status)


if __name__ == '__main__':
    print("In main")
    main()
