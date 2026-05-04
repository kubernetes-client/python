# Copyright 2026 The Kubernetes Authors.
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

from setuptools import setup

# Do not edit these constants. They will be updated automatically
# by scripts/update-client.sh.
CLIENT_VERSION = "36.0.0+snapshot"
PACKAGE_NAME = "kubernetes_asyncio"
DEVELOPMENT_STATUS = "3 - Alpha"

# To install the library, run the following
#
# python setup-asyncio.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

with open('requirements-asyncio.txt') as f:
    REQUIRES = f.readlines()

with open('test-requirements-asyncio.txt') as f:
    TESTS_REQUIRES = f.readlines()

setup(
    name=PACKAGE_NAME,
    version=CLIENT_VERSION,
    description="Kubernetes asynchronous python client",
    author_email="",
    author="Kubernetes",
    license="Apache License Version 2.0",
    url="https://github.com/kubernetes-client/kubernetes_asyncio",
    keywords=["Swagger", "OpenAPI", "Kubernetes"],
    install_requires=REQUIRES,
    python_requires=">=3.8",
    tests_require=TESTS_REQUIRES,
    packages=[
        'kubernetes_asyncio',
        'kubernetes_asyncio.client',
        'kubernetes_asyncio.client.api',
        'kubernetes_asyncio.client.models'],
    include_package_data=True,
    long_description="Python asynchronous client for kubernetes http://kubernetes.io/",
    classifiers=[
        "Development Status :: %s" % DEVELOPMENT_STATUS,
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
