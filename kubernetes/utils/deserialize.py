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

import inspect
import json
import re
import sys
from os import path

import yaml
from kubernetes import client


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
    failures = []

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
    # Expect the user to load namespaced objects more often
    if hasattr(k8s_api, "read_namespaced_{0}_with_http_info".format(kind)):
        fnc_lookup = "read_namespaced_{0}_with_http_info".format(kind)
    elif hasattr(k8s_api, "read_{0}_with_http_info".format(kind)):
        fnc_lookup = "read_{0}_with_http_info".format(kind)
    # Try with the create if no read fnc found
    elif hasattr(k8s_api, "create_{0}_with_http_info".format(kind)):
        fnc_lookup = "create_{0}_with_http_info".format(kind)
    else:
        fnc_lookup = None

    info = {
        "group": group,
        "version": version,
        "kind": kind,
        "fcn_to_call": fcn_to_call,
        "fnc_lookup": fnc_lookup,
    }
    if verbose:
        print("Lookup info: {}".format(info))

    if fnc_lookup:
        if hasattr(k8s_api, fnc_lookup):
            fnc_source, fnc_line_num = inspect.getsourcelines(
                getattr(k8s_api, fnc_lookup)
            )

            # Look for response_type parameter in return
            # self.api_client.call_api
            return_line_found = False
            for line in fnc_source:
                # Look for fnc return line
                if "return self.api_client.call_api" in line:
                    return_line_found = True
                # Search for response_type only after fnc return has
                # been found
                if return_line_found:
                    response_type_regex = r"response_type='(\w*)'"
                    m = re.search(response_type_regex, line)
                    if m:
                        # Group 1 is the extracted str we need from
                        # regex
                        # line example: response_type='V1Pod',
                        # we need to extract V1Pod as response_type
                        response_type = m.group(1)
                        # exit loop after first match
                        break
            if verbose:
                print(
                    "Lookup function found: {} in k8s_api: {} response_type: "
                    "{} info: ".format(
                        fnc_lookup,
                        k8s_api,
                        response_type,
                        info))
        else:
            if verbose:
                print(
                    "Lookup function not found: {} in k8s_api: {} response_type: "
                    "{} info: ".format(
                        fnc_lookup,
                        k8s_api,
                        response_type,
                        info))
    else:
        msg = "Failed to find a function to inspect; lookup info: {}".format(
            info)
        raise FailToLoadError(reason=msg)

    return response_type


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
    # If it is a list type, will need to iterate its items
    load_exceptions = []
    obj = None
    if "List" in data["kind"]:
        obj_list = []
        # Could be "List" or "Pod/Service/...List"
        # This is a list type. iterate within its items
        kind = data["kind"].replace("List", "")
        if verbose:
            print("List detected # of items: {}".format(len(data["items"])))
        for item in data["items"]:
            # Mitigate cases when server returns a xxxList object
            # See kubernetes-client/python#586
            if kind is not "":
                item["apiVersion"] = data["apiVersion"]
                item["kind"] = kind
            try:
                obj = load_single_item(item, klass=klass, verbose=verbose)
                obj_list.append(obj)
            except FailToLoadError as load_exception:
                load_exceptions.append(load_exception)

        obj = obj_list

    else:
        try:
            obj = load_single_item(data, klass=klass, verbose=verbose)
        except FailToLoadError as load_exception:
            load_exceptions.append(load_exception)

    # In case we have exceptions waiting for us, raise them
    if load_exceptions:
        raise FailToLoadError(load_exceptions)

    return obj


def load_single_item(data, klass=None, verbose=False):
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
