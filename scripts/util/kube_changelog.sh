#!/bin/bash

# Copyright 2021 The Kubernetes Authors.
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


# Utilities for parsing Kubernetes changelog.

# find_latest_patch_version finds the latest released patch version for the
# given branch.
# We use the version to track what API surface the generated Python client
# cooresponds to, and collect all API change release notes up to that version.
# There is one tricky point: the code generator we use pulls the latest OpenAPI
# spec from the given branch. The spec may contain API changes that aren't
# documented in the Kubernetes release notes. Until the code generator pulls
# the spec from a tag instead of the branch, we can only collect the release
# notes the next time we generate the client.
function util::kube_changelog::find_latest_patch_version {
  local kubernetes_branch=$1

  # trim "release-" prefix
  local version=${kubernetes_branch:8}
  local changelog="/tmp/k8s-changelog-$version.md"
  curl -s -o $changelog "https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-$version.md"
  echo $(grep "v$version" $changelog | head -1 | sed 's/- \[//g' | sed 's/\].*//g')
  rm -f $changelog
}

# get_api_changelog gets the API Change release notes in the given Kubernetes
# branch for all versions newer than the given trim version.
function util::kube_changelog::get_api_changelog {
  local kubernetes_branch="$1"
  local trim_version="$2"

  # trim "release-" prefix
  local version=${kubernetes_branch:8}
  local changelog="/tmp/k8s-changelog-$version.md"
  curl -s -o $changelog "https://raw.githubusercontent.com/kubernetes/kubernetes/master/CHANGELOG/CHANGELOG-$version.md"

  # remove changelog for versions less than or equal to $trim_version
  sed -i "/^# $trim_version$/q" $changelog
  # ignore section titles and empty lines; add "kubernetes/kubernetes" to links; replace newline with liternal "\n"
  release_notes=$(sed -n "/^### API Change/,/^#/{/^#/!p}" $changelog | sed -n "{/^$/!p}" | sed 's/(\[\#/(\[kubernetes\/kubernetes\#/g' | sed ':a;N;$!ba;s/\n/\\n/g')
  rm -f $changelog
  echo "$release_notes"
}
