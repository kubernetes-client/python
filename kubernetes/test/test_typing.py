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

from importlib.resources import files
import unittest

from typing_extensions import assert_type

from kubernetes import client
from kubernetes.aio import client as aio_client


class TestPackageTyping(unittest.TestCase):
    def test_root_package_is_marked_as_typed(self):
        self.assertTrue(files('kubernetes').joinpath('py.typed').is_file())

    def test_synchronous_nested_model_types(self):
        pod = client.V1Pod(status=client.V1PodStatus(container_statuses=[
            client.V1ContainerStatus(
                image='image',
                image_id='image-id',
                name='container',
                ready=True,
                restart_count=0,
                state=client.V1ContainerState(),
            ),
        ]))

        status = assert_type(pod.status, client.V1PodStatus | None)
        assert status is not None
        containers = assert_type(
            status.container_statuses,
            list[client.V1ContainerStatus] | None,
        )
        assert containers is not None
        state = assert_type(
            containers[0].state,
            client.V1ContainerState | None,
        )
        self.assertIsInstance(state, client.V1ContainerState)

    def test_asynchronous_nested_model_types(self):
        pod = aio_client.V1Pod(
            status=aio_client.V1PodStatus(container_statuses=[
                aio_client.V1ContainerStatus(
                    image='image',
                    image_id='image-id',
                    name='container',
                    ready=True,
                    restart_count=0,
                    state=aio_client.V1ContainerState(),
                ),
            ]),
        )

        status = assert_type(pod.status, aio_client.V1PodStatus | None)
        assert status is not None
        containers = assert_type(
            status.container_statuses,
            list[aio_client.V1ContainerStatus] | None,
        )
        assert containers is not None
        state = assert_type(
            containers[0].state,
            aio_client.V1ContainerState | None,
        )
        self.assertIsInstance(state, aio_client.V1ContainerState)
