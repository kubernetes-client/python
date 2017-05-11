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

import json
import operator
import os.path
import sys
from collections import OrderedDict

import urllib3

from constants import KUBERNETES_BRANCH

# these four constants are shown as part of this example in []:
# "[watch]Pod[List]" is the deprecated version of "[list]Pod?[watch]=True"
WATCH_OP_PREFIX = "watch"
WATCH_OP_SUFFIX = "List"
LIST_OP_PREFIX = "list"
WATCH_QUERY_PARAM_NAME = "watch"

SPEC_URL = 'https://raw.githubusercontent.com/kubernetes/kubernetes/' \
           '%s/api/openapi-spec/swagger.json' % KUBERNETES_BRANCH

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'swagger.json')

_ops = ['get', 'put', 'post', 'delete', 'options', 'head', 'patch']


class PreprocessingException(Exception):
    pass


def _title(s):
    if len(s) == 0:
        return s
    return s[0].upper() + s[1:]


def _to_camel_case(s):
    return ''.join(_title(y) for y in s.split("_"))


def apply_func_to_spec_operations(spec, func, *params):
    """Apply func to each operation in the spec.

    :param spec: The OpenAPI spec to apply func to.
    :param func: the function to apply to the spec's operations. It should be
                 a func(operation, parent) where operation will be each
                 operation of the spec and parent would be the parent object of
                 the given operation.
                 If the return value of the func is True, then the operation
                 will be deleted from the spec.
    """
    for k, v in spec['paths'].iteritems():
        for op in _ops:
            if op not in v:
                continue
            if func(v[op], v, *params):
                del v[op]


def _has_property(prop_list, property_name):
    for prop in prop_list:
        if prop["name"] == property_name:
            return True


def remove_watch_operations(op, parent, operation_ids):
    op_id = op['operationId']
    if not op_id.startswith(WATCH_OP_PREFIX):
        return
    list_id = (LIST_OP_PREFIX +
               op_id.replace(WATCH_OP_SUFFIX, "")[len(WATCH_OP_PREFIX):])
    if list_id not in operation_ids:
        raise PreprocessingException("Cannot find %s" % list_id)
    list_op = operation_ids[list_id]
    params = []
    if 'parameters' in list_op:
        params += list_op['parameters']
    if 'parameters' in parent:
        params += parent['parameters']
    if not _has_property(params, WATCH_QUERY_PARAM_NAME):
        raise PreprocessingException("%s has no watch query param" % list_id)
    return True


def strip_tags_from_operation_id(operation, _):
    operation_id = operation['operationId']
    for t in operation['tags']:
        operation_id = operation_id.replace(_to_camel_case(t), '')
    operation['operationId'] = operation_id


def add_thirdparty_resource_paths(spec):
    with open('thirdpartypaths.json', 'r') as third_party_spec_file:
        third_party_spec = json.loads(third_party_spec_file.read())
    for path in third_party_spec.keys():
        if path not in spec['paths'].keys():
            spec['paths'][path] = third_party_spec[path]
    return spec


def process_swagger(spec):
    spec = add_thirdparty_resource_paths(spec)

    apply_func_to_spec_operations(spec, strip_tags_from_operation_id)

    operation_ids = {}
    apply_func_to_spec_operations(spec, lambda op, _: operator.setitem(
        operation_ids, op['operationId'], op))

    try:
        apply_func_to_spec_operations(
            spec, remove_watch_operations, operation_ids)
    except PreprocessingException as e:
        print(e.message)

    remove_model_prefixes(spec)

    inline_primitive_models(spec)

    return spec


def rename_model(spec, old_name, new_name):
    if new_name in spec['definitions']:
        raise PreprocessingException(
            "Cannot rename model %s. new name %s exists." %
            (old_name, new_name))
    find_rename_ref_recursive(spec,
                              "#/definitions/" + old_name,
                              "#/definitions/" + new_name)
    spec['definitions'][new_name] = spec['definitions'][old_name]
    del spec['definitions'][old_name]


def find_rename_ref_recursive(root, old, new):
    if isinstance(root, list):
        for r in root:
            find_rename_ref_recursive(r, old, new)
    if isinstance(root, dict):
        if "$ref" in root:
            if root["$ref"] == old:
                root["$ref"] = new
        for k, v in root.iteritems():
            find_rename_ref_recursive(v, old, new)


def remove_model_prefixes(spec):
    """Remove full package name from OpenAPI model names.

    Starting kubernetes 1.6, all models has full package name. This is
    verbose and inconvenient in python client. This function tries to remove
    parts of the package name but will make sure there is no conflicting model
    names. This will keep most of the model names generated by previous client
    but will change some of them.
    """
    models = {}
    for k, v in spec['definitions'].iteritems():
        if k.startswith("io.k8s"):
            models[k] = {"split_n": 2}

    conflict = True
    while conflict:
        for k, v in models.iteritems():
            splits = k.rsplit(".", v["split_n"])
            v["removed_prefix"] = splits.pop(0)
            v["new_name"] = ".".join(splits)

        conflict = False
        for k, v in models.iteritems():
            for k2, v2 in models.iteritems():
                if k != k2 and v["new_name"] == v2["new_name"]:
                    v["conflict"] = True
                    v2["conflict"] = True
                    conflict = True

        if conflict:
            for k, v in models.iteritems():
                if "conflict" in v:
                    print("Resolving conflict for %s" % k)
                    v["split_n"] += 1
                    del v["conflict"]

    for k, v in models.iteritems():
        if "new_name" not in v:
            raise PreprocessingException("Cannot rename model %s" % k)
        print("Removing prefix %s from %s...\n" % (v["removed_prefix"], k))
        rename_model(spec, k, v["new_name"])


def find_replace_ref_recursive(root, ref_name, replace_map):
    if isinstance(root, list):
        for r in root:
            find_replace_ref_recursive(r, ref_name, replace_map)
    if isinstance(root, dict):
        if "$ref" in root:
            if root["$ref"] == ref_name:
                del root["$ref"]
                for k, v in replace_map.iteritems():
                    if k in root:
                        if k != "description":
                            raise PreprocessingException(
                                "Cannot inline model %s because of "
                                "conflicting key %s." % (ref_name, k))
                        continue
                    root[k] = v
        for k, v in root.iteritems():
            find_replace_ref_recursive(v, ref_name, replace_map)


def inline_primitive_models(spec):
    to_remove_models = []
    for k, v in spec['definitions'].iteritems():
        if "properties" not in v:
            print("Making primitive mode `%s` inline ..." % k)
            if "type" not in v:
                v["type"] = "object"
            find_replace_ref_recursive(spec, "#/definitions/" + k, v)
            to_remove_models.append(k)

    for k in to_remove_models:
        del spec['definitions'][k]


def main():
    pool = urllib3.PoolManager()
    with pool.request('GET', SPEC_URL, preload_content=False) as response:
        if response.status != 200:
            print "Error downloading spec file. Reason: %s" % response.reason
            return 1
        in_spec = json.load(response, object_pairs_hook=OrderedDict)
        out_spec = process_swagger(in_spec)
        with open(OUTPUT_PATH, 'w') as out:
            json.dump(out_spec, out, sort_keys=False, indent=2,
                      separators=(',', ': '), ensure_ascii=True)
    return 0


sys.exit(main())
