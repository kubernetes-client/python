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


def create_from_yaml(
        k8s_client,
        yaml_file,
        verbose=False,
        namespace="default",
        **kwargs):
    """
    Perform an action from a yaml file. Pass True for verbose to
    print confirmation information.
    Input:
    yaml_file: string. Contains the path to yaml file.
    k8s_client: an ApiClient object, initialized with the client args.
    verbose: If True, print confirmation from the create action.
        Default is False.
    namespace: string. Contains the namespace to create all
        resources inside. The namespace must preexist otherwise
        the resource creation will fail. If the API object in
        the yaml file already contains a namespace definition
        this parameter has no effect.

    Returns:
    An k8s api object or list of apis objects created from YAML.
    When a single object is generated, return type is dependent
    on output_list.

    Throws a FailToCreateError exception if creation of any object
    fails with helpful messages from the server.

    Available parameters for creating <kind>:
    :param async_req bool
    :param bool include_uninitialized: If true, partially initialized
        resources are included in the response.
    :param str pretty: If 'true', then the output is pretty printed.
    :param str dry_run: When present, indicates that modifications
        should not be persisted. An invalid or unrecognized dryRun
        directive will result in an error response and no further
        processing of the request.
        Valid values are: - All: all dry run stages will be processed
    """

    with open(path.abspath(yaml_file)) as f:
        yml_document_all = yaml.safe_load_all(f)
        api_exceptions = []
        # Load all documents from a single YAML file
        for yml_document in yml_document_all:
            # If it is a list type, will need to iterate its items
            if "List" in yml_document["kind"]:
                # Could be "List" or "Pod/Service/...List"
                # This is a list type. iterate within its items
                kind = yml_document["kind"].replace("List", "")
                for yml_object in yml_document["items"]:
                    # Mitigate cases when server returns a xxxList object
                    # See kubernetes-client/python#586
                    if kind is not "":
                        yml_object["apiVersion"] = yml_document["apiVersion"]
                        yml_object["kind"] = kind
                    try:
                        create_from_yaml_single_item(
                            k8s_client, yml_object, verbose, namespace, **kwargs)
                    except client.rest.ApiException as api_exception:
                        api_exceptions.append(api_exception)
            else:
                # This is a single object. Call the single item method
                try:
                    create_from_yaml_single_item(
                        k8s_client, yml_document, verbose, namespace, **kwargs)
                except client.rest.ApiException as api_exception:
                    api_exceptions.append(api_exception)
    # In case we have exceptions waiting for us, raise them
    if api_exceptions:
        raise FailToCreateError(api_exceptions)


def create_from_yaml_single_item(
        k8s_client,
        yml_object,
        verbose=False,
        namespace="default",
        **kwargs):
    group, _, version = yml_object["apiVersion"].partition("/")
    if version == "":
        version = group
        group = "core"
    # Take care for the case e.g. api_type is "apiextensions.k8s.io"
    # Only replace the last instance
    group = "".join(group.rsplit(".k8s.io", 1))
    # convert group name from DNS subdomain format to
    # python class name convention
    group = "".join(word.capitalize() for word in group.split('.'))
    fcn_to_call = "{0}{1}Api".format(group, version.capitalize())
    k8s_api = getattr(client, fcn_to_call)(k8s_client)
    # Replace CamelCased action_type into snake_case
    kind = yml_object["kind"]
    kind = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', kind)
    kind = re.sub('([a-z0-9])([A-Z])', r'\1_\2', kind).lower()
    # Decide which namespace we are going to put the object in,
    # if any
    if "namespace" in yml_object["metadata"]:
        namespace = yml_object["metadata"]["namespace"]
    # Expect the user to create namespaced objects more often
    if hasattr(k8s_api, "create_namespaced_{0}".format(kind)):
        resp = getattr(k8s_api, "create_namespaced_{0}".format(kind))(
            body=yml_object, namespace=namespace, **kwargs)
    else:
        resp = getattr(k8s_api, "create_{0}".format(kind))(
            body=yml_object, **kwargs)
    if verbose:
        print("{0} created. status='{1}'".format(kind, str(resp.status)))


class FailToCreateError(Exception):
    """
    An exception class for handling error if an error occurred when
    handling a yaml file.
    """

    def __init__(self, api_exceptions):
        self.api_exceptions = api_exceptions

    def __str__(self):
        msg = ""
        for api_exception in self.api_exceptions:
            msg += "Error from server ({0}): {1}".format(
                api_exception.reason, api_exception.body)
        return msg
