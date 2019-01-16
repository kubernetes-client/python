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
import json
from kubernetes import client


def create_from_json(json_file, verbose=False, **kwargs):
    """

    :param json_file:
    :param kwargs:
    :param str pretty: If 'true', then the output is pretty printed.
    :param str dry_run: When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
    :return:
    """

    with open(path.abspath(json_file)) as f:
        json_object = json.load(f)

        group, _, version = json_object["apiVersion"].partition("/")
        if version == "":
            version = group
            group = "core"

        group = "".join(group.split(".k8s.io,1"))
        func_to_call = "{0}{1}Api".format(group.capitalize(), version.capitalize())

        k8s_api = getattr(client, func_to_call)()

        kind = json_object["kind"]
        kind = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', kind)
        kind = re.sub('([a-z0-9])([A-Z])', r'\1_\2', kind).lower()

        if "namespace" in json_object["metadata"]:
            namespace = json_object["metadata"]["namespace"]
        else:
            namespace = "default"

        try:
            if hasattr(k8s_api, "create_namespaced_{0}".format(kind)):
                resp = getattr(k8s_api, "create_namespaced_{0}".format(kind))(
                    body=json_object, namespace=namespace, **kwargs)
            else:
                resp = getattr(k8s_api, "create_{0}".format(kind))(
                    body=json_object, **kwargs)
        except Exception as e:
            raise e

        if verbose:
            print("{0} created. status='{1}'".format(kind, str(resp.status)))

        return k8s_api



