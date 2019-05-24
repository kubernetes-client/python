"""Example for Post Start Hook """

from kubernetes import client, config

# Fetching and loading Kubernetes Information
config.load_kube_config()

extension = client.ExtensionsV1beta1Api()

# Container
container = client.V1Container(
  name="hooktest",
  image="nginx:1.7.9",
  image_pull_policy="IfNotPresent",
  ports=[client.V1ContainerPort(container_port=80)],

  lifecycle=client.V1Lifecycle(
    post_start=client.V1Handler(
       _exec=client.V1ExecAction(
           command=[
                 "touch kube-test.txt"
                   ]

              )

          )

     )
)

# Template
template = client.V1PodTemplateSpec(
  metadata=client.V1ObjectMeta(labels={"app": "hooktest"}),
  spec=client.V1PodSpec(containers=[container]))


# Spec
spec = client.ExtensionsV1beta1DeploymentSpec(
  replicas=1,
  template=template)


# Deployment
deployment = client.ExtensionsV1beta1Deployment(
  api_version="extensions/v1beta1",
  kind="Deployment",
  metadata=client.V1ObjectMeta(name="hooktest-deployment"),
  spec=spec)


# Creation of the Deployment in specified namespace
extension.create_namespaced_deployment(
    namespace="kube-client",
    body=deployment)
