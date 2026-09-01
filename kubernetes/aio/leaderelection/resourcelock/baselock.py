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

from abc import abstractmethod

from kubernetes.aio.leaderelection.leaderelectionrecord import (
    LeaderElectionRecord,
)


class BaseLock:
    def __init__(self, name: str, namespace: str, identity: str) -> None:
        self.name = name
        self.namespace = namespace
        self.identity = str(identity)

    # get returns the election record from a ConfigMap Annotation
    @abstractmethod
    async def get(
        self, name: str, namespace: str
    ) -> tuple[bool, LeaderElectionRecord] | tuple[bool, Exception] | tuple[bool, None]:
        """
        :param name: Name of the configmap object information to get
        :param namespace: Namespace in which the configmap object is to be searched
        :return: 'True, election record' if object found else 'False, exception response'
        """
        ...

    @abstractmethod
    async def create(
        self, name: str, namespace: str, election_record: LeaderElectionRecord
    ) -> bool:
        """
        :param electionRecord: Annotation string
        :param name: Name of the configmap object to be created
        :param namespace: Namespace in which the configmap object is to be created
        :return: 'True' if object is created else 'False' if failed
        """
        ...

    @abstractmethod
    async def update(
        self, name: str, namespace: str, updated_record: LeaderElectionRecord
    ) -> bool:
        """
        :param name: name of the lock to be updated
        :param namespace: namespace the lock is in
        :param updated_record: the updated election record
        :return: True if update is successful False if it fails
        """
        ...
