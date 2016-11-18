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
import os.path
import sys
from collections import OrderedDict

_ops = ['get', 'put', 'post', 'delete', 'options', 'head', 'patch']


def _title(s):
    if len(s) == 0:
        return s
    return s[0].upper() + s[1:]


def _to_camel_case(s):
    return ''.join(_title(y) for y in s.split("_"))


def iterate_through_operations(spec, func):
    for k, v in spec['paths'].iteritems():
        for op in _ops:
            if op in v:
                func(v[op])


def process_swagger(infile, outfile):
    with open(infile, 'r') as f:
        spec = json.load(f, object_pairs_hook=OrderedDict)

        def strip_tags_from_operation_id(operation):
            operation_id = operation['operationId']
            for t in operation['tags']:
                operation_id = operation_id.replace(_to_camel_case(t), '')
            operation['operationId'] = operation_id

        iterate_through_operations(spec, strip_tags_from_operation_id)

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
