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
import sys
from os import path

import yaml
from six import iteritems

from kubernetes import client


def create_from_yaml(k8s_client, yaml_file, **kwargs):
    """
    Perform an action from a yaml file. Pass True for verbose to
    print confirmation information.
    Input:
    yaml_file: string. Contains the path to yaml file.
    k8s_cline: an ApiClient object, initialized with the client args.

    Available parameters for performing the subsequent action:
    :param async_req bool
    :param bool include_uninitialized: If true, partially initialized resources are included in the response.
    :param str pretty: If 'true', then the output is pretty printed.
    :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    """

    with open(path.abspath(yaml_file)) as f:
        yml_object = list(yaml.safe_load_all(f))

    return create_from_dict(k8s_client, yml_object, **kwargs)


def create_from_dict(k8s_client, k8s_dicts, verbose=False, **kwargs):
    """
    Perform an action from a dict or list of dicts. Pass True for verbose to
    print confirmation information.
    Input:
    k8s_dicts: dictionaries (single or list) to create
    k8s_client: an ApiClient object, initialized with the client args.

    Available parameters for performing the subsequent action:
    :param async_req bool
    :param bool include_uninitialized: If true, partially initialized resources are included in the response.
    :param str pretty: If 'true', then the output is pretty printed.
    :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    """
    if isinstance(k8s_dicts, dict):
        k8s_dicts = [k8s_dicts]

    responses = [
        _create(k8s_client, k8s_dict, verbose=verbose, **kwargs)
        for k8s_dict in k8s_dicts
    ]
    if verbose:
        return responses

    statuses = [
        '%s:%s\n%s\n---\n' % (k8s_dict.get('kind'), k8s_dict.get(
            'metadata', {}).get('name'), resp.status)
        for k8s_dict, resp in zip(k8s_dicts, responses)
    ]
    return ''.join(statuses)


def _create(k8s_client, k8s_dict, verbose=False, **kwargs):
    """
    Perform an action from a dict. Pass True for verbose to
    print confirmation information.
    Input:
    k8s_dict: single dictionary to create
    k8s_client: an ApiClient object, initialized with the client args.

    Available parameters for performing the subsequent action:
    :param async_req bool
    :param bool include_uninitialized: If true, partially initialized resources are included in the response.
    :param str pretty: If 'true', then the output is pretty printed.
    :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    """
    assert isinstance(
        k8s_dict, dict), 'k8s_dict is %s, expected a dict' % (type(k8s_dict))

    group, _, version = k8s_dict["apiVersion"].partition("/")
    if version == "":
        version = group
        group = "core"
    # Take care for the case e.g. api_type is "apiextensions.k8s.io"
    # Only replace the last instance
    group = "".join(group.rsplit(".k8s.io", 1))
    fcn_to_call = "{0}{1}Api".format(group.capitalize(), version.capitalize())
    k8s_api = getattr(client, fcn_to_call)(k8s_client)
    # Replace CamelCased action_type into snake_case
    kind = k8s_dict["kind"]
    kind = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', kind)
    kind = re.sub('([a-z0-9])([A-Z])', r'\1_\2', kind).lower()
    # Decide which namespace we are going to put the object in,
    # if any
    if "namespace" in k8s_dict["metadata"]:
        namespace = k8s_dict["metadata"]["namespace"]
    else:
        namespace = "default"
    # Expect the user to create namespaced objects more often
    if hasattr(k8s_api, "create_namespaced_{0}".format(kind)):
        resp = getattr(k8s_api, "create_namespaced_{0}".format(kind))(
            body=k8s_dict, namespace=namespace, **kwargs)
    else:
        resp = getattr(k8s_api, "create_{0}".format(kind))(
            body=k8s_dict, **kwargs)
    if verbose:
        print("{0} created. status='{1}'".format(kind, str(resp.status)))
    return resp
