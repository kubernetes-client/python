# Copyright 2018 The Kubernetes Authors.
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


import re
from os import path

import yaml

from kubernetes import client


def create_from_file(k8s_client, yaml_path, verbose=False, **kwargs):
    """
    Perform an action from a yaml file.

    :param k8s_client: an ApiClient object, initialized with the client args
    :yaml_path: the path on the file system to the yaml file
    :type yaml_path: str
    :param verbose: print confimation information
    :type verbose: bool

    Available parameters for performing the subsequent action:
    :param async_req:
    :type async_req: bool
    :param include_uninitialized: include partially initialized resources in
    the response.
    :type include_uninitialized: bool
    :param str pretty: pretty print the output
    :param str dry_run: When present, indicates that modifications should not
    be persisted. An invalid or unrecognized dry_run directive will result in
    an error response and no further processing of the request.
    Valid values are: - All: all dry run stages will be processed
    """
    with open(path.abspath(yaml_path)) as f:
        k8s_api = create_from_yaml(k8s_client, f.read(), verbose=verbose,
                                   **kwargs)

    return k8s_api


def create_from_yaml(k8s_client, yaml_str, verbose=False, **kwargs):
    """
    Perform an action from a yaml string.

    :param k8s_client: an ApiClient object, initialized with the client args
    :yaml_str: a string containing valid yaml or json.
    :type yaml: str
    :param verbose: print confimation information
    :type verbose: bool

    Available parameters for performing the subsequent action:
    :param async_req:
    :type async_req: bool
    :param include_uninitialized: include partially initialized resources in
    the response.
    :type include_uninitialized: bool
    :param str pretty: pretty print the output
    :param str dry_run: When present, indicates that modifications should not
    be persisted. An invalid or unrecognized dry_run directive will result in
    an error response and no further processing of the request.
    Valid values are: - All: all dry run stages will be processed
    """
    stream = yaml.safe_load_all(yaml_str)
    for obj in stream:
        k8s_api = create_from_map(k8s_client, obj, verbose, **kwargs)

    return k8s_api


def create_from_map(k8s_client, yml_object, verbose, **kwargs):
    """
    performe an action from a valid parsed yaml object (as dict).

    :param k8s_client: an ApiClient objcet initialized with the client args
    :yml_object dict: a parsed yaml object
    :param verbose: print confimation information
    :type verbose: bool

    Available parameters for performing the subsequent action:
    :param async_req:
    :type async_req: bool
    :param include_uninitialized: include partially initialized resources in
    the response.
    :type include_uninitialized: bool
    :param str pretty: pretty print the output
    :param str dry_run: When present, indicates that modifications should not
    be persisted. An invalid or unrecognized dry_run directive will result in
    an error response and no further processing of the request.
    Valid values are: - All: all dry run stages will be processed
    """
    group, _, version = yml_object["apiVersion"].partition("/")
    if version == "":
        version = group
        group = "core"
    # Take care for the case e.g. api_type is "apiextensions.k8s.io"
    # Only replace the last instance
    group = "".join(group.rsplit(".k8s.io", 1))
    fcn_to_call = "{0}{1}Api".format(group.capitalize(),
                                     version.capitalize())
    k8s_api = getattr(client, fcn_to_call)(k8s_client)
    # Replace CamelCased action_type into snake_case
    kind = yml_object["kind"]
    kind = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', kind)
    kind = re.sub('([a-z0-9])([A-Z])', r'\1_\2', kind).lower()
    # Decide which namespace we are going to put the object in,
    # if any
    if "namespace" in yml_object["metadata"]:
        namespace = yml_object["metadata"]["namespace"]
    else:
        namespace = "default"
    # Expect the user to create namespaced objects more often
    if hasattr(k8s_api, "create_namespaced_{0}".format(kind)):
        resp = getattr(k8s_api, "create_namespaced_{0}".format(kind))(
             body=yml_object, namespace=namespace, **kwargs)
    else:
        resp = getattr(k8s_api, "create_{0}".format(kind))(
            body=yml_object, **kwargs)
    if verbose:
        print("{0} created. status='{1}'".format(kind, str(resp.status)))
    return k8s_api
