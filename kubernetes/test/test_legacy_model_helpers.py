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

import json

import pytest

from kubernetes import client
from kubernetes.aio import client as aio_client


@pytest.fixture(params=[client, aio_client], ids=["sync", "asyncio"])
def models(request):
    return request.param


def test_nested_models_keep_legacy_and_wire_field_names(models):
    pod = models.V1Pod(
        api_version="v1",
        metadata=models.V1ObjectMeta(name="example"),
        spec=models.V1PodSpec(
            containers=[models.V1Container(name="app", image="example:v1")],
            service_account_name="worker",
        ),
    )

    legacy = pod.to_dict()
    assert legacy["api_version"] == "v1"
    assert legacy["status"] is None
    assert legacy["spec"]["service_account_name"] == "worker"
    assert legacy["spec"]["containers"][0]["image"] == "example:v1"

    wire = pod.to_dict(serialize=True)
    assert wire["apiVersion"] == "v1"
    assert wire["status"] is None
    assert wire["spec"]["serviceAccountName"] == "worker"

    expected = {
        "apiVersion": "v1",
        "metadata": {"name": "example"},
        "spec": {
            "containers": [{"name": "app", "image": "example:v1"}],
            "serviceAccountName": "worker",
        },
    }
    assert json.loads(pod.to_json()) == expected
    api_client = object.__new__(models.ApiClient)
    assert api_client.sanitize_for_serialization(pod) == expected


def test_inherited_model_keeps_generated_serialization(models):
    class CustomPod(models.V1Pod):
        pass

    pod = CustomPod(api_version="v1")
    assert pod.to_dict()["api_version"] == "v1"
    assert pod.to_dict(serialize=True)["apiVersion"] == "v1"
    assert json.loads(pod.to_json()) == {"apiVersion": "v1"}


def test_nested_to_dict_override_accepts_no_serialize_argument(models):
    class CustomMetadata(models.V1ObjectMeta):
        def to_dict(self):
            return {"customName": self.name}

    pod = models.V1Pod(metadata=CustomMetadata(name="example"))
    assert pod.to_dict()["metadata"] == {"customName": "example"}
    assert pod.to_dict(serialize=True)["metadata"] == {
        "customName": "example",
    }
    assert json.loads(pod.to_json()) == {
        "metadata": {"customName": "example"},
    }


def test_dictionary_values_keep_legacy_conversion(models):
    resource = models.V1JSONSchemaProps(
        properties={"name": models.V1JSONSchemaProps(type="string")},
    )
    assert resource.to_dict()["properties"]["name"]["type"] == "string"
    wire = resource.to_dict(serialize=True)
    assert wire["properties"]["name"]["type"] == "string"
    assert json.loads(resource.to_json()) == {
        "properties": {"name": {"type": "string"}},
    }
