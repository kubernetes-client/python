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

import sys

# Kubernetes branch to get the OpenAPI spec from.
KUBERNETES_BRANCH = "release-1.30"

# client version for packaging and releasing.
CLIENT_VERSION = "30.0.0+snapshot"

# Name of the release package
PACKAGE_NAME = "kubernetes"

# Stage of development, mainly used in setup.py's classifiers.
DEVELOPMENT_STATUS = "3 - Alpha"


# If called directly, return the constant value given
# its name. Useful in bash scripts.
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python constant.py CONSTANT_NAME")
        sys.exit(1)

    if sys.argv[1] in globals():
        print(globals()[sys.argv[1]])
    else:
        print("Cannot find constant %s" % sys.argv[1])
        sys.exit(1)
