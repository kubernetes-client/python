from kubernetes import client, config


def create_deployment(apps_v1_api):
    container = client.V1Container(
        name="nginx1",
        image="nginx",
        image_pull_policy="Never",
        ports=[client.V1ContainerPort(container_port=80)],
    )
    # Template
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
        spec=client.V1PodSpec(containers=[container]))
    # Spec
    spec = client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "nginx"}
        ),
        template=template)
    # Deployment
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name="deployment-nginx"),
        spec=spec)
    # Createthe Deployment in default namespace
    apps_v1_api.create_namespaced_deployment(
        namespace="default", body=deployment
    )
