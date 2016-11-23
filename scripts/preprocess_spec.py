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


# these four constants are shown as part of this example in []:
# "[watch]Pod[List]" is the deprecated version of "[list]Pod?[watch]=True"
WATCH_OP_PREFIX = "watch"
WATCH_OP_SUFFIX = "List"
LIST_OP_PREFIX = "list"
WATCH_QUERY_PARAM_NAME = "watch"


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


def process_swagger(infile, outfile):
    with open(infile, 'r') as f:
        spec = json.load(f, object_pairs_hook=OrderedDict)

        apply_func_to_spec_operations(spec, strip_tags_from_operation_id)

        operation_ids = {}
        apply_func_to_spec_operations(spec, lambda op, _: operator.setitem(
            operation_ids, op['operationId'], op))

        try:
            apply_func_to_spec_operations(
                spec, remove_watch_operations, operation_ids)
        except PreprocessingException as e:
            print(e.message)

        # TODO: Kubernetes does not set a version for OpenAPI spec yet,
        # remove this when that is fixed.
        spec['info']['version'] = "v1.5.0-beta.1"

        with open(outfile, 'w') as out:
            json.dump(spec, out, sort_keys=False, indent=2,
                      separators=(',', ': '), ensure_ascii=True)


def main():
    if len(sys.argv) < 3:
        print "Usage:\n\tpython %s infile outfile.\n" % sys.argv[0]
        sys.exit(0)
    if not os.path.isfile(sys.argv[1]):
        print "Input file %s does not exist." % sys.argv[1]
    process_swagger(sys.argv[1], sys.argv[2])

main()
