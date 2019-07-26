from kubernetes import client, config


def main():
    # Fetching and loading Kubernetes Information
    config.load_kube_config()

    extension = client.ExtensionsV1beta1Api()

    # Container
    container = client.V1Container(
      name="nginx",
      image="nginx:1.7.9",
      image_pull_policy="IfNotPresent",
      ports=[client.V1ContainerPort(container_port=80)]
    )

    # Template
    template = client.V1PodTemplateSpec(
      metadata=client.V1ObjectMeta(labels={"app": "nginx", "version":"v1.0"}),
      spec=client.V1PodSpec(containers=[container]))


    # Spec
    spec = client.ExtensionsV1beta1DeploymentSpec(
      replicas=3,
      selector=client.V1LabelSelector(match_labels={"app":"nginx"}),
      strategy=client.ExtensionsV1beta1DeploymentStrategy(type="Recreate"),
      template=template)

    #Deployment
    deployment = client.ExtensionsV1beta1Deployment(
      api_version="extensions/v1beta1",
      kind="Deployment",
      metadata=client.V1ObjectMeta(name="nginx-deployment"),
      spec=spec)

    # Creation of the Deployment in specified namespace
    extension.create_namespaced_deployment(namespace="ratanb", body=deployment)


if __name__ == "__main__":
    main()
