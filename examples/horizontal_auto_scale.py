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
GET, UPDATE and DELETE for kind : HorizontalPodAutoscaler.
The below class has common functions for HPA referenced
from core_v1_api.py with little tweaks.
"""

from kubernetes import client, config
from kubernetes.client.exceptions import (
    ApiTypeError,
    ApiValueError
)


import six


class KubeExample():

    def __init__(self, kube_config_file=None, namespace=None):
        """
        """
        self.kube_config_file = kube_config_file
        self.namespace = namespace
        config.load_kube_config(kube_config_file)
        self.api_client = client.CoreV1Api().api_client

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

    def get_namespaced_hpa(self, name, namespace, **kwargs):  # noqa: E501
        """get_namespaced_hpa # noqa: E501

        partially update the specified hpa  # noqa: E501
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
        return self.hpa_namespaced_with_http_info(name=name, namespace=namespace, body=None, _request_type='GET', _ignore_params=['body'])  # noqa: E501

    def delete_namespaced_hpa(self, name, namespace, **kwargs):  # noqa: E501
        """get_namespaced_hpa # noqa: E501

        partially update the specified hpa  # noqa: E501
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
        return self.hpa_namespaced_with_http_info(name=name, namespace=namespace, body=None, _request_type='DELETE', _ignore_params=['body'])  # noqa: E501

    def hpa_namespaced_with_http_info(self, name, namespace, body, **kwargs):  # noqa: E501
        """patch_namespaced_hpa  # noqa: E501

        partially update the specified hpa  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.hpa_namespaced_with_http_info(name, namespace, body, request_type='GET|PATCH',async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str name: name of the hpa (required)
        :param str namespace: object name and auth scope, such as for teams and projects (required)
        :param object body: (required)
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
                    " to method patch_namespaced_hpa" % key
                )
            local_var_params[key] = val

        del local_var_params['kwargs']
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                       local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `patch_namespaced_hpa`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if self.api_client.client_side_validation and ('namespace' not in local_var_params or  # noqa: E501
                                                       local_var_params['namespace'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `namespace` when calling `patch_namespaced_hpa`")  # noqa: E501

        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and 'body' not in local_var_params['_ignore_params'] and ('body' not in local_var_params or  # noqa: E501
                                                                                                            local_var_params['body'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `body` when calling `patch_namespaced_hpa`")  # noqa: E501

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

        # HTTP header `Content-Type`

        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/merge-patch+json', 'application/strategic-merge-patch+json', 'application/apply-patch+yaml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerToken']  # noqa: E501
        print(local_var_params['_request_type'])

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
    kubeEx = KubeExample(kube_config_file="<kube config file>", namespace="<namespace>")  # noqa: E501
    namespace = "<namespace>"
    hpa = "<hpa>"

    """
     Patching max and min replicas in Horizontal pod autoscaler.
    """
    resp = kubeEx.patch_namespaced_hpa(hpa, namespace, {"spec": {"maxReplicas": 3, "minReplicas": 3}})  # noqa: E501
    print(resp)

    """
      Getting details of Horizontal pod autoscaler.
    """
    resp_get, status, dict = kubeEx.get_namespaced_hpa(hpa, namespace)
    print(resp_get.read().decode())

    """Delete of Horizontal pod autoscaler.
    """
    resp_del = kubeEx.delete_namespaced_hpa(hpa, namespace)
    print(resp_del)


if __name__ == '__main__':

    print("In main")
    main()
