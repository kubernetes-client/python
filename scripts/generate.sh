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

if ! which mvn > /dev/null 2>&1; then
  echo "Maven is not installed."
  exit
fi

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
CLIENT_ROOT="${SCRIPT_ROOT}/.."

pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null

pushd "${CLIENT_ROOT}" > /dev/null
CLIENT_ROOT=`pwd`
popd > /dev/null

PACKAGE_NAME=${PACKAGE_NAME:-k8sclient}

if [[ ! -n ${SWAGGER_FILE-} ]]; then
  if [[ ! -n ${KUBE_ROOT-} ]]; then
    echo "\${KUBE_ROOT} variable is not set"
    exit
  fi
  SWAGGER_FILE="${KUBE_ROOT}/api/openapi-spec/swagger.json"
fi

echo "--- Cleaning up previously generated folders"
rm -rf "${CLIENT_ROOT}/${PACKAGE_NAME}"
rm -rf "${CLIENT_ROOT}/docs"
rm -rf "${CLIENT_ROOT}/test"

echo "--- Generating client ..."
mvn -f "${SCRIPT_ROOT}/pom.xml" clean generate-sources -Dgenerator.spec.path="${SWAGGER_FILE}" -Dgenerator.output.path="${CLIENT_ROOT}" -Dgenerator.package.name=${PACKAGE_NAME}

echo "--- Patching generated code..."
cp "${CLIENT_ROOT}/README.md" "${CLIENT_ROOT}/GEN_README.md"
cp "${SCRIPT_ROOT}/ROOT_README.md" "${CLIENT_ROOT}/README.md"
cp "${SCRIPT_ROOT}/LICENSE" "${CLIENT_ROOT}"
rm -rf "${CLIENT_ROOT}/test"
echo "---Done."
