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

import os

import k8sclient
import k8sutil


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility
    k8sutil.load_kube_config(os.environ["HOME"] + '/.kube/config')

    print("Supported APIs (* is preferred version):")
    print("%-20s %s" %
          ("core", ",".join(k8sclient.CoreApi().get_api_versions().versions)))
    for api in k8sclient.ApisApi().get_api_versions().groups:
        versions = []
        for v in api.versions:
            name = ""
            if v.version == api.preferred_version.version and len(
                    api.versions) > 1:
                name += "*"
            name += v.version
            versions.append(name)
        print("%-20s %s" % (api.name, ",".join(versions)))


if __name__ == '__main__':
    main()
