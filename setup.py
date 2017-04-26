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

from setuptools import find_packages, setup

# Do not edit these constants. They will be updated automatically
# by scripts/update-client.sh.
CLIENT_VERSION = "1.0.0"
PACKAGE_NAME = "kubernetes"
DEVELOPMENT_STATUS = "5 - Production/Stable"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "certifi",
    "ipaddress",
    "oauth2client",
    "setuptools",
    "six",
    "urllib3!=1.21",
    "python-dateutil",
    "pyyaml",
    "websocket-client",
]

setup(
    name=PACKAGE_NAME,
    version=CLIENT_VERSION,
    description="Kubernetes python client",
    author_email="",
    author="Kubernetes",
    license="Apache License Version 2.0",
    url="https://github.com/kubernetes-incubator/client-python",
    keywords=["Swagger", "OpenAPI", "Kubernetes"],
    install_requires=REQUIRES,
    packages=['kubernetes', 'kubernetes.client', 'kubernetes.config',
              'kubernetes.watch', 'kubernetes.client.apis',
              'kubernetes.client.models'],
    include_package_data=True,
    long_description="""\
    Python client for kubernetes http://kubernetes.io/
    """,
    classifiers=[
        "Development Status :: %s" % DEVELOPMENT_STATUS,
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
