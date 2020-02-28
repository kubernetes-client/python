# Copyright 2020 The Kubernetes Authors.
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

import json
import pydoc
import re
import sys
from copy import deepcopy
from os import path

import yaml

from kubernetes import client

PYDOC_RETURN_LABEL = ":return:"


class RespMock(object):
    """
    A dummy class to mock RESTResponse object
    """

    def __init__(self, *args):
        self.data = None


def load_from_json(json_file, klass=None, verbose=False):
    """
    Load objects from json file. Pass True for verbose to
    print additional information.
    Input:
    json_file: string. Contains the path to json file.
    klass: class literal for deserialized object,
    or string of class name.
    verbose: If True, print information about the object lookup info.
        Default is False.

    Raises:
        FailToLoadError which holds list of load failures..
    """
    with open(path.abspath(json_file)) as file:
        data = file.read()
        # python 2 has problems decoding unicode from json.load
        # use yaml.load instead
        if sys.version_info[0] < 3:
            data = yaml.safe_load(data)
        else:
            data = json.loads(data)
        obj = load_from_dict(data, klass=klass, verbose=verbose)

        return obj


def load_from_yaml(yaml_file, klass=None, verbose=False):
    """
    Perform an action from a yaml file. Pass True for verbose to
    print additional information.
    Input:
    yaml_file: string. Contains the path to yaml file.
    klass: class literal for deserialized object,
    or string of class name.
    verbose: If True, print information about the object lookup info.
        Default is False.

    Raises:
        FailToLoadError which holds list of load failures.
    """
    with open(path.abspath(yaml_file)) as f:
        yml_document_all = yaml.safe_load_all(f)
        failures = []
        objs = []
        for yml_document in yml_document_all:
            try:
                obj = load_from_dict(
                    yml_document, klass=klass, verbose=verbose)
                # Prevent returning list of lists when doing multi
                # document yaml
                if isinstance(obj, list):
                    objs.extend(obj)
                else:
                    objs.append(obj)

            except FailToLoadError as failure:
                failures.extend(failure.load_exceptions)

        if objs:
            result = objs if len(objs) > 1 else objs[0]

        if failures:
            raise FailToLoadError(failures)

        return result


def response_type_from_dict(data, verbose=False):
    """
    Helper function to do source code lookup and extract the
    response_type of an kubernetes object.
    Input:
    data: a dictionary holding a valid kubernetes object
    verbose: If True, print confirmation from the create action.
        Default is False.

    Raises:
        FailToLoadError which holds list of load failures.
    """
    response_type = None
    items_kind = None
    failures = []

    if "List" in data["kind"]:
        # Lookup the first item apiVersion
        group, _, version = data["items"][0]["apiVersion"].partition("/")
    else:
        group, _, version = data["apiVersion"].partition("/")
    if version == "":
        version = group
        group = "core"
    # Take care for the case e.g. api_type is "apiextensions.k8s.io"
    # Only replace the last instance
    group = "".join(group.rsplit(".k8s.io", 1))
    # convert group name from DNS subdomain format to
    # python class name convention
    group = "".join(word.capitalize() for word in group.split("."))
    fcn_to_call = "{0}{1}Api".format(group, version.capitalize())
    k8s_api = getattr(client, fcn_to_call)
    # Replace CamelCased action_type into snake_case
    kind = data["kind"]
    kind = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", kind)
    kind = re.sub("([a-z0-9])([A-Z])", r"\1_\2", kind).lower()

    # Expect List of the same kind
    if "List" in data["kind"] and data["items"]:
        # Lookup the first item kind
        items_kind = data["items"][0]["kind"]
        # Replace CamelCased action_type into snake_case
        items_kind = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", items_kind)
        items_kind = re.sub("([a-z0-9])([A-Z])", r"\1_\2", items_kind).lower()
        # Expect the user to load list of namespaced objects more often
        if hasattr(
                k8s_api,
                "list_namespaced_{0}_with_http_info".format(items_kind)):
            fnc_lookup = "list_namespaced_{0}_with_http_info".format(
                items_kind)
        elif hasattr(
            k8s_api, "list_{0}_for_all_namespaces_with_http_info".format(items_kind)
        ):
            fnc_lookup = "list_{0}__for_all_namespaces_with_http_info".format(
                items_kind
            )
        # Try with non-namespaced list
        elif hasattr(k8s_api, "list_{0}_with_http_info".format(items_kind)):
            fnc_lookup = "list_{0}_with_http_info".format(items_kind)
        else:
            fnc_lookup = None
    else:
        # Expect the user to load namespaced objects more often
        if hasattr(k8s_api, "read_namespaced_{0}_with_http_info".format(kind)):
            fnc_lookup = "read_namespaced_{0}_with_http_info".format(kind)
        elif hasattr(k8s_api, "read_{0}_with_http_info".format(kind)):
            fnc_lookup = "read_{0}_with_http_info".format(kind)
        # Try with the get if no read fnc found
        # elif hasattr(k8s_api, "get_{0}_with_http_info".format(kind)):
        #     fnc_lookup = "get_{0}_with_http_info".format(kind)
        else:
            fnc_lookup = None

    info = {
        "group": group,
        "version": version,
        "kind": kind,
        "items_kind": items_kind,
        "fcn_to_call": fcn_to_call,
        "fnc_lookup": fnc_lookup,
    }
    if verbose:
        print("Lookup info: {}".format(info))

    if fnc_lookup:
        if hasattr(k8s_api, fnc_lookup):
            # Get response_type from func pydoc
            response_type = _find_response_type(getattr(k8s_api, fnc_lookup))
            if verbose:
                print(
                    "Lookup function found: {} in k8s_api: {} response_type: "
                    "{} lookup info: {}".format(
                        fnc_lookup, k8s_api, response_type, info
                    )
                )
        else:
            if verbose:
                print(
                    "Lookup function not found: {} in k8s_api: {} "
                    "response_type: {} lookup info: {}".format(
                        fnc_lookup, k8s_api, response_type, info
                    )
                )
    else:
        msg = "Failed to find a function to inspect; lookup info: {}".format(
            info)
        raise FailToLoadError(reason=msg)

    return response_type


def _find_response_type(func):
    for line in pydoc.getdoc(func).splitlines():
        if line.startswith(PYDOC_RETURN_LABEL):
            return line[len(PYDOC_RETURN_LABEL):].strip()
    return ""


def load_from_dict(data, klass=None, verbose=False):
    """
    Load object/objects from a dictionary containing valid kubernetes
    API object (i.e. List, Service, etc).

    Input:
    data: a dictionary holding valid kubernetes objects
    klass: class literal for deserialized object,
    or string of class name.
    verbose: If True, print additional info.
        Default is False.
    Raises:
        FailToLoadError which holds list of load failures.
    """
    load_exceptions = []
    obj = None
    # Check if List has multiple kinds and break it:
    if "List" in data["kind"] and _is_list_multi_kind(data):
        if verbose:
            print(
                "Multi kind list detected kinds: {} items: {}".format(
                    len(_get_list_kinds(data)), len(data["items"])
                )
            )
        kind_lists = []
        for kind_list in _break_list_multi_kind(data):
            try:
                obj = load_single_obj(kind_list, klass=klass, verbose=verbose)
                kind_lists.append(obj)
            except FailToLoadError as load_exception:
                load_exceptions.append(load_exception)

        obj = kind_lists

    else:
        try:
            obj = load_single_obj(data, klass=klass, verbose=verbose)
        except FailToLoadError as load_exception:
            load_exceptions.append(load_exception)

    # In case we have exceptions waiting for us, raise them
    if load_exceptions:
        raise FailToLoadError(load_exceptions)

    return obj


def _is_list_multi_kind(data):
    """
    Helper function to detect if it's a multi-kind list.
    Input:
    data: a dictionary holding a kubernetes object list
    """
    return True if len(_get_list_kinds(data)) > 1 else False


def _get_list_kinds(data):
    """
    Helper function to extract the kinds in a list.
    Input:
    data: a dictionary holding a kubernetes object list
    """
    kinds = []

    # Add kinds in an ordered way:
    for obj in data.get("items"):
        kind = obj.get("kind")
        if kind not in kinds:
            kinds.append(kind)

    return kinds


def _break_list_multi_kind(data):
    """
    Helper function to break a multi kind list into separate
    kind lists.
    Input:
    data: a dictionary holding a multi kind kubernetes object list
    """
    kinds = _get_list_kinds(data)
    new_list = []

    for kind in kinds:
        new_data = deepcopy(data)
        kind_list = list(
            filter(
                lambda obj: obj["kind"] == kind,
                data["items"]))
        new_data["items"] = kind_list
        new_list.append(new_data)

    return new_list


def load_single_obj(data, klass=None, verbose=False):
    """
    Load a single object from a dictionary containing valid kubernetes
    API object (i.e. List, Service, etc).
    Input:
    data: a dictionary holding a valid kubernetes object
    klass: class literal for deserialized object,
    or string of class name.
    verbose: If True, print additional info.
        Default is False.
    """
    # Mock api response from dict
    resp_mock = RespMock()
    resp_mock.data = json.dumps(data)

    # Infer response_type from json data when not provided
    if not klass:
        klass = response_type_from_dict(data, verbose=verbose)
    api_client = client.api_client.ApiClient()
    obj = api_client.deserialize(response=resp_mock, response_type=klass)

    return obj


class FailToLoadError(Exception):
    """
    An exception class for handling error if an error occurred when
    loading a file.
    """

    def __init__(self, load_exceptions=[], reason=""):
        self.load_exceptions = load_exceptions
        self.reason = reason

    def __str__(self):
        msg = self.reason
        if len(self.load_exceptions) > 1:
            msg = "Error loading {} objects".format(len(self.load_exceptions))

        for load_exception in self.load_exceptions:
            msg += " reason: {}".format(load_exception.reason)
        return msg
