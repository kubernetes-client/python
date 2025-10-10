# Copyright 2025 The Kubernetes Authors.
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


import os
import re

import yaml
from kubernetes import client
from kubernetes.dynamic.client import DynamicClient

UPPER_FOLLOWED_BY_LOWER_RE = re.compile("(.)([A-Z][a-z]+)")
LOWER_OR_NUM_FOLLOWED_BY_UPPER_RE = re.compile("([a-z0-9])([A-Z])")


def process_from_directory(
        k8s_client,
        yaml_dir=None,
        verbose=False,
        namespace="default",
        apply=False,
        action="create",
        **kwargs):
    """
    Perform an action (create/delete) from files from a directory. Pass True for verbose to
    print confirmation information.

    Input:
    k8s_client: an ApiClient object, initialized with the client args.
    yaml_dir: string. Contains the path to directory.
    verbose: If True, print confirmation from the action.
        Default is False.
    namespace: string. Contains the namespace to process all
        resources inside. The namespace must preexist otherwise
        the resource processing will fail. If the API object in
        the yaml file already contains a namespace definition
        this parameter has no effect.
    apply: bool. If True, use server-side apply for processing resources.
    action: string. The action to perform, either "create" or "delete".

    Available parameters for processing <kind>:
    :param async_req bool
    :param bool include_uninitialized: If true, partially initialized
        resources are included in the response.
    :param str pretty: If 'true', then the output is pretty printed.
    :param str dry_run: When present, indicates that modifications
        should not be persisted. An invalid or unrecognized dryRun
        directive will result in an error response and no further
        processing of the request.
        Valid values are: - All: all dry run stages will be processed

    Returns:
        The list containing the processed kubernetes API objects.

    Raises:
        FailToProcessError which holds list of `client.rest.ApiException`
        instances for each object that failed to process.
    """

    if not yaml_dir:
        raise ValueError("`yaml_dir` argument must be provided")
    elif not os.path.isdir(yaml_dir):
        raise ValueError("`yaml_dir` argument must be a path to directory")

    files = [
        os.path.join(yaml_dir, i)
        for i in os.listdir(yaml_dir)
        if os.path.isfile(os.path.join(yaml_dir, i))
    ]
    if not files:
        raise ValueError("`yaml_dir` contains no files")

    failures = []
    k8s_objects_all = []

    for file in files:
        try:
            k8s_objects = process_from_yaml(
                k8s_client,
                file,
                verbose=verbose,
                namespace=namespace,
                apply=apply,
                action=action,
                **kwargs,
            )
            k8s_objects_all.append(k8s_objects)
        except FailToProcessError as failure:
            failures.extend(failure.api_exceptions)
    if failures:
        raise FailToProcessError(failures)
    return k8s_objects_all


def process_from_yaml(
    k8s_client,
    yaml_file=None,
    yaml_objects=None,
    verbose=False,
    namespace="default",
    apply=False,
    action="create",
    **kwargs,
):
    """
    Perform an action (create/delete) from a yaml file. Pass True for verbose to
    print confirmation information.
    Input:
    yaml_file: string. Contains the path to yaml file.
    k8s_client: an ApiClient object, initialized with the client args.
    yaml_objects: List[dict]. Optional list of YAML objects; used instead
        of reading the `yaml_file`. Default is None.
    verbose: If True, print confirmation from the action.
        Default is False.
    namespace: string. Contains the namespace to process all
        resources inside. The namespace must preexist otherwise
        the resource processing will fail. If the API object in
        the yaml file already contains a namespace definition
        this parameter has no effect.
    apply: bool. If True, use server-side apply for processing resources.
    action: string. The action to perform, either "create" or "delete".

    Available parameters for processing <kind>:
    :param async_req bool
    :param bool include_uninitialized: If true, partially initialized
        resources are included in the response.
    :param str pretty: If 'true', then the output is pretty printed.
    :param str dry_run: When present, indicates that modifications
        should not be persisted. An invalid or unrecognized dryRun
        directive will result in an error response and no further
        processing of the request.
        Valid values are: - All: all dry run stages will be processed

    Returns:
        The processed kubernetes API objects.

    Raises:
        FailToProcessError which holds list of `client.rest.ApiException`
        instances for each object that failed to process.
    """

    def process_with(objects, apply=apply):
        failures = []
        k8s_objects = []
        for yml_document in objects:
            if yml_document is None:
                continue
            try:
                processed = process_from_dict(
                    k8s_client,
                    yml_document,
                    verbose,
                    namespace=namespace,
                    apply=apply,
                    action=action,
                    **kwargs,
                )
                k8s_objects.append(processed)
            except FailToProcessError as failure:
                failures.extend(failure.api_exceptions)
        if failures:
            raise FailToProcessError(failures)
        return k8s_objects

    class Loader(yaml.loader.SafeLoader):
        yaml_implicit_resolvers = yaml.loader.SafeLoader.yaml_implicit_resolvers.copy()
        if "=" in yaml_implicit_resolvers:
            yaml_implicit_resolvers.pop("=")

    if yaml_objects:
        yml_document_all = yaml_objects
        return process_with(yml_document_all)
    elif yaml_file:
        with open(os.path.abspath(yaml_file)) as f:
            yml_document_all = yaml.load_all(f, Loader=Loader)
            return process_with(yml_document_all, apply)
    else:
        raise ValueError(
            "One of `yaml_file` or `yaml_objects` arguments must be provided"
        )


def process_from_dict(
    k8s_client, data, verbose=False, namespace="default", apply=False, action="create", **kwargs
):
    """
    Perform an action (create/delete) from a dictionary containing valid kubernetes
    API object (i.e. List, Service, etc).

    Input:
    k8s_client: an ApiClient object, initialized with the client args.
    data: a dictionary holding valid kubernetes objects
    verbose: If True, print confirmation from the action.
        Default is False.
    namespace: string. Contains the namespace to process all
        resources inside. The namespace must preexist otherwise
        the resource processing will fail. If the API object in
        the yaml file already contains a namespace definition
        this parameter has no effect.
    apply: bool. If True, use server-side apply for processing resources.
    action: string. The action to perform, either "create" or "delete".

    Returns:
        The processed kubernetes API objects.

    Raises:
        FailToProcessError which holds list of `client.rest.ApiException`
        instances for each object that failed to process.
    """
    # If it is a list type, will need to iterate its items
    api_exceptions = []
    k8s_objects = []

    if "List" in data["kind"]:
        # Could be "List" or "Pod/Service/...List"
        # This is a list type. iterate within its items
        kind = data["kind"].replace("List", "")
        for yml_object in data["items"]:
            # Mitigate cases when server returns a xxxList object
            # See kubernetes-client/python#586
            if kind != "":
                yml_object["apiVersion"] = data["apiVersion"]
                yml_object["kind"] = kind
            try:
                processed = process_from_yaml_single_item(
                    k8s_client,
                    yml_object,
                    verbose,
                    namespace=namespace,
                    apply=apply,
                    action=action,
                    **kwargs,
                )
                k8s_objects.append(processed)
            except client.rest.ApiException as api_exception:
                api_exceptions.append(api_exception)
    else:
        # This is a single object. Call the single item method
        try:
            processed = process_from_yaml_single_item(
                k8s_client,
                data,
                verbose,
                namespace=namespace,
                apply=apply,
                action=action,
                **kwargs)
            k8s_objects.append(processed)
        except client.rest.ApiException as api_exception:
            api_exceptions.append(api_exception)

    # In case we have exceptions waiting for us, raise them
    if api_exceptions:
        raise FailToProcessError(api_exceptions)

    return k8s_objects


def process_from_yaml_single_item(
    k8s_client, yml_object, verbose=False, apply=False, action="create", **kwargs
):
    kind = yml_object["kind"]
    if apply is True:
        apply_client = DynamicClient(k8s_client).resources.get(
            api_version=yml_object["apiVersion"], kind=kind
        )
        if action == "create":
            resp = apply_client.server_side_apply(
                body=yml_object, field_manager="python-client", **kwargs
            )
        elif action == "delete":
            name = yml_object["metadata"]["name"]
            resp = apply_client.delete(
                name=name, **kwargs
            )
        if verbose:
            msg = "{0} {1}d.".format(kind, action)
            if hasattr(resp, "status"):
                msg += " status='{0}'".format(str(resp.status))
            print(msg)
        return resp
    group, _, version = yml_object["apiVersion"].partition("/")
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
    k8s_api = getattr(client, fcn_to_call)(k8s_client)
    # Replace CamelCased action_type into snake_case
    kind = UPPER_FOLLOWED_BY_LOWER_RE.sub(r"\1_\2", kind)
    kind = LOWER_OR_NUM_FOLLOWED_BY_UPPER_RE.sub(r"\1_\2", kind).lower()
    # Prepare the arguments for the API call
    api_args = {
        "body": client.V1DeleteOptions(
            propagation_policy="Background",
            grace_period_seconds=5
        ) if action == "delete" else yml_object,
        **kwargs
    }

    if action == "delete":
        name = yml_object["metadata"]["name"]
        api_args["name"] = name

    # Expect the user to process namespaced objects more often
    if hasattr(k8s_api, "{0}_namespaced_{1}".format(action, kind)):
        # Decide which namespace we are going to put the object in,
        # if any
        if "namespace" in yml_object["metadata"]:
            namespace = yml_object["metadata"]["namespace"]
            api_args["namespace"] = namespace
        resp = getattr(k8s_api, "{0}_namespaced_{1}".format(
            action, kind))(**api_args)
    else:
        api_args.pop("namespace", None)
        resp = getattr(k8s_api, "{0}_{1}".format(action, kind))(**api_args)

    if verbose:
        msg = "{0} {1}d.".format(kind, action)
        if hasattr(resp, "status"):
            msg += " status='{0}'".format(str(resp.status))
        print(msg)
    return resp


class FailToProcessError(Exception):
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
                api_exception.reason, api_exception.body
            )
        return msg


def create_from_directory(
    k8s_client, yaml_dir=None, verbose=False, namespace="default", apply=False, **kwargs
):
    """
    Perform an action from files from a directory. Pass True for verbose to
    print confirmation information.

    Input:
    k8s_client: an ApiClient object, initialized with the client args.
    yaml_dir: string. Contains the path to directory.
    verbose: If True, print confirmation from the create action.
        Default is False.
    namespace: string. Contains the namespace to create all
        resources inside. The namespace must preexist otherwise
        the resource creation will fail. If the API object in
        the yaml file already contains a namespace definition
        this parameter has no effect.
    apply: bool. If True, use server-side apply for creating resources.

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

    Returns:
        The list containing the created kubernetes API objects.

    Raises:
        FailToCreateError which holds list of `client.rest.ApiException`
        instances for each object that failed to create.
    """
    return process_from_directory(
        k8s_client,
        yaml_dir,
        verbose=verbose,
        namespace=namespace,
        apply=apply,
        action="create",
        **kwargs,
    )


def create_from_yaml(
        k8s_client,
        yaml_file=None,
        yaml_objects=None,
        verbose=False,
        namespace="default",
        apply=False,
        **kwargs):
    """
    Perform an action from a yaml file. Pass True for verbose to
    print confirmation information.
    Input:
    yaml_file: string. Contains the path to yaml file.
    k8s_client: an ApiClient object, initialized with the client args.
    yaml_objects: List[dict]. Optional list of YAML objects; used instead
        of reading the `yaml_file`. Default is None.
    verbose: If True, print confirmation from the create action.
        Default is False.
    namespace: string. Contains the namespace to create all
        resources inside. The namespace must preexist otherwise
        the resource creation will fail. If the API object in
        the yaml file already contains a namespace definition
        this parameter has no effect.

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

    Returns:
        The created kubernetes API objects.

    Raises:
        FailToCreateError which holds list of `client.rest.ApiException`
        instances for each object that failed to create.
    """
    return process_from_yaml(
        k8s_client,
        yaml_file,
        yaml_objects,
        verbose,
        namespace,
        apply,
        action="create",
        **kwargs)


def create_from_dict(k8s_client, data, verbose=False, namespace='default',
                     **kwargs):
    """
    Perform an action from a dictionary containing valid kubernetes
    API object (i.e. List, Service, etc).

    Input:
    k8s_client: an ApiClient object, initialized with the client args.
    data: a dictionary holding valid kubernetes objects
    verbose: If True, print confirmation from the create action.
        Default is False.
    namespace: string. Contains the namespace to create all
        resources inside. The namespace must preexist otherwise
        the resource creation will fail. If the API object in
        the yaml file already contains a namespace definition
        this parameter has no effect.

    Returns:
        The created kubernetes API objects.

    Raises:
        FailToCreateError which holds list of `client.rest.ApiException`
        instances for each object that failed to create.
    """
    return process_from_dict(k8s_client, data, verbose, namespace, action="create", **kwargs)


class FailToCreateError(FailToProcessError):
    """
    An exception class for handling error if an error occurred when
    handling a yaml file.
    """
