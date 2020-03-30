#!/bin/sh

# Copyright 2020 The Kubernetes Authors.
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

# Script to apply hotfixes after generating the client
# More details: https://github.com/kubernetes-client/python/blob/master/devel/release.md#hot-issues

# Check if working directory is dirty
if [ $(git status --porcelain | wc -l) -gt 0 ]
then
    echo Your working directory is not clean. Please clean your working directory.
    exit 1
fi

# Check if the current branch is a release branch (release-*)
# If it is not a release branch, don't let the patch be applied
GIT_BRANCH=$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')
if ! [[ $GIT_BRANCH =~ .*release-.* ]]; then
    echo Current branch: $GIT_BRANCH
    echo You are not in a release branch, e.g., release-11.0, release-10.0
    echo Please switch to a release branch to run this script.
    exit 1
fi

# Patching commit for custom client behavior
# Ref: https://github.com/kubernetes-client/python/pull/995/commits/9959273625b999ae9a8f0679c4def2ee7d699ede
git cherry-pick -n 9959273625b999ae9a8f0679c4def2ee7d699ede
if [ $? -eq 0 ]
then
    echo Succesfully patched changes for custom client behavior
else
    echo Failed to patch changes for custom client behavior
    git restore --staged .
    exit 1
fi

# Patching commits for enabling from kubernetes import apis
# Ref: https://github.com/kubernetes-client/python/blob/0976d59d6ff206f2f428cabc7a6b7b1144843b2a/kubernetes/client/apis/__init__.py
git cherry-pick -n dee078639b5e848db73232397087a81f1a336510 b3164930dd1789dd66915acd6772f92f512cec47
if [ $? -eq 0 ]
then
    echo Succesfully patched changes for enabling from kubernetes import apis
else
    echo Failed to patch changes for enabling from kubernetes import apis
    git restore --staged .
    exit 1
fi;

# Patching commits for Client Context Manager
# Ref: https://github.com/kubernetes-client/python/pull/1073
git cherry-pick -n 18d21df367bf9ab5554635f5c6d107f2cf2206a5 13dffb897617f87aaaee247095107d7011e002d5
if [ $? -eq 0 ]
then
    echo Succesfully patched changes for Client Context Manager
else
    echo Failed to patch changes for Client Context Manager
    git restore --staged .
    exit 1
fi;

git commit -m "Apply hotfixes"
