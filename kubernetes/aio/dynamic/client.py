# Copyright 2019 The Kubernetes Authors.
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

from kubernetes.aio import watch
from kubernetes.aio.client.rest import ApiException

from .discovery import EagerDiscoverer, LazyDiscoverer
from .exceptions import KubernetesValidateMissing, api_exception
from .resource import (
    Resource, ResourceField, ResourceInstance, ResourceList, Subresource,
)

try:
    import kubernetes_validate
    HAS_KUBERNETES_VALIDATE = True
except ImportError:
    HAS_KUBERNETES_VALIDATE = False

try:
    from kubernetes_validate.utils import VersionNotSupportedError
except ImportError:
    class VersionNotSupportedError(NotImplementedError):
        pass

__all__ = [
    'DynamicClient',
    'ResourceInstance',
    'Resource',
    'ResourceList',
    'Subresource',
    'EagerDiscoverer',
    'LazyDiscoverer',
    'ResourceField',
]


def meta_request(func):
    """ Handles parsing response structure and translating API Exceptions """
    async def inner(self, *args, **kwargs):
        serialize_response = kwargs.pop('serialize', True)
        serializer = kwargs.pop('serializer', ResourceInstance)
        try:
            resp = await func(self, *args, **kwargs)
        except ApiException as e:
            raise api_exception(e)
        if serialize_response:
            try:
                data = await resp.json()
                return serializer(self, data)
            except ValueError:
                data = await resp.json()
                return data
        return resp

    return inner


class DynamicClient(object):
    """ A kubernetes client that dynamically discovers and interacts with
        the kubernetes API
    """

    def __init__(self, client, cache_file=None, discoverer=None):
        self.cache_file = cache_file
        self.client = client
        self.configuration = client.configuration
        self.discoverer = discoverer or LazyDiscoverer

    def __await__(self):
        async def closure():
            self.__discoverer = await self.discoverer(self, self.cache_file)
            return self

        return closure().__await__()

    async def __aenter__(self):
        self.__discoverer = await self.discoverer(self, self.cache_file)
        return self

    async def __aexit__(self, *args, **kwargs):
        return

    @property
    def resources(self):
        return self.__discoverer

    @property
    def version(self):
        return self.__discoverer.version

    @staticmethod
    def ensure_namespace(resource, namespace, body):
        namespace = namespace or body.get('metadata', {}).get('namespace')
        if not namespace:
            raise ValueError("Namespace is required for {}.{}".format(resource.group_version, resource.kind))
        return namespace

    @staticmethod
    def serialize_body(body):
        """Serialize body to raw dict so apiserver can handle it

        :param body: kubernetes resource body, current support: Union[Dict, ResourceInstance]
        """
        # This should match any `ResourceInstance` instances
        if callable(getattr(body, 'to_dict', None)):
            return body.to_dict()
        return body or {}

    async def get(self, resource, name=None, namespace=None, **kwargs):
        path = resource.path(name=name, namespace=namespace)
        return await self.request('get', path, **kwargs)

    async def create(self, resource, body=None, namespace=None, **kwargs):
        body = self.serialize_body(body)
        if resource.namespaced:
            namespace = self.ensure_namespace(resource, namespace, body)
        path = resource.path(namespace=namespace)
        return await self.request('post', path, body=body, **kwargs)

    async def delete(self, resource, name=None, namespace=None, body=None, label_selector=None,
                     field_selector=None, **kwargs):
        if not (name or label_selector or field_selector):
            raise ValueError("At least one of name|label_selector|field_selector is required")
        if resource.namespaced and not (label_selector or field_selector or namespace):
            raise ValueError("At least one of namespace|label_selector|field_selector is required")
        path = resource.path(name=name, namespace=namespace)
        return await self.request('delete', path, body=body, label_selector=label_selector,
                                  field_selector=field_selector, **kwargs)

    async def replace(self, resource, body=None, name=None, namespace=None, **kwargs):
        body = self.serialize_body(body)
        name = name or body.get('metadata', {}).get('name')
        if not name:
            raise ValueError("name is required to replace {}.{}".format(resource.group_version, resource.kind))
        if resource.namespaced:
            namespace = self.ensure_namespace(resource, namespace, body)
        path = resource.path(name=name, namespace=namespace)
        return await self.request('put', path, body=body, **kwargs)

    async def patch(self, resource, body=None, name=None, namespace=None, **kwargs):
        body = self.serialize_body(body)
        name = name or body.get('metadata', {}).get('name')
        if not name:
            raise ValueError("name is required to patch {}.{}".format(resource.group_version, resource.kind))
        if resource.namespaced:
            namespace = self.ensure_namespace(resource, namespace, body)

        content_type = kwargs.pop('content_type', 'application/strategic-merge-patch+json')
        path = resource.path(name=name, namespace=namespace)

        return await self.request('patch', path, body=body, content_type=content_type, **kwargs)

    async def server_side_apply(self, resource, body=None, name=None, namespace=None, force_conflicts=None, **kwargs):
        body = self.serialize_body(body)
        name = name or body.get('metadata', {}).get('name')
        if not name:
            raise ValueError("name is required to patch {}.{}".format(resource.group_version, resource.kind))
        if resource.namespaced:
            namespace = self.ensure_namespace(resource, namespace, body)

        # force content type to 'application/apply-patch+yaml'
        kwargs.update({'content_type': 'application/apply-patch+yaml'})
        path = resource.path(name=name, namespace=namespace)

        return await self.request('patch', path, body=body, force_conflicts=force_conflicts, **kwargs)

    @staticmethod
    async def watch(resource, namespace=None, name=None, label_selector=None, field_selector=None,
                    resource_version=None, timeout=None, watcher=None):
        """
        Stream events for a resource from the Kubernetes API

        :param resource: The API resource object that will be used to query the API
        :param namespace: The namespace to query
        :param name: The name of the resource instance to query
        :param label_selector: The label selector with which to filter results
        :param field_selector: The field selector with which to filter results
        :param resource_version: The version with which to filter results. Only events with
                                 a resource_version greater than this value will be returned
        :param timeout: The amount of time in seconds to wait before terminating the stream
        :param watcher: The Watcher object that will be used to stream the resource

        :return: Event object with these keys:
                   'type': The type of event such as "ADDED", "DELETED", etc.
                   'raw_object': a dict representing the watched object.
                   'object': A ResourceInstance wrapping raw_object.

        Example:
            client = DynamicClient(k8s_client)
            watcher = watch.Watch()
            v1_pods = client.resources.get(api_version='v1', kind='Pod')

            for e in v1_pods.watch(resource_version=0, namespace=default, timeout=5, watcher=watcher):
                print(e['type'])
                print(e['object'].metadata)
                # If you want to gracefully stop the stream watcher
                watcher.stop()
        """
        if not watcher:
            watcher = watch.Watch()

        # Use field selector to query for named instance so the watch parameter is handled properly.
        if name:
            field_selector = f"metadata.name={name}"

        kwargs = {}
        if timeout is not None:
            kwargs['timeout_seconds'] = timeout

        async for event in watcher.stream(
            resource.get,
            namespace=namespace,
            field_selector=field_selector,
            label_selector=label_selector,
            resource_version=resource_version,
            serialize=False,
            **kwargs
        ):
            if event == "":
                break
            event['object'] = ResourceInstance(resource, event['object'])
            yield event

    @meta_request
    async def request(self, method, path, body=None, **params):
        if not path.startswith('/'):
            path = '/' + path

        path_params = params.get('path_params', {})
        query_params = params.get('query_params', [])
        if params.get('pretty') is not None:
            query_params.append(('pretty', params['pretty']))
        if params.get('_continue') is not None:
            query_params.append(('continue', params['_continue']))
        if params.get('include_uninitialized') is not None:
            query_params.append(('includeUninitialized', params['include_uninitialized']))
        if params.get('field_selector') is not None:
            query_params.append(('fieldSelector', params['field_selector']))
        if params.get('label_selector') is not None:
            query_params.append(('labelSelector', params['label_selector']))
        if params.get('limit') is not None:
            query_params.append(('limit', params['limit']))
        if params.get('resource_version') is not None:
            query_params.append(('resourceVersion', params['resource_version']))
        if params.get('timeout_seconds') is not None:
            query_params.append(('timeoutSeconds', params['timeout_seconds']))
        if params.get('watch') is not None:
            query_params.append(('watch', params['watch']))
        if params.get('grace_period_seconds') is not None:
            query_params.append(('gracePeriodSeconds', params['grace_period_seconds']))
        if params.get('propagation_policy') is not None:
            query_params.append(('propagationPolicy', params['propagation_policy']))
        if params.get('orphan_dependents') is not None:
            query_params.append(('orphanDependents', params['orphan_dependents']))
        if params.get('dry_run') is not None:
            query_params.append(('dryRun', params['dry_run']))
        if params.get('field_manager') is not None:
            query_params.append(('fieldManager', params['field_manager']))
        if params.get('force_conflicts') is not None:
            query_params.append(('force', params['force_conflicts']))

        header_params = params.get('header_params', {})
        form_params = []
        local_var_files = {}

        # Checking Accept header.
        new_header_params = dict((key.lower(), value) for key, value in header_params.items())
        if 'accept' not in new_header_params:
            header_params['Accept'] = self.client.select_header_accept([
                'application/json',
                'application/yaml',
            ])

        # HTTP header `Content-Type`
        if params.get('content_type'):
            header_params['Content-Type'] = params['content_type']
        else:
            # Discovery routes require JSON and reject a literal */* with 415:
            # https://github.com/kubernetes/kubernetes/blob/8ba6370120c1371ab70428be16341c3cf6ba8584/staging/src/k8s.io/apiserver/pkg/server/routes/version.go#L40-L49
            header_params['Content-Type'] = 'application/json'

        # Authentication setting
        auth_settings = ['BearerToken']

        # The modern transport accepts a serialized request rather than the
        # removed legacy call_api keyword arguments.
        request = await self.client.param_serialize(
            method.upper(),
            path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=form_params,
            files=local_var_files,
            auth_settings=auth_settings,
        )
        api_response = await self.client.call_api(
            *request,
            _request_timeout=params.get('_request_timeout'),
        )
        if not 200 <= api_response.status <= 299:
            await api_response.read()
            self.client.response_deserialize(api_response, {})
        return api_response.response

    def validate(self, definition, version=None, strict=False):
        """validate checks a kubernetes resource definition

        Args:
            definition (dict): resource definition
            version (str): version of kubernetes to validate against
            strict (bool): whether unexpected additional properties should be considered errors

        Returns:
            warnings (list), errors (list): warnings are missing validations, errors are validation failures
        """
        if not HAS_KUBERNETES_VALIDATE:
            raise KubernetesValidateMissing()

        errors = list()
        warnings = list()
        try:
            if version is None:
                try:
                    version = self.version['kubernetes']['gitVersion']
                except KeyError:
                    version = kubernetes_validate.latest_version()
            kubernetes_validate.validate(definition, version, strict)
        except kubernetes_validate.utils.ValidationError as e:
            errors.append("resource definition validation error at %s: %s" % ('.'.join([str(item) for item in e.path]),
                                                                              e.message))  # noqa: B306
        except VersionNotSupportedError:
            errors.append("Kubernetes version %s is not supported by kubernetes-validate" % version)
        except kubernetes_validate.utils.SchemaNotFoundError as e:
            warnings.append("Could not find schema for object kind %s with API version %s in Kubernetes version %s"
                            " (possibly Custom Resource?)" %
                            (e.kind, e.api_version, e.version))
        return warnings, errors
