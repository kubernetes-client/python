#!/bin/bash

# Copyright 2015 The Kubernetes Authors.
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

# Script to fetch latest swagger spec.
# Puts the updated spec at api/swagger-spec/

set -o errexit
set -o nounset
set -o pipefail

# The openapi-generator version used by this client
export OPENAPI_GENERATOR_COMMIT="v4.3.0"

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
CLIENT_ROOT="${SCRIPT_ROOT}/../kubernetes"
DOC_ROOT="${SCRIPT_ROOT}/../doc"
CLIENT_VERSION=$(python "${SCRIPT_ROOT}/constants.py" CLIENT_VERSION)
PACKAGE_NAME=$(python "${SCRIPT_ROOT}/constants.py" PACKAGE_NAME)
DEVELOPMENT_STATUS=$(python "${SCRIPT_ROOT}/constants.py" DEVELOPMENT_STATUS)

pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null

source ${SCRIPT_ROOT}/util/common.sh
util::common::check_sed

pushd "${CLIENT_ROOT}" > /dev/null
CLIENT_ROOT=`pwd`
popd > /dev/null

TEMP_FOLDER=$(mktemp -d)
trap "rm -rf ${TEMP_FOLDER}" EXIT SIGINT

SETTING_FILE="${TEMP_FOLDER}/settings"
echo "export KUBERNETES_BRANCH=\"$(python ${SCRIPT_ROOT}/constants.py KUBERNETES_BRANCH)\"" > $SETTING_FILE
echo "export CLIENT_VERSION=\"$(python ${SCRIPT_ROOT}/constants.py CLIENT_VERSION)\"" >> $SETTING_FILE
echo "export PACKAGE_NAME=\"client\"" >> $SETTING_FILE

if [[ -z ${GEN_ROOT:-} ]]; then
    GEN_ROOT="${TEMP_FOLDER}/gen"
    echo ">>> Cloning gen repo"
    git clone --recursive https://github.com/kubernetes-client/gen.git "${GEN_ROOT}"
else
    echo ">>> Reusing gen repo at ${GEN_ROOT}"
fi

echo ">>> Running python generator from the gen repo"
"${GEN_ROOT}/openapi/python.sh" "${CLIENT_ROOT}" "${SETTING_FILE}"
mv "${CLIENT_ROOT}/swagger.json" "${SCRIPT_ROOT}/swagger.json"

echo ">>> updating version information..."
sed -i'' "s/^CLIENT_VERSION = .*/CLIENT_VERSION = \\\"${CLIENT_VERSION}\\\"/" "${SCRIPT_ROOT}/../setup.py"
sed -i'' "s/^__version__ = .*/__version__ = \\\"${CLIENT_VERSION}\\\"/" "${CLIENT_ROOT}/__init__.py"
sed -i'' "s/^PACKAGE_NAME = .*/PACKAGE_NAME = \\\"${PACKAGE_NAME}\\\"/" "${SCRIPT_ROOT}/../setup.py"
sed -i'' "s,^DEVELOPMENT_STATUS = .*,DEVELOPMENT_STATUS = \\\"${DEVELOPMENT_STATUS}\\\"," "${SCRIPT_ROOT}/../setup.py"

# This is a terrible hack:
# first, this must be in gen repo not here
# second, this should be ported to swagger-codegen
echo ">>> patching client..."
git apply "${SCRIPT_ROOT}/rest_client_patch.diff"
# The fix this patch is trying to make is already in the upstream swagger-codegen
# repo but it's not in the version we're using. We can remove this patch
# once we upgrade to a version of swagger-codegen that includes it (version>= 6.6.0).
# See https://github.com/OpenAPITools/openapi-generator/pull/15283
git apply "${SCRIPT_ROOT}/rest_sni_patch.diff"
# The following is commented out due to:
# AttributeError: 'RESTResponse' object has no attribute 'headers'
# OpenAPI client generator prior to 6.4.0 uses deprecated urllib3 APIs.
# git apply "${SCRIPT_ROOT}/rest_urllib_headers.diff"

echo ">>> generating docs..."
pushd "${DOC_ROOT}" > /dev/null
make rst
git add -A .
popd > /dev/null

echo ">>> Done."
