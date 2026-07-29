# Copyright 2016 The Kubernetes Authors.
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

import asyncio
import inspect
import json
import pydoc
from functools import partial
from typing import Any

from kubernetes.aio import client

PYDOC_RETURN_LABEL = ":rtype:"
PYDOC_FOLLOW_PARAM = ":param follow:"

# Removing this suffix from return type name should give us event's object
# type. e.g., if list_namespaces() returns "NamespaceList" type,
# then list_namespaces(watch=true) returns a stream of events with objects
# of type "Namespace". In case this assumption is not true, user should
# provide return_type to Watch class's __init__.
TYPE_LIST_SUFFIX = "List"


def _find_return_type(func):
    return_type = inspect.signature(func).return_annotation
    if (
        return_type is not inspect.Signature.empty
        and return_type is not Any
        and inspect.isclass(return_type)
    ):
        return return_type
    if (
        isinstance(return_type, str)
        and hasattr(client.models, return_type)
    ):
        return return_type
    for line in (pydoc.getdoc(func) or '').splitlines():
        if line.startswith(PYDOC_RETURN_LABEL):
            return line[len(PYDOC_RETURN_LABEL):].strip()
    return ""


class Stream(object):

    def __init__(self, func, *args, **kwargs):
        pass


class Watch(object):

    def __init__(self, return_type=None):
        self._raw_return_type = return_type
        self._stop = False
        self._api_client = client.ApiClient()
        self.resource_version = None
        self.resp = None

    def stop(self):
        self._stop = True

    def get_return_type(self, func):
        if self._raw_return_type:
            return self._raw_return_type
        return_type = _find_return_type(func)
        return_type_name = (
            return_type if isinstance(return_type, str) else return_type.__name__
        )
        if return_type_name.endswith(TYPE_LIST_SUFFIX):
            item_type_name = return_type_name[:-len(TYPE_LIST_SUFFIX)]
            if isinstance(return_type, str):
                return item_type_name
            return getattr(client.models, item_type_name)
        return return_type

    def get_watch_argument_name(self, func):
        if PYDOC_FOLLOW_PARAM in pydoc.getdoc(func):
            return 'follow'
        else:
            return 'watch'

    def unmarshal_event(self, data: str, response_type):
        """Return the K8s response `data` in JSON format.

        """
        try:
            js = json.loads(data)
        except ValueError:
            return data

        if 'object' not in js or 'type' not in js:
            # raise error with code if set
            if 'code' in js:
                reason = "{}: {}".format(js.get('reason'), js.get('message'))
                raise client.exceptions.ApiException(status=js['code'], reason=reason)

            raise Exception(("Malformed JSON response, the 'object' and/or "
                             "'type' field is missing. JSON: {}").format(js))
        # Make a copy of the original object and save it under the
        # `raw_object` key because we will replace the data under `object` with
        # a Python native type shortly.
        js['raw_object'] = js['object']

        # Something went wrong. A typical example would be that the user
        # supplied a resource version that was too old. In that case K8s would
        # not send a conventional ADDED/DELETED/... event but an error. Turn
        # this error into a Python exception to save the user the hassle.
        if js['type'].lower() == 'error':
            obj = js['raw_object']
            reason = "{}: {}".format(obj['reason'], obj['message'])
            raise client.exceptions.ApiException(status=obj['code'], reason=reason)

        if js['type'].lower() != 'bookmark':
            # If possible, compile the JSON response into a Python native response
            # type, eg `V1Namespace` or `V1Pod`,`ExtensionsV1beta1Deployment`, ...
            if response_type:
                js['object'] = self._api_client.deserialize(
                    response_text=json.dumps(js['raw_object']),
                    response_type=response_type,
                    content_type='application/json',
                )

            # decode and save resource_version to continue watching
            if hasattr(js['object'], 'metadata'):
                self.resource_version = js['object'].metadata.resource_version

            # For custom objects that we don't have model defined, json
            # deserialization results in dictionary
            elif (isinstance(js['object'], dict)
                    and 'metadata' in js['object']
                    and 'resourceVersion' in js['object']['metadata']):
                self.resource_version = js['object']['metadata']['resourceVersion']

        elif js['type'].lower() == 'bookmark':
            if (isinstance(js['raw_object'], dict)
                    and 'metadata' in js['raw_object']
                    and 'resourceVersion' in js['raw_object']['metadata']):
                self.resource_version = js['raw_object']['metadata']['resourceVersion']
            else:
                raise Exception(("Malformed JSON response for bookmark event, "
                                 "'metadata' or 'resourceVersion' field is missing. "
                                 "JSON: {}").format(js))

        return js

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            return await self.next()
        except:  # noqa: E722
            await self.close()
            raise

    def _reconnect(self):
        self.resp.close()
        self.resp = None
        if self.resource_version:
            self.func.keywords['resource_version'] = self.resource_version

    async def next(self):

        watch_forever = 'timeout_seconds' not in self.func.keywords
        retry_410 = watch_forever

        while 1:

            # Set the response object to the user supplied function (eg
            # `list_namespaced_pods`) if this is the first iteration.
            if self.resp is None:
                self.resp = await self.func()

            # Abort at the current iteration if the user has called `stop` on this
            # stream instance.
            if self._stop:
                raise StopAsyncIteration

            # Fetch the next K8s response.
            try:
                line = await self.resp.content.readline()
            except asyncio.TimeoutError:
                # This exception can be raised by aiohttp (client timeout)
                # but we don't retry if server side timeout is applied.
                if watch_forever:
                    self._reconnect()
                    continue
                else:
                    raise

            line = line.decode('utf8')

            # Special case for faster log streaming
            if self.return_type == 'str':
                if line == '':
                    # end of log
                    raise StopAsyncIteration
                return line

            # Stop the iterator if K8s sends an empty response. This happens when
            # eg the supplied timeout has expired.
            if line == '':
                if watch_forever:
                    self._reconnect()
                    continue
                raise StopAsyncIteration

            # retry 410 error only once
            try:
                event = self.unmarshal_event(line, self.return_type)
            except client.exceptions.ApiException as ex:
                if ex.status == 410 and retry_410:
                    retry_410 = False  # retry only once
                    self._reconnect()
                    continue
                raise
            retry_410 = watch_forever
            return event

    def stream(self, func, *args, **kwargs):
        """Watch an API resource and stream the result back via a generator.

        :param func: The API function pointer. Any parameter to the function
                     can be passed after this parameter.

        :return: Event object with these keys:
                   'type': The type of event such as "ADDED", "DELETED", etc.
                   'raw_object': a dict representing the watched object.
                   'object': A model representation of raw_object. The name of
                             model will be determined based on
                             the func's doc string. If it cannot be determined,
                             'object' value will be the same as 'raw_object'.

        Example:
            v1 = kubernetes.aio.client.CoreV1Api()
            watch = kubernetes.aio.watch.Watch()
            async for e in watch.stream(v1.list_namespace, timeout_seconds=10):
                type = e['type']
                object = e['object']  # object is one of type return_type
                raw_object = e['raw_object']  # raw_object is a dict
                ...
                if should_stop:
                    watch.stop()
        """
        self._stop = False
        self.return_type = self.get_return_type(func)
        kwargs[self.get_watch_argument_name(func)] = True
        if inspect.ismethod(func):
            raw_func = getattr(
                func.__self__,
                f'{func.__name__}_without_preload_content',
                None,
            )
            if raw_func is not None:
                func = raw_func
            else:
                kwargs['_preload_content'] = False
        else:
            kwargs['_preload_content'] = False
        if 'resource_version' in kwargs:
            self.resource_version = kwargs['resource_version']

        self.func = partial(func, *args, **kwargs)

        return self

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.close()

    async def close(self):
        await self._api_client.close()
        if self.resp is not None:
            self.resp.release()
            self.resp = None
