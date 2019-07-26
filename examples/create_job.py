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

from kubernetes import client, config


def main():
    # Fetching and loading Kubernetes Information
    config.load_kube_config()
    # For incluster details
    # config.incluster_kube_config()

    extension = client.BatchV1Api()

    # Volume
    volume = client.V1Volume(
        name="test-volume",
        empty_dir=client.V1EmptyDirVolumeSource(medium=""))

    # Container
    container = client.V1Container(
        name="jobtest",
        image="nginx:1.7.9",
        image_pull_policy="IfNotPresent",
        ports=[client.V1ContainerPort(container_port=80)],
        volume_mounts=[client.V1VolumeMount(
            name=volume.name,
            mount_path="/kube-example"
        )]
    )

    # Init-Container
    init_container = client.V1Container(
        name="init-container",
        image="alpine",
        image_pull_policy="IfNotPresent",
        command=[
            "echo \"Hello World\""
        ],
        volume_mounts=[client.V1VolumeMount(
            name=volume.name,
            mount_path="/kube-example"
        )]
    )

    # Template
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "jobtest"}),
        spec=client.V1PodSpec(
            init_containers=[init_container],
            containers=[container],
            volumes=[volume],
            restart_policy="Never"
        )
    )

    # Spec
    spec_pod = client.V1JobSpec(
        ttl_seconds_after_finished=0,
        template=template
    )

    # job
    job = client.V1Job(
        kind="Job",
        metadata=client.V1ObjectMeta(name="jobtest"),
        spec=spec_pod
    )

    extension.create_namespaced_job(
        namespace="kube-client",
        body=job
    )


if __name__ == "__main__":
    main()
