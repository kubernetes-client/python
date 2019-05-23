from kubernetes import client, config

# Fetching and loading Kubernetes Information
config.load_kube_config()

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
  volume_mounts=[client.V1VolumeMount(name=volume.name, mount_path="/kube-example")]
)

# Init-Container
init_container = client.V1Container(
  name="init-container",
  image="alpine",
  image_pull_policy="IfNotPresent",
  command=[
          "touch kube-test.txt"
          ],
  volume_mounts=[client.V1VolumeMount(name=volume.name, mount_path="/kube-example")]
)

# Template
template = client.V1PodTemplateSpec(
    metadata=client.V1ObjectMeta(labels={"app": "jobtest"}),
    spec=client.V1PodSpec(init_containers=[init_container], containers=[container], volumes=[volume], restart_policy="Never")
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

extension.create_namespaced_job(namespace="kube-client", body=job)


