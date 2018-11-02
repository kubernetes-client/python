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

ENV=${VIRTUAL_ENV:-}

if [[ -z ${ENV} ]]; then
    if ! which virtualenv > /dev/null 2>&1; then
      echo "virtualenv is not installed. run: [sudo] pip install virtualenv"
      exit
    fi
fi

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
CLIENT_ROOT="${SCRIPT_ROOT}/../kubernetes"

pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null

pushd "${CLIENT_ROOT}" > /dev/null
CLIENT_ROOT=`pwd`
popd > /dev/null

if [[ -z ${ENV} ]]; then
    echo "--- Creating virtualenv"
    virtualenv "${SCRIPT_ROOT}/.py"

    VIRTUAL_ENV_DISABLE_PROMPT=1; source "${SCRIPT_ROOT}/.py/bin/activate"
    trap "deactivate" EXIT SIGINT

    echo "--- Updating tools"
    pip install --upgrade pycodestyle
    pip install --upgrade autopep8
    pip install --upgrade isort
fi

SAVEIFS=$IFS
trap "IFS=$SAVEIFS" EXIT SIGINT
IFS=,

SOURCES="${SCRIPT_ROOT}/../setup.py,${CLIENT_ROOT}/config/*.py,${CLIENT_ROOT}/watch/*.py,${CLIENT_ROOT}/utils/*.py,${SCRIPT_ROOT}/*.py,${CLIENT_ROOT}/../examples/*.py"

echo "--- applying autopep8"
for SOURCE in $SOURCES; do
    autopep8 -i -a -a $SOURCE
done

echo "--- applying isort"
for SOURCE in $SOURCES; do
    isort -y $SOURCE
done

echo "--- check pycodestyle (all need to be fixed manually)"
set +o errexit
for SOURCE in $SOURCES; do
    pycodestyle $SOURCE
done

if [[ ! -z ${ENV} ]]; then
    if [[ $(git status --porcelain) != "" ]]; then
        cd "${SCRIPT_ROOT}/.."
        git --no-pager diff
        cd "${SCRIPT_ROOT}/../kubernetes/base"
        git --no-pager diff
        exit 1
    fi
fi

echo "---Done."
